# Stage 5 — Fact Audit

Đọc `01_research.md`, `02_hook_lab.md` và `04_draft.md`.

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

## Comprehension accuracy audit

Dùng `Audience Vocabulary / Technical Term Map` trong Research để kiểm tra các term xuất hiện trong Draft.

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

## Output

Lưu `05_fact_audit.md`:

```md
# Fact Audit

- Verdict: PASS | FAIL

## Selected hook audit
...

## Required changes
...

## Technical explanation audit
| Term / explanation | Accuracy risk | Evidence/source | Action | Final plain wording |
|---|---|---|---|---|

## Claim audit
| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
```

Nếu FAIL, sửa Research/Draft hoặc quay lại Hook Lab khi blocker nằm ở selected hook trước Stage 6.
