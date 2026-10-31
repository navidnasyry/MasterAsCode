# سرویس پیش‌بینی عمر مفید باقیمانده (LSTM RUL API)

مسیر کد: `Implementation/lstm-rul-api/`  
نوت‌بوک مرجع آموزش: `Implementation/jupyter-notebook/main_lstm_1_v3_loss_function_changed.ipynb`  
مدل استقرار‌یافته: `lstm-rul-api/AiModels/LSTM/LSTM_ATTENTION_LossChanged_V3`

---

## بخش ۱: روش‌شناسی (Methodology)

### ۱.۱ مسئله

پیش‌بینی عمر مفید باقیمانده (\(\mathrm{RUL}\)) برای موتورهای توربوفن شبیه‌سازی‌شده در زیرمجموعه \(\mathrm{FD001}\) از مجموعه داده \(\mathrm{CMAPSS}\) به‌صورت رگرسیون روی پنجره‌های زمانی حسگرها فرموله می‌شود. برای هر نمونه با ورودی \(\mathbf{X}\in\mathbb{R}^{w\times d}\) مدل مقدار \(\hat{y}\) را در آخرین گام پنجره تخمین می‌زند.

| نماد | مقدار در پژوهش |
|------|----------------|
| \(w\) | ۵۰ چرخه |
| \(d\) | ۱۶ ویژگی در هر گام (شامل حسگرهای منتخب و `cycle_norm`) |
| هدف | \(\mathrm{RUL}\) خام (بدون سقف‌گذاری piecewise) |

### ۱.۲ پیش‌پردازش داده

1. **حذف ستون‌های ثابت:** `TRA`, `T2`, `P2`, `epr`, `farB`, `Nf_dmd`, `PCNfR_dmd`
2. **حذف ویژگی‌های کم‌اطلاع / تکراری:** `setting_1`, `setting_2`, `P15`, `NRc` (همبستگی \(\mathrm{Nc}\)–\(\mathrm{NRc}\) ≈ ۰٫۹۶)
3. **برچسب‌گذاری آموزش:** \(y^{(i)}(t)=t^{(i)}_{\mathrm{end}}-t\)
4. **برچسب‌گذاری آزمون:** ادغام با `RUL_FD001.txt`
5. **هنجارسازی Min-Max** فقط روی داده آموزشی؛ اعمال همان پارامترها روی آزمون
6. **ساخت توالی:** پنجره لغزنده ۵۰؛ صفرگذاری ابتدای دنباله‌های کوتاه

جزئیات تحلیلی در فصل روش‌شناسی پایان‌نامه و خروجی‌های نوت‌بوک (`describe`, نقشه همبستگی) مستند شده است.

### ۱.۳ معماری شبکه

شبکه با API تابعی Keras ساخته می‌شود:

| لایه | تنظیمات |
|------|---------|
| Input | `(50, 16)` |
| LSTM ۱ | ۱۰۰ واحد، `return_sequences=True` |
| Dropout ۱ | ۰٫۲ |
| LSTM ۲ | ۵۰ واحد، `return_sequences=True` |
| Dropout ۲ | ۰٫۲ |
| AttentionLayer | وزن زمانی \(\alpha\) + بردار زمینه |
| Dense | ۱ واحد، فعال‌سازی خطی |
| مجموع پارامترها | ≈ ۷۷٬۱۵۱ |

لایه توجه امتیاز زمانی را با \(\tanh\) و Softmax محاسبه می‌کند و بردار زمینه را به‌صورت جمع وزن‌دار گام‌ها می‌سازد. همین وزن‌ها مبنای توضیح‌پذیری سهم حسگرها در سرویس پیش‌بینی هستند.

### ۱.۴ تابع زیان سفارشی (Pinball / Quantile)

به‌جای MSE، تابع زیان Pinball با پارامتر \(\tau=0.125\) به‌کار می‌رود. با تعریف \(e=y_{\mathrm{true}}-y_{\mathrm{pred}}\):

\[
L_\tau(e)=\max\big(\tau\, e,\;(\tau-1)\, e\big)
\]

برای \(\tau<0.5\) جریمه بیش‌برآورد (\(\hat{y}>y\)) سنگین‌تر از کم‌برآورد است. در \(\tau=0.125\) وزن بیش‌برآورد برابر \(0.875\) و وزن کم‌برآورد برابر \(0.125\) است؛ یعنی بیش‌برآورد حدود هفت برابر بیشتر جریمه می‌شود. هدف تئوریک: سوق دادن خطا به سمت کم‌برآورد محافظه‌کارانه در نگهداری پیش‌بینانه.

> توجه: در برخی بخش‌های نگارش مفهومی پایان‌نامه از فرم وزن‌دار مربعی با \(\alpha,\beta\) نیز صحبت شده است؛ **پیاده‌سازی آموزش واقعی در نوت‌بوک v3 و مدل استقرار‌یافته مبتنی بر Pinball با \(\tau=0.125\) است.**

### ۱.۵ هایپرپارامترهای آموزش

| پارامتر | مقدار |
|---------|--------|
| Optimizer | RMSprop (نرخ یادگیری پیش‌فرض Keras ≈ ۰٫۰۰۱) |
| Loss | Pinball / `PinballLoss(tau=0.125)` |
| Metrics | MAE، \(R^2\) سفارشی (`r2_keras`) |
| Batch size | ۲۰۰ |
| Epochs | ۶۰ |
| Validation split | ۰٫۰۵ |
| Sequence length | ۵۰ |

### ۱.۶ توضیح‌پذیری

