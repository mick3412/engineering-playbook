# 待試與複查清單

> 由 `python3 pb.py build` 產生。`pb.py review` 會依日期和實戰紀錄提出建議。

## 待試與爭議的做法

| 代號 | 狀態 | 要點 | 複查條件 |
|---|---|---|---|
| CO-03 | 待試 | 一個 agent 負責一塊工作，不是一件事 | — |
| CO-09 | 待試 | 進度看板直接從專案檔推導 | — |
| CO-12 | 待試 | 交代 AI 寫目標不寫步驟，學方法不學口氣 | — |
| S0-01 | 待試 | 新專案一開始就設強約束 | — |
| TL-03 | 待試 | 每次選服務都記錄理由 | — |

## 待試與待查的工具

| 代號 | 工具 | 狀態 | 何時用 | 複查條件 |
|---|---|---|---|---|
| T-01 | Trail-code（原名 Graft） | 待試 | 用 tree-sitter 把程式畫成地圖（檔案、函式、誰呼叫誰），Claude Code 每次改檔前先查；另存「學到的事」在 .trail/ | — |
| T-03 | REA（Reverse Engineer Anything） | 待查 | 看到別的 app 或網站有喜歡的功能，想知道它怎麼運作時 | 安裝前讀過 setup 會改哪些設定，並確認要分析的軟體條款允許 |
| T-04 | Playwright CLI（Microsoft） | 待試 | 要在瀏覽器實際跑、截圖或錄測試時 | — |
| T-05 | Agent Skills（Addy Osmani） | 待試 | 想要一套 spec、plan、test、review、ship 的工作流程時 | — |
| T-06 | Playwright MCP（Microsoft） | 待試 | 要讓 agent 實際操作瀏覽器測網站時 | — |
| T-07 | Firecrawl MCP | 待查 | 要大量讀取公開網站內容時 | 需要大量抓網站時 |
| T-09 | Composio | 待查 | 要一次接很多 App 時 | 要接多個 App 時 |
| T-10 | llm-council 技能 | 待查 | 重要決策想要其他模型的意見時 | 有預算或改成只用免費模型時 |
| T-11 | Expo Skills | 待試 | 做行動 app（Expo、React Native）時 | 要做行動 app 時 |
