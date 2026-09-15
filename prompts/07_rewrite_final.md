# Stage 7 Prompt — Final Rewrite

Đọc Draft + Fact Audit + Retention Audit + Research Ledger + Architecture + Outline + `docs/STYLE_DNA.md` + `docs/HOOK_STRATEGY_REGISTRY.md`.

Viết lại thành `07_final_script.md`.

## Priority

1. factual integrity;
2. viewer-question chain;
3. central question + payoff;
4. act progression + causal/story coherence;
5. retention + scale escalation + reveal ladder;
6. playable scene density;
7. spoken clarity;
8. anti-template naturalness;
9. duration;
10. style.

Accuracy là hard boundary. Bên trong boundary đó, ưu tiên version khiến viewer muốn biết chuyện gì xảy ra tiếp theo.

## Core rewrite doctrine

**Dramatize structure, never dramatize facts.**

Được phép:

- reorder evidence;
- delay explanation;
- reveal trước methodology khi không gây hiểu sai;
- build contrast/before-after;
- tighten act turns;
- widen/narrow scale;
- turn verified mechanisms into clear physical sequences;
- compress attribution;
- choose stronger verified cases/detours.

Không được bịa dialogue, emotion, sensory detail, exact historical action, motive, crowd behavior hoặc causal certainty.

## Required fixes

- áp dụng toàn bộ Fact Audit action bắt buộc;
- áp dụng Retention Audit ở cấp **reorder/structure/act/scale**, không chỉ polish câu;
- cắt padding;
- di chuyển methodology/caveat xuống sau first payoff khi accuracy cho phép;
- đưa reveal mạnh ra khỏi các đoạn explanation bị chôn;
- sửa mọi `BROKEN HANDOFF`, `RESEARCH ORDER LEAK`, `NO STORY EXPANSION`, `FLAT ACT`, `WEAK ACT TURN`;
- sửa scale stagnation và abstraction block dài;
- đảm bảo mỗi beat tạo consequence hoặc curiosity handoff tự nhiên;
- đảm bảo mỗi beat deepens mechanism, widens scale, changes interpretation hoặc raises stakes;
- thay transition lặp;
- giảm proper noun/date load;
- thêm qualification ở disputed claims;
- đảm bảo mọi open loop được payoff hoặc xóa;
- tăng playable scene/concrete sequence density khi evidence hỗ trợ;
- cắt decorative detour không tạo scale/scene/reframe/stakes value;
- đưa final về duration tolerance;
- xóa editor notes/citations khỏi narration nếu user không yêu cầu.

## Remove Narrator Scaffolding Pass

Sau khi structure đã đúng, chạy một pass riêng để **che skeleton của pipeline khỏi prose**.

Tìm các câu/phrase mà narrator đang tự giải thích chức năng của đoạn thay vì để evidence/consequence làm việc, ví dụ:

- “Đây là bước ngoặt.”
- “Đây là nơi câu chuyện thay đổi.”
- “Và đây là điều thú vị.”
- “Bây giờ câu chuyện trở nên lớn hơn.”
- “Nhưng câu hỏi tiếp theo là…”
- “Câu trả lời đầu tiên…”
- “Đến đây, nghịch lý…”
- “Điều đó đưa chúng ta trở lại…”
- các biến thể tiếng Anh tương đương.

### Rule

- Xóa hoặc rewrite phần lớn scaffolding nếu câu kế bên đã tự thể hiện reveal/turn/handoff.
- Không thay bằng một catchphrase template khác.
- Giữ tối đa một số ít câu meta-transition khi chúng thực sự giúp comprehension.
- Ưu tiên `evidence/action → consequence` thay cho `narrator announces turn → evidence`.
- Không ép mọi beat phải kết bằng rhetorical question.
- Không ép mọi act turn phải có một one-liner dramatic.
- Cho phép nhịp bất đối xứng: có beat chuyển mềm, có beat chuyển bằng evidence, có beat chuyển bằng consequence.

Sau pass này, `narrator_scaffolding_gate` chỉ được PASS khi final không còn cảm giác “script đang tự thuyết minh architecture của nó”.

## Cross-Project Opening Check

Trước khi chốt final:

1. Đọc `Hook Strategy Selection` trong `02_story_architecture.md`.
2. Đọc `style_fingerprint` của tối đa 5 project hoàn tất gần nhất.
3. Kiểm tra opening final thực tế vẫn đúng strategy/surface đã chọn.
4. Không được vô tình quay lại surface lặp kiểu `imperative_imagination` nếu Architecture đã chọn surface khác.
5. Nếu opening signature hoặc surface form trùng gần project trước, rewrite opening mà không phá central contradiction/early payoff.