پس از پیش‌بینی، مدل میانی Keras خروجی لایه Attention را می‌گیرد. سهم نسبی حسگرها از بردار زمینه نرمال‌سازی می‌شود (با حذف شناسه موتور، شماره چرخه و `cycle_norm`) و \(k\) حسگر برتر به API بازگردانده می‌شود. عامل زبانی از این فهرست برای روایت فارسی استفاده می‌کند.

---

## بخش ۲: پیاده‌سازی (Implementation)

### ۲.۱ پشته فناوری

| جزء | فناوری |
|-----|--------|
| API | FastAPI ۰٫۱۱۵ + Uvicorn ۰٫۳۲ |
| ML | TensorFlow ۲٫۱۷، scikit-learn ۱٫۵٫۲، NumPy، Pandas |
| تصویر Docker | `python-api:2.0.0` |
| پورت میزبان | **۸۰۰۰** |

### ۲.۲ ساختار ماژول‌ها

| مسیر | نقش |
|------|-----|
| `app/main.py` | ساخت اپ، CORS، اتصال روترها |
| `app/api/routes_health.py` | سلامت سرویس |
| `app/api/routes_prediction.py` | بارگذاری مدل در import و نقاط پیش‌بینی |
| `app/models/lstm_model.py` | `AttentionLayer`، `load_lstm_model` |
| `app/services/prediction_service.py` | آماده‌سازی توالی، پیش‌بینی، attribution |
| `app/schemas/prediction_schemas.py` | مدل‌های Pydantic |
| `app/core/config.py` | مسیر مدل |
| `app/core/utils.py` | متریک `r2_keras` |

### ۲.۳ تکه‌کد تعریف لایه توجه و بارگذاری مدل

```python
class AttentionLayer(Layer):
    def call(self, x):
        e = K.tanh(K.dot(x, self.W) + self.b)
        alpha = K.softmax(e, axis=1)
        context = K.sum(alpha * x, axis=1)
        return context, alpha
```

مدل از فایل `.h5` با `custom_objects={'r2_keras': r2_keras, 'AttentionLayer': AttentionLayer}` بارگذاری می‌شود؛ همراه با `_history.pkl` و `_data.pkl` (شامل `lstm_test_df`, `sequence_length`, `sequence_cols`).

### ۲.۴ تکه‌کد تابع زیان در نوت‌بوک آموزش

```python
def pinball_loss(tau=0.2):
    def loss(y_true, y_pred):
        error = y_true - y_pred
        return K.mean(K.maximum(tau * error, (tau - 1) * error), axis=-1)
    return loss

tau = 0.125
model.compile(loss=pinball_loss(tau=tau), optimizer='rmsprop', metrics=['mae', r2_keras])
```

### ۲.۵ نقاط پایانی API

پایه: `http://<host>:8000`

| روش | مسیر | ورودی | خروجی موفق |
|-----|------|--------|------------|
| GET | `/api/health` | — | `{"status":"ok"}` |
| GET | `/api/predict/predict_rul/{engine_number}` | `k_most_effictive` (پیش‌فرض ۵) | `engine_number`, `predicted_rul`, `sensor_impacts[]` |
| GET | `/api/predict/engines_with_low_rul/` | `threshold` (پیش‌فرض ۵۰)، `until_clock?` | فهرست موتورهای کم‌RUL |
| POST | `/api/predict/predict_new_engine_rul/` | `{"data":[[...],...]}` | `predicted_rul` |

نمونه پاسخ پیش‌بینی:

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

پارامتر `until_clock` فقط داده‌های تا چرخه مشخص را برای شبیه‌سازی جریان زمان در عامل پایش به‌کار می‌برد.

### ۲.۶ مدیریت خطا

- شکست بارگذاری مدل در راه‌اندازی → `model=None` و پاسخ `{"error":"Model not loaded."}`
- موتور ناموجود → `{"error":"Engine number N not found."}`
- ابعاد نادرست در POST → پیام خطای تعداد ویژگی
- الگوی غالب: بازگرداندن JSON خطا با HTTP ۲۰۰ (soft error) به‌جای HTTPException

### ۲.۷ یکپارچه‌سازی

| مصرف‌کننده | نحوه اتصال |
|------------|------------|
| Dify (عامل زبانی) | `env.lstm_host_addr` → درخواست‌های HTTP GET |
| engine-monitor | `REACT_APP_API_BASE_URL=http://${HOST_IP}:8000/api` |
| Volume مدل | `./AiModels` → `/app/AiModels` |

---

## بخش ۳: ارزیابی و نتایج (Results)

جزئیات عددی کامل در [`Experimental_Results.md`](Experimental_Results.md) آمده است. خلاصه آزمون روی ۱۰۰ موتور \(\mathrm{FD001}\):

| معیار | LSTM پایه (MSE) | LSTM v3 (Pinball + Attention) |
|-------|-----------------|-------------------------------|
| MAE آزمون | ۱۷٫۵۶ | **۱۷٫۲۱** |
| \(R^2\) آزمون | ۰٫۲۴ | **۰٫۷۱** |
| RMSE آزمون | — | ۲۲٫۹۲ |
| نسبت کم‌برآورد | ۴۷٪ | **۸۷٪** |

نمودارهای آموزش/اعتبارسنجی (Loss، MAE، \(R^2\)) در خروجی سلول‌های `lstm_test_evaluation_graphs` نوت‌بوک v3 تولید می‌شوند و برای فصل ارزیابی پایان‌نامه قابل استخراج‌اند.

### رفتار حالت خاص

- با `until_clock` کوچک، داده ناکافی → صفرگذاری توالی؛ پیش‌بینی ممکن است محافظه‌کارانه‌تر شود.
- آستانه پیش‌فرض API برای کم‌RUL برابر ۵۰ است؛ در Dify معمولاً `threshold=30` تنظیم می‌شود (دو منبع پیکربندی جدا).
