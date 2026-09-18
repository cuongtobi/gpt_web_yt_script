# Stage 5 — Fact Audit

Đọc `00_input.md`, `01_research.md`, `02_hook_lab.md`, `04_draft.md` và `docs/LANGUAGE_COMPREHENSION.md`. Chọn language profile theo output language trước khi audit.

Audit factual risk của cả opening lẫn body. Mục tiêu là sửa factual problems, **không redesign story nếu không cần**.

## Bắt buộc kiểm tra

- factual premise của selected hook;
- precise number / percentage / date;
- quote;
- named study/person/institution;
- `first`, `oldest`, `only`, `largest`, `never`, `always`;
- causal claim;
- consensus claim;
- current fact;
- cinematic/sensory detail kể như fact;
- plain-language explanation của technical concept;
- analogy/metaphor dùng để giải thích science/history/mechanism;
- technical label bị dùng sai nghĩa hoặc rộng hơn evidence support.

Với high-risk claim, quay lại original/primary source khi có thể. Không chỉ tin research summary nếu claim quá quan trọng.

## Draft Term Inventory — bắt buộc

**Không bắt đầu từ Research map rồi chỉ kiểm những term đã biết.** Trước tiên extract tất cả technical/academic/foreign/unfamiliar terms **thực sự xuất hiện trong Draft**, kể cả term Draft tự sinh sau Research.

Tạo inventory với:

- `Term actually used`
- `In Research Map?`: `YES | NO`
- `Audience risk`: `LOW | MEDIUM | HIGH`
- `Native/spoken naturalness`: `NATURAL | BORDERLINE | UNNATURAL`
- `Action`: `KEEP | EXPLAIN | REPLACE | REMOVE`
- `Replacement / first-use explanation`

Một term mới `In Research Map = NO` không được miễn audit.

## Language Comprehension Audit

Dùng `Audience Vocabulary / Technical Term Map` trong Research **sau khi** đã extract Draft Term Inventory. Áp dụng profile trong `docs/LANGUAGE_COMPREHENSION.md`.

Với mỗi risky wording, audit hai trục độc lập:

1. **Factual accuracy** — explanation có giữ đúng evidence/mechanism không?
2. **Native comprehensibility** — một general native viewer có hiểu tự nhiên khi nghe không?

Một câu có thể factually correct và grammatically correct nhưng vẫn phải `REWRITE` vì nghe quá academic, quá foreign, quá dense hoặc không tự nhiên với output language.

Kiểm thêm:

- unnecessary foreign borrowing/code-switching;
- English calque/literal translation;
- German compound/Nominalstil risk;
- French academic/Anglicism risk;
- Spanish locale/false-friend risk;
- Korean speech-level và Sino-Korean density;
- Japanese register, kanji density và katakana jargon;
- repeated explanation của CORE concept đã được giải thích rõ trước đó.

## Comprehension accuracy audit

Mỗi explanation phải trả lời:

1. Viewer có hiểu được không?
2. Cách nói đơn giản có còn đúng không?
3. Có bỏ mất qualification quan trọng không?
4. Analogy có khiến viewer suy ra một mechanism sai không?
5. Technical label có thật sự cần giữ không?

Ví dụ `TRPV1 là receptor của vị cay` phải `REWRITE` vì dễ tạo hiểu lầm rằng đây là taste receptor chuyên cho “vị cay”. Một wording kiểu `TRPV1 là một cảm biến trên tế bào thần kinh có thể phản ứng với nhiệt gây đau và capsaicin` phù hợp hơn nếu source support.

Fact Audit không được ép script quay lại jargon chỉ vì plain-language wording chưa hoàn hảo. Mục tiêu là **plain + accurate**, không phải technical + opaque.

## Hook-specific rule

Hook không được ưu tiên hơn factual integrity.

Nếu selected hook premise cần sửa nhỏ, `QUALIFY` hoặc `REWRITE` nhưng giữ mechanism nếu có thể.

Nếu premise cốt lõi của selected hook không support và sửa sẽ làm mất mechanism/meaning, Fact Audit = FAIL và phải quay lại Hook Lab để user chọn/revise. Không âm thầm thay bằng hook khác.

## Action

Mỗi claim cần một action:

- `KEEP`
- `QUALIFY`
- `REWRITE`
- `REMOVE`
- `VERIFY`

`VERIFY` còn tồn tại = audit chưa PASS.

## Hard rules

FAIL nếu có fabricated source/quote/number, unsupported probability, theory/interpretation nói như settled fact, current claim quan trọng chưa kiểm tra, exact historical/sensory detail không support, hoặc plain-language explanation làm thay đổi materially scientific/historical meaning.

Comprehension problems thường là `REWRITE/REMOVE` requirement chứ không tự động biến factual verdict thành FAIL; nhưng Fact Audit không được ghi PASS nếu Required changes cho term HIGH-risk/native-unnatural vẫn chưa có final wording xử lý.

## Output

Lưu `05_fact_audit.md`:

```md
# Fact Audit

- Verdict: PASS | FAIL

## Selected hook audit
...

## Required changes
...

## Draft Term Inventory
| Term actually used | In Research Map? | Audience risk | Native/spoken naturalness | Action | Replacement / first-use explanation |
|---|---|---|---|---|---|

## Language comprehension audit
| Wording / term | Factual accuracy | Native comprehension risk | Register / language issue | Action | Final native wording |
|---|---|---|---|---|---|

## Technical explanation audit
| Term / explanation | Accuracy risk | Evidence/source | Action | Final plain wording |
|---|---|---|---|---|

## Claim audit
| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
```

Nếu FAIL, sửa Research/Draft hoặc quay lại Hook Lab khi blocker nằm ở selected hook trước Stage 6.
