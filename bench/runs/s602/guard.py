#!/usr/bin/env python3
"""PreToolUse hook sample: block `npm run migrate` and say what to do instead (S6-02)."""
import json, sys
d = json.load(sys.stdin)
cmd = d.get("tool_input", {}).get("command", "")
if "npm run migrate" in cmd:
    print("擋下：npm run migrate 可能連到正式資料庫。替代做法：先跑 `npm run migrate -- --dry-run` 看要改什麼，"
          "或請負責人在預覽資料庫上跑；確認後由負責人執行。", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
