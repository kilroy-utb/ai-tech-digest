# 廠商與框架動態 (2026-10-26)

> **來源**：各廠商官方 API changelog / 官方 blog / GitHub Releases API
> **抓取範圍**：10 家模型廠商 + 14 個推論/訓練框架專案
> **原則**：只收官方來源，不用新聞稿轉述。star 數與下載量為 2026-10-26 即時 API 回傳值。

---

## 一、廠商動態

### OpenAI

| 模型 | 日期 | 規格 | 重點 |
|---|---|---|---|
| **GPT-6.1 Sol** | 2026-10-08 | 1,050,000 context，最大輸入 922K / 輸出 128K | 接近 Astra 品質但成本更低，支援 `service_tier: "ultrafast"` 降低 token 間隔延遲；美國與歐盟資料落地 |
| **GPT-6 Astra** | 旗艦 | 1,050,000 context，128K output，知識截止 2026-04-30 | 最強推理/編碼/電腦操作/研究模型，`reasoning.effort` 支援 low→max；$10/$1/$50 per MTok |
| **GPT-6 Luna** | 2026-10-06 | 1,050,000 context，知識截止 2026-05-18 | 成本敏感大量場景，$0.1/$0.01/$0.5 per MTok；10-22 起 Decisions API GA（單次可 400 題） |
| **GPT-Live 1** | 2026-10-16 / 10-20 | 語音 + 12 小時 prompt caching | prompt-to-voice 全面開放（新增 9 種自然語音）；12 小時快取寫入成本 2.5x |

### Anthropic

| 模型 | 日期 | 規格 | 重點 |
|---|---|---|---|
| **Claude Opus 5.5** | 2026-10-22 | 1M context，128K output，知識截止 2026-06 | 長期 agentic coding 與知識工作首選，$4/$20 per MTok；cache read 為基礎價 5% |
| **Claude Fable 5.1 / Mythos 5.1** | 2026-09-01 | 1M context（預設），128K output | Fable 5.1 為長時程 agentic coding/研究用後繼模型，$10/$50 per MTok，cache read 降至 $0.25/MTok（0.025x）；已上 Bedrock、Google Cloud、Microsoft Foundry |
| **Claude Sonnet 5.5 / Haiku 5.5** | 現役 | — | Sonnet $2/$10、Haiku 從 $0.10/$0.50；Haiku 5.5 為高併發低延遲（分類、抽取、路由） |
| **API 版本 2026-10-21** | 2026-10-21 | SDK 全面改版 | Python SDK 2.0.0、TypeScript 1.0.0、C# 13.0.0、Go 2.0.0、Java 3.0.0、PHP 1.0.0、Ruby 2.0.0、ant CLI 2.0.0；授權由 **MIT 改為 Apache 2.0** |

### Google（DeepMind / Gemini）

| 模型 | 日期 | 規格 | 重點 |
|---|---|---|---|
| **Gemini 4 Argon** | 2026-10-13 GA | context 1,048,576，最大輸出 65,536（long decode 可達 1M） | 最新旗艦推理模型，專為複雜軟體工程、數學/科學、多步 agent 打造；支援 text/image/video/audio/PDF 輸入、code execution、computer use (Preview)、search grounding；**不支援** image generation 與 Live API |
| **Gemini 3.8 Flash / 3.6 Flash** | 2026-10-08 棄用遷移 | — | `gemini-3.7-flash` → `3.8-flash`、`gemini-3.5-flash` → `3.6-flash`（自動路由，需改 model string） |
| **Gemini Nano Banana 2.1** | 2026-10-06 GA | — | 圖像生成/對話式編輯；支援 1:4、4:1、1:8、8:1 寬幅比例與 1K/2K/4K 解析度 |
| **Gemma 4 開放權重** | 2026-03-11 發布 | 31B 稠密 / 26B-A4B (MoE) / 12B / E4B / E2B | 開源家族中下載量最高的 Google 開放權重模型（31B-it 843 萬次） |

