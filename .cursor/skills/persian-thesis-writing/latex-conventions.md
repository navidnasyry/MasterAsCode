# قراردادهای LaTeX — قالب IUT

## ساختار پروژه

```
IUT_Theses/
├── EhsanKarimi.tex      # فایل اصلی
├── preamble.tex         # بسته‌ها و تنظیمات
├── dictionary.tex       # استایل واژه‌نامه
├── dict_acn.tex         # تعریف اختصارات و واژه‌ها
├── firstpages.tex       # صفحات ابتدایی
├── abstract.tex         # چکیده فارسی
├── chap1.tex … chap5.tex
├── references.tex
├── abstract_english.tex
└── lastpages.tex
```

**کامپایل**: XeLaTeX + BibTeX + glossaries (xindy). جزئیات در `README.md`.

## فونت و صفحه

| بخش | تنظیم |
|-----|-------|
| متن فارسی | `\settextfont{XB Zar}`، `\fontsize{12}{6}` |
| متن لاتین | `\setlatintextfont{Times New Roman}`، `\fontsize{11}{6}` |
| فاصله خط | `\baselineskip=.9cm` (بدنه) |
| حاشیه | `left=2.5cm, right=3cm, top=3cm, bottom=2.5cm` |
| شماره فصل | `\SepMark{-}` → «فصل ۱-۱» |

## واژه‌نامه و اختصارات

### تعریف در `dict_acn.tex`

```latex
% اختصار
\newacronym{LSTM}{LSTM}{Long Short-Term Memory}

% واژه با معادل فارسی
\newword{Digital Twins}{Digital Twins}{دوقلوی دیجیتال}{دوقلو‌های دیجیتال}
```

### استفاده در متن

| دستور | کاربرد |
|-------|--------|
| `\gls{key}` | اولین/عادی — معادل فارسی + پانویس |
| `\glspl{key}` | جمع |
| `\gls*{key}` | بدون پانویس (چکیده) |
| `\Gls{key}` | با حرف بزرگ |

**قبل از افزودن واژه جدید** بررسی کن در `dict_acn.tex` وجود نداشته باشد.

## متن لاتین در خط

```latex
\datasets شبیه‌سازی \lr{CMAPSS} ناسا
نویسنده \lr{Grieves (2003)}
شبکه \lr{LSTM}
```

- کد، نام فایل، URL: `\lr{...}`
- داخل `\lr` از فارسی پرهیز کن

## ارجاع و bibliograph

- فایل: `my_ref.bib`
- استایل: `ModifiedIEEEtranFa` در `references.tex`
- چند منبع: `\cite{a,b,c}` — ترتیب عددی خودکار با بسته `cite`

## عناوین

```latex
\chapter{مقدمه}
\section{بیان مسئله و ضرورت پژوهش}
\subsection{عنوان فرعی}
\subsection*{عنوان بدون شماره}  % مثلاً «اهداف کلی»
```

- `\label{chap:review}` روی `\chapter` برای ارجاع بین‌فصل

## شکل

```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.85\textwidth]{images/DT_1.png}
  \caption{ساختار مفهومی دوقلوی دیجیتال \cite{marah2024madtwin}}
  \label{fig:dt-structure}
\end{figure}
```

- `[H]` برای قرارگیری دقیق (بسته `float`)
- مسیر تصاویر: `images/`
- `\subfloat` برای زیرشکل (بسته `subfig`)

## جدول

- بسته‌های `booktabs`, `tabularray`, `makecell`, `threeparttable`
- `\toprule`, `\midrule`, `\bottomrule` برای خطوط حرفه‌ای

## فرمول

```latex
\begin{equation}
  \label{eq:loss}
  L = \|y - \hat{y}\|^2
\end{equation}
```

ارجاع: `\eqref{eq:loss}`

## فهرست‌ها

```latex
\begin{enumerate}
  \item \textbf{نگهداری واکنشی}: توضیح...
\end{enumerate}

\begin{itemize}
  \item مورد اول
\end{itemize}

\begin{descitemize}
  \item[عنوان بولد] توضیح...
\end{descitemize}
```

## محیط `\comment`

متن پیش‌نویس و یادداشت نویسنده را در `%` یا `\begin{comment}...\end{comment}` نگه دار؛ در نسخه نهایی حذف کن.

## برچسب‌ها (labels)

| نوع | پیشوند | مثال |
|-----|--------|------|
| شکل | `fig:` | `fig:dt-structure` |
| جدول | `tab:` | `tab:results` |
| فرمول | `eq:` | `eq:bias-var` |
| فصل | `chap:` | `chap:review` |
| بخش | `sec:` | `sec:method` |

## ابزارهای اختیاری

- `\usepackage[final]{showkeys}` — نمایش label در حاشیه (حالت `final` خاموش)
- `\zmakeperpage[1]{footnote}` — شماره پاورقی از ۱ در هر صفحه

## چکیده انگلیسی

محیط `\begin{latin}...\end{latin}` در `abstract_english.tex` — متن کاملاً انگلیسی، جدا از قواعد فارسی.

## بیلد واژه‌نامه

1. تعریف واژه‌ها در `dict_acn.tex`
2. از Tools → glossaries (TeXstudio) یا xindy
3. مراجع: [README.md](../../IUT_Theses/README.md)
