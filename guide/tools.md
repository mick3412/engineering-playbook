# 工具總覽

> 由 `python3 pb.py build` 產生。依第一個階段分組；狀態：已整合、已安裝、待試、待查、未採用、避開。

## 1 理解現況

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Trail-code（原名 Graft）](https://github.com/trailhq/Trail-Code)（T-01） | 待試 | 不明 | MIT（寬鬆） | 用 tree-sitter 把程式畫成地圖（檔案、函式、誰呼叫誰），Claude Code 每次改檔前先查；另存「學到的事」在 .trail/ |
| [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server)（T-07） | 待試 | 部分付費 | MIT（寬鬆） | 要大量讀取公開網站內容時 |
| [REA（Reverse Engineer Anything）](https://github.com/morluto/rea)（T-03） | 待查 | 免費 | MIT（寬鬆） | 看到別的 app 或網站有喜歡的功能，想知道它怎麼運作時 |
| [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)（T-02） | 未採用 | 不明 | MIT（寬鬆） | 把程式、文件整理成本機關係圖（17 個 MCP 工具），查改一處會牽動哪裡、找沒人用的程式 |
| [Perplexity MCP](https://github.com/perplexityai/modelcontextprotocol)（T-08） | 未採用 | 付費 | MIT（寬鬆） | 需要附來源的深入研究時 |

## 2 設計

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Agent Skills（Addy Osmani）](https://github.com/addyosmani/agent-skills)（T-05） | 已安裝 | 免費 | MIT（寬鬆） | 想要一套 spec、plan、test、review、ship 的工作流程時 |

## 4 實作

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Expo Skills](https://github.com/expo/skills)（T-11） | 已安裝 | 免費 | MIT（寬鬆） | 做行動 app（Expo、React Native）時 |

## 5 驗證

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Playwright MCP（Microsoft）](https://github.com/microsoft/playwright-mcp)（T-06） | 已安裝 | 免費 | Apache-2.0（寬鬆） | 要讓 agent 實際操作瀏覽器測網站時 |
| [Playwright CLI（Microsoft）](https://github.com/microsoft/playwright-cli)（T-04） | 待試 | 免費 | Apache-2.0（寬鬆） | 要在瀏覽器實際跑、截圖或錄測試時 |

## 6 審查

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [llm-council 技能](https://github.com/gcpdev/llm-council-skill)（T-10） | 待試 | 免費 | MIT（寬鬆） | 重要決策想要其他模型的意見時 |

## 協作

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [claude-mem](https://github.com/thedotmack/claude-mem)（T-12） | 未採用 | 部分付費 | Apache 2.0（寬鬆） | 想讓 agent 跨對話記得過去做過的事時 |
| [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)（T-13） | 未採用 | 免費 | MIT（寬鬆） | — |

## 工具

| 工具 | 狀態 | 費用 | 授權 | 何時用 |
|---|---|---|---|---|
| [Composio](https://docs.composio.dev/docs/composio-connect)（T-09） | 待試 | 部分付費 | 未標（未標） | 要一次接很多 App 時 |