### Meta（Meta Superintelligence Lab）

| 模型 | 日期 | 規格 | 重點 |
|---|---|---|---|
| **Muse Glimmer 30B** | 2026-08-09 | 稠密因果 Transformer + ViT-G/14 (~1.8B)，總參數 ~29.6B，context 131,072+，Apache 2.0 | **專為消費級硬體上的自主 agent 任務打造**（多步推理、可靠工具呼叫、失敗復原、多模態輸入），從 Muse Spark 蒸餾而來；官方 GGUF 已發布 |
| **Muse Spark Open 816B-A42B** | 2026-09-15 | MoE，816B 總參數 / 42B 啟用 | Meta 開源大型 MoE，NVIDIA 發布 NVFP4 權重 |
| **Llama 4 Scout / Maverick** | 2025-04 | Scout 17B×16E、Maverick 17B×128E | 仍為官方 Llama 家族最新開放權重，但下載量較前代下滑（Scout 13.4 萬），**官方重心已轉向 Muse 系列** |

### DeepSeek

| 模型 | 日期 | 關鍵指標 | 重點 |
|---|---|---|---|
| **DeepSeek-V4.1-Flash-1017** | 2026-10-17 | HLE 42.6、Terminal-Bench 4.0 42.3、DeepSWE v1.1 77.0 | 原生多模態視覺理解；API 呼叫方式不變（`deepseek-flash`）；同日記錄開放自研搜尋 API |
| **DeepSeek-V4.1-Flash** | 2026-09-10 | GPQA Diamond 90.9、Codeforces 3471、Terminal-Bench 2.1 90.6、CyberGym 88.1 | 新架構家族中最小模型，原生多模態；舊代自動退役路由；API 降價 |
| **DeepSeek-V4-Flash-Vision-Exp** | 2026-08-21 | Terminal Bench 2.1 83.9、NL2Repo 57.7 | 實驗性多模態視覺模型 |
| **DeepSeek-V4-Pro / V4-Flash** | 2026-04-24 / 07-31 | V4-Flash Terminal Bench 2.1 82.7、Toolathlon 70.3 | 同時支援 OpenAI 與 Anthropic 介面；8-16 起採離峰價格 |

### Mistral AI

| 模型 | 日期 | 規格 | 重點 |
|---|---|---|---|
| **Mistral Large 4** | 2026-10-06 (Preview) | MoE 1.05T 總參數 / 52B 啟用，1.6B 視覺編碼器，context 1M | 開源權重通用多模態旗艦；$1.36/$0.14/$4.18 per MTok |
| **Voxtral TTS 3 / Mini Transcribe 3** | 2026-10-20 | 32k context | TTS 支援零樣本音色複製與 9 種語言串流；Transcribe 3 為 SOTA 準確率 |
| **Shieldstral 1.0** | 2026-08-04 | 3.8B，32k context | 緊湊型多模態內容安全分類模型 |
| **Timestral 1.0** | 2026-10-14 | 5M/28M/123M/209M，32K context | 時間序列基礎模型 |
| **Mistral Small 4 / Medium 3.5** | 2026-03 / 04 | Small 4：119B / 6.5B 啟用；Medium 3.5：128B | Small 4 Apache 2.0；Medium 3.5 為 agentic/coding 多模態前沿模型 |

### 阿里 Qwen

| 模型 | 日期 | 重點 |
|---|---|---|
| **Qwen3.8-27B** | 2026-08-05 | 稠密 27B，image-text-to-text，Safetensors 55.6GB；**社群最歡迎的 Qwen 3.8 稠密模型（776 萬下載、1.8 萬 likes）** |
| **Qwen3.8-Flash-Next** | 2026-08-24 | `qwen4_exp` 架構；下載 309 萬、6,484 likes；**GGUF 社群版下載 685 萬，是 2026 年 8-10 月本地部署最熱的新模型** |
| **Qwen3.8-2.4T-A95B** | 2026-08-08 | MoE 2.4T 總參數 / 95B 啟用，512 experts |
| **Qwen-Image-2.1 / 2.1-Turbo / PE** | 2026-09-14 / 09-20 / 10-09 | 20B 級 MMDiT 影像模型；PE-I2I（編輯）與 PE-T2I（生成）兩種 prompt 編碼器版本 |
| **Qwen-Drive-1.0-4B** | 2026-08-27 | 4B 端側多模態 |

