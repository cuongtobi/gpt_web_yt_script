# Quality Gates — Simple Pipeline v2

Pipeline chỉ giữ hard gate cho những thứ làm project sai hoặc unusable. Hook diversity chủ yếu là editorial judgment, ngoại trừ việc **user phải chọn hook trước khi pipeline tiếp tục**.

Audience comprehension là quality requirement xuyên suốt: technical concept cần thiết phải được giải thích đủ cho khán giả phổ thông, nhưng pipeline không biến mọi jargon thành hard dictionary check.

## Gate A — Research readiness

PASS khi central question có thể trả lời bằng evidence, thesis không dựa trên `UNVERIFIED`, causal/chronological steps lớn có support, có concrete cases đủ mạnh, technical terms có khả năng đi vào narration đã được phân loại `CORE | SUPPORTING | DISPENSABLE`, và mỗi CORE term có plain-language meaning đủ chính xác.

---

## Gate B — Hook Lab readiness

PASS để trình user khi:

- có đủ H1–H10;
- mỗi candidate dùng một mechanism khác trong danh sách Hook Lab;
- candidate không chỉ paraphrase cùng một opening;
- không candidate nào cần fabricated scene/detail để hoạt động;
- factual hook claims nằm trong research boundary;
- central question có thể explicit hoặc implicit;
- technical term trong hook không khiến khán giả cần kiến thức chuyên ngành trước để hiểu tension;
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
- technical concept được introduce trước khi trở thành mắt xích trong lập luận;
- CORE terms có first-use explanation plan;
- SUPPORTING/DISPENSABLE terms đã được cân nhắc bỏ label nếu viewer không cần nhớ tên;
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
- chronology/causal chain dễ theo dõi;
- người xem phổ thông không cần biết trước jargon để hiểu logic;
- CORE term được giải thích ở first use;
- không acronym/technical label dư thừa chỉ để narration có vẻ chuyên môn;
- explanation ưu tiên function/meaning trước taxonomy.

---

## Gate E — Fact Audit

PASS khi mọi high-risk claim đã KEEP/QUALIFY/REWRITE/REMOVE, không còn VERIFY blocker, không fabricated source/quote/number, không unsupported probability, theory/interpretation không bị viết như settled fact, plain-language explanation không materially distort meaning, analogy không tạo inference sai và technical label được dùng đúng nghĩa.

---

## Gate F — Final Validation

Hard PASS khi:

- đủ artifact bắt buộc cho pipeline version;
- Hook Lab selection = SELECTED với `simple_v2`;
- Fact Audit = PASS;
- final nằm trong ±7% target words;
- final không còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Editorial readiness còn yêu cầu cold-reader pass: CORE concepts hiểu được mà không cần tra cứu, không concept quan trọng nào bị dùng trước khi giải thích, SUPPORTING jargon không làm narration nặng, DISPENSABLE labels được bỏ khi plain language tốt hơn, và simplification vẫn đúng factual meaning.

Checker tự động hiện chỉ enforce structural/factual-state/timing markers; comprehension vẫn là editorial gate do agent thực hiện.

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
- conclusion chỉ recap mà không trả central question;
- technical term xuất hiện trước plain meaning;
- định nghĩa kiểu textbook dài hơn giá trị nó đóng góp cho story;
- nhiều acronym mới dồn trong một đoạn;
- dùng jargon khi một cụm plain language ngắn đã đủ.

Không biến các anti-pattern này thành quota hoặc hard score. Chỉ sửa khi narration tốt hơn.

**North star:** viewer hiểu mechanism mà không cảm thấy mình đang nghe glossary.
