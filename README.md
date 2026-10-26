# AI 技術統整 (ai-tech-digest)

模型進展 · Local LLM · Agent 與 Skill 生態 — 定期追蹤與整理。

🌐 **網頁版**：https://kilroy-utb.github.io/ai-tech-digest/
🏠 **整合於**：https://kilroy-utb.github.io/hub/ （Kilroy's Hub 首頁有入口卡片）

## 這個 repo 是什麼

一個**可重跑**的 AI 技術情報站。每份報告的每個數字都來自可驗證的官方端點，
原始 JSON 存在 `data/`，抓取邏輯存在 `scripts/`，隨時可以重跑驗證。

```
ai-tech-digest/
├── index.html          # 網站首頁（GitHub Pages 從 repo 根目錄服務）
├── hub.yaml            # 給 hub 首頁的設定（外部連結卡片）
├── reports/            # 報告（markdown）
│   ├── 2026-10-26-baseline.md            # 基準報告
│   ├── 2026-10-26-papers.md              # 87 篇 arXiv 論文逐篇摘要
│   └── 2026-10-26-vendors-frameworks.md  # 廠商 + 框架版本動態
├── data/               # 原始抓取資料（JSON）
│   ├── arxiv-papers.json
│   ├── github-releases.json
│   ├── huggingface-models.json
│   ├── ollama-models.json
│   └── chatart-announcements.json
└── scripts/            # 可重跑的抓取腳本
    ├── fetch-all.sh
    ├── fetch_arxiv.py
    ├── fetch_github_releases.py
    ├── fetch_huggingface.py
    ├── fetch_ollama.py
    └── fetch_chatart.py
```

## 資料來源分層

這個 repo 的核心設計是**每一份資料都標明來源層級**，避免把 SEO 農場文當成事實。

| Tier | 來源 | 為什麼可信 |
|---|---|---|
| **A** | arXiv API、GitHub Releases API、HuggingFace API、Ollama registry、各廠商 changelog、ChatArt 訊息中心 API | 直接問官方端點，回傳結構化、可重現的資料 |
| **B** | X / Reddit / Hacker News / YouTube | 社群訊號，**必須標註為「社群說法」**，不作為主要依據 |
| **C** | 私密社群、限時動態、付費內容 | 需人工提供後再分析 |

**原則**：Tier B/C 的內容不能單獨支撐任何結論。報告中每個主張都要有 Tier A 的連結。

## 重新抓取

```bash
git clone https://github.com/kilroy-utb/ai-tech-digest.git
cd ai-tech-digest

# 需要 ChatArt 公告的話（選用）
export CHATART_CRED_FILE=/path/to/credentials.json

# 全部重抓
bash scripts/fetch-all.sh
```

單獨抓某個來源：

```bash
python3 scripts/fetch_huggingface.py
python3 scripts/fetch_github_releases.py
python3 scripts/fetch_arxiv.py
python3 scripts/fetch_ollama.py
python3 scripts/fetch_chatart.py
```

所有腳本只用 Python 標準函式庫，不需要 pip install。

## 環境需求

| 變數 | 必要性 | 用途 |
|---|---|---|
| `CHATART_CRED_FILE` | 選用 | ChatArt 公告。沒有則該來源跳過 |
| `GITHUB_TOKEN` | 選用 | GitHub API。沒有則用匿名（速率限制較低），token 會從 `~/.git-credentials` 自動讀取 |

## 已驗證的事實

這些是 2026-10-26 實際抓取確認的，不是推測：

- **OpenClaw 393,089 stars** — 開源 AI 執行閘道，全社群體量最大的 agent 專案
- **Anthropic 官方 Agent Skills repo 183,831 stars**
- **Claude Code 153,396 stars**，每週發布多個版本
- **MCP 規格 2026-07-28 為 stable 版**，servers v2.0.0 完成 modern era 重構
- **`minimax-m3.1-flash` 存在於 Ollama 官方 library**（本機 config 當時仍指向 M3）
- **GGUF 佔 HuggingFace 熱門模型量化變體的 32.4%**，MLX 5.4%、NVFP4 3.3%、FP8 1.5%
- **Qwen3.8-27B 的社群 fine-tune（`HauhauCS/...-Aggressive-MTP-GGUF`）下載 231 萬**，但 `unsloth/Qwen3.8-27B-GGUF` 官方路徑 586 萬更高
- **llama.cpp 已改用滾動式 `b<build>` prerelease**，不再發 semver tag
- **`exo` 與 `llamafile` 實質停滯** — release 分別停在 2026-04 與 2026-09，近期 commit 僅動 UI
- **`Mozilla-Ocho/llamafile` 與 `comfyanonymous/ComfyUI` 已 301 重導**到新 owner，API 呼叫需開 `-L` 跟隨
- **低精度 KV cache 已是預設路徑** — vLLM 讓 NVFP4 走遍 SM8x/12x/90，GLM-5.x 在 SM100 預設 FP8

## 已知限制

- **PAT 缺 `workflow` scope** — `.github/workflows/` 無法推送，所以「每月自動檢查資料新鮮度」未啟用。Pages 用 legacy build（main 根目錄），不受影響。
- **引用數幾乎全為 0** — 這批論文都是 2026-09/10 新文，Semantic Scholar 尚未建立引用索引。報告中的排序依據是「技術貢獻實質性」而非引用數。
- **Ollama API 回傳固定 23 個 trending 集合** — `sort` 參數不影響排序，抓取到的就是首頁那份清單。

## 授權

內容與腳本：MIT。原始資料的所有權歸各來源平台。
