# دیاگرام توالی تعامل عامل‌ها برای پرس‌وجوی پیش‌بینی RUL

این شکل **دیاگرام توالی (sequenceDiagram)** است. سناریو: کاربر با زبان طبیعی عمر مفید باقیمانده موتور k را می‌پرسد. عامل زبانی به مدل LSTM دسترسی مستقیم ندارد و فقط از طریق عامل دوقلو و عامل پیش‌بینی عمل می‌کند.

شرکت‌کننده‌ها از راست به چپ چیده شده‌اند تا خوانش فارسی راست‌چین باشد.

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#eef1f4"
    primaryTextColor: "#1a1a1a"
    primaryBorderColor: "#1f3a5f"
    lineColor: "#1f3a5f"
    actorBkg: "#eef1f4"
    actorBorder: "#1f3a5f"
    actorTextColor: "#1a1a1a"
    signalColor: "#1f3a5f"
    signalTextColor: "#1a1a1a"
    noteBkgColor: "#eef1f4"
    noteBorderColor: "#1f3a5f"
    noteTextColor: "#1a1a1a"
---
sequenceDiagram
    autonumber
    participant M as "عامل پایش"
    participant P as "عامل پیش‌بینی RUL"
    participant D as "عامل دوقلوی دیجیتال"
    participant L as "عامل تعامل زبانی"
    actor U as "کاربر"

    U->>L: پرسش زبان طبیعی RUL موتور k چیست
    Note over L: ترجمه به فراخوان ابزار بدون دسترسی مستقیم به LSTM
    L->>D: درخواست وضعیت و پیش‌بینی موتور k
    D->>P: ارسال پنجره حسگرهای هنجارشده
    P-->>D: RUL تخمینی و اهمیت حسگرها
    D->>M: انتشار مقدار RUL
    M-->>D: حالت عادی یا هشدار یا بحرانی
    D-->>L: وضعیت زنده و RUL و حالت پایش
    L-->>U: پاسخ زبان طبیعی توضیح‌پذیر
```

## نسخه فشرده (فقط مسیر پرس‌وجو)

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#eef1f4"
    primaryTextColor: "#1a1a1a"
    primaryBorderColor: "#1f3a5f"
    lineColor: "#1f3a5f"
    actorBkg: "#eef1f4"
    actorBorder: "#1f3a5f"
    actorTextColor: "#1a1a1a"
    signalColor: "#1f3a5f"
    signalTextColor: "#1a1a1a"
    noteBkgColor: "#eef1f4"
    noteBorderColor: "#1f3a5f"
    noteTextColor: "#1a1a1a"
---
sequenceDiagram
    autonumber
    participant P as "عامل پیش‌بینی RUL"
    participant D as "عامل دوقلوی دیجیتال"
    participant L as "عامل تعامل زبانی"
    actor U as "کاربر"

    U->>L: RUL موتور k چیست
    L->>D: درخواست پیش‌بینی موتور k
    D->>P: پنجره حسگرهای موتور k
    P-->>D: RUL و اهمیت حسگرها
    D-->>L: وضعیت زنده و RUL
    L-->>U: پاسخ توضیح‌پذیر
```

## نسخه گسترش‌یافته (سناریوی سرتاسری)

از ورود چرخه تا پرسش «چرا RUL کاهش یافته است».

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryColor: "#eef1f4"
    primaryTextColor: "#1a1a1a"
    primaryBorderColor: "#1f3a5f"
    lineColor: "#1f3a5f"
    actorBkg: "#eef1f4"
    actorBorder: "#1f3a5f"
    actorTextColor: "#1a1a1a"
    signalColor: "#1f3a5f"
    signalTextColor: "#1a1a1a"
    noteBkgColor: "#eef1f4"
    noteBorderColor: "#1f3a5f"
    noteTextColor: "#1a1a1a"
---
sequenceDiagram
    autonumber
    participant L as "عامل تعامل زبانی"
    actor U as "کاربر"
    participant M as "عامل پایش"
    participant P as "عامل پیش‌بینی RUL"
    participant D as "عامل دوقلوی دیجیتال"
    participant I as "لایه ادغام"
    participant S as "عامل شبیه‌سازی"

    S->>I: چرخه t موتور k
    I->>D: پنجره هنجارشده
    D->>P: درخواست پیش‌بینی
    P-->>D: RUL و اهمیت حسگرها
    D->>M: انتشار RUL
    M-->>D: حالت پایش
    U->>L: چرا RUL موتور k کاهش یافته است
    L->>D: پرس‌وجوی وضعیت و توضیح
    D-->>L: RUL و حالت پایش و حسگرهای مؤثر
    L-->>U: توضیح زبان طبیعی
```

برای عنوان فعلی شکل در فصل ۳، **نمودار اول یا فشرده** مناسب‌تر است.

## راهنمای تبدیل به تصویر

- خروجی: `images/arch_sequence.png` (حداقل ۳۰۰ dpi)
- پس از ساخت فایل، در `chap3.tex` مسیر این شکل را از `images/DT_1.png` به `images/arch_sequence.png` تغییر دهید