### Moonshot AI / Kimi

| 模型 | 日期 | 重點 |
|---|---|---|
| **Kimi K3.1 Pro** | 2026 年 | 3 萬億級參數，1M token context，原生視覺；另有 `kimi-k3.1-pro-highspeed`（約 2-3 倍速度）；`reasoning_effort` 可調 low/high/max |
| **Kimi K3** | 2026-07 | 2.8 萬億參數（全球首個開源 3 萬億級模型），1M context，原生視覺；HF 下載 87.4 萬、1.18 萬 likes |
| **Kimi K2.7 Code / highspeed** | 2026-06 | 256k context；highspeed 約 180 tok/s、短上下文可達 260 tok/s |
| **Kimi 託管智能體（Beta）** | 2026-09 | Kimi Durable Harness 全託管 7x24 agent 運行環境（多智能體編排、技能/外掛/憑證庫、跨會話記憶）；`/v1/tools/search` 搜尋 API |
| **舊版退役** | — | `kimi-k2.5` 與 `moonshot-v1` 2026-08-31 下線；K2 系列 10-31 停止新用戶註冊，預計 12 月底全數下線 |

### Nous Research

| 模型 | 日期 | 重點 |
|---|---|---|
| **Hermes 4.3 — Seed 36B** | 2025-11-17 | base: ByteDance-Seed-OSS-36B-Base，Apache 2.0；首個以 Psyche 去中心化方式訓練的 Hermes；後訓練語料從 1M 樣本/1.2B token 擴增至 ~5M 樣本/~60B token；混合推理模式、schema 遵循 |
| **Hermes 4 系列** | 2025-08 | 14B / 70B / 405B，含 FP8 量化 |
| **Hermes 3 Llama 3.1 8B / 70B FP8** | 2024-08 | Nous 累積下載量最高（8B 46.4 萬、70B-FP8 10.1 萬） |
| **NousCoder-14B** | 2025-12-23 | 競技程式導向 |

### xAI

| 模型 | 日期 | 重點 |
|---|---|---|
| **Grok 4.7** | 2026-09 | 500k context，text+image 輸入、純文字輸出、無輸出上限；$2/$0.50/$6 per MTok（<200k prompt），>200k 為 $4/$1/$12；`reasoning.effort` 支援 low/medium/high/xhigh |
| **Grok Voice 3.0** | 2026-10 | Speech to Speech，成本與 Voice 2.0 相同；Voice 2.0 棄用 |
| **Grok 4.6** | 2026-08 | 同定價架構；同月推出 Grok Bot（持久雲端電腦上的 AI 隊友） |

### 智譜 GLM（補充）

| 模型 | 日期 | 重點 |
|---|---|---|
| **GLM-5.3 / GLM-5.3-Flash** | 2026-08-25 | 1M context；GLM-5.3-Flash 下載 635 萬、GLM-5.3 下載 207 萬；Mistral API 亦以 `zai-glm-5-3` 上架 |

---

## 二、推論框架

### Ollama — 184,799 stars（2026-10-24 v0.40.11）

- **v0.40.11**：**Speech 支援** — macOS 上 `ollama run` 可在生成時直接朗讀模型回覆，並可透過 OpenAI 相容的 `/v1/audio/speech` endpoint 串流音訊。**d3 decision models** — 把 vLLM Semantic Router 的 decision model 帶進 Ollama，可對文字、結構化狀態或圖片做分類/是非題/帶機率的選項評分，家族含 2B/4B/9B/27B。
- **v0.40.10**（10-23）：新增 NVIDIA Nemotron 3.5 Bolt E4B（Gemma 4 架構 VLM），128K context，**內建 DFlash draft model 做 speculative decoding**。
- **v0.40.9**（10-22）：Flint 模型擴充到 Linux 與 Windows。修正 streaming OpenAI Responses 與 Anthropic Messages 請求在部分輸出後靜默中斷的問題。`ollama launch` 現在會把雲端模型的 context 長度與 capabilities 傳給 coding tool。