## Style Fingerprint

Sau khi final ổn định, cập nhật `project_state.json.style_fingerprint`:

```json
{
  "hook_strategy": "<Hxx / strategy id>",
  "hook_surface_form": "<surface family>",
  "opening_signature": "<functional sequence>",
  "opening_first_words": "<8-16 từ đầu, chỉ để audit>",
  "dominant_transition_forms": ["<form>", "<form>"],
  "narrator_scaffolding_hits": 0,
  "rhetorical_question_count": 0,
  "sentence_length_profile": "mixed | short-heavy | long-heavy",
  "finalized": true
}
```

Đồng thời cập nhật:

- `narrator_scaffolding_gate`: PASS/FAIL;
- `cross_project_similarity_gate.verdict`: PASS/FAIL;
- `cross_project_similarity_gate.compared_projects`;
- `closest_project`;
- `max_opening_similarity` nếu checker có kết quả;
- `surface_form_repeat`;
- `opening_signature_repeat`.

Không tự bịa similarity score nếu chưa chạy checker. Có thể để `max_opening_similarity` ở 0 và để `scripts/check_project.py --write-style-state` điền sau.

## First 3 minutes rewrite test

Final 0–3 phút phải:

1. cho thấy central contradiction/transformation;
2. đặt central question;
3. trả ít nhất một real payoff/reveal;
4. dùng payoff đó mở câu hỏi mạnh hơn;
5. có concrete scene/physical contrast;
6. không biến thành methodology lecture.

Nếu fail, rewrite phần đầu trước khi chốt final.

## Act progression test

Với từng act:

- opening state/question rõ;
- payoff rõ;
- story lớn/sâu/khác đi;
- có scale/stakes/depth movement;
- consequence mở act tiếp theo.

Nếu act chỉ là cluster fact, restructure.

## Story momentum test

Với từng beat, hoàn thành:

> “Viewer vừa biết ______, nên bây giờ họ muốn biết ______.”

Nếu không hoàn thành được, beat cần cut/reorder/bridge.

Mỗi 2–3 beats, story phải tăng ít nhất một: novelty, evidence strength, mechanism depth, scale, consequence hoặc reframe.

## Scale escalation test

Kiểm tra toàn script:

- có intentional zoom-in/zoom-out;
- không có 3+ beat abstract cùng scale nếu có alternative;
- story ở middle/end phải cảm thấy lớn hơn hoặc sâu hơn opening;
- after abstraction, return to human/object/physical consequence khi phù hợp;
- scale shift phục vụ meaning, không phải gimmick.

## Reveal test

Major reveal phải có:

- setup đủ để viewer hiểu vì sao nó quan trọng;
- câu reveal rõ, không bị chôn;
- consequence sau reveal;
- handoff sang câu hỏi tiếp theo.

Phải có R1/R2 sớm, ít nhất một R3, và R4 nếu evidence/topic hỗ trợ. Không dùng dramatic wording để giả R4.

## Scene density test

- khoảng 60–90 giây nên có một playable scene/physical sequence nếu topic cho phép;
- không để >2 phút chỉ abstraction;
- visual anchor không được thay thế hoàn toàn playable scene;
- không bịa chi tiết để tăng cinematic density.

## Detour test

Mỗi detour phải ít nhất một:

- widen scale;
- create playable scene;
- prove causal step;
- create pattern interrupt;
- create reframe/reversal;
- raise stakes/consequence.

Nếu không, cut.

## Ending test

Ending phải làm đủ 4 việc:

1. trả lời central question bằng ngôn ngữ đơn giản;
2. cho thấy answer thay đổi cách hiểu chủ đề thế nào;
3. zoom out tới implication đủ lớn nhưng vẫn grounded;
4. callback opening image/contrast mà không lặp nguyên văn.

Ưu tiên final image cụ thể nếu topic cho phép.

Không thêm fact mới ở conclusion.

## Final self-check

Trước khi lưu:

- đọc thầm như voice-over;
- kiểm tra word count;
- kiểm tra câu quá dài/khó nói;
- kiểm tra first 3 minutes;
- kiểm tra act turns;
- kiểm tra viewer-question chain;
- kiểm tra payoff cadence;
- kiểm tra scale movement;
- kiểm tra scene density;
- kiểm tra R3/R4/R5;
- kiểm tra false precision;
- kiểm tra theory vs fact;
- kiểm tra decorative factual detail;
- kiểm tra transition phrase lặp;
- kiểm tra narrator scaffolding;
- kiểm tra opening similarity với recent projects;
- kiểm tra style fingerprint đã được cập nhật;
- kiểm tra ending callback.

Chỉ lưu final khi không còn blocker.
