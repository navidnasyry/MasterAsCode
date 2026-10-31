# دیاگرام توالی تعامل عامل‌ها برای پرس‌وجوی پیش‌بینی عمر مفید باقیمانده

این شکل **دیاگرام توالی (sequenceDiagram)** است. سناریو: کاربر با زبان طبیعی عمر مفید باقیمانده موتور k را می‌پرسد. عامل زبانی به مدل LSTM دسترسی مستقیم ندارد و فقط از طریق عامل دوقلو و عامل پیش‌بینی عمل می‌کند.

ترتیب `participant` از چپ به راست است تا **کاربر سمت راست** قرار گیرد.

## تبدیل آنلاین به PNG/SVG

1. برو به [mermaid.live](https://mermaid.live)
2. محتوای یکی از فایل‌های زیر را باز کن و **همه را** در ویرایشگر بچسبان:
   - **فشرده:** `arch_sequence_compact.mmd`
   - **کامل (با عامل پایش):** `arch_sequence_full.mmd`
3. از منوی Actions گزینه **PNG** یا **SVG** را بگیر
4. فایل را با نام `arch_sequence.png` در همین پوشه ذخیره کن

> Mermaid در sequenceDiagram HTML و کاراکتر RTL نامرئی را پشتیبانی نمی‌کند؛ متن فارسی ساده داخل `"..."` کافی است. اگر متن در PNG کمی چپ‌چین بود، SVG را در Inkscape باز کن و روی متن `direction: rtl` بگذار.

---

## نسخه فشرده (فقط مسیر پرس‌وجو)

فایل آماده: `arch_sequence_compact.mmd`

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#eef1f4",
    "primaryTextColor": "#1a1a1a",
    "primaryBorderColor": "#1f3a5f",
    "lineColor": "#1f3a5f",
    "actorBkg": "#eef1f4",
    "actorBorder": "#1f3a5f",
    "actorTextColor": "#1a1a1a",
    "signalColor": "#1f3a5f",
    "signalTextColor": "#1a1a1a",
    "noteBkgColor": "#eef1f4",
    "noteBorderColor": "#1f3a5f",
    "noteTextColor": "#1a1a1a"
  }
}}%%
sequenceDiagram
    autonumber
    participant P as "عامل پیش‌بینی عمر مفید باقیمانده"
    participant D as "عامل دوقلوی دیجیتال"
    participant L as "عامل تعامل زبانی"
    actor U as "کاربر"

    U->>L: عمر مفید باقیمانده موتور k چیست؟
    L->>D: درخواست پیش‌بینی موتور k
    D->>P: پنجره حسگرهای موتور k
    P-->>D: عمر مفید باقیمانده و اهمیت حسگرها
    D-->>L: وضعیت زنده و عمر مفید باقیمانده
    L-->>U: پاسخ توضیح‌پذیر
```

## نسخه کامل (با عامل پایش)

فایل آماده: `arch_sequence_full.mmd`

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#eef1f4",
    "primaryTextColor": "#1a1a1a",
    "primaryBorderColor": "#1f3a5f",
    "lineColor": "#1f3a5f",
    "actorBkg": "#eef1f4",
    "actorBorder": "#1f3a5f",
    "actorTextColor": "#1a1a1a",
    "signalColor": "#1f3a5f",
    "signalTextColor": "#1a1a1a",
    "noteBkgColor": "#eef1f4",
    "noteBorderColor": "#1f3a5f",
    "noteTextColor": "#1a1a1a"
  }
}}%%
sequenceDiagram
    autonumber
    participant M as "عامل پایش"
    participant P as "عامل پیش‌بینی عمر مفید باقیمانده"
    participant D as "عامل دوقلوی دیجیتال"
    participant L as "عامل تعامل زبانی"
    actor U as "کاربر"

    U->>L: پرسش زبان طبیعی عمر مفید باقیمانده موتور k چیست
    Note over L: ترجمه به فراخوان ابزار بدون دسترسی مستقیم به LSTM
    L->>D: درخواست وضعیت و پیش‌بینی موتور k
    D->>P: ارسال پنجره حسگرهای هنجارشده
    P-->>D: عمر مفید باقیمانده تخمینی و اهمیت حسگرها
    D->>M: انتشار مقدار عمر مفید باقیمانده
    M-->>D: حالت عادی یا هشدار یا بحرانی
    D-->>L: وضعیت زنده و عمر مفید باقیمانده و حالت پایش
    L-->>U: پاسخ زبان طبیعی توضیح‌پذیر
```

برای عنوان فعلی شکل در فصل ۳، **نسخه فشرده** مناسب‌تر است.

## راهنمای LaTeX

- خروجی: `images/arch_sequence.png` (حداقل ۳۰۰ dpi)
- در `chap3.tex` مسیر شکل: `images/arch_sequence.png`
