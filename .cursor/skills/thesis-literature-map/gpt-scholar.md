بله. جست‌وجوی هدفمند برای **انتشارات سال ۲۰۲۶** انجام دادم و نتایج را بر اساس میزان نزدیکی به ترکیب‌های مدنظر شما دسته‌بندی کردم. یک نکته مهم این است که در ادبیات ۲۰۲۶، ترکیب دقیق **CMAPSS + LLM + Digital Twin** هنوز بسیار کم‌تعداد است؛ در مقابل، دو خط پژوهشی بسیار فعال‌ترند: **CMAPSS + LSTM/Transformer برای RUL** و **Digital Twin + LLM/Multi-Agent/Agentic AI**. بنابراین در فهرست زیر هم مقالات کاملاً منطبق و هم مقالاتی را که از نظر معماری به پروژه شما نزدیک‌اند آورده‌ام.

> **وضعیت جست‌وجو:** تا ۱۲ اوت ۲۰۲۶، با تمرکز روی مقالات/کنفرانس‌های منتشرشده یا نمایه‌شده در ۲۰۲۶.
> **هشدار اعتبار:** برخی نتایج ۲۰۲۶ به‌صورت preprint یا proceedings هستند؛ بنابراین آنها را از مقالات ژورنالی داوری‌شده تفکیک کرده‌ام.

---

# ۱. نزدیک‌ترین مقالات به ترکیب Digital Twin + LLM

### 1) Digital Twin AI: Opportunities and Challenges from Large Language Models to World Models

