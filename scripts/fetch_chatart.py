#!/usr/bin/env python3
"""ChatArt 官方公告抓取 — 真實 release note（官網 product-updates 頁已過時）。

需要 ChatArt API 憑證。設定方式:
  export CHATART_CRED_FILE=/workspace/.chatart/credentials.json
  或 export CHATART_UID=... CHATART_API_KEY=...

用法: python3 scripts/fetch_chatart.py [output_dir]
輸出: data/chatart-announcements.json

API 說明見 chatart-api-auth skill。
"""
import datetime, hashlib, json, os, sys, urllib.parse, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else "data"
BASE = "https://api.chatartpro.com/web"
SECRET = "uN3lu01bFtumul8W"
UA = {"User-Agent": "ai-tech-digest/1.0"}


def sign(params, data):
    """ChatArt 請求簽名: UPPERCASE(MD5(sorted_key_value_concat + secret))"""
    m = {**(params or {}), **(data or {})}
    m.pop("signature", None)
    for k in [k for k, v in m.items() if v is None]:
        del m[k]
    s = ""
    for k in sorted(m):
        v = m[k]
        if isinstance(v, bool):
            sv = "1" if v else ""
        elif isinstance(v, (list, dict)):
            sv = json.dumps(v, separators=(",", ":"))
        else:
            sv = str(v)
        s += f"{k}{sv}"
    return hashlib.md5((s + SECRET).encode()).hexdigest().upper()


def load_creds():
    uid = os.environ.get("CHATART_UID", "").strip()
    key = os.environ.get("CHATART_API_KEY", "").strip()
    if uid and key:
        return uid, key
    paths = []
    cf = os.environ.get("CHATART_CRED_FILE")
    if cf:
        paths.append(cf)
    paths += ["/workspace/.chatart/credentials.json",
              os.path.expanduser("~/.chatart/credentials.json"),
              "/opt/data/.chatart/credentials.json"]
    for p in paths:
        if os.path.exists(p):
            d = json.load(open(p))
            k = d.get("api_key") or d.get("token", "").strip()
            u = d.get("uid") or d.get("identity-id", "").strip()
            if k and u:
                return u, k
    raise SystemExit("找不到 ChatArt 憑證。設定 CHATART_CRED_FILE 或 CHATART_UID/CHATART_API_KEY。")


def http(url, method="GET", body=None, headers=None, params=None):
    h = dict(UA)
    if headers:
        h.update(headers)
    if body is not None:
        h["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    else:
        data = None
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=h, data=data, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def main():
    os.makedirs(OUT, exist_ok=True)
    uid, key = load_creds()
    H = {"Token": key, "Identity-Id": uid, "Language": "EN",
         "Skill": "1", "App-Type": "2"}

    # Token 可能過期 -> 先 guest-login 取新 token
    try:
        d = http(f"{BASE}/member/guest-login", "POST", {"type": 2}, H)
        if d.get("code") == 200:
            H["Token"] = d["data"]["token"]
            H["Identity-Id"] = d["data"]["user_id"]
    except Exception as e:
        print(f"  guest-login 失敗（沿用原 token）: {e}")

    params = {"page": 1, "size": 80}
    r = http(f"{BASE}/message/message-center", "GET", headers=H,
             params={**params, "signature": sign(params, {})})
    if r.get("code") != 200:
        print(f"  API 回 {r.get('code')}: {r.get('message')}")
        SystemExit(1)

    items = r.get("data", [])
    seen, uniq = set(), []
    for it in items:
        t = it.get("title", "")
        if t in seen:
            continue
        seen.add(t)
        uniq.append({
            "id": it.get("id"),
            "name": it.get("name"),
            "title": it.get("title"),
            "content": it.get("content"),
            "open_url": it.get("open_url"),
            "image_url": it.get("image_url"),
            "effective_time": int(it.get("effective_time") or 0),
            "date": datetime.datetime.fromtimestamp(
                int(it.get("effective_time") or 0)).strftime("%Y-%m-%d"),
            "is_pop": it.get("is_pop"),
        })
    uniq.sort(key=lambda x: -x["effective_time"])

    result = {"_source": f"{BASE}/message/message-center",
              "_fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "count": len(uniq), "announcements": uniq}
    path = os.path.join(OUT, "chatart-announcements.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"OK -> {path}  ({len(uniq)} announcements)")
    for a in uniq[:8]:
        print(f"  [{a['date']}] {a['title'][:70]}")


if __name__ == "__main__":
    main()
