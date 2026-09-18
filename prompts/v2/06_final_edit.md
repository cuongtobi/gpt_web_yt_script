# Stage 6 — Final Edit

Đọc `00_input.md`, `01_research.md`, `02_hook_lab.md`, `03_story_spine.md`, `04_draft.md` và `05_fact_audit.md`.

Chỉ chạy khi Fact Audit = PASS.

Viết `06_final_script.md`.

## Mục tiêu

Biến draft thành voice-over sạch, tự nhiên, đúng thời lượng, dễ hiểu với khán giả phổ thông mà vẫn giữ opening direction user đã chọn.

## Làm

- áp dụng mọi Required change của Fact Audit;
- áp dụng correction trong Technical explanation audit;
- cắt câu/đoạn lặp ý;
- cắt research detail không phục vụ central question;
- sửa câu khó nói thành spoken language;
- rút methodology/attribution dài;
- bỏ technical label không cần thiết;
- giữ plain-language explanation cho CORE concept;
- giữ các concrete case mạnh;
- giữ selected hook mechanism, trừ khi Fact Audit buộc quay lại Hook Lab;
- sửa transition máy móc khi cần;
- đảm bảo central question được trả lời rõ ở cuối;
- callback opening nếu tự nhiên;
- đưa final về ±7% target words.

## Audience Comprehension Pass

Chạy một lượt riêng như **cold reader**. Giả định viewer tò mò, có trình độ phổ thông, chưa đọc Research, không học chuyên ngành của topic và không thể dừng video để tra Google.

Với từng đoạn, hỏi:

- có term nào viewer cần Google mới theo được logic không?
- term đó có thực sự cần tên chuyên ngành không?
- nếu cần giữ, meaning đã xuất hiện trước hoặc ngay tại first use chưa?
- explanation có đủ ngắn để không làm mất nhịp narration không?
- có acronym nào chỉ xuất hiện một lần không?
- có quá nhiều term mới dồn trong cùng một câu/đoạn không?
- explanation có đúng đại ý nhưng sai mechanism khi đọc kỹ không?

Quy tắc sửa:

- viewer cần concept nhưng không cần nhớ tên → giữ meaning, bỏ technical label;
- viewer cần cả concept và tên → meaning first, label second;
- `SUPPORTING` → ưu tiên appositive ngắn hoặc plain-language replacement;
- `DISPENSABLE` → xóa label;
- explanation dài hơn 3–4 câu nhưng không phải central mechanism → cắt taxonomy/detail thay vì biến narration thành lecture.

Không thêm glossary section vào narration. Explanation phải nằm tự nhiên tại đúng điểm story cần concept đó.

## Opening preservation check

So `06_final_script.md` với selected candidate trong `02_hook_lab.md`:

- mechanism còn nhận ra được;
- opening không bị genericize thành `question → explicit answer phrase` chỉ vì edit;
- không tự thêm scaffold `Câu trả lời là...`, `Câu trả lời bắt đầu...`, `The short answer is...` nếu selected hook không cần;
- exact wording có thể thay đổi để spoken hơn;
- factual qualifications từ Fact Audit được ưu tiên hơn wording gốc;
- jargon không làm hook khó hiểu hơn Hook Lab candidate.

## Không làm

- không thêm framework label vào narration;
- không ép mỗi section phải có question/cliffhanger;
- không đổi hook chỉ vì một archetype khác quen tay hơn;
- không thay toàn bộ story nếu Fact Audit chỉ yêu cầu sửa claim;
- không thêm fact mới chưa research/audit;
- không thay một term bằng cách giải thích “dễ hiểu” nhưng sai;
- không định nghĩa mọi technical term chỉ vì chúng xuất hiện trong Research.

## Soft anti-template check

Đọc lại nếu opening dùng các phrase/meta scaffold quen thuộc chỉ vì thói quen, hoặc nhiều project gần nhau cùng có skeleton `setup → question → answer announcement`.

Naturalness > artificial uniqueness.

## Final comprehension check

Final chỉ đạt editorial readiness khi:

- CORE terms được giải thích đủ để viewer hiểu;
- SUPPORTING terms không làm narration nặng;
- DISPENSABLE jargon đã được bỏ khi có thể;
- không có concept quan trọng được dùng trước khi meaning của nó xuất hiện;
- explanation không làm sai factual meaning.

## Final format

```md
# <working title>

<voice-over only>
```

Không citation/editor note trong narration trừ khi user yêu cầu.
