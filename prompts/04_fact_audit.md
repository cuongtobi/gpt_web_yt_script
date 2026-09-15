# Stage 4 — Fact Audit

Đọc `01_research.md` và `03_draft.md`.

Audit các claim có rủi ro cao. Mục tiêu là sửa factual problems, **không redesign toàn bộ story**.

## Bắt buộc kiểm tra

- precise number / percentage / date;
- quote;
- named study/person/institution;
- `first`, `oldest`, `only`, `largest`, `never`, `always`;
- causal claim;
- consensus claim;
- current fact;
- cinematic/sensory detail được kể như fact.

Với high-risk claim, quay lại original/primary source khi có thể. Không chỉ tin research summary nếu claim quá quan trọng.

## Action

Mỗi claim cần một action:

- `KEEP`
- `QUALIFY`
- `REWRITE`
- `REMOVE`
- `VERIFY`

`VERIFY` còn tồn tại = audit chưa PASS.

## Hard rules

FAIL nếu có:

- fabricated source/quote/number;
- unsupported probability;
- theory/interpretation được nói như settled fact;
- current claim quan trọng không được kiểm tra;
- exact historical/sensory detail không có support.

## Output

Lưu `04_fact_audit.md` với:

```md
# Fact Audit

- Verdict: PASS | FAIL

## Required changes
...

## Claim audit
| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
```

Nếu FAIL, sửa Draft hoặc Research trước Stage 5.
