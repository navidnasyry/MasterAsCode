# سرویس پیش‌بینی عمر مفید باقیمانده (LSTM RUL API)

**مسیر کد:** `Implementation/lstm-rul-api/`  
**مسیر آموزش مدل:** `Implementation/jupyter-notebook/main_lstm_1_v3_loss_function_changed.ipynb`  
**پورت سرویس:** `8000`  
**نسخه مدل استقرار:** `AiModels/LSTM/LSTM_ATTENTION_LossChanged_V3`

این سند سه لایهٔ مورد نیاز پایان‌نامه را پوشش می‌دهد: روش‌شناسی مدل، پیاده‌سازی سرویس، و خلاصهٔ نتایج تجربی مرتبط با مدل.

---

## ۱. روش‌شناسی (Methodology)

### ۱.۱ مسئله و فرمولاسیون

پیش‌بینی عمر مفید باقیمانده (RUL) به‌صورت رگرسیون روی توالی‌های زمانی حسگرهای CMAPSS-FD001 تعریف می‌شود. به‌ازای پنجرهٔ ورودی \(\mathbf{X}\in\mathbb{R}^{w\times d}\) با \(w=50\) و \(d=16\)، شبکه مقدار اسکالر \(\hat{y}\) را به‌عنوان RUL پیش‌بینی می‌کند.

برچسب آموزشی بدون سقف‌گذاری (بدون piecewise clipping) محاسبه می‌شود:

\[
y^{(i)}(t)=t^{(i)}_{\mathrm{end}}-t
\]

در آزمون، مقدار فایل `RUL_FD001.txt` با آخرین چرخهٔ مشاهده‌شده ترکیب می‌شود:

\[
y^{(i)}(t)=t^{(i)}_{\mathrm{last}}+y^{(i)}_{\mathrm{file}}-t
\]

### ۱.۲ معماری شبکه

معماری نسخهٔ نهایی ترکیبی از LSTM دوطبقه و لایهٔ توجه زمانی است:

| لایه | مشخصات |
|------|--------|
| Input | شکل `(50, 16)` |
| LSTM-1 | ۱۰۰ واحد، `return_sequences=True` |
| Dropout | ۰٫۲ |
| LSTM-2 | ۵۰ واحد، `return_sequences=True` |
| Dropout | ۰٫۲ |
| AttentionLayer | وزن‌های زمانی \(\alpha\) و بردار زمینه |
| Dense | ۱ واحد، فعال‌سازی خطی |
| تعداد پارامترها | ۷۷٬۱۵۱ |

لایهٔ توجه برای هر گام زمانی وزن \(\alpha_t\) می‌سازد و بردار زمینه را به‌صورت \(\sum_t \alpha_t\,h_t\) محاسبه می‌کند. همین وزن‌ها مبنای توضیح سهم حسگرها در سرویس استنتاج هستند.

### ۱.۳ تابع زیان سفارشی (Pinball / Quantile Loss)

برای سوق دادن خطا به سمت کم‌برآورد محافظه‌کارانه، به‌جای MSE از تابع زیان Pinball با پارامتر \(\tau=0.125\) استفاده شده است:

\[
e = y_{\mathrm{true}}-y_{\mathrm{pred}},\qquad
L_\tau(e)=\max\big(\tau\,e,\;(\tau-1)\,e\big)
\]

با \(\tau<0.5\)، جریمهٔ بیش‌برآورد RUL (\(\hat{y}>y\)) سنگین‌تر از کم‌برآورد است؛ زیرا ضریب بیش‌برآورد برابر \(|\tau-1|=0.875\) و ضریب کم‌برآورد برابر \(0.125\) است. این طراحی با هزینهٔ نامتقارن نگهداری پیش‌بینانه هم‌راستاست: پیش‌بینی خوش‌بینانهٔ عمر می‌تواند به تأخیر در نگهداری و خرابی پرهزینه بینجامد.

> نکته: در کد آموزش، پارامترهای \(\alpha,\beta\) برای MSE وزن‌دار به‌کار نرفته‌اند؛ سوگیری محافظه‌کارانه از طریق \(\tau\) در Pinball اعمال می‌شود.

