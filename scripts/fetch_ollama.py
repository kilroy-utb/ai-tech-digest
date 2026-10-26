#!/usr/bin/env python3
"""Ollama registry 抓取 — trending/popular 模型清單與尺寸。

用法: python3 scripts/fetch_ollama.py [output_dir]
輸出: data/ollama-models.json
"""
import datetime, json, os, sys, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else "data"
UA = {"User-Agent": "ai-tech-digest/1.0"}


def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def main():
    os.makedirs(OUT, exist_ok=True)
    result = {"_source": "ollama.com/api/tags", "_fetched_at": None,
              "models": [], "note": "Ollama API 回傳固定 23 個 trending 集合，sort 參數不影響排序。"}

    try:
        d = get("https://ollama.com/api/tags?sort=trending")
        rows = d.get("models", []) if isinstance(d, dict) else d
        for m in rows:
            result["models"].append({
                "name": m.get("name"),
                "size_bytes": m.get("size"),
                "size_gb": round((m.get("size") or 0) / 1e9, 1),
                "pulls": m.get("pulls"),
                "description": (m.get("description") or "")[:200],
                "tags": m.get("tags") or [],
                "modified_at": m.get("modified_at"),
            })
        result["models"].sort(key=lambda r: (r["size_gb"] or 0))
    except Exception as e:
        result["error"] = str(e)

    result["_fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    path = os.path.join(OUT, "ollama-models.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"OK -> {path}  ({len(result['models'])} models)")


if __name__ == "__main__":
    main()
