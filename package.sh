#!/bin/bash

# 設定原始碼目錄和打包後的檔案名稱
SOURCE_DIR="."
OUTPUT_FILE="youbikeCrawler.zip"

# 要排除的檔案格式（示例）
EXCLUDE_PATTERNS=(".env" "**/__pycache__/*" ".gitignore" "package.sh" ".git/*" ".DS_Store")

# 建立排除參數
EXCLUDE_ARGS=()
for pattern in "${EXCLUDE_PATTERNS[@]}"; do
  EXCLUDE_ARGS+=(-x "$pattern")
done

# 執行 zip 命令
zip -r $OUTPUT_FILE $SOURCE_DIR "${EXCLUDE_ARGS[@]}"

echo "打包完成: $OUTPUT_FILE"
