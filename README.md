# Engineering Playbook（AI 協作開發手冊）

用 AI agent 開發軟體的手把手手冊：從講清楚「怎樣算完成」，到看懂程式、設計、拆成可驗證的小步驟、用硬約束擋錯、留下驗證證據、審查、小步交付，再把失誤變成規則。

不綁任何產品。產品的事實和限制寫在各產品專案的 `.agents/product-marketing.md`（產品設定檔），和其他手冊共用。

## 階段

| # | 階段 | 產出 |
|---|---|---|
| 0 | 開案 | 完成的定義、範圍、核准點 |
| 1 | 理解現況 | 要改的地方、可重用的做法 |
| 2 | 設計 | 方案與理由、驗證方式、三角度自查 |
| 3 | 拆工 | 可驗證的小步驟 |
| 4 | 實作 | 程式變更，硬約束通過 |
| 5 | 驗證 | 實際執行的證據 |
| 6 | 審查 | 審查結果、規則化 |
| 7 | 交付 | 小的 commit 或 PR，經人核准 |
| 8 | 回顧與收錄 | 實戰紀錄、失誤變規則 |

另有兩條跨階段軌道：**協作**、**工具**。類型：新功能、修 bug、重構、新專案、自動化腳本、技能與 agent；階段卡可以只顯示某一類的步驟和條目。每一步可以列出幾種做法。

每一步的「幾種做法」會點名這台電腦已有的技能和子 agent（例如 engineering:debug、code-review、simplify、security-review、Plan、Explore），手冊本身不內附技能。

每個階段的完整清單在 [`guide/`](guide/README.md)，由資料自動產生。

## 安裝（Claude Code 外掛）

```bash
python3 pb.py setup                                   # 記住 repo 位置，寫入一律回到這裡
claude plugin marketplace add "<這個 repo 的路徑>"
claude plugin install engineering-playbook@engineering-playbook-local
```

裝好後在任何專案都有技能 `engineering-playbook`、斜線指令 `/eng-start`、`/eng-status`、`/eng-next`、`/eng-card`、`/eng-add`、`/eng-review`、`/eng-pause`、`/eng-done`，以及進行中工作的一行提醒。進度存在產品專案的 `.engineering/`。

## 共用引擎

`pb.py` 和其他手冊（production-playbook、marketing-playbook）是同一份程式，`playbook.json` 決定名稱、環境變數 `ENGINEERING_PLAYBOOK_HOME` 和進度資料夾。改引擎時所有手冊一起改，測試會檢查是否相同。