### vLLM — 95,542 stars（2026-10-18 v0.32.0）

**v0.32.0**（814 commits / 363 contributors）：
- **低精度 KV cache 全面普及** — NVFP4 KV cache 支援 SM8x/SM12x/SM90；GLM-5.x 在 SM100 預設改用 FP8 KV cache（每 rank KV 記憶體減半、吞吐 +2.3~5.5%，TTFT 付出 7~11% 代價）；ROCm 加入 4-bit `ultraquant_4bit`
- Model Runner V2 成為 ROCm 預設
- 新增 `POST /v1/systemone` 結構化決策 endpoint 與 `hf` tool/reasoning parser
- **Breaking changes**：Python 3.10 移除、CORS 預設收緊、`transformers>=5.16.1,<5.20.0`、torch.compile sequence parallelism 與 AsyncTP 移除、cascade attention 移除、`max_tokens` 不再預先保留
- 修復 3 個 CVE（chat template 資源耗盡、tokenizer `max_token_id`、P2P ZMQ socket 耗盡）

**v0.31.0**（10-05，717 commits）：DeepSeek-V4.1-Flash 效能（FlashMLA + V4.1 NVFP4 壓縮 KV cache 成為 SM100 預設）。**Fast restart** — `vllm preload` 啟動 weight-cache daemon，讓量化後權重常駐 GPU 記憶體跨重啟。

**v0.30.0**（09-22，762 commits）：新增 DeepSeek-V4.1-Flash、GLM-5.3-Flash、Qwen3.8-Flash-Next。**Watermarking**（Gumbel-max）。**Fast Start** — `--load-format ipc_cache` 讓重啟直接映射 CUDA IPC 記憶體而非重讀磁碟。

### llama.cpp — 132,384 stars

**發布模式已變更**：不再發布 semver tag release，最新 tag 停在 `v0.7.0`；現在只發布滾動式 `b<build>` prerelease（單週就發了 b11853–b11889 共 30 個）。

- **b11888**（10-25）：grammar 模組加入**強制遞迴深度上限**（`GRAMMAR_RECURSIVE_LIMIT`）。同時修掉實質 bug — 原本深度計算會把 token 的 code point 數算進去，導致任何 ≥256 字元的 token 在 grammar 下必被拒絕（例如 GLM-4.7-Flash 的 512-space token）。**這是語意面變更，深度限制從「非必要」變成「強制」**。
- **b11889**（10-25）：CUDA 後端 `archName` 從 VLA 改為 `std::string`。
- CI 產出的 backend 涵蓋 CUDA 12.8 / 13.4、ROCm 10.0、Vulkan、SYCL (FP32/FP16)、OpenVINO 2026.4.1、Metal、Snapdragon（CPU+Adreno GPU+Hexagon NPU）。

### SGLang — 38,177 stars（2026-10-19 v0.5.22）

**v0.5.22**（950 PRs / 245 contributors）：
- **DeepSeek-V4.1 在 H200 單 GPU 吞吐最高 2.3 倍**；AMD MI350X/MI355X 最高 1.9 倍
- Qwen3.8-Flash-Next 在 B200 decode 快 12%；GLM-5.3-Flash + DFlash 在 B300 快 10%
- **InstantTensor loader 讓模型載入快 10 倍**
- PD disaggregation 吞吐最高 +27%、p95 TTFT 減半
- **SGLang 現在可用標準 PyTorch backend 在 Apple Silicon Mac 上執行**
- **MiniMax-H3 與 Qwen-Image 2.1 可在 ComfyUI 中以 SGLang Diffusion 執行**，並能載入社群 GGUF checkpoint 與 LoRA
- **Breaking change：要求 Python 3.11 以上**

