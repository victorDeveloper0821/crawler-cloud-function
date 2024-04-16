# Google Cloud Function 定期爬蟲服務

本項目使用 Python 開發，結合 Google Cloud Function 和 Google Cloud Scheduler 實現自動化的網絡爬蟲服務。此服務旨在定期抓取指定網站的數據並進行處理。

## 功能描述

- **自動觸發**：利用 Google Cloud Scheduler 定期觸發 Cloud Function。
- **數據抓取**：自動從目標網站抓取最新數據。
- **數據處理**：對抓取的數據進行必要的處理和格式化。
- **數據存儲**：將處理後的數據保存至 Google Cloud Storage 或 BigQuery。

## 技術棧

- Python
- Google Cloud Functions
- Google Cloud Scheduler
- MongoDB

## 開始使用

### Requirement

確保您已有 Google Cloud Platform 賬戶，並且已經啟用以下服務：
- Google Cloud Functions
- Google Cloud Scheduler
- Python with miniconda or anaconda installed

### deployments

1. **clone the repo**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   
2. **create virtualenv for repo**
  
  ```bash
  pip3 install -r requirements.txt
  ```

## Features Checklist

- [x] 定義爬蟲需求和目標網站
- [x] 設計爬蟲架構
- [x] 實現爬蟲邏輯
- [x] 集成 Google Cloud Functions
- [x] 設定 Google Cloud Scheduler 進行定時觸發
- [ ] 測試爬蟲的穩定性和性能
- [ ] 部署至生產環境
- [ ] 監控和優化生產環境運行