### ۱.۴ هایپرپارامترهای آموزش

| پارامتر | مقدار |
|---------|-------|
| Optimizer | RMSprop (نرخ یادگیری پیش‌فرض Keras ≈ ۰٫۰۰۱) |
| Batch size | ۲۰۰ |
| Epochs | ۶۰ |
| Validation split | ۰٫۰۵ |
| Sequence length | ۵۰ |
| Metrics | MAE، \(R^2\) سفارشی (`r2_keras`) |
| Loss | `PinballLoss(tau=0.125)` یا معادل سفارشی |

### ۱.۵ خط‌لولهٔ پیش‌پردازش (مفهومی)

1. حذف ستون‌های ثابت: `TRA`, `T2`, `P2`, `epr`, `farB`, `Nf_dmd`, `PCNfR_dmd`
2. حذف ویژگی‌های کم‌اطلاع/تکراری بر اساس همبستگی: `setting_1`, `setting_2`, `P15`, `NRc`
3. برچسب‌گذاری RUL (بدون clipping)
4. هنجارسازی Min-Max روی حسگرها (پارامترها فقط از آموزش)
5. افزودن `cycle_norm`
6. ساخت پنجره‌های لغزنده به طول ۵۰ با صفرگذاری دنباله‌های کوتاه

ویژگی‌های توالی نهایی (۱۶ ستون):  
`unit_number`, `time_in_cycles`, `T24`, `T30`, `T50`, `P30`, `Nf`, `Nc`, `Ps30`, `phi`, `NRf`, `BPR`, `htBleed`, `W31`, `W32`, `cycle_norm`

جزئیات عددی بیشتر در [`Experimental_Results.md`](Experimental_Results.md) آمده است.

---

## ۲. پیاده‌سازی (Implementation)

### ۲.۱ پشته فناوری

| جزء | فناوری |
|-----|--------|
| API | FastAPI ۰٫۱۱۵ + Uvicorn ۰٫۳۲ |
| مدل | TensorFlow / Keras ۲٫۱۷ |
| داده | pandas، numpy، scikit-learn ۱٫۵٫۲ |
| کانتینر | Docker؛ ایمیج پایه `python-api:2.0.0` |
| وابستگی‌های اضافی در requirements | torch، torch-geometric (برای مسیرهای آزمایشی/توسعه) |

### ۲.۲ ساختار ماژول‌ها

```
lstm-rul-api/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── routes_health.py
│   │   └── routes_prediction.py
│   ├── models/lstm_model.py          # AttentionLayer + load
│   ├── services/prediction_service.py
│   ├── schemas/prediction_schemas.py
│   ├── core/config.py, utils.py
│   └── AiModels/LSTM/...             # وزن‌ها و pickle
├── Dockerfile
└── docker-compose.yaml               # host:8000
```

### ۲.۳ بارگذاری مدل در استارت‌آپ

مدل یک‌بار هنگام import روتر بارگذاری می‌شود. در صورت شکست، `model=None` می‌ماند و endpointها خطای نرم برمی‌گردانند:

```python
try:
    model, history, model_data = load_lstm_model(MODEL_BASE_PATH)
    lstm_test_df = model_data["lstm_test_df"]
    sequence_length = model_data["sequence_length"]
    sequence_cols = model_data["sequence_cols"]
except Exception as e:
    model = None
    ...
```

`AttentionLayer` و `r2_keras` به‌عنوان `custom_objects` به `load_model` پاس داده می‌شوند.

### ۲.۴ APIها

**پایه:** `http://<host>:8000`

| Method | Path | توضیح |
|--------|------|--------|
| GET | `/api/health` | سلامت سرویس |
| GET | `/api/predict/predict_rul/{engine_number}?k_most_effictive=5` | RUL + top-k حسگر |
| GET | `/api/predict/engines_with_low_rul/?threshold=50&until_clock=` | فهرست موتورهای کم‌عمر |
| POST | `/api/predict/predict_new_engine_rul/` | پیش‌بینی روی توالی دلخواه |

**نمونه پاسخ `predict_rul`:**

