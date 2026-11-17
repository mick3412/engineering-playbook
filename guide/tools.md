# 工具總覽

> 由 `python3 pb.py build` 產生。依第一個階段分組；狀態：已整合、已安裝、待試、待查、未採用、避開。

## 0 開案

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [claude-work-mode](https://github.com/danyuchn/claude-work-mode)（T-14） | 未採用 | 免費 | MIT（寬鬆） | 想一鍵切換「不要中途問」「批次外派」「收尾收斂」三種工作方式時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |
| [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)（T-18） | 未採用 | 免費 | 未標（未標） | 要改善 Claude Code 寫程式時的常見毛病時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |

## 1 理解現況

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Graphify](https://github.com/Graphify-Labs/graphify)（T-21） | 待試 | 免費 | Apache-2.0（寬鬆） | 要讓 agent 理解大型程式碼庫時 |
| [book-to-skill（virgiliojr94）](https://github.com/virgiliojr94/book-to-skill)（T-38） | 待試 | 免費 | MIT（寬鬆） | 有一本領域書（技術書、方法論）想讓 agent 工作時照著查、照著做時。只用自己合法持有的書，產出的技能不公開散布 |
| [Trail-code（原名 Graft）](https://github.com/trailhq/Trail-Code)（T-01） | 未採用 | 不明 | MIT（寬鬆） | 用 tree-sitter 把程式畫成地圖（檔案、函式、誰呼叫誰），Claude Code 每次改檔前先查；另存「學到的事」在 .trail/。會加 hooks、讀過去對話、預設開遙測；為測試改 agent 環境不划算 |
| [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)（T-02） | 未採用 | 不明 | MIT（寬鬆） | 把程式、文件整理成本機關係圖（17 個 MCP 工具），查改一處會牽動哪裡、找沒人用的程式 |
| [REA（Reverse Engineer Anything）](https://github.com/morluto/rea)（T-03） | 未採用 | 免費 | MIT（寬鬆） | 看到別的 app 或網站有喜歡的功能，想知道它怎麼運作時。用途是逆向分析，不是我們的工作 |
| [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)（T-07） | 未採用 | 部分付費 | MIT（寬鬆） | 要大量讀取公開網站內容時 |
| [Perplexity MCP](https://github.com/perplexityai/modelcontextprotocol)（T-08） | 未採用 | 付費 | MIT（寬鬆） | 需要附來源的深入研究時 |

## 2 設計

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Agent Skills（Addy Osmani）](https://github.com/addyosmani/agent-skills)（T-05） | 已安裝 | 免費 | MIT（寬鬆） | 想要一套 spec、plan、test、review、ship 的工作流程時 |
| [superpowers（obra）](https://github.com/obra/superpowers)（T-16） | 未採用 | 免費 | MIT（寬鬆） | 要一套完整的 agent 開發方法（計畫、測試先行、除錯、協作）時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |

## 3 拆工

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [agency-agents（開發挑 3 個）](https://github.com/msitarzewski/agency-agents)（T-15） | 未採用 | 免費 | MIT（寬鬆） | 需要交接範本、最小改動的審查、或自動化上線前評估時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |
| [Orca](https://github.com/stablyai/orca)（T-22） | 未採用 | 免費 | MIT（寬鬆） | 想同時跑多個 coding agent 時 |
| [T3 Code](https://github.com/pingdotgg/t3code)（T-23） | 未採用 | 免費 | MIT（寬鬆） | 想要另一個 coding agent 圖形介面時 |

## 4 實作

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Expo Skills](https://github.com/expo/skills)（T-11） | 已安裝 | 免費 | MIT（寬鬆） | 做行動 app（Expo、React Native）時 |
| [Scrapling](https://github.com/D4Vinci/Scrapling)（T-37） | 待試 | 免費 | BSD-3-Clause（寬鬆） | 要抓的網頁會擋爬蟲（Cloudflare 等），或網頁常改版、選擇器一直壞掉時。先看對方的使用條款與 robots.txt；有官方 API 就用 API；Meta、IG 等平台不用 |
| [Context7（Upstash）](https://context7.com)（T-41） | 待試 | 部分付費 | MIT（MCP 伺服器）（寬鬆） | 用到更新很快的套件（Next.js、Tailwind 等），怕 agent 寫出舊版 API 時 |
| [n8n（自架）](https://n8n.io)（T-42） | 待試 | 部分付費 | Sustainable Use License（自架免費，公司內部與商業營運可用；轉賣 n8n 本身或當代管服務受限）（特殊） | 要把跨服務的固定流程自動化（表單 → CRM → 追蹤信、排程報表）又不想按次付費時 |
| [mattpocock/skills](https://github.com/mattpocock/skills)（T-17） | 未採用 | 免費 | MIT（寬鬆） | 要參考資深工程師平常給 agent 的工程技能時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |
| [Ponytail](https://github.com/DietrichGebert/ponytail)（T-19） | 未採用 | 免費 | MIT（寬鬆） | agent 容易過度設計時。精華已拆成手冊條目（S1-03、S1-04、S2-05、S4-08、S4-09、S5-05、S6-03、S8-02 等）；整包安裝會和手冊重複 |

## 5 驗證

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Playwright MCP（Microsoft）](https://github.com/microsoft/playwright-mcp)（T-06） | 已安裝 | 免費 | Apache-2.0（寬鬆） | 要讓 agent 實際操作瀏覽器測網站時 |
| [agent-browser（Vercel Labs）](https://github.com/vercel-labs/agent-browser)（T-34） | 待試 | 免費 | Apache-2.0（寬鬆） | 要讓 agent 實際開頁面、填表單、截圖來驗證時；和已安裝的 Playwright MCP（T-06）比，看哪個步驟少、結果穩 |
| [Playwright CLI（Microsoft）](https://github.com/microsoft/playwright-cli)（T-04） | 未採用 | 免費 | Apache-2.0（寬鬆） | 要在瀏覽器實際跑、截圖或錄測試時。Python 版 Playwright 已能完成同樣的流程測試（網站手冊 T-07） |

## 6 審查

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [llm-council 技能](https://github.com/gcpdev/llm-council-skill)（T-10） | 待試 | 免費 | MIT（寬鬆） | 重要決策想要其他模型的意見時。很耗 token，用前先問負責人 |
| [security-audit（Cloudflare）](https://github.com/cloudflare/security-audit-skill)（T-36） | 待試 | 免費 | MIT（寬鬆） | 上線前或大改後，要對整個 repo 做一次有紀錄、可重跑的資安稽核時 |
| [Codex CLI（OpenAI）](https://developers.openai.com/codex)（T-40） | 待試 | 部分付費 | Apache-2.0（寬鬆） | 要一個不同模型的第二意見審查程式時。免費替代：開一個沒看過對話的子代理審（/code-review） |

## 7 交付

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [GitHub CLI（gh）](https://cli.github.com)（T-39） | 已安裝 | 免費 | MIT（寬鬆） | 在終端機開 PR、看 CI、發 release、管 issue 時 |

## 8 回顧與收錄

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [AI Engineering from Scratch（課程與教學技能）](https://github.com/rohitg00/ai-engineering-from-scratch)（T-35） | 待試 | 免費 | MIT（寬鬆） | 想弄懂 agent loop、MCP、技能、驗證關卡這類機制怎麼運作，或要找一份現成的檢查清單（每課 outputs/ 有技能檔）時 |
| [Ollama](https://ollama.com)（T-43） | 待試 | 免費 | MIT（寬鬆） | 大量簡單工作（分類、摘要、改格式）想在本機跑、不花 API 費用時 |

## 協作

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [find-skills（vercel-labs/skills）](https://github.com/vercel-labs/skills)（T-27） | 已安裝 | 免費 | MIT（寬鬆） | 想找現成技能時。找技能時用 `npx skills find <關鍵字>`（實跑：幾秒列出技能、安裝次數，比 gh 搜尋準） |
| [task-observer（rebelytics）](https://github.com/rebelytics/one-skill-to-rule-them-all)（T-30） | 待試 | 免費 | CC-BY-4.0（寬鬆） | 想讓技能和手冊從實際修正中持續改進時 |
| [context-mode](https://github.com/mksglu/context-mode)（T-32） | 待查 | 免費 | 未標（未標） | 長任務中工具輸出塞爆 context 時 |
| [claude-mem](https://github.com/thedotmack/claude-mem)（T-12） | 未採用 | 部分付費 | Apache 2.0（寬鬆） | 想讓 agent 跨對話記得過去做過的事時 |
| [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)（T-13） | 未採用 | 免費 | MIT（寬鬆） | — |
| [ECC（affaan-m）](https://github.com/affaan-m/ECC)（T-20） | 未採用 | 部分付費 | MIT（寬鬆） | 想參考整套 agent 效能優化（技能、記憶、安全、研究優先）時 |
| [OpenCode](https://github.com/anomalyco/opencode)（T-24） | 未採用 | 免費 | MIT（寬鬆） | 想換其他開源 coding agent 時 |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（T-25） | 未採用 | 免費 | MIT（寬鬆） | 想用 DeepSeek 的 agent 框架時 |
| [claude-hud](https://github.com/jarrodwatts/claude-hud)（T-26） | 未採用 | 免費 | MIT（寬鬆） | 長時間工作想隨時看 context 用量、進行中的工具與子代理時。會改 Claude Code 狀態列設定，手冊用不到 |
| [gstack（garrytan）](https://github.com/garrytan/gstack)（T-28） | 未採用 | 免費 | MIT（寬鬆） | 想參考一整套開發流程（追問需求、定架構、審查、上線）時 |
| [caveman](https://github.com/JuliusBrussee/caveman)（T-29） | 未採用 | 免費 | Apache-2.0（寬鬆） | 想省 token 時 |
| [claude-mem（thedotmack）](https://github.com/thedotmack/claude-mem)（T-31） | 未採用 | 免費 | Apache-2.0（寬鬆） | 想要跨對話記憶時 |
| [Camofox Browser](https://github.com/jo-inc/camofox-browser)（T-33） | 避開 | 免費 | MIT（寬鬆） | 想讓 agent 自動瀏覽網站時 |

## 工具

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Composio](https://docs.composio.dev/docs/composio-connect)（T-09） | 未採用 | 部分付費 | 未標（未標） | 要一次接很多 App 時 |
