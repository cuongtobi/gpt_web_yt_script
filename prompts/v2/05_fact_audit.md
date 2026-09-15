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
- cinematic/sensory detail kể như fact.

Với high-risk claim, quay lại original/primary source khi có thể. Không chỉ tin research summary nếu claim quá quan trọng.

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

FAIL nếu có fabricated source/quote/number, unsupported probability, theory/interpretation nói như settled fact, current claim quan trọng chưa kiểm tra hoặc exact historical/sensory detail không support.

## Output

Lưu `05_fact_audit.md`:

```md
# Fact Audit

- Verdict: PASS | FAIL

## Selected hook audit
...

## Required changes
...

## Claim audit
| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
```

Nếu FAIL, sửa Research/Draft hoặc quay lại Hook Lab khi blocker nằm ở selected hook trước Stage 6.