**v0.5.21**（10-02）：prefix cache 預設改用 Rust core。**新增 Decisions API（`/v1/decisions`）與 Score API（`/v1/score`）**，把 LLM/VLM 變成低延遲 classifier 與 scorer。

**v0.5.20**（09-18）：**Sampling masks for RL rollouts** — `return_sampling_mask` 讓每個 decode step 回傳 sampler 實際抽樣的 token support 與 log-prob，trainer 可重播 rollout 而不必重建 top-k/top-p（batch 1 快 17%、batch 64 快 52%）。**Unified radix tree** — DeepSeek-V4-Flash 共用 system prompt 時 token 命中率由 43.8% 升至 60.8%，平均 TTFT 由 1.57s 降至 1.07s。**Breaking change：`/v1/responses` 預設不再保留結果**。

### MLX — 28,941 stars（2026-10-14 v0.32.4）

- **v0.32.4**：新增 scaled dot product attention 與 gated delta net 的 VJP（微分）。**CUDA 後端**：`fp_gather_qmv`、`gather_qmm_rhs_sm80`、Cholesky 走 cuSOLVER。**Metal**：M1 quantized matmul dispatch 調校、SDPA D512 的 pre-M5 記憶體改善。支援 Python 3.15。
- **v0.32.3**：CUDA Cholesky via cuSOLVER、NAX attention 對 D512 支援、M5 ultra 非量化 matmul 調校、Windows 用 DXGI 取得準確 WDDM VRAM 預算。
- **v0.32.2**：新增 `force_fused` 選項給 scaled_dot_product_attention、GGUF metadata 邊界檢查（修一個 OOB 讀取風險）。

### llamafile — 26,489 stars ⚠️ 已更名

**repo 已更名為 `mozilla-ai/llamafile`**（原 `Mozilla-Ocho/llamafile` 會 301 重導）。

- **0.10.6**（09-15）：更新內嵌 llama.cpp 至 b10441。新增 **Vulkan toolchain**。修正 `llamafile_open_zip` 的 zip entry window 邊界檢查（對應 zip 解析的 OOB 讀取風險）。
- **0.10.5**（08-03）：核心是改進「與 upstream llama.cpp 同步」的流程（含給 AI agent 用的 llamafile skill/plugin），讓自動產生的草稿 PR 更容易過審。
- **0.10.4**（07-16）：首次帶入 **transcribefile**（transcribe.cpp 的 cosmocc 打包版本，支援 16+ 個語音模型家族）。新增 HTTPS 支援。
- **⚠️ 活躍度警訊**：最後 push 2026-10-12，最新 release 已近一個月。近期 commit 包含「Agentfile v0.0000001」這種實驗性條目。

### exo — 48,050 stars ⚠️ 實質停滯

- **v1.0.71**（2026-04-23）：新增 Kimi K2.6（含多模態）、Qwen3.6 27B / GLM 5.1 model card。加入模型供應商建議的 sampling 預設值。
- **v1.0.70**（2026-04-17）：**Flash Attention 落地**（Qwen3.5 與 Gemma 4），peak 記憶體降低 3~6 倍。**新增 OpenCode、n8n、OpenClaw 一鍵連接 helper**。
- **v1.0.69**（2026-03-27）：**Continuous batching 預設開啟**，特別適合 agentic workflow。
- **⚠️ 活躍度警訊**：最新 release 停在 2026-04-23，最後 push 2026-10-13，且 10-13 那批 commit 全是 macOS app 與 dashboard 的 UI/UX 修改，**核心推論部分近半年沒有明顯推進**。

---

## 三、訓練與微調框架

### Unsloth — 78,573 stars（2026-10-23 v0.1.910-beta）

