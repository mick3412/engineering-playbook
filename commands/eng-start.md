---
description: 開一件新工作，從開案開始
argument-hint: "<名稱> <新功能|修 bug|重構|新專案|自動化腳本|技能與 agent>"
---

用 engineering-playbook 開一件新工作。參數：$ARGUMENTS（第一個是名稱，第二個是類型；缺類型就問我）。

執行 `python3 "$(cat ~/.config/engineering-playbook/home)/pb.py" start "<名稱>" --type <類型>`，然後照技能的格式回覆「現在／下一步／工具／注意／提升」五行，接著從 0.1 開始問我需要的資訊。
