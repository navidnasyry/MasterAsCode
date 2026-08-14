---
name: thesis-mermaid
description: >-
  Applies IUT thesis Mermaid colors (fill #eef1f4, stroke #1f3a5f, text
  #1a1a1a) and right-aligns Persian diagram text. Use when creating or
  editing mermaid flowcharts or sequenceDiagrams for this thesis
  (method_flow.md, arch_sequence.md, or new figures).
---

# رنگ و راست‌چین نمودارهای Mermaid

مرجع: `Writing/Theses/IUT_Theses/images/method_flow.md`.

## رنگ

یک تم رسمی. پالت چندرنگ برای گره‌ها ممنوع است.

| نقش | مقدار |
|-----|--------|
| پر کردن | `#eef1f4` |
| حاشیه و خط | `#1f3a5f` |
| متن | `#1a1a1a` |
| ضخامت حاشیه | `2px` |

### flowchart

```
classDef thesis fill:#eef1f4,stroke:#1f3a5f,stroke-width:2px,color:#1a1a1a
class n1,n2,n3 thesis
```

### sequenceDiagram

`%%{init:...}%%` نگذار. رنگ را با بلوک `config` اول نمودار بگذار:

```
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
```

اگر پیش‌نمایش خطا داد، `config` را حذف کن و همان رنگ‌ها را در خروجی PNG اعمال کن.

## راست‌چین فارسی (همیشه)

متن فارسی داخل نمودار باید راست‌چین و RTL باشد.

- در برچسب گره: کل متن را در `<span dir=rtl>...</span>` بگذار.
- عنوان را با `<b>` پررنگ کن. شکست خط فقط با `<br>` (نه `<br/>`).
- از `div` و `style=` استفاده نکن.
- در `sequenceDiagram` شرکت‌کننده‌ها را طوری بنویس که **کاربر/شروع سناریو سمت راست** باشد: اول کسی را اعلام کن که باید سمت چپ دیده شود.

نمونه گره:

```
n1["<span dir=rtl><b>۱. عنوان</b><br>خط توضیح</span>"]
```
