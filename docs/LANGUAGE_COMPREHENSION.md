# Language Comprehension Profiles

Tài liệu này định nghĩa cách đánh giá **dễ hiểu tự nhiên theo chính ngôn ngữ output** cho documentary narration.

Mục tiêu không phải dịch jargon sang một ngôn ngữ khác bằng mọi giá. Mục tiêu là để một **native general-audience viewer** hiểu được narration khi nghe lần đầu, không cần kiến thức chuyên ngành và không cần dừng video để tra cứu.

Supported profiles:

- Vietnamese — `vi`
- English — `en`
- German — `de`
- French — `fr`
- Spanish — `es`
- Korean — `ko`
- Japanese — `ja`

Nếu language khác danh sách trên, dùng General profile và giữ register/locale của input.

---

## General profile — áp dụng cho mọi ngôn ngữ

### Native cold-reader model

Giả định viewer:

- là native speaker hoặc fluent speaker của output language;
- có trình độ phổ thông;
- tò mò nhưng không phải specialist;
- chưa đọc Research;
- đang **nghe**, không đọc paper;
- không thể dừng video để tra một term.

### Core doctrine

1. **Meaning first, label second.**
2. **Function before taxonomy.**
3. Giữ technical label chỉ khi viewer có lợi từ việc biết tên đó.
4. Không giữ term chỉ vì source hoặc paper dùng nó.
5. Không dùng foreign borrowing chỉ vì nó nghe “chuyên môn”.
6. Không thay một technical term bằng wording đơn giản nếu wording đó làm sai mechanism.
7. CORE term phải được hiểu trước khi trở thành mắt xích trong lập luận.
8. SUPPORTING term nên giải thích ngắn hoặc thay bằng wording phổ thông.
9. DISPENSABLE term nên bỏ label.
10. Nếu term chỉ xuất hiện một lần và label không quan trọng, ưu tiên bỏ label.

### Required post-draft scan

Sau khi Draft được viết, **không được chỉ dựa vào Audience Vocabulary Map từ Research**.

Phải extract mọi term thực sự xuất hiện trong Draft có thể gây comprehension risk:

- technical / academic term;
- acronym;
- discipline-specific phrase;
- foreign-language borrowing;
- untranslated English;
- rare compound;
- research-method word;
- abstract label;
- terminology invented during Draft mà Research chưa dự đoán.

Với mỗi term, quyết định:

`KEEP | EXPLAIN | REPLACE | REMOVE`

### Register consistency

Giữ:

- mức độ trang trọng;
- cách xưng hô;
- regional variant nếu user đã chỉ định;
- spoken conventions tự nhiên của output language.

Không lấy English/Vietnamese làm chuẩn chung cho rhythm hoặc sentence construction.

---

## Vietnamese — vi

### Main risks

- code-switching English không cần thiết;
- academic/research-note vocabulary;
- từ Hán-Việt đúng nhưng dày đặc và khó nghe;
- dùng English label thay vì wording Việt tự nhiên;
- một-liner quá dày kiểu AI documentary.

### Watch for

Ví dụ thường cần kiểm:

- `feedback loop`
- `gradient`
- `pattern`
- `population`
- `lineage`
- `selection`
- `paper`
- `dataset`
- `reconstruction`
- `contrast`
- `niche`

Không cấm tuyệt đối. Giữ khi label thật sự cần và đã được giải thích.

### Preferred behavior

- `population` → `quần thể`
- `lineage` → `dòng tổ tiên / dòng di truyền`
- `selection` → `chọn lọc`
- `feedback loop` → diễn đạt quan hệ tác động qua lại
- `reconstruction` → `cách tái dựng`
- `pattern` → `mô hình / kiểu / xu hướng` tùy nghĩa

Không dịch tên khoa học/proper noun chỉ để tránh ngoại ngữ.

---

## English — en

### Main risks

English scientific terminology often looks “normal” because source papers are in English. Do not assume it is general-audience language.

Watch for:

- Latinate academic wording;
- nominalization chains;
- dense noun phrases;
- methodology language;
- unnecessary abbreviation;
- paper-like syntax instead of spoken narration.

Examples to question:

- utilization
- facilitation
- subsequent dispersal
- population differentiation
- anthropogenic modification
- phenotypic variation

Prefer verbs and concrete causal phrasing when meaning stays intact.

Example:

`anthropogenic niche exploitation`
→ `wildcats took advantage of a new hunting ground created by human settlements`

Do not replace a familiar scientific word merely because it is technical. Replace/explain it only when a general viewer needs prior knowledge to understand the sentence.

---

## German — de

### Main risks

- long technical compounds;
- `Nominalstil`;
- multiple abstract nouns in one clause;
- bureaucratic written syntax;
- deep subordinate-clause nesting;
- unnecessary English technical borrowings.

Question terms such as:

- Populationsdifferenzierung
- Nahrungsressourcennutzung
- Domestizierungsprozess
- Selektionsdruck
- Verhaltensanpassung

A correct compound is not automatically good spoken narration.

### Preferred behavior

If a technical compound contains several conceptual parts, ask whether a verb phrase is clearer.

Example:

`Nahrungsressourcennutzung`
→ `Die Tiere nutzten diese neue Nahrungsquelle.`

`Domestizierungsprozesse führten zu Verhaltensanpassungen.`
→ `Über viele Generationen passten sich die Tiere immer stärker an das Leben mit Menschen an.`

Preserve natural German documentary rhythm; do not mechanically imitate short English sentence patterns.

