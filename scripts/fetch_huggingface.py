#!/usr/bin/env python3
"""HuggingFace API 抓取 — 模型下載量、量化變體分佈。

用法: python3 scripts/fetch_huggingface.py [output_dir]
輸出: data/huggingface-models.json
"""
import json, os, sys, time, urllib.request
from collections import Counter

OUT = sys.argv[1] if len(sys.argv) > 1 else "data"
UA = {"User-Agent": "ai-tech-digest/1.0"}


def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


ORGS = [
    ("Qwen", "阿里 Qwen"), ("meta-llama", "Meta Llama"),
    ("NousResearch", "Nous Research"), ("mistralai", "Mistral"),
    ("deepseek-ai", "DeepSeek"), ("moonshotai", "Moonshot/Kimi"),
    ("google", "Google"), ("openai", "OpenAI"), ("nvidia", "NVIDIA"),
    ("unsloth", "Unsloth"), ("bartowski", "bartowski"),
    ("lmstudio-community", "LM Studio"), ("ggml-org", "llama.cpp 官方"),
    ("mradermacher", "mradermacher"), ("HauhauCS", "HauhauCS"),
    ("huihui-ai", "huihui-ai"), ("JonathanColetti", "JonathanColetti"),
]


def detect_quant(mid):
    up = mid.upper()
    for f, label in [("NVFP4", "NVFP4"), ("MXFP4", "MXFP4"), ("FP8", "FP8"),
                     ("AWQ", "AWQ"), ("GPTQ", "GPTQ"), ("GGUF", "GGUF"),
                     ("MLX", "MLX"), ("QAT", "QAT"), ("BF16", "BF16"),
                     ("INT4", "INT4"), ("INT8", "INT8")]:
        if f in up:
            return label
    if "4BIT" in up or "4-BIT" in up:
        return "4bit"
    if "8BIT" in up or "8-BIT" in up:
        return "8bit"
    return "base"


def main():
    os.makedirs(OUT, exist_ok=True)
    result = {"_source": "huggingface.co/api/models", "_fetched_at": None,
              "orgs": {}, "gguf": [], "quant_distribution": {}, "top_text_generation": []}

    all_models = []
    for org, label in ORGS:
        try:
            ms = get(f"https://huggingface.co/api/models?author={org}"
                     f"&sort=downloads&direction=-1&limit=40")
        except Exception as e:
            result["orgs"][org] = {"label": label, "error": str(e)}
            continue
        rows = []
        for m in ms:
            mid = m.get("modelId") or m.get("id")
            rows.append({
                "id": mid,
                "downloads": m.get("downloads") or 0,
                "likes": m.get("likes") or 0,
                "last_modified": (m.get("lastModified") or "")[:10],
                "quant": detect_quant(mid),
                "tags": [t for t in (m.get("tags") or [])
                         if t in ("gguf", "text-generation", "conversational",
                                  "mlx", "safetensors", "nvfp4", "fp8", "awq")],
            })
        result["orgs"][org] = {"label": label, "models": rows}
        all_models.extend(rows)
        time.sleep(0.35)

    # GGUF / 量化分支
    gguf = [r for r in all_models if r["quant"] != "base"]
    gguf.sort(key=lambda r: -r["downloads"])
    result["gguf"] = gguf[:60]

    # 量化格式分佈
    cnt = Counter(r["quant"] for r in all_models)
    total = sum(cnt.values()) or 1
    result["quant_distribution"] = {k: {"count": v, "pct": round(v * 100 / total, 1)}
                                    for k, v in cnt.most_common()}

    # 全站 text-generation top
    try:
        ms = get("https://huggingface.co/api/models?sort=downloads&direction=-1"
                 "&limit=50&filter=text-generation")
        result["top_text_generation"] = [
            {"id": m.get("modelId") or m.get("id"),
             "downloads": m.get("downloads") or 0,
             "likes": m.get("likes") or 0,
             "quant": detect_quant(m.get("modelId") or m.get("id"))}
            for m in ms]
    except Exception as e:
        result["top_text_generation"] = {"error": str(e)}

    import datetime
    result["_fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

    path = os.path.join(OUT, "huggingface-models.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"OK -> {path}")
    print(f"  orgs: {len(result['orgs'])} | gguf rows: {len(result['gguf'])}")
    print("  quant distribution:")
    for k, v in result["quant_distribution"].items():
        print(f"    {k:<12} {v['count']:>4} ({v['pct']}%)")


if __name__ == "__main__":
    main()