**نویسندگان:** R. Zhou, D. Chen, Z. Jia, Y. Su, Y. Liu, Y. Lu, D. Shi et al.
**سال:** 2026
**نوع:** arXiv preprint
**ارتباط:** ⭐⭐⭐⭐⭐ LLM + Digital Twin
**لینک:** [https://arxiv.org/abs/2601.01321](https://arxiv.org/abs/2601.01321)

**خلاصه:**
این مقاله یکی از منابع مهم برای معماری کلی **DT–LLM** در سال ۲۰۲۶ است. نویسندگان مسیر تکامل Digital Twin را از مدل‌های یادگیری ماشین به سمت مدل‌های زبانی بزرگ و سپس World Models بررسی می‌کنند. کاربردهای مورد بحث شامل تولید، هوافضا، رباتیک و سیستم‌های هوشمند است. برای پروژه‌ای که قصد دارد LLM را به‌عنوان لایه استدلال و تعامل روی Digital Twin قرار دهد، این مقاله بیشتر نقش **چارچوب مفهومی و نقشه راه** دارد تا یک مدل اختصاصی CMAPSS.

---

### 2) Cross-domain Digital Twin Architecture for Predictive Maintenance via Machine Learning and Large Language Models

**نویسندگان:** J. Williams, G. Jones, T. Berg, L. Birt, A. Stowe et al.
**سال:** 2026
**مجله:** *Computers & Industrial Engineering*
**ارتباط:** ⭐⭐⭐⭐⭐ DT + ML + LLM + Predictive Maintenance
**لینک:**
[https://www.sciencedirect.com/science/article/pii/S0360835226001154](https://www.sciencedirect.com/science/article/pii/S0360835226001154)

**خلاصه:**
یک معماری Digital Twin برای نگهداری پیشگویانه ارائه می‌کند که **پیام‌رسانی بلادرنگ، یادگیری نظارت‌شده، visualization و LLM روی edge** را در یک سیستم واحد ترکیب می‌کند. از نظر معماری، این مقاله یکی از نزدیک‌ترین منابع به ایده‌ای است که در آن مدل RUL مانند LSTM نقش موتور پیش‌بینی را دارد و LLM در لایه بالاتر مسئول تفسیر، توضیح و تصمیم‌یار است.

---

### 3) D2M (Design-to-Manufacturing) by Integrating Digital Twins and Large Language Models: Conceptual Framework

**نویسندگان:** Z. Zhang, J. Li, J. Xiong, D. Tang, Q. Wang, D. Guo
**سال:** 2026
**مجله:** *Digital Twin*
**ارتباط:** ⭐⭐⭐⭐⭐ DT + LLM
**لینک:**
[https://www.tandfonline.com/doi/abs/10.1080/27525783.2026.2645373](https://www.tandfonline.com/doi/abs/10.1080/27525783.2026.2645373)

**خلاصه:**
یک چارچوب مفهومی برای ادغام LLM و Digital Twin در فرایند Design-to-Manufacturing ارائه می‌کند. اگرچه CMAPSS محور اصلی آن نیست، اما برای طراحی لایه **LLM-as-Reasoner** در یک Digital Twin صنعتی بسیار مرتبط است؛ مخصوصاً برای تبدیل داده‌های ساختاریافته Twin به توضیحات، تصمیم‌ها و تعامل زبان طبیعی.

---

### 4) Generative AI-Driven Digital Twin in the Manufacturing Internet of Things: A Comprehensive Survey

**نویسندگان:** X. Fu, M. Qin, P. Pace, C. Savaglio, W. Li et al.
**سال:** 2026
**مجله:** *IEEE Internet of Things Journal*
**ارتباط:** ⭐⭐⭐⭐⭐ Generative AI + DT
**لینک:**
[https://ieeexplore.ieee.org/abstract/document/11357935/](https://ieeexplore.ieee.org/abstract/document/11357935/)

**خلاصه:**
یک مرور جامع از استفاده GenAI در Digital Twinهای صنعتی و IIoT است. تمرکز مقاله روی موضوعاتی مانند داده‌های ناهمگون، synchronization، مدل‌سازی Twin و استفاده از AI مولد برای افزایش intelligence سیستم است. برای بخش literature review پروژه شما بسیار ارزشمند است، زیرا ارتباط بین **sensor data → DT → AI/LLM → decision** را در سطح معماری بررسی می‌کند.

---

### 5) Digital Twin Designs with Generative AI: Crafting a Comprehensive Framework for Manufacturing Systems

**نویسندگان:** O. Mata, P. Ponce, C. Perez, M. Ramirez et al.
**سال:** 2026
**مجله:** *Journal of Intelligent Manufacturing*
**ارتباط:** ⭐⭐⭐⭐⭐ DT + Generative AI
**DOI:** [https://doi.org/10.1007/s10845-025-02583-8](https://doi.org/10.1007/s10845-025-02583-8)

**خلاصه:**
چارچوبی برای طراحی Digital Twinهای مجهز به Generative AI در سیستم‌های تولیدی ارائه می‌کند. نکته مهم برای کار شما، ادغام دانش انسانی و GenAI با ساختار Digital Twin است. این مقاله بیشتر برای طراحی معماری سطح سیستم مناسب است و مستقیماً مدل RUL مبتنی بر CMAPSS را هدف نمی‌گیرد.

---

# ۲. CMAPSS + Digital Twin + LSTM

### 6) Digital Twin Framework for Interpretable Aero-Engine RUL Prediction via Multi-Branch LSTM and Unity Visualization

**نویسندگان:** A. Wan, Z. Zhu, K. Al-Bukhaiti, R. Yin et al.
**سال:** 2026
**مجله:** *IEEE Transactions*
**ارتباط:** ⭐⭐⭐⭐⭐ CMAPSS/N-CMAPSS + LSTM + Digital Twin
**لینک:**
[https://ieeexplore.ieee.org/abstract/document/11491907/](https://ieeexplore.ieee.org/abstract/document/11491907/)

**خلاصه:**
از **N-CMAPSS DS01** برای پیش‌بینی Remaining Useful Life موتور هواپیما استفاده می‌کند و یک معماری **Multi-Branch LSTM** را با Digital Twin و visualization در Unity ترکیب می‌کند. این مورد از مهم‌ترین نتایج برای پروژه شماست، زیرا دقیقاً در تقاطع **Aero-engine + CMAPSS + LSTM + Digital Twin** قرار دارد. تفاوت اصلی با ایده سه‌گانه شما این است که لایه LLM در این معماری محور اصلی نیست.

---

### 7) A Digital Twin-Enabled Deep Learning Framework for Remaining Useful Life Prediction of Turbofan Engines

**نویسندگان:** N. I. Knai, B. Arun, B. V. Manikandan, S. S. Abdullah et al.
**سال:** 2026
**مجله:** *International Journal of Research and Multidisciplinary*
**ارتباط:** ⭐⭐⭐⭐⭐ CMAPSS + LSTM + Digital Twin
**لینک:**
[http://ijrm.net/index.php/ijrm/article/view/51](http://ijrm.net/index.php/ijrm/article/view/51)

**خلاصه:**
یک چارچوب Deep Learning مجهز به Digital Twin برای RUL موتورهای turbofan ارائه می‌کند و از **NASA C-MAPSS** برای ارزیابی استفاده می‌کند. LSTM هسته پیش‌بینی degradation است و Digital Twin برای ایجاد representation دیجیتال از وضعیت موتور استفاده می‌شود. از لحاظ ایده کلی، یکی از نزدیک‌ترین مقالات به ترکیب **CMAPSS + LSTM + DT** است.

---

### 8) A Physics-Informed Intelligent Digital Twin Using Multi-Task CNN–LSTM for Acoustic Emission-Based Fault Prognostics in Safety-Critical Systems

**نویسندگان:** A. Karkadakattil
**سال:** 2026
**مجله:** *Journal of Intelligent Manufacturing and Special Equipment*
**ارتباط:** ⭐⭐⭐⭐ DT + CNN-LSTM + Prognostics
**لینک:**
[https://www.emerald.com/jimse/article/7/1/33/1336171](https://www.emerald.com/jimse/article/7/1/33/1336171)

**خلاصه:**
یک Digital Twin هوشمند physics-informed را با **Multi-task CNN–LSTM** ترکیب می‌کند. کاربرد اصلی acoustic emission و fault prognostics است، بنابراین CMAPSS هسته اصلی آن نیست؛ بااین‌حال از نظر معماری برای شما بسیار مهم است، زیرا نشان می‌دهد چگونه می‌توان **مدل temporal مانند LSTM را داخل Digital Twin** قرار داد.

---

# ۳. CMAPSS + LSTM / RUL در سال ۲۰۲۶

### 9) A Multi-Class Predictive Maintenance Framework for Jet Engines Using the C-MAPSS Dataset

**نویسندگان:** B. Dong, X. Zhang, L. Hou, C. Yan, Y. Feng, W. Zhu, L. Lin
**سال:** 2026
**مجله:** *Machines*
**ارتباط:** ⭐⭐⭐⭐ CMAPSS + Bi-LSTM + Predictive Maintenance
**لینک:**
[https://www.mdpi.com/2075-1702/14/6/695](https://www.mdpi.com/2075-1702/14/6/695)

**خلاصه:**
از NASA C-MAPSS برای health assessment موتورهای جت استفاده شده و **Bidirectional LSTM** با روش‌های دیگر مقایسه می‌شود. نتایج گزارش‌شده نشان می‌دهد Bi-LSTM در subsetهای مختلف عملکرد مناسبی دارد. این مقاله برای بخش baseline پروژه شما مفید است، زیرا می‌توانید LSTM/Bi-LSTM را به‌عنوان predictive engine در معماری Digital Twin استفاده کنید.

---

### 10) Towards Decision Transformer for Remaining Useful Life Prediction: A Sequence Modeling Based Approach

**نویسندگان:** S. Shata, A. Aboelhassan
**سال:** 2026
**مجله:** *IEEE Access*
**ارتباط:** ⭐⭐⭐⭐ CMAPSS + Transformer + RUL
**لینک:**
[https://ieeexplore.ieee.org/abstract/document/11568459/](https://ieeexplore.ieee.org/abstract/document/11568459/)

**خلاصه:**
به‌جای اتکای صرف به LSTM، Decision Transformer را برای RUL بررسی می‌کند و نتایج را روی چهار subset اصلی C-MAPSS ارزیابی می‌کند. اهمیت آن برای پروژه شما این است که می‌توان LSTM را به‌عنوان baseline و Transformer/LLM را به‌عنوان نسل جدیدتر sequence modeling در نظر گرفت.

---

### 11) DiTA-RUL: Diffusion–Transformer Augmentation for CMAPSS

**نویسندگان:** Y. Tafakor, A. Jahan, R. Tavakoli et al.
**سال:** 2026
**کنفرانس:** *2026 International Conference*
**ارتباط:** ⭐⭐⭐⭐ CMAPSS + Transformer + RUL
**لینک:**
[https://ieeexplore.ieee.org/abstract/document/11620896/](https://ieeexplore.ieee.org/abstract/document/11620896/)

**خلاصه:**
از diffusion برای augmentation و Transformer برای RUL استفاده می‌کند. در معماری آن، RNN/LSTM نیز به‌عنوان مقایسه در نظر گرفته شده است. برای پروژه شما از این جهت مهم است که نشان می‌دهد **CMAPSS در حال حرکت از LSTMهای کلاسیک به Transformer-based prognostics** است؛ بنابراین می‌توان LLM را در لایه reasoning و Transformer/RUL model را در لایه prediction قرار داد.

---

### 12) Starnet: Stacked Transfer-Aware for Robust Remaining Useful Life Prediction for C-MAPSS Multi-Regime Engines

**نویسندگان:** D. Kapoor, D. Gupta, S. Agarwal, M. Uppal et al.
**سال:** 2026
**ارتباط:** ⭐⭐⭐⭐ CMAPSS + RUL + transfer learning
**لینک:**
[https://ieeexplore.ieee.org/abstract/document/11394718/](https://ieeexplore.ieee.org/abstract/document/11394718/)

**خلاصه:**
روی مسئله robustness در شرایط چندرژیمی C-MAPSS تمرکز دارد و مدل transfer-aware ارائه می‌کند. در نتایج، مدل پیشنهادی با LSTM و CNN-LSTM مقایسه شده است. مقاله مستقیماً DT/LLM ندارد، اما برای بخش **RUL prediction engine** یک گزینه مناسب برای مقایسه با LSTM محسوب می‌شود.

---

### 13) Multi-Scale Mixed-Learning and Evaluation Prediction Method for the Remaining Useful Life of Aero-Engine

**نویسندگان:** S. Chang, D. Zhao, J. Liu, H. Wang et al.
**سال:** 2026
**مجله:** *Journal of Computational Design and Engineering*
**ارتباط:** ⭐⭐⭐⭐ C-MAPSS + RUL
**لینک:**
[https://academic.oup.com/jcde/article-abstract/13/2/151/8431413](https://academic.oup.com/jcde/article-abstract/13/2/151/8431413)

**خلاصه:**
یک روش multi-scale برای RUL موتور هواپیما ارائه می‌کند و روی C-MAPSS ارزیابی شده است. مقاله به محدودیت‌هایی نظیر از دست رفتن بخشی از اطلاعات زمانی توسط مکانیزم‌های متداول LSTM اشاره دارد. برای طراحی مدل hybrid آینده، این مقاله می‌تواند به توجیه عبور از LSTM ساده به معماری‌های چندمقیاسی کمک کند.

---

# ۴. LLM + CMAPSS

### 14) LKG-STNet: A Large Language Model-Assisted Knowledge Graph-Guided Spatiotemporal Network for Aero-Engine Remaining Useful Life Prediction

**نویسندگان:** P. Qiu, J. Yan, H. Xu, Y. Yu
**سال:** 2026
**مجله:** *Advanced Engineering Informatics*
**ارتباط:** ⭐⭐⭐⭐⭐ **LLM + C-MAPSS + RUL**
**لینک:**
[https://www.sciencedirect.com/science/article/pii/S1474034626005008](https://www.sciencedirect.com/science/article/pii/S1474034626005008)

**خلاصه:**
این مقاله احتمالاً یکی از **مهم‌ترین مقالات برای ایده شما** است. از LLM برای کمک به ایجاد/استفاده از knowledge graph و سپس یک شبکه spatiotemporal برای RUL موتور هواپیما استفاده می‌کند و نتایج روی C-MAPSS گزارش شده‌اند. بنابراین برخلاف بسیاری از مقالات LLM، اینجا LLM صرفاً chatbot نیست، بلکه در pipeline پیش‌بینی degradation وارد می‌شود.

**اهمیت برای پروژه شما:** بسیار بالا؛ می‌توان معماری آن را یک گام جلوتر برد و خروجی RUL/health state را وارد Digital Twin کرد.

---

### 15) Large Language Models in Manufacturing: A Comprehensive Review

**نویسندگان:** M. Maghanaki, M. Shahin, F. F. Chen
**سال:** 2026
**مجله:** *The International Journal of Advanced Manufacturing Technology*
**ارتباط:** ⭐⭐⭐⭐ LLM + Manufacturing + CMAPSS
**DOI:** [https://doi.org/10.1007/s00170-026-18711-4](https://doi.org/10.1007/s00170-026-18711-4)

**خلاصه:**
یک مرور جامع از کاربرد LLMها در تولید است که داده‌های time-series و نمونه‌هایی مانند NASA C-MAPSS را نیز بررسی می‌کند. برای شناسایی جایگاه LLM در predictive maintenance و تفاوت آن با مدل‌های تخصصی time-series مانند LSTM منبع خوبی است.

---

# ۵. ترکیب سه‌گانه / معماری‌های بسیار نزدیک به CMAPSS + LSTM + LLM + DT

در جست‌وجوی ۲۰۲۶، **یک مقاله ژورنالی معتبر که دقیقاً هر چهار جزء CMAPSS + LSTM + LLM + Digital Twin را در یک آزمایش واحد ترکیب کرده باشد، به‌طور روشن پیدا نشد**. این نکته خودش یک یافته پژوهشی مهم است.

اما نزدیک‌ترین معماری‌ها عبارت‌اند از:

### 16) Generative AI and Digital Twin Integration for Predictive Maintenance in Industry 5.0 Manufacturing Systems: A Systematic Literature Review and Future Research Directions

**نویسندگان:** B. Paul, M. D. A. H. Abir, R. Rahman, M. D. T. A. Towfiq et al.
**سال:** 2026
**نوع:** Research Square / preprint
**ارتباط:** ⭐⭐⭐⭐⭐ GenAI + DT + Predictive Maintenance + LLM/Agents
**لینک:**
[https://www.researchsquare.com/article/rs-10590522/latest](https://www.researchsquare.com/article/rs-10590522/latest)

**خلاصه:**
مروری سیستماتیک بر ادغام Generative AI و Digital Twin برای predictive maintenance در Industry 5.0 است. به استفاده از LLM، agentها و مدل‌های زمانی برای تحلیل داده‌های صنعتی می‌پردازد و CMAPSS را نیز در بحث benchmarkها مطرح می‌کند. برای پیدا کردن **research gap** در معماری سه‌گانه شما بسیار مفید است، هرچند preprint است.

---

### 17) A Standards-Aligned Hybrid AI–Digital Twin Framework for Robust Predictive Maintenance Under Data Scarcity

**نویسندگان:** D. Park, J. Jeong, J. Kang, D. Shin
**سال:** 2026
**مجله:** *Applied Sciences*
**ارتباط:** ⭐⭐⭐⭐⭐ DT + AI + LSTM + C-MAPSS
**لینک:**
[https://www.mdpi.com/2076-3417/16/11/5303](https://www.mdpi.com/2076-3417/16/11/5303)

**خلاصه:**
چارچوب hybrid AI–Digital Twin برای predictive maintenance تحت شرایط کمبود داده ارائه می‌کند. در آن Domain-Knowledge Enhanced LSTM مطرح شده و mapping سنسورها و داده‌ها مورد توجه قرار گرفته است. مقاله برای طراحی معماری‌ای که در آن **C-MAPSS به‌عنوان digital testbed** و LSTM به‌عنوان health estimator استفاده شود بسیار مناسب است.

---

# ۶. Multi-Agent Systems + Digital Twin

### 18) Multi-Agent System-Driven Digital Twins for Predictive Maintenance: Architectures, Technologies and Open Research Challenges

**نویسندگان:** K. A. Coulibaly, M. Hamlich
**سال:** 2026
**نوع:** arXiv
**ارتباط:** ⭐⭐⭐⭐⭐ MAS + DT + Predictive Maintenance
**لینک:**
[https://arxiv.org/abs/2607.21873](https://arxiv.org/abs/2607.21873)

**خلاصه:**
یک systematic review بسیار مرتبط با ایده **Multi-Agent Digital Twin برای predictive maintenance** است. معماری‌های distributed DT، agent collaboration و کاربردهای predictive maintenance را بررسی می‌کند و C-MAPSS نیز در بحث benchmarkها ظاهر می‌شود. برای بخش معماری multi-agent پروژه شما منبع کلیدی محسوب می‌شود.

---

### 19) Self-Evolving Digital Twins in Flexible Manufacturing: A Large Language Model-Powered Multi-Agent Approach

**نویسندگان:** D. Gao, X. Wen, J. Lv, J. Si, C. Wang, J. Bao
**سال:** 2026
**مجله:** *Digital Engineering*
**ارتباط:** ⭐⭐⭐⭐⭐ **LLM + Multi-Agent + Digital Twin**
**لینک:**
[https://www.sciencedirect.com/science/article/pii/S2950550X26000129](https://www.sciencedirect.com/science/article/pii/S2950550X26000129)

**خلاصه:**
یکی از **مهم‌ترین مقالات برای ایده سه‌گانه شما** است. یک Digital Twin برای خطوط تولید انعطاف‌پذیر را با **LLM-powered Multi-Agent System** ترکیب می‌کند. عامل‌های مختلف می‌توانند وظایف تخصصی داشته باشند و LLM به coordination/reasoning کمک کند. اگر مدل RUL مبتنی بر CMAPSS را به چنین معماری‌ای متصل کنید، تقریباً به معماری پیشنهادی پژوهشی شما می‌رسید.

---

### 20) A Digital Twin Framework for Enhancing Human–Agentic AI–Machine Collaboration

**نویسندگان:** B. Nicoletti, A. Appolloni
**سال:** 2026
**مجله:** *Journal of Intelligent Manufacturing*
**ارتباط:** ⭐⭐⭐⭐⭐ Agentic AI + DT
**DOI:** [https://doi.org/10.1007/s10845-025-02637-x](https://doi.org/10.1007/s10845-025-02637-x)

**خلاصه:**
چارچوبی برای همکاری انسان، Agentic AI و ماشین با Digital Twin ارائه می‌کند. از نظر شما، اهمیت اصلی مقاله در معماری **human → agent → digital twin → physical asset** است. این ساختار می‌تواند لایه تصمیم‌گیری پس از پیش‌بینی RUL را شکل دهد.

---

### 21) Agentic Digital Twin-Embedded Maintenance Methodology for Energy Equipment: A Self-Evolving Operational Paradigm

**نویسندگان:** W. Cong, W. Tao, B. Jinsong
**سال:** 2026
**مجله:** *Journal of Manufacturing Systems*
**ارتباط:** ⭐⭐⭐⭐⭐ Agentic AI + DT + Maintenance
**لینک:**
[https://www.sciencedirect.com/science/article/pii/S027861252500281X](https://www.sciencedirect.com/science/article/pii/S027861252500281X)

**خلاصه:**
Digital Twin را درون یک maintenance methodology مبتنی بر agentic AI قرار می‌دهد و به سمت سیستم self-evolving حرکت می‌کند. نکته مهم این است که Twin صرفاً visualization نیست؛ بلکه محیطی برای مشاهده وضعیت، تصمیم‌گیری و adaptation عامل‌هاست. این مفهوم برای تبدیل RUL prediction به **autonomous maintenance decision** بسیار مهم است.

---

### 22) Digital Twin-Enabled Adaptive Robotics: Multi-Agent Reasoning over Language, Vision, and Structured Database

**نویسندگان:** S. Nambiar, O. Ikechukwu, R. Chiramel Paul et al.
**سال:** 2026
**مجله:** *Journal of Intelligent Manufacturing* / Taylor & Francis indexing
**ارتباط:** ⭐⭐⭐⭐⭐ DT + Multi-Agent + LLM + multimodal data
**DOI:** [https://doi.org/10.1080/21693277.2026.2708530](https://doi.org/10.1080/21693277.2026.2708530)

**خلاصه:**
یک Digital Twin adaptive را با **multi-agent reasoning، language، vision و structured databases** ترکیب می‌کند. از نظر معماری، بسیار نزدیک به نسل جدید سیستم‌هایی است که در آنها LLM نقش reasoning layer دارد و agentها وظایف تخصصی را انجام می‌دهند. اگر sensor/RUL data حاصل از CMAPSS یا یک engine twin به آن افزوده شود، معماری موردنظر شما قابل تصور است.

---

### 23) Agentic Digital Twins: Bridging Model-Based and AI-Driven Decision-Making Support for a New Era of Supply Chain and Operations Management

**نویسنده:** D. Ivanov
**سال:** 2026
**مجله:** *International Journal of Production Research*
**ارتباط:** ⭐⭐⭐⭐⭐ Agentic AI + DT + decision support
**لینک:**
[https://www.tandfonline.com/doi/abs/10.1080/00207543.2026.2630277](https://www.tandfonline.com/doi/abs/10.1080/00207543.2026.2630277)

**خلاصه:**
مفهوم Agentic Digital Twin را برای تصمیم‌گیری در سیستم‌های پیچیده معرفی می‌کند. ارزش مقاله برای کار شما این است که Digital Twin را از یک مدل passive به یک محیط **model-based + AI-driven decision-making** تبدیل می‌کند؛ دقیقاً همان جهتی که می‌توان بعد از پیش‌بینی RUL دنبال کرد.

---

# ۷. مقالات تکمیلی مهم

### 24) Integrating Digital Twins, Data Management and Artificial Intelligence for Predictive Maintenance in Aviation: A Comprehensive Review

**نویسندگان:** S. Mehdipour, A. Habibzadeh, N. Esmi et al.
**سال:** 2026
**مجله:** *Digital Twins and Applications* / Wiley
**ارتباط:** ⭐⭐⭐⭐⭐ Aviation + DT + AI + C-MAPSS
**لینک:**
[https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/dgt2.70029](https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/dgt2.70029)

**خلاصه:**
مروری تخصصی بر predictive maintenance در هوانوردی، Digital Twin، AI و benchmarkهایی نظیر C-MAPSS است. برای ساخت بخش مرور ادبیات هوافضایی پروژه شما بسیار مناسب است و نشان می‌دهد C-MAPSS چگونه می‌تواند به‌عنوان bridge بین مدل‌های آزمایشگاهی RUL و معماری Digital Twin استفاده شود.

---

### 25) A Novel Framework for Secure and Interoperable Digital Twins in the Industrial Metaverse

**نویسندگان:** V. G. Menon et al.
**سال:** 2026
**مجله:** *Enterprise Information Systems*
**ارتباط:** ⭐⭐⭐⭐ C-MAPSS + LSTM + DT
**لینک:**
[https://www.tandfonline.com/doi/abs/10.1080/17517575.2026.2659635](https://www.tandfonline.com/doi/abs/10.1080/17517575.2026.2659635)

**خلاصه:**
چارچوبی برای Digital Twinهای امن و interoperable ارائه می‌کند و C-MAPSS، LSTM و Digital Twin را در مثال‌ها/معماری مطرح می‌کند. برای پروژه‌هایی که علاوه بر prediction به synchronization، interoperability و deployment فکر می‌کنند مفید است.

---

### 26) Digital Twin-Assisted Multi-Objective Optimization Method Based on Multi-Agent Reinforcement Learning for Five-Axis CNC Machining

**نویسندگان:** J. Li, J. Li, X. Zhou, J. An
**سال:** 2026
**مجله:** *Processes*
**ارتباط:** ⭐⭐⭐⭐ DT + Multi-Agent RL
**لینک:**
[https://www.mdpi.com/2227-9717/14/13/2139](https://www.mdpi.com/2227-9717/14/13/2139)

**خلاصه:**
Digital Twin را با Multi-Agent Reinforcement Learning برای optimization فرایند ماشین‌کاری ترکیب می‌کند. CMAPSS و LSTM در آن محور اصلی نیستند، ولی از نظر **DT → agents → optimization/action** مکمل بسیار خوبی برای معماری predictive-maintenance شماست.

## جمع‌بندی مقایسه‌ای

| ترکیب | وضعیت ادبیات ۲۰۲۶ | نمونه شاخص |
| --- | --- | --- |
| **CMAPSS + LSTM** | بسیار فعال | Dong et al.; Chang et al. |
| **CMAPSS + Transformer** | بسیار فعال | DiTA-RUL; Decision Transformer |
| **CMAPSS + LLM** | نوظهور | **LKG-STNet** |
| **CMAPSS + Digital Twin** | فعال | DT-enabled RUL frameworks |
| **CMAPSS + LSTM + Digital Twin** | وجود دارد | **Wan et al.** |
| **LLM + Digital Twin** | بسیار فعال | Zhou et al.; Williams et al. |
| **Digital Twin + Multi-Agent** | بسیار فعال | Coulibaly; Cong et al. |
| **LLM + Multi-Agent + Digital Twin** | بسیار جدید و فعال | **Gao et al.** |
| **CMAPSS + LLM + Digital Twin** | بسیار کم | عمدتاً شکاف پژوهشی |
| **CMAPSS + LSTM + LLM + DT** | بسیار کم/فاقد نمونه روشن | **فرصت پژوهشی قوی** |
| **CMAPSS + LSTM + LLM + DT + MAS** | تقریباً شکاف پژوهشی | **فرصت پژوهشی بسیار قوی** |

### اولویت پیشنهادی برای مطالعه عمیق

1. **LKG-STNet** — CMAPSS + LLM + RUL
2. **Digital Twin Framework for Interpretable Aero-Engine RUL Prediction...** — CMAPSS/N-CMAPSS + LSTM + DT
3. **Self-Evolving Digital Twins...** — LLM + MAS + DT
4. **Multi-Agent System-Driven Digital Twins for Predictive Maintenance** — MAS + DT
5. **Cross-domain Digital Twin Architecture...** — DT + ML + LLM + PdM
6. **Digital Twin AI: Opportunities and Challenges...** — DT + LLM/World Models
7. **A Standards-Aligned Hybrid AI–Digital Twin Framework...** — AI/LSTM + DT + PdM
8. **Generative AI and Digital Twin Integration...** — GenAI + DT + PdM

**نکته روش‌شناختی:** برای استناد در پایان‌نامه، وضعیت نهایی publication و DOI هر مورد قبل از citation نهایی بررسی شود.
