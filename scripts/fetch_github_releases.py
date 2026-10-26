#!/usr/bin/env python3
"""GitHub API 抓取 — agent/skill 生態與推論框架的最新 release。

用法: python3 scripts/fetch_github_releases.py [output_dir]
Token: 環境變數 GITHUB_TOKEN，或 ~/.git-credentials。
輸出: data/github-releases.json
"""
import datetime, json, os, re, sys, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else "data"
UA = {"User-Agent": "ai-tech-digest/1.0"}


def get_token():
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        return tok.strip()
    for p in ("/workspace/home/.git-credentials", os.path.expanduser("~/.git-credentials")):
        if os.path.exists(p):
            for line in open(p):
                m = re.search(r"https://[^:]+:([^@]+)@github\.com", line)
                if m:
                    return m.group(1)
    return None


def api(path, token, timeout=30):
    h = dict(UA)
    if token:
        h["Authorization"] = f"Bearer {token}"
    h["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request("https://api.github.com" + path, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


REPOS = {
    "agent_skill": [
        ("anthropics/claude-code", "AI 編碼 agent CLI"),
        ("openclaw/openclaw", "OpenClaw 執行閘道"),
        ("chatart-ai/skill", "ChatArt Skill 多模態工具包"),
        ("modelcontextprotocol/servers", "MCP 官方 server 集合"),
        ("modelcontextprotocol/modelcontextprotocol", "MCP 規格"),
        ("anthropics/skills", "Anthropic 官方 Agent Skills"),
        ("obra/superpowers", "社群 skills 框架"),
        ("google-gemini/gemini-cli", "Gemini CLI"),
        ("cline/cline", "Cline agent"),
        ("continuedev/continue", "Continue agent"),
        ("sst/opencode", "opencode agent"),
        ("Aider-AI/aider", "aider"),
        ("BerriAI/litellm", "LLM 統一 gateway"),
        ("microsoft/vscode-copilot-chat", "VS Code Copilot Chat"),
    ],
    "inference": [
        ("ggml-org/llama.cpp", "llama.cpp"),
        ("ollama/ollama", "Ollama"),
        ("vllm-project/vllm", "vLLM"),
        ("ml-explore/mlx", "MLX"),
        ("exo-explore/exo", "exo"),
        ("sgl-project/sglang", "SGLang"),
        ("Mozilla-Ocho/llamafile", "llamafile"),
    ],
    "training": [
        ("unslothai/unsloth", "Unsloth"),
        ("axolotl-ai-cloud/axolotl", "Axolotl"),
        ("huggingface/trl", "TRL"),
        ("huggingface/peft", "PEFT"),
    ],
    "tools": [
        ("comfyanonymous/ComfyUI", "ComfyUI"),
        ("huggingface/transformers", "Transformers"),
        ("ggml-org/whisper.cpp", "whisper.cpp"),
    ],
}


def clean(body):
    return re.sub(r"\s+", " ", (body or "")).strip()


def main():
    os.makedirs(OUT, exist_ok=True)
    token = get_token()
    result = {"_source": "api.github.com", "_fetched_at": None,
              "_authenticated": bool(token), "groups": {}}

    for group, repos in REPOS.items():
        out = []
        for full, desc in repos:
            entry = {"repo": full, "desc": desc, "releases": []}
            try:
                d = api(f"/repos/{full}", token)
                entry.update({
                    "stars": d.get("stargazers_count"),
                    "forks": d.get("forks_count"),
                    "language": d.get("language"),
                    "pushed_at": d.get("pushed_at"),
                    "created_at": d.get("created_at"),
                    "license": (d.get("license") or {}).get("spdx_id"),
                    "description": d.get("description"),
                    "open_issues": d.get("open_issues_count"),
                })
            except Exception as e:
                entry["error"] = f"repo: {e}"
            try:
                rels = api(f"/repos/{full}/releases?per_page=3", token)
                for r in rels:
                    entry["releases"].append({
                        "tag": r.get("tag_name"),
                        "published": (r.get("published_at") or "")[:10],
                        "prerelease": r.get("prerelease"),
                        "body": clean(r.get("body"))[:800],
                        "url": r.get("html_url"),
                    })
            except Exception as e:
                entry.setdefault("error", f"releases: {e}")
            out.append(entry)
            print(f"  {full:<45} {entry.get('stars', '?'):>8} stars")
        result["groups"][group] = out

    result["_fetched_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    path = os.path.join(OUT, "github-releases.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"OK -> {path}  (authenticated={bool(token)})")


if __name__ == "__main__":
    main()
