# Stage 2 Prompt — Story Architecture

Đọc `00_input.md`, `01_research_ledger.md`, `AGENTS.md`, `docs/STYLE_DNA.md`.

Không viết full script. Thiết kế trải nghiệm kể chuyện từ góc nhìn viewer.

## 1. Viewer promise

Một câu: người xem sẽ hiểu điều gì mà trước video họ chưa hiểu?

## 2. Central contradiction

Viết một nghịch lý/đối lập trung tâm có thể hình dung và liên quan trực tiếp tới câu hỏi video.

Ví dụ dạng trừu tượng:

- cùng một thứ nhưng hai kết quả đối lập;
- một hệ thống trông tự nhiên nhưng thực ra rất mới;
- bằng chứng hiện đại mâu thuẫn với câu chuyện phổ biến;
- một vật nhỏ dẫn tới hệ quả rất lớn.

Đây phải là hạt nhân của hook.

## 3. Hook archetype

Ưu tiên một trong hai archetype mạnh:

### A. Transformation Hook
`concrete before-state → extreme present/after contrast → impossible-looking transformation → central question`

### B. World-Before-X Hook
`place viewer in world before X → remove familiar assumption → show why modern X is strange → central question`

Có thể dùng archetype khác nếu topic đòi hỏi, nhưng opening phải làm viewer nghĩ: **“Tôi cần biết làm sao chuyện này xảy ra.”**

Không mở bằng methodology, disclaimer, taxonomy hoặc caveat dài.

## 4. Central question

Một câu hỏi đủ lớn để giữ cả video nhưng đủ cụ thể để trả lời.

## 5. Act Architecture

Thiết kế 4–5 acts. Không bắt buộc tên cố định, nhưng progression nên có cảm giác:

1. **The mystery / before-state** — dựng contradiction và promise.
2. **How it began** — payoff đầu + causal mechanism gốc.
3. **How humans/systems pushed it further** — specialization, expansion, institutionalization hoặc deeper mechanism.
4. **Unexpected consequence / reversal** — model ban đầu không còn đủ.
5. **What it became / what it means** — convergence, modern consequence, synthesis, callback.

Mỗi act phải trả lời:

- viewer bước vào act với belief/question nào?
- act payoff là gì?
- act làm scale/stakes/depth tăng ra sao?
- act kết thúc bằng consequence nào mở act kế tiếp?

Không chia act chỉ theo chronology hoặc số phút.

## 6. Viewer-question chain

Viết chuỗi 5–10 câu hỏi tự nhiên mà viewer sẽ lần lượt muốn biết.

Mỗi câu hỏi phải phát sinh từ payoff/consequence của câu trước, không phải danh sách câu hỏi độc lập.

Format:

```md
Q1: <question>
- Trigger: <điều vừa thấy/nghe khiến viewer hỏi câu này>
- Payoff: <answer/reveal sẽ trả>
- Consequence: <vì sao answer tạo Q2>
```

Không nhất thiết đọc các câu hỏi này thành lời trong final.

## 7. Causal ladder

Tạo 5–9 bước. Mỗi bước phải có:

- cause/condition;
- change/problem produced;
- human/system response;
- consequence;
- supporting claim IDs từ Research Ledger.

Nếu giữa hai bước chỉ có quan hệ chronological, đánh dấu và tìm causal bridge hoặc bỏ.

## 8. Scale Escalation Controller

Gắn scale cho từng beat/act:

- object;
- individual;
- community;
- institution;
- civilization;
- global/system.

Rule:

- không cần tăng scale tuyến tính;
- nhưng mỗi 2–3 beats phải có thay đổi scale hoặc giải thích rõ vì sao giữ cùng scale là cần thiết;
- ưu tiên nhịp close-up → wider system → close-up khác → wider consequence;
- tránh 5–6 beats liên tiếp chỉ ở một lớp abstract như genetics, policy hoặc chronology.