---

## French — fr

### Main risks

- academic nominalization;
- highly written/formal syntax in spoken narration;
- English calques;
- unnecessary Anglicisms;
- strings of abstract nouns.

Question both English borrowings and correct-but-opaque French scientific labels.

Examples:

- commensalisme
- phylogénétique
- introgression
- différenciation des populations
- dispersion ultérieure

### Preferred behavior

Explain the mechanism in ordinary French before the label.

Example:

`Ces chats sauvages ont commencé à vivre près des humains parce qu'ils y trouvaient davantage de proies. Les biologistes parlent ici d'une relation commensale.`

Do not keep `pattern`, `feedback loop`, `dataset`, `cluster` in English when natural French wording is clearer.

---

## Spanish — es

### Default locale

Nếu user không chỉ định vùng, dùng **español internacional / neutral**.

Nếu user chỉ định Spain, Mexico, Argentina, Colombia hoặc variant khác, giữ vocabulary/register của variant đó.

### Main risks

- English calques;
- academic nominalization;
- technical cognates that look easy but are not;
- false friends;
- regional vocabulary drift;
- literal translation of English narration style.

Watch for context-sensitive false-friend/calque risk around words such as:

- eventualmente
- realizar
- soportar
- evidencia

Do not ban these words; verify that they mean what the sentence intends in natural Spanish.

### Preferred behavior

`diferenciación poblacional`
may be replaced first with:

`Con el paso de las generaciones, esos grupos empezaron a cambiar de forma distinta.`

Keep the technical label only if the video benefits from teaching it.

---

## Korean — ko

### Main risks

- dense Sino-Korean scientific vocabulary;
- multiple new technical nouns in one sentence;
- untranslated English/acronyms;
- inconsistent speech level;
- written academic style that sounds unnatural aloud.

Examples requiring audience judgment:

- 개체군
- 선택압
- 유전적 분화
- 공생 관계
- 미토콘드리아 DNA

A viewer may be able to pronounce a Sino-Korean term without actually understanding the concept.

### Preferred behavior

Use:

`plain Korean explanation → Korean technical term if useful → acronym only if reused`

Example:

`야생 고양이는 사람들이 만든 마을 주변에서 먹이를 쉽게 구할 수 있었습니다. 이런 식으로 인간 주변에서 이익을 얻으며 살아가는 관계를 연구자들은 공생 관계라고 부릅니다.`

### Register

Keep one narration register consistently.

Do not casually mix:

- 합니다체
- 해요체
- plain written `한다` style

unless the original project deliberately uses a mixed stylistic device.

---

## Japanese — ja

### Main risks

- high kanji density;
- dense Sino-Japanese technical compounds;
- unnecessary katakana English loans;
- academic written syntax;
- inconsistent `です・ます` vs `だ・である` register.

Examples requiring audience judgment:

- 個体群
- 選択圧
- 遺伝的分化
- コメンサリズム
- フィードバックループ

### Preferred behavior

Use:

`plain explanation → Japanese technical term only if useful`

Example:

`世代を重ねるうちに、集団の遺伝的な特徴にも少しずつ違いが生まれました。`

may be clearer than a dense phrase like:

`遺伝的集団分化が進行しました。`

Avoid katakana terminology when natural Japanese explanation carries the meaning better.

### Register

Choose and preserve one narration register:

- `です・ます`, or
- `だ・である`

Do not drift between them without a deliberate reason.

---

## Research Vocabulary Map fields

For supported languages, each likely technical term should track:

- `Term`
- `Importance`: `CORE | SUPPORTING | DISPENSABLE`
- `Plain-language meaning`
- `Native preferred wording`
- `Common to general audience?`: `YES | MAYBE | NO`
- `Foreign label necessary?`: `YES | OPTIONAL | NO`
- `Register risk`
- `Risk if simplified`

`Native preferred wording` must be written in the output language, not translated through English unless English is the output language.

---

## Draft Term Inventory

After Draft generation, extract actual risky terms from the narration.

Minimum fields:

| Term actually used | In Research Map? | Audience risk | Native/spoken naturalness | Action | Replacement / first-use explanation |
|---|---|---|---|---|---|

Actions:

- `KEEP`
- `EXPLAIN`
- `REPLACE`
- `REMOVE`

This inventory may be recorded in Fact Audit rather than inserted into voice-over.

A new term that did not exist in Research Map is **not exempt** from review.

---

## Language Comprehension Audit

Fact Audit evaluates two separate questions:

1. **Factual accuracy** — does the explanation preserve the evidence/mechanism?
2. **Native comprehensibility** — would a general native viewer understand this naturally when hearing it?

A phrase can be:

- factually correct;
- grammatically correct;
- yet still fail audience comprehension.

That is a valid `REWRITE`.

---

## Native Cold Reader Pass

Before Final is accepted, read the entire narration as a native general-audience listener.

Check:

- unexplained technical terms;
- technical terms invented after Research;
- unnecessary foreign-language borrowings;
- acronyms used once;
- dense compounds / kanji / Sino-Korean terminology;
- English calques;
- inconsistent register;
- textbook definitions;
- repeated explanation of an already-understood CORE concept;
- unnatural literal translation from English;
- one-liner fragmentation or paragraph rhythm that feels templated in that language.

### Final principle

Do not ask:

> “Can this term be translated?”

Ask:

> “Would a general native viewer understand this sentence naturally on first listen, and does the simpler wording still preserve the truth?”