```json
{
  "engine_number": 10,
  "predicted_rul": 164.67,
  "sensor_impacts": [
    {"sensor": "T30", "percent": 18.5},
    {"sensor": "Ps30", "percent": 12.1}
  ]
}
```

پارامتر `until_clock` در `engines_with_low_rul` امکان شبیه‌سازی پیشرفت زمان را برای عامل پایش فراهم می‌کند: فقط داده تا چرخهٔ مشخص برای هر موتور استفاده می‌شود.

### ۲.۵ توضیح‌پذیری مبتنی بر Attention

تابع `get_rul_and_attribution`:
1. خروجی میانی Attention را می‌گیرد؛
2. سهم حسگرها را از بردار زمینه نرمال می‌کند (L1)؛
3. شناسه‌ها و ستون‌های غیرحسی (`unit_number`, `time_in_cycles`, `cycle_norm`) را کنار می‌گذارد؛
4. top-k را برای عامل زبانی برمی‌گرداند.

### ۲.۶ مدیریت خطا

| حالت | رفتار |
|------|--------|
| مدل بارگذاری نشده | `{"error": "Model not loaded."}` (غالباً HTTP 200) |
| موتور ناموجود | `{"error": "Engine number N not found."}` |
| عرض ویژگی نادرست در POST | پیام خطا با تعداد ویژگی مورد انتظار |
| استثنای عمومی در attribution | چاپ لاگ / بازگشت خطا نرم |

> الگوی خطا «نرم» است (بدنهٔ JSON با کلید `error`) و لزوماً کد 4xx/5xx برنمی‌گرداند. در یکپارچه‌سازی با Dify، مسیر کنترل وضعیت موتور بیشتر به HTTP status تکیه دارد تا به این خطاهای نرم.

### ۲.۷ یکپارچه‌سازی

| مصرف‌کننده | نحوهٔ اتصال |
|------------|-------------|
| Dify Workflow | `env.lstm_host_addr` → GETهای پیش‌بینی |
| engine-monitor | `REACT_APP_API_BASE_URL=http://HOST:8000/api` |
| Volume مدل | `./AiModels` → `/app/AiModels` |

---

## ۳. ارزیابی و نتایج (Results)

### ۳.۱ معیارهای آزمون (۱۰۰ موتور FD001)

| معیار | LSTM پایه (MSE، بدون Attention) | نسخهٔ V3 (Pinball + Attention) |
|-------|----------------------------------|--------------------------------|
| MAE | ۱۷٫۵۶ | **۱۷٫۲۱** |
| \(R^2\) | ۰٫۲۴ | **۰٫۷۱** |
| RMSE | — | **۲۲٫۹۲** |
| نسبت کم‌برآورد | ۴۷٪ | **۸۷٪** |

نتیجهٔ اصلی: MAE تقریباً پایدار مانده، اما \(R^2\) به‌طور چشمگیر بهبود یافته و سوگیری محافظه‌کارانه (کم‌برآورد) مطابق طراحی تابع زیان تقویت شده است.

### ۳.۲ پایان آموزش (Epoch 60)

| Split | Loss (Pinball) | MAE | \(R^2\) |
|-------|----------------|-----|---------|
| Train | ۳٫۸۵۳۲ | ۲۷٫۱۷ | ۰٫۴۶ |
| Val | ۴٫۱۶۰۰ | ۲۳٫۵۷ | ۰٫۵۳ |

### ۳.۳ رفتار تحت بار / حالت خاص

- با `until_clock` می‌توان وضعیت ناوگان را در افق‌های زمانی مختلف بازسازی کرد؛ مناسب برای دموی پایش بی‌درنگ.
- اگر مدل هنگام استارت موجود نباشد، همهٔ پیش‌بینی‌ها با پیام خطا پاسخ می‌دهند بدون crash کردن process.
- امتیاز ناسا (NASA scoring function) در کد نوت‌بوک تعریف شده ولی برای اجرای LSTM نهایی لاگ نشده است؛ در فصل ارزیابی می‌توان آن را به‌عنوان کار آینده یا محاسبهٔ پسینی ذکر کرد.

جزئیات آماری کامل و مقایسه با عامل زبانی در [`Experimental_Results.md`](Experimental_Results.md) آمده است.
