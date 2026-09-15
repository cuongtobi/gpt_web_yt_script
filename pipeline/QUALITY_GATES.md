# Quality Gates — Simple Pipeline v2

Pipeline chỉ giữ hard gate cho những thứ làm project sai hoặc unusable. Hook diversity chủ yếu là editorial judgment, ngoại trừ việc **user phải chọn hook trước khi pipeline tiếp tục**.

## Gate A — Research readiness

PASS khi central question có thể trả lời bằng evidence, thesis không dựa trên `UNVERIFIED`, causal/chronological steps lớn có support và có concrete cases đủ mạnh.

---

## Gate B — Hook Lab readiness

PASS để trình user khi:

- có đủ H1–H10;
- mỗi candidate dùng một mechanism khác trong danh sách Hook Lab;
- candidate không chỉ paraphrase cùng một opening;
- không candidate nào cần fabricated scene/detail để hoạt động;
- factual hook claims nằm trong research boundary;
- central question có thể explicit hoặc implicit;
- không mặc định dùng `Câu trả lời là...`, `Câu trả lời bắt đầu...`, `The answer is...`, `The short answer is...` làm scaffold.

Sau đó pipeline bắt buộc ở trạng thái `awaiting_hook_selection`.

### Human selection gate — HARD

Không sang Story Spine khi:

- `hook_selection != SELECTED`;
- `selected_hook` trống;
- user chưa explicit chọn H1–H10 hoặc mechanism.

Model không được tự chọn phương án “tốt nhất” thay user.

---

## Gate C — Story Spine readiness

PASS khi:

- selected hook được dùng làm opening direction;
- central question rõ trong planning, dù hook không nhất thiết hỏi trực tiếp;
- 6–10 beats tạo thành transformation/causal/chronological chain;
- mỗi beat giải thích vì sao nó quan trọng và dẫn tới đâu;
- ending có direct answer.

Nếu 3–4 beats có thể đổi chỗ tự do mà story không thay đổi, revise.

---

## Gate D — Draft usability

PASS khi:

- draft khoảng ±10% target;
- narration nghe được khi đọc thành tiếng;
- selected hook mechanism còn nhận ra được ở opening;
- không bị rewrite thành generic `question → explicit answer phrase` nếu hook gốc không dùng kiểu đó;
- không lặp luận điểm để kéo thời lượng;
- factual claims nằm trong research boundary;
- chronology/causal chain dễ theo dõi.

---

## Gate E — Fact Audit

PASS khi mọi high-risk claim đã KEEP/QUALIFY/REWRITE/REMOVE, không còn VERIFY blocker, không fabricated source/quote/number, không unsupported probability và theory/interpretation không bị viết như settled fact.

---

## Gate F — Final Validation

Hard PASS khi:

- đủ artifact bắt buộc cho pipeline version;
- Hook Lab selection = SELECTED với `simple_v2`;
- Fact Audit = PASS;
- final nằm trong ±7% target words;
- final không còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Checker có thể WARN về:

- transition/template phrase lặp;
- opening kiểu `Hãy tưởng tượng...` / `Imagine...`;
- early-answer scaffolding như `Câu trả lời là...` / `The short answer is...`;
- percentage claims cần double-check support.

WARN không làm project FAIL.

---

## Editorial anti-patterns — soft only

Đọc lại nếu có:

- nhiều project cùng dùng `scene → question → Câu trả lời...`;
- mọi hook đều đặt direct question ở cùng vị trí;
- spam `Đây là...`, `Và đây là nơi...`, `Nhưng câu hỏi...`;
- one-liner quá dày;
- attribution kiểu author + institution + journal + year liên tục;
- nhiều paragraph có cùng nhịp/skeleton;
- conclusion chỉ recap mà không trả central question.

Không biến các anti-pattern này thành quota hoặc hard score. Chỉ sửa khi narration tốt hơn.
