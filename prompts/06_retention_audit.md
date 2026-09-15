# Stage 6 Prompt — Retention / Story Momentum Audit

Đọc Draft như một viewer chưa biết research phía sau và chưa cam kết xem hết video.

## Core test

Không hỏi “đoạn này hay không?”.

Hỏi liên tục:

- người xem đang chờ payoff nào?
- họ vừa nhận được payoff gì?
- payoff đó làm họ muốn biết gì tiếp?
- nếu dừng video ngay bây giờ, lý do mạnh nhất để tiếp tục là gì?
- story đã thay đổi hiểu biết/stakes/scale ra sao trong 60–90 giây vừa qua?
- viewer vừa **hiểu nhiều hơn** hay chỉ **biết thêm fact**?
- hình gì đang xuất hiện trên màn hình?

Nếu câu trả lời là “đang cung cấp thêm context”, flag drop-off risk.

## First 3 minutes audit

Kiểm tra riêng 0–3 phút:

- central contradiction có rõ không?
- central question có xuất hiện đủ sớm không?
- có real payoff/reveal trước khi methodology/caveat kéo dài không?
- reveal đầu có tạo câu hỏi tiếp theo không?
- có concrete scene/visual đủ mạnh không?
- có scale movement hoặc transformation rõ nếu topic cho phép không?
- có đoạn nào đúng nhưng nên dời xuống sau first payoff không?

FAIL nếu phần đầu chủ yếu là setup/methodology mà chưa cho viewer reward đáng kể.

## Act Progression Audit

Với từng act:

- viewer bước vào với belief/question nào?
- act payoff là gì?
- act làm story lớn hơn/sâu hơn/khác đi thế nào?
- scale/stakes/depth thay đổi ra sao?
- consequence nào mở act kế tiếp?

Flag `FLAT ACT` nếu act chỉ gom các fact cùng chủ đề.

Flag `WEAK ACT TURN` nếu chuyển act nhưng viewer không cảm thấy story đổi cấp độ, scale hoặc interpretation.

## Audit từng beat

Ghi:

- act;
- viewer question entering beat;
- retention function;
- reveal/payoff;
- consequence;
- curiosity handoff;
- scale;
- scale movement;
- story expansion function;
- playable scene / concrete anchor;
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

## Story Expansion Test

Mỗi beat phải làm ít nhất một:

- deepen mechanism;
- widen scale;
- change interpretation;
- raise stakes.

Nếu không làm mục nào, flag `NO STORY EXPANSION` và đề xuất cut/compress/fold.

## Scale Escalation Audit

Kiểm tra chuỗi scale:

`object → individual → community → institution → civilization → global/system`

Không bắt buộc đi tuyến tính, nhưng:

- flag nếu 3+ beats liên tiếp ở cùng abstract scale mà không có lý do;
- flag nếu video không có ít nhất 2 intentional zoom-in/zoom-out moments khi topic cho phép;
- flag nếu story không hề cảm thấy lớn hơn so với opening;
- ưu tiên close-up sau abstraction và zoom-out sau concrete consequence.

## Reveal Ladder Audit

Xác nhận:

- R1/R2 xuất hiện sớm;
- có ít nhất một R3 reframe;
- có R4 major reversal nếu evidence/topic hỗ trợ;
- R5 synthesis trả central question.

Flag nếu:

- reveal mạnh bị chôn;
- R4 chỉ là wording dramatic chứ không thay model viewer;
- video không có belief change nào đáng kể.

## Reward cadence

Flag nếu:

- >90 giây không có reveal, mechanism, meaningful consequence, concrete case, playable scene hoặc reversal;
- 2 beat liên tiếp chỉ qualify/hedge/methodology;
- open loop kéo dài nhưng không có partial payoff;
- reveal mạnh bị chôn sau phần giải thích có thể dời xuống;
- major reveal xuất hiện nhưng không được setup/consequence tương xứng.

## Visual Scene Density Audit

Phân biệt visual anchor với playable scene.

Flag nếu:

- >2 phút toàn abstraction;
- genetics/methodology/system explanation không có human-scale hoặc concrete anchor;
- opening cinematic nhưng phần thân trở thành lecture;
- playable scenes quá thưa so với chủ đề có nhiều physical evidence;
- scene chỉ dựa vào imagined historical detail không có support;
- ending chỉ summary, không callback visual/theme.

## Detour Audit

Với mỗi historical/explanatory detour, hỏi:

- nó widen scale không?
- có playable scene mạnh không?
- chứng minh causal step không?
- tạo pattern interrupt/reversal không?
- tăng stakes/consequence không?
- quay lại central story bằng consequence nào?

Nếu không có câu trả lời mạnh, flag `DECORATIVE DETOUR`.

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

## Compression test

Thử tưởng tượng cắt 10% số từ.

Nếu có thể cắt mà không mất fact, causal logic, scene, emotional/intellectual beat, reveal, curiosity handoff, scale movement hoặc payoff, những phần đó là padding.

## Reorder test

Tìm ít nhất 3 beat/paragraph có thể được cải thiện bằng reorder. Đặc biệt tìm:

`methodology/caveat → reveal`

và thử:

`reveal → evidence → qualification/reframe`.

Không reorder nếu làm claim misleading.

## Narrative Momentum Verdict

Ngoài PASS/FAIL, trả lời một câu:

> “Tại sao viewer muốn xem thêm 60 giây nữa ở phần yếu nhất của video?”

Nếu không có câu trả lời cụ thể, Retention Audit không được PASS.

## Output

Điền `06_retention_audit.md`:

- Verdict: PASS/FAIL
- Score theo `QUALITY_GATES.md`
- First 3 minutes verdict
- Act progression verdict
- Scale escalation verdict
- Scene density verdict
- Reveal ladder verdict
- Top retention strengths
- Drop-off risks theo timestamp
- Broken handoffs
- Research-order leaks
- No-story-expansion beats
- Flat acts / weak act turns
- Scale stagnation
- Payoff cadence problems
- Visual scene density problems
- Decorative detours
- Repetition/template flags
- Cuts
- Reorders
- Rewrite directives