- **v0.1.910-beta**：**MLX MoE 模型超過 Mac 記憶體時，expert 留在 SSD**，讓 Qwen3.8-Flash-Next 在 32GB Mac 上跑得動。新增 chat-only 安裝選項。**MoE expert pruning**（用 REAP 移除 25% 或 50% 最沒用的 expert）。支援 Recursive 的 40B coding-agent MoE **Flint**（3-bit 塞進 24GB，SWE-bench Pro v2 得分 89.7 vs Qwen 3.6 的 73.8）。**安全修正**：安裝流程會拒絕 eMudhra 已遭入侵的 emSign 憑證，但選擇性安裝的 vLLM 與 SGLang engine 仍信任它們。
- **v0.1.909-beta**：**DeepSeek-V4.1-Flash-1017**（552B 總參數 + 196B Engram table、約 16B active、1M context），Engram table 留在 SSD 時 1-bit 只需約 125GB 記憶體、4-bit 需 300GB；Terminal-Bench 4.0 從 31.2 提升到 42.3。**FLUX.3 Image Klein** 24GB 可跑。**FSDP2 多卡訓練（alpha）** 支援 LoRA / QLoRA / 全參數微調。`unsloth mcp add` 一鍵把 Claude Code / Codex / Cursor 接上。
- **v0.1.908-beta**：新增 **text-diffusion LLM**（LLaDA、Dream、SDAR、DiffusionGemma）訓練與對話。**DeepSpeed ZeRO-2/3 訓練支援**。coding agent 在本機 GGUF 模型上的 prompt cache 大幅改善，Claude Code 首次回應快最多 4 倍。

### Axolotl — 12,632 stars（2026-10-16 v0.21.0）

- **v0.21.0**（59 commits）：**Reflection Beam**（501B MoE / 23B active）可用 QLoRA 在單一 8×H200 節點微調。**原生 diffusion LM 訓練**（頂層 `diffusion_lm:` 區塊）。**多模態 DPO / IPO / KTO / GRPO / GDPO** 可用影像資料集。**DeepSpeed 下可設定 `context_parallel_size`**。**效能**：packed flash-attention LoRA 在 Llama-3.1-8B 上的 host-device sync 從 390 次降到每 micro-step 1 次；500B 級 MoE 的 fused-expert 轉換從約 20 分鐘縮到 6 分鐘。**Heads up：`vllm>=0.30.0` 為必要條件。**
- **v0.20.0**（09-30）：**GGUF 匯出**（`axolotl export config.yml --quantize Q4_K_M,Q8_0`）。**Ringmaster context parallelism**。**原生 NVFP4 LoRA 與 merge-aware training**（確保合併後的 checkpoint 與訓練時實際使用的量化 base+adapter 權重一致）。**Breaking change：Python 3.12 與 torch 2.13.0 為最低需求，FSDP1 已移除。**
- **v0.19.0**（09-10）：**宣告式 model support profile** 系統。**Ternary（BitNet b1.58）QAT**。兩個新 optimizer：PoLoRA（LoRA 專用的 Muon-like）與 AdamC。chat-template tokenization 加速 16.4 倍（80 輪對話 1577.6ms → 96.4ms）。

### TRL — 19,602 stars（2026-10-15 v1.16.0）

