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
- probability/confidence number;
- motive được gán cho historical actor/group;
- dialogue hoặc lời nói được tái dựng;
- sensory/cinematic detail được kể như fact: music, weather, smell, sound, crowd behavior, emotion, exact movement/action;
- generic reconstruction có vô tình biến thành claim về event cụ thể không.

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

### Cinematic integrity

Rule: **dramatize structure, never facts**.

Audit riêng mọi câu cinematic:

- Có source support cho chi tiết cụ thể không?
- Nếu không, câu đó có thể chuyển thành generic hypothetical/reconstruction rõ ràng không?
- Câu có ngụ ý ta biết exact action/motive/emotion mà evidence không cho phép không?

Unsupported sensory/historical detail kể như fact → `REMOVE/REWRITE`.

Bịa dialogue, motive, exact action hoặc sensory scene để tăng drama = audit FAIL.

### Reconstruction boundary

Được phép dùng generic explanatory visualization như:

- “A farmer saving seed from the tallest plants would favor those traits over time.”

Không được biến nó thành historical claim kiểu:

- “One morning, an ancient farmer walked the field and chose the tallest stalk.”

trừ khi source thực sự support event đó.

## Output

Điền `05_fact_audit.md`, gồm:

- Verdict: PASS/FAIL
- Critical issues
- Claim-by-claim table
- Cinematic detail audit
- Reconstruction boundary issues
- Required edits
- Claims safe to keep
