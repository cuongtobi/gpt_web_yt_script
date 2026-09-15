# Stage 5 Prompt — Fact Audit

Đọc Draft đối chiếu Research Ledger. Không đánh giá prose trước; đánh giá truthfulness trước.

## Audit list

Trích và kiểm tra tất cả:

- số liệu, phần trăm, kích thước, số người;
- ngày/năm;
- superlative: first, oldest, biggest, only;
- named scholar/study/book/journal;
- direct quote;
- causal statement;
- consensus statement;
- current status;
- probability/confidence number.

## Action

Mỗi claim gắn một action:

- `KEEP` — source support đúng mức.
- `QUALIFY` — đúng hướng nhưng certainty quá mạnh.
- `REWRITE` — wording làm sai nghĩa/source.
- `REMOVE` — không cần hoặc không support.
- `VERIFY` — chưa đủ evidence.

## Special tests

### False precision

Nếu draft có `%` hoặc con số xác suất mà ledger không có nguồn báo trực tiếp → `REMOVE/REWRITE`, audit FAIL.

### Theory laundering

Nếu một academic framework được viết thành “đó là lý do sự việc xảy ra” nhưng nguồn chỉ đề xuất explanation → `QUALIFY`.

### Quote integrity

Không verify nguyên văn → paraphrase, bỏ quotation marks.

### Causal integrity

Nếu evidence chỉ correlation hoặc temporal sequence, không dùng `caused`, `because`, `therefore` như direct causation.

## Output

Điền `05_fact_audit.md`, gồm:

- Verdict: PASS/FAIL
- Critical issues
- Claim-by-claim table
- Required edits
- Claims safe to keep