- **v1.16.0**：**可在 AWS Trainium 上訓練**（`pad_to_multiple_of` 預設改為 `"auto"`；Trainium2 + Qwen3-0.6B SFT 20 steps：130s vs 260s）。**AsyncGRPO 的 tree attention** — 每個 micro-batch row 打包成 prefix tree 而非扁平序列，多輪 rollout 共用的 prompt token 只 forward 一次（packing ratio 2.29 時 1.90 倍加速、peak 記憶體 35.2 → 18.0 GiB；3.37 時 2.97 倍加速、35.2 → 13.6 GiB）。**Muse Spark Open** 支援（8 節點 × 8×H100，實測 14.2s/step、131k tokens/step）。
- **v1.15.0**（10-08）：**Fused LM head 為本季最重要改版** — Triton kernel 直接從 hidden state 投影到 per-token log-prob 與 entropy，**永不建出 `[batch, seq, vocab]` logits 張量**。同一張 GPU 上可訓練序列長度大幅延長：DPO 10,240 → 59,392 token（**5.80 倍**）、KTO 9,216 → 63,488（**6.89 倍**）、GRPO 28,672 → 114,688（**4.00 倍**）。**Breaking change**：GRPO/RLOO/DPO/KTO 的 full-logits scoring 路徑移除；**掛在 `lm_head` 上的 PEFT adapter 會直接 raise**，必須改用 `modules_to_save=["lm_head"]`。
- **v1.14.2**（10-06）：修兩個會導致**靜默錯誤訓練**的問題 — 以只有 generation config 宣告的 id 結束回合的模型（Gemma 3/4、Phi-3.5）不會停下，之後產生的內容全被拿去訓練，唯一徵兆是 `completions/clipped_ratio` 接近 1。

### PEFT — 21,851 stars（2026-10-01 v0.21.2）

- **v0.21.0**（09-15）：**4 個新方法** — **Riemannian-preconditional LoRA optimizer**（對 LoRA 梯度套用 Riemannian 預條件，免去 A/B 矩陣分別調 LR）、**KaSA**（辨識 base weight 中知識相關的奇異值）、**Super-Tuning**（免校準的 magnitude scoring 配置稀疏調參預算）、**ShadowPEFT**（小型 shadow network 與凍結 base model 並行，適合把 shadow 放邊緣、base 放雲端）。**OSF（Orthogonal Subspace Fine-tuning）記憶體降 22%、訓練時間減 46%**。修 `add_weighted_adapter` 在 SVD 路徑下 LoRA scaling 被套用兩次的 bug。
- **v0.21.1**（09-29）：讓 **Tensor Parallel 與 PEFT 正確協作**。
- **v0.21.2**（10-01）：修 encoder-decoder 模型在 `transformers>=5.18.0` 下無法運作。

---

## 四、工具與周邊

### ComfyUI — 143,047 stars（2026-10-19 v0.42.1）⚠️ 已更名

**repo 已更名為 `Comfy-Org/ComfyUI`**（原 `comfyanonymous/ComfyUI` 會 301 重導）。

- **v0.42.0**（10-18）：**MOSS-image 支援**（OpenMOSS 5.1B，可產生含中英文文字的圖像）。新增 **Krea 3 Image** partner node。**Qwen 3.x 效能改善 Part 2**。支援將 embedding 模型載入 Qwen3.5。**ARM Linux 加入執行與單元測試**。**明確聲明 CPU device 不支援 fp8 / nvfp4 / mxfp8 / int8**。
- **v0.41.0**（10-15）：**FLUX3-image 模型支援**、MiniMax-H3 LightVAE 支援。新增 ImageSDRToHDR 與 ReferenceMultiLatent 節點。**LoRA stack 節點曾因前端未支援 DynamicGroup 而暫時停用，隨即 revert** — 屬於上下游版本落差。

### Transformers — 168,170 stars（2026-10-19 v5.20.2）

- **v5.20.0**（10-15）：**新模型** — Meta **Muse Spark Open**（816B / 42B active，1,048,576 token context，BF16 與 NVFP4）、InclusionAI **Ling 3.0 Flash**（hybrid MoE，KDA 層與 MLA 層交錯）、Aleph Alpha **Kolibri 1**（50 層，sigmoid routing，每 token 路由到 384 個專家中的 6 個）、**MiniCPM-V 4.7**、Baidu **UnlimitedOcr**（3B，Reference Sliding Window Attention 讓 decode 期間 KV cache 保持定值，單次 forward 可轉錄數十頁）、**UltraBERT**、**MOSS-Transcribe-Diarize** 0.9B。**官方公告 EP 推論速度有回歸，正在修。**
- **v5.20.1**（10-16）：加入 **Reflection AI 的 Beam** 模型。
- **Breaking changes**：`cache_utils.py` 已 deprecated 的方法被移除（影響 minimax_m3_vl、pi0）；移除跨模型 import；`kernels` 最低版本升至 0.17.2。

