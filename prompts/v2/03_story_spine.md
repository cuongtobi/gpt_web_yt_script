# Stage 3 — Story Spine

Đọc `00_input.md`, `01_research.md`, `02_hook_lab.md` và `docs/LANGUAGE_COMPREHENSION.md`.

Chỉ chạy khi:

- `02_hook_lab.md` có `Status: SELECTED`;
- state có `hook_selection = SELECTED`;
- `selected_hook` không trống.

Mục tiêu: xây một đường kể rõ sau khi user đã chọn opening direction.

Lưu vào `03_story_spine.md`.

## 1. Selected hook

Ghi:

- Selected ID
- Mechanism
- Hook text
- Vì sao nó phù hợp với topic

Giữ mechanism đã chọn. Có thể polish wording nhẹ để bridge tự nhiên hơn, nhưng không đổi sang mechanism khác hoặc generic `question → explicit answer` chỉ vì dễ outline.

Nếu selected hook dựa trên factual premise không còn support sau review, **không tự thay hook**. Quay lại Hook Lab và yêu cầu chọn/revise.

## 2. Central question

Viết đúng một câu hỏi lớn mà video sẽ trả lời trong planning.

Central question không bắt buộc phải được narrator nói nguyên văn trong opening. Nó có thể implicit nếu selected hook tạo curiosity tốt hơn theo cách đó.

## 3. Story spine

Tạo 6–10 beats. Mỗi beat trả lời:

```text
What happened / what do we learn?
Why does it matter to the central question?
What does it naturally lead to next?
Evidence / cases used:
Technical concepts introduced:
How will a general viewer understand them?
Can the technical label be removed?
```

Ưu tiên causal, chronological hoặc mechanistic chain tùy topic. Không ép một sequence duy nhất cho mọi documentary.

Không thêm beat chỉ để đạt quota. Một beat có thể dài hơn beat khác.

## 4. Audience comprehension planning

Dùng `Audience Vocabulary / Technical Term Map` trong `01_research.md` và language profile tương ứng với output language.

Với mỗi technical concept thực sự đi vào Story Spine:

- xác định lần đầu viewer cần hiểu nó;
- quyết định giữ label hay chỉ giữ plain meaning;
- xác định native preferred wording và register phù hợp với chính ngôn ngữ đầu ra;
- nếu giữ label, ghi cách giải thích first-use;
- không cho một term làm mắt xích trong lập luận **trước khi viewer đã có đủ meaning để hiểu nó**.

Mặc định ưu tiên: `plain meaning/function → technical label nếu cần → mechanism/consequence`.

Explanation budget:

- `CORE`: dành đủ 1–3 câu khi first use nếu concept phức tạp;
- `SUPPORTING`: thường chỉ cần một appositive/câu ngắn;
- `DISPENSABLE`: bỏ technical label, dùng plain language.

Không giải thích lại đầy đủ mỗi lần term xuất hiện.

## 5. Evidence placement

Đặt 5–8 case/object/study mạnh nhất vào đúng chỗ chúng chứng minh bước đang kể. Không biến script thành literature review.

## 6. Opening bridge test

Đọc selected hook rồi Beat 1–2 liên tục.

PASS khi:

- hook tạo lực kéo mà Beat 1 có thể tiếp nhận ngay;
- không cần một câu meta kiểu `Câu trả lời là...` để nối;
- không có cảm giác hook là trailer rời khỏi story;
- không reveal toàn bộ thesis quá sớm nếu mechanism được chọn dựa trên mystery/contradiction;
- nếu hook chứa technical concept, viewer được cung cấp meaning đủ sớm để không bị rơi khỏi câu chuyện.

## 7. Ending

Ending gồm:

- direct answer: trả central question bằng ngôn ngữ đơn giản;
- synthesis: chuỗi thay đổi/mechanism nào tạo kết quả;
- callback selected hook nếu tự nhiên.

Không thêm fact mới ở ending. Không đưa thuật ngữ mới ở ending nếu term đó chưa được chuẩn bị trước.

## Test trước khi lưu

Nếu 3–4 beats có thể đổi chỗ tự do mà logic không đổi, spine còn quá modular. Sắp lại để mỗi đoạn tạo lý do tự nhiên cho đoạn tiếp theo.

Sau đó chạy **cold-reader planning test**:

- một người không học ngành này có hiểu Beat 1 → Beat cuối mà không cần Google term nào không?
- term nào chỉ tồn tại vì researcher biết nó, chứ viewer không cần?
- có concept nào được dùng để suy luận trước khi được giải thích không?

Nếu có, sửa Story Spine trước Draft.

Không dùng một chuẩn comprehension chung cho mọi ngôn ngữ: German phải được đọc như spoken German, French như spoken French, Spanish theo locale đã chọn, Korean/Japanese phải giữ speech/register nhất quán.
