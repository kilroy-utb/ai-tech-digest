#!/usr/bin/env python3
"""arXiv API 抓取 — local LLM 推論/量化/fine-tune 與 agent/skills 論文。

用法: python3 scripts/fetch_arxiv.py [output_dir]
輸出: data/arxiv-papers.json
"""
import datetime, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

OUT = sys.argv[1] if len(sys.argv) > 1 else "data"
NS = {"a": "http://www.w3.org/2005/Atom"}
API = "https://export.arxiv.org/api/query"

TOPICS = {
    "quantization": "cat:cs.LG AND (all:quantization OR all:GGUF OR all:NVFP4 OR all:AWQ OR all:GPTQ)",
    "inference": "cat:cs.LG AND (all:\"inference engine\" OR all:\"KV cache\" OR all:\"speculative decoding\" OR all:\"attention optimization\")",
    "finetuning": "cat:cs.LG AND (all:LoRA OR all:GRPO OR all:\"preference optimization\" OR all:\"parameter-efficient\")",
    "agents": "cat:cs.AI AND (all:\"LLM agent\" OR all:\"tool use\" OR all:agentic OR all:\"multi-agent\")",
    "agentic_coding": "cat:cs.SE AND (all:\"code agent\" OR all:\"SWE-bench\" OR all:\"software engineering agent\")",
    "skills_context": "cat:cs.CL AND (all:\"tool learning\" OR all:\"context engineering\" OR all:\"model context protocol\" OR all:\"skill learning\")",
}


def fetch(query, max_results=15):
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results),
    }
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "ai-tech-digest/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read()
    root = ET.fromstring(data)
    papers = []
    for e in root.findall("a:entry", NS):
        def txt(tag):
            n = e.find(f"a:{tag}", NS)
            return n.text.strip() if n is not None and n.text else ""
        raw_id = txt("id").split("/abs/")[-1]
        papers.append({
            "id": raw_id,
            "title": re.sub(r"\s+", " ", txt("title")),
            "published": txt("published")[:10],
            "updated": txt("updated")[:10],
            "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
            "summary": re.sub(r"\s+", " ", txt("summary"))[:700],
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "url": f"https://arxiv.org/abs/{raw_id}",
            "pdf": f"https://arxiv.org/pdf/{raw_id}",
        })
        time.sleep(0.2)
    return papers


def main():
    os.makedirs(OUT, exist_ok=True)
    result = {"_source": "export.arxiv.org/api/query",
              "_fetched_at": None, "topics": {}}
    for name, q in TOPICS.items():
        try:
            ps = fetch(q)
            result["topics"][name] = {"query": q, "papers": ps}
            print(f"  {name:<16} {len(ps)} papers")
        except Exception as e:
            result["topics"][name] = {"query": q, "error": str(e), "papers": []}
            print(f"  {name:<16} ERR {e}")
        time.sleep(3)  # arXiv 建議 3 秒一次請求

    result["_fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    path = os.path.join(OUT, "arxiv-papers.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    total = sum(len(t.get("papers", [])) for t in result["topics"].values())
    print(f"OK -> {path}  (total {total} papers)")


if __name__ == "__main__":
    main()
