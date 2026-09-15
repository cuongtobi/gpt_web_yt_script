# Stage 6 Prompt — Retention Audit

Đọc Draft như một viewer chưa biết research phía sau và chưa cam kết xem hết video.

## Core test

Không hỏi “đoạn này hay không?”.

Hỏi liên tục:

- người xem đang chờ payoff nào?
- họ vừa nhận được payoff gì?
- payoff đó làm họ muốn biết gì tiếp?
- nếu dừng video ngay bây giờ, lý do mạnh nhất để tiếp tục là gì?
- story đã thay đổi hiểu biết/stakes ra sao trong 60–90 giây vừa qua?
- hình gì đang xuất hiện trên màn hình?

Nếu câu trả lời là “đang cung cấp thêm context”, flag drop-off risk.

## First 3 minutes audit

Kiểm tra riêng 0–3 phút:

- central contradiction có rõ không?
- central question có xuất hiện đủ sớm không?
- có real payoff/reveal trước khi methodology/caveat kéo dài không?
- reveal đầu có tạo câu hỏi tiếp theo không?
- có đoạn nào đúng nhưng nên dời xuống sau first payoff không?

FAIL nếu phần đầu chủ yếu là setup/methodology mà chưa cho viewer reward đáng kể.

## Audit từng beat

Ghi:

- viewer question entering beat;
- retention function;
- reveal/payoff;
- consequence;
- curiosity handoff;
- visual anchor;
- open loop status;
- repetition risk;
- abstraction risk;
- methodology/caveat drag;
- proper noun load;
- suggested cut/reorder/rewrite.

## Curiosity chain test

Với mỗi cặp beat N → N+1, hoàn thành:

> “Because the viewer just learned ______, they now naturally want to know ______.”

Nếu không hoàn thành được, flag `BROKEN HANDOFF`.

Nếu beat tiếp theo chỉ tồn tại vì research có thêm fact liên quan, không phải vì story cần nó, flag `RESEARCH ORDER LEAK`.

## Reward cadence

Flag nếu:

- >90 giây không có reveal, mechanism, meaningful consequence, concrete case hoặc reversal;
- 2 beat liên tiếp chỉ qualify/hedge/methodology;
- open loop kéo dài nhưng không có partial payoff;
- reveal mạnh bị chôn sau phần giải thích có thể dời xuống;
- major reveal xuất hiện nhưng không được dramatize bằng setup/consequence tương xứng.

## Escalation test

Mỗi 2–3 beats, hỏi:

> “Tại sao story bây giờ quan trọng, lạ hoặc sâu hơn vài phút trước?”

Flag nếu các beat có thể đổi thứ tự tự do mà không ảnh hưởng causal experience.

## Detect template feel

Flag:

- transition phrase lặp;
- cùng syntax mở 3 đoạn;
- quá nhiều “And here is...” / “But...”;
- quoteable line liên tục đến mức artificial;
- mỗi section có cùng nhịp fact → dramatic sentence → question;
- authority stacking;
- chronology không có causal bridge;
- cliffhanger generic không xuất phát từ consequence thật.

## Visual momentum

Flag nếu:

- >2 phút toàn abstraction;
- genetics/methodology/system explanation không có human-scale hoặc concrete anchor;
- opening cinematic nhưng phần thân trở thành lecture;
- ending chỉ summary, không callback visual/theme.

## Compression test

Thử tưởng tượng cắt 10% số từ.

Nếu có thể cắt mà không mất fact, causal logic, emotional beat, reveal, curiosity handoff hoặc payoff, những phần đó là padding.

## Reorder test

Tìm ít nhất 3 beat/paragraph có thể được cải thiện bằng reorder. Đặc biệt tìm pattern:

`methodology/caveat → reveal`

và thử chuyển thành:

`reveal → evidence → qualification/reframe`.

Không reorder nếu làm claim trở nên misleading.

## Output

Điền `06_retention_audit.md`:

- Verdict: PASS/FAIL
- Score theo `QUALITY_GATES.md`
- First 3 minutes verdict
- Top retention strengths
- Drop-off risks theo timestamp
- Broken handoffs
- Research-order leaks
- Payoff cadence problems
- Repetition/template flags
- Cuts
- Reorders
- Rewrite directives