Lập **Scale Escalation Map** và chỉ ra ít nhất 2 chỗ story zoom out hoặc zoom in có chủ ý.

## 9. Story Expansion Test

Mỗi beat phải làm ít nhất một việc:

- `deepens mechanism`;
- `widens scale`;
- `changes interpretation`;
- `raises stakes`.

Nếu beat chỉ thêm fact mà không làm một trong bốn việc trên, cut/compress hoặc biến thành evidence trong beat khác.

Hỏi thêm:

> Câu trả lời này có làm câu chuyện lớn hơn, sâu hơn hoặc khác đi không?

## 10. Reveal ladder

Gắn các reveal chính theo cấp:

- R1 orientation payoff;
- R2 mechanism payoff;
- R3 reframe;
- R4 major reveal/reversal nếu topic cho phép;
- R5 synthesis/central answer.

Không giữ tất cả payoff đến cuối. Trong 10–15% đầu phải có ít nhất một R1/R2 thật sự đáng giá.

Với video 15–30 phút, nếu evidence cho phép phải chủ động tìm ít nhất một **R4**: một counterexample, consequence hoặc new evidence khiến model viewer vừa hình thành phải được sửa lại.

## 11. Curiosity debt map

- 1 macro loop từ hook.
- 3–7 micro loops tổng thể.
- Chỉ 1–3 micro loops active cùng lúc.
- Mỗi loop có nơi mở, partial payoff nếu cần, final payoff và curiosity handoff.
- Không mở loop giả chỉ để clickbait.

## 12. Historical / explanatory detours

Detour được phép nếu nó làm ít nhất một trong các việc:

- widen scale;
- provide a vivid playable scene;
- prove a causal step;
- create a strong pattern interrupt;
- create a reframe/reversal;
- raise consequence/stakes.

Detour phải quay lại central question bằng một consequence rõ. Nếu chỉ là fact thú vị, bỏ.

## 13. Story-order test

Tách **research order** khỏi **story order**.

Hỏi với từng beat:

- Viewer cần biết điều này ngay bây giờ không?
- Có thể cho reveal trước rồi qualification sau không?
- Nếu đưa methodology/caveat lên trước, nó có làm chậm first payoff không?
- Nếu bỏ beat này, causal chain hoặc escalation có gãy không?

Ưu tiên `reward → evidence → meaning → necessary qualification` khi không gây hiểu sai.

## 14. Escalation map

Xếp novelty/stakes 1–5.

Mỗi 2–3 beats phải chỉ ra chính xác story đã tăng ở đâu:

- evidence mạnh hơn;
- mechanism sâu hơn;
- scale lớn hơn;
- consequence rộng hơn;
- reversal/reframe;
- modern relevance.

Nếu beat sau có thể đổi chỗ với beat trước mà không ảnh hưởng story, cấu trúc còn quá modular.

## 15. Visual Scene Density Map

Phân biệt:

- **Visual anchor** — chart/map/object giúp minh họa;
- **Playable scene** — editor có thể dựng một cảnh có địa điểm/vật thể/người/hành động/mechanism đang diễn ra.

Mỗi 60–90 giây nếu topic cho phép cần ít nhất một playable scene hoặc concrete physical sequence.

Sau một beat abstract/genomic/system-heavy, ưu tiên một human-scale scene hoặc physical consequence.

Không bịa historical action/sensory detail để đạt scene density.

## 16. Uncertainty map

Liệt kê nơi script phải dùng wording như `may`, `one explanation`, `evidence suggests`, `researchers disagree`.

Không biến uncertainty map thành phần mở đầu. Qualification phải được đặt ở nơi chính xác nhưng ít phá momentum nhất.

## 17. Ending

`answer → reframe → larger implication → callback to opening image/contradiction`.

Ending không chỉ tóm tắt. Nó phải cho viewer thấy câu hỏi ban đầu bây giờ trông khác đi thế nào.

Điền `02_story_architecture.md`.
