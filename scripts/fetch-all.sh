#!/usr/bin/env bash
# 抓取所有來源。輸出到 data/。
#
# 用法: bash scripts/fetch-all.sh
#
# 環境變數:
#   CHATART_CRED_FILE  ChatArt 憑證路徑（選用，沒有就跳過該來源）
#   GITHUB_TOKEN       GitHub PAT（選用，沒有的話匿名 API 速率較低）
set -u
cd "$(dirname "$0")/.."

echo "=== ai-tech-digest fetch-all ==="
echo "cwd: $(pwd)"
echo

run() {
  name="$1"; shift
  echo "--- $name ---"
  if python3 "$@" 2>&1; then
    echo "    ✓ $name"
  else
    echo "    ✗ $name 失敗（略過）"
  fi
  echo
}

run "HuggingFace"  scripts/fetch_huggingface.py
run "GitHub"      scripts/fetch_github_releases.py
run "Ollama"      scripts/fetch_ollama.py
run "arXiv"       scripts/fetch_arxiv.py

if [ -n "${CHATART_CRED_FILE:-}" ] || [ -f /workspace/.chatart/credentials.json ]; then
  export CHATART_CRED_FILE="${CHATART_CRED_FILE:-/workspace/.chatart/credentials.json}"
  run "ChatArt" scripts/fetch_chatart.py
else
  echo "--- ChatArt --- 略過（未設定 CHATART_CRED_FILE）"
  echo
fi

echo "=== 完成，data/ 內容 ==="
ls -la data/ 2>/dev/null