### whisper.cpp — 54,675 stars（2026-10-06 v1.9.5）

- **v1.9.5**：更新 ggml v0.26.0。**WebGPU 新增 MMVQ 支援**（Q1_0/Q5_0/Q5_1/Q3_K/Q5_K/Q6_K/MXFP4 都能用）；CUDA NVFP4 的 mmq 累積最佳化；Vulkan 量化 K/V 的 sparse flash attention；Metal 的 few-row MMA 與 F16 KV flash attention；OpenVINO 升到 2026.4.1。
- 與 llama.cpp 一致，另有 nightly `b5454` prerelease。

---

## 五、生態訊號

### 1. 低精度 KV cache 全面落地是這一季最明顯的趨勢
vLLM 讓 NVFP4 走遍 SM8x/SM12x/SM90、GLM-5.x 在 SM100 預設改用 FP8（KV 記憶體減半、吞吐 +2.3~5.5%）；ROCm 導入 4-bit `ultraquant_4bit`。**這已從「實驗性開關」變成「預設路徑」。**

### 2. 量化格式競賽集中在 NVFP4 / MXFP4 / MXFP8 這一組 Blackwell-native 格式
且出現「線上重量化」與「merge-aware training」這類新要求。**Axolotl v0.20.0 的原生 NVFP4 LoRA 特別強調「合併後的 checkpoint 必須與訓練時實際使用的量化權重一致」** — 這是訓練與推論格式交界處真正變難的地方。

### 3. 推論引擎正在「往推論框架裡長出訓練／RL 能力」，也反過來
vLLM 新增 `/v1/systemone` 結構化決策 endpoint，Ollama 帶入 d3 decision model，SGLang 推 Decisions API 與 Score API — 這是為了服務 agentic routing 與分類需求。反過來 Unsloth 用 FSDP2 做多卡訓練、Axolotl 支援 diffusion LM 訓練、SGLang 提供 `return_sampling_mask` 讓 trainer 能重播 rollout。

### 4. MoE 模型太大了，於是「把東西留在 SSD / CPU」變成主流解法
Unsloth 讓 MLX MoE 的 expert 留在 SSD；DeepSeek-V4.1-Flash-1017 的 Engram table 放 SSD 後 1-bit 只需約 125GB。Unsloth 同期加入 MoE expert pruning（REAP 移除 25~50%），是同一方向上用相反的解法。

### 5. 前端的版本協作開始出現摩擦
ComfyUI v0.41.0 曾停用 LoRA stack 節點隨即 revert；Unsloth 修了「拒絕 eMudhra 被入侵的 emSign 憑證」但明說選用的 vLLM / SGLang engine 仍信任它們。**Unsloth、Axolotl、TRL、PEFT 的 release notes 都出現「需要新版 transformers」的硬性版本下限**（Axolotl 要求 `vllm>=0.30.0`、TRL 要求 `transformers>=5.20.0`），顯示模型定義層的版本迭代已成為下游的固定摩擦成本。

### 6. 有兩個專案在 star 數上仍是巨頭，但實質開發明顯放慢
**exo**（48,050 stars）最新 release 停在 2026-04-23，10 月的 commit 幾乎全是 UI 修改；**llamafile**（26,489 stars）最後 push 2026-10-12，出現「Agentfile v0.0000001」這種實驗性條目。相對之下 Unsloth、Axolotl、TRL、PEFT 的 10 月 release 節奏都相當密集。

### 7. 一個容易踩到的陷阱
`Mozilla-Ocho/llamafile` 與 `comfyanonymous/ComfyUI` 兩個路徑都已 301 重導到新 owner（`mozilla-ai/llamafile`、`Comfy-Org/ComfyUI`），**用舊路徑的 API 呼叫必須開 `-L` 跟隨重導，否則會拿到空結果**。
