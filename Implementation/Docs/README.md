# فهرست مستندات پیاده‌سازی (Implementation Docs Index)

این پوشه منبع مستقیم نگارش سه فصل پایان‌نامه است: روش‌شناسی، پیاده‌سازی، ارزیابی.

## اسناد اصلی

| فایل | موضوع | فصل‌های هدف |
|------|--------|-------------|
| [`Architecture_and_Integrations.md`](Architecture_and_Integrations.md) | معماری، پورت‌ها، دیاگرام‌های Mermaid، Tech Stack | روش‌شناسی + پیاده‌سازی |
| [`Experimental_Results.md`](Experimental_Results.md) | معیارهای LSTM، Case Study عامل زبانی، Latency | ارزیابی و نتایج |
| [`LSTM_RUL_API.md`](LSTM_RUL_API.md) | مدل Pinball+Attention و API استنتاج | هر سه فصل |
| [`DTAgent.md`](DTAgent.md) | دوقلوی وضعیتی و دادهٔ حسگری | روش‌شناسی + پیاده‌سازی |
| [`Engine_Monitor.md`](Engine_Monitor.md) | پایش بی‌درنگ | پیاده‌سازی + نتایج |
| [`Motor_Dashboard.md`](Motor_Dashboard.md) | داشبورد وضعیت / شبیه‌سازی ورودی | پیاده‌سازی + نتایج |
| [`LLM_Agent_Dify.md`](LLM_Agent_Dify.md) | ورک‌فلو Dify، پرامپت، Q&A | هر سه فصل |
| [`LLM Agent.md`](LLM%20Agent.md) | نمونه‌های خام پرسش‌وپاسخ | نتایج |
| [`LLMAgent Response Time Report.csv`](LLMAgent%20Response%20Time%20Report.csv) | دادهٔ خام Latency | نتایج |

## رسانه

- `Images/` — تصاویر UI، فرمان‌ها، ورک‌فلو و پایش  
- `Demos/` — ویدیوهای تعامل و شبیه‌سازی  
- `../Dify DSL Backups/Nasa Engine Digital Twin.yml` — پشتیبان ورک‌فلو

## نگاشت سریع سرویس → پورت

| سرویس | پورت |
|-------|------|
| lstm-rul-api | 8000 |
| DTAgent | 8001 |
| motor-dashboard | 3000 |
| engine-monitor | 3001 |
| Dify (nginx) | 80 / 443 |
