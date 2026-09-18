# Stage 6 — Final Edit

Đọc `00_input.md`, `01_research.md`, `02_hook_lab.md`, `03_story_spine.md`, `04_draft.md`, `05_fact_audit.md` và `docs/LANGUAGE_COMPREHENSION.md`. Chọn đúng native-language profile trước khi edit.

Chỉ chạy khi Fact Audit = PASS.

Viết `06_final_script.md`.

## Mục tiêu

Biến draft thành voice-over sạch, tự nhiên, đúng thời lượng, dễ hiểu với khán giả phổ thông mà vẫn giữ opening direction user đã chọn.

## Làm

- áp dụng mọi Required change của Fact Audit;
- áp dụng correction trong Draft Term Inventory, Language comprehension audit và Technical explanation audit;
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

## Native Audience Comprehension Pass

Chạy một lượt riêng như **native cold reader**. Giả định viewer là native/fluent speaker của output language, tò mò, có trình độ phổ thông, chưa đọc Research, không học chuyên ngành của topic và không thể dừng video để tra cứu.

Đánh giá theo storytelling/spoken conventions của chính output language. Không dùng tiếng Việt hoặc tiếng Anh làm chuẩn chung.

Với từng đoạn, hỏi:

- có term nào viewer cần Google mới theo được logic không?
- term đó có thực sự cần tên chuyên ngành không?
- nếu cần giữ, meaning đã xuất hiện trước hoặc ngay tại first use chưa?
- explanation có đủ ngắn để không làm mất nhịp narration không?
- có acronym nào chỉ xuất hiện một lần không?
- có quá nhiều term mới dồn trong cùng một câu/đoạn không?
- explanation có đúng đại ý nhưng sai mechanism khi đọc kỹ không?
- có term mới xuất hiện sau Research nhưng chưa được audit không?
- có foreign borrowing/code-switching không cần thiết không?
- register/locale/speech level có nhất quán không?
- có câu nghe như literal translation từ English hoặc một ngôn ngữ khác không?
- một CORE concept đã được giải thích rõ rồi có bị định nghĩa lại dài dòng lần nữa không?

Quy tắc sửa:

- viewer cần concept nhưng không cần nhớ tên → giữ meaning, bỏ technical label;
- viewer cần cả concept và tên → meaning first, label second;
- `SUPPORTING` → ưu tiên appositive ngắn hoặc plain-language replacement;
- `DISPENSABLE` → xóa label;
- explanation dài hơn 3–4 câu nhưng không phải central mechanism → cắt taxonomy/detail thay vì biến narration thành lecture.

Không thêm glossary section vào narration. Explanation phải nằm tự nhiên tại đúng điểm story cần concept đó.

### Language-specific final checks

- `en`: academic nominalization, dense noun phrase, methodology language;
- `de`: compound density, Nominalstil, bureaucratic/deep-clause syntax;
- `fr`: written-academic register, calques, unnecessary Anglicisms;
- `es`: locale consistency, false friends, English calques;
- `ko`: Sino-Korean term density, English/acronyms, speech-level consistency;
- `ja`: kanji density, katakana jargon, `です・ます` vs `だ・である` consistency;
- `vi`: unnecessary English/code-switching, research-note wording.

### Explanation repetition check

Nếu CORE concept đã được giải thích rõ ở first use, các lần sau chỉ callback ngắn khi cần. Không định nghĩa lại đầy đủ chỉ để chứng minh clarity.

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
- explanation không làm sai factual meaning;
- term thực tế trong Final đã được kiểm, kể cả term không có trong Research Map;
- native wording/register tự nhiên và nhất quán với output language;
- không còn unnecessary foreign borrowing hoặc repeated definition đáng kể.

## Final format

```md
# <working title>

<voice-over only>
```

Không citation/editor note trong narration trừ khi user yêu cầu.
