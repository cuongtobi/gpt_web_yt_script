# Simple YouTube Documentary Pipeline — v2

Pipeline này giữ triết lý **đơn giản + evidence-grounded**, nhưng thêm một bước Hook Lab có human choice để opening không hội tụ về cùng một skeleton.

## Stage 0 — Input

Artifact: `00_input.md`

Chuẩn hóa topic, language, duration, audience/title/angle nếu có, target WPM và target words.

---

## Stage 1 — Research

Prompt: `prompts/01_research.md`

Artifact: `01_research.md`

Research pack gồm central question candidates, timeline/causal background, 10–20 core claims, 5–8 strong cases/objects/studies, useful numbers/quotes, important uncertainties và `Audience Vocabulary / Technical Term Map` cho các term có khả năng đi vào narration.

### Gate A

Không sang Hook Lab nếu thesis chính dựa trên `UNVERIFIED` claim hoặc các bước lớn chưa có support. CORE technical terms phải có plain-language explanation đủ chính xác trước khi sang downstream.

---

## Stage 2 — Hook Lab

Prompt: `prompts/v2/02_hook_lab.md`

Artifact: `02_hook_lab.md`

Tạo 10 candidate theo 10 curiosity mechanisms khác nhau:

1. Contradiction
2. Concrete scene
3. Mystery / evidence first
4. Reverse assumption
5. Mechanism in motion
6. Before → after transformation
7. Object hook
8. Stakes hook
9. Timeline jump
10. Unexpected cause

Các mechanism là **creative entry points**, không phải sentence templates. Candidate phải thực sự khác cách mở, không chỉ paraphrase.

Central question không bắt buộc xuất hiện dưới dạng câu hỏi trực tiếp. Không mặc định dùng `scene → question → answer` hoặc các scaffold như `Câu trả lời là...` / `The short answer is...`.

### Human gate — bắt buộc

Sau khi tạo Hook Lab:

- state → `current_stage: awaiting_hook_selection`;
- `hook_selection: PENDING`;
- trình bày H1–H10 cho user;
- **STOP**.

Không tự chọn hook. Không chạy Story Spine trước khi user chọn rõ ràng.

Khi user chọn H1–H10 hoặc tên mechanism, ghi selection vào `02_hook_lab.md` và state, rồi tiếp tục.

---

## Stage 3 — Story Spine

Prompt: `prompts/v2/03_story_spine.md`

Artifact: `03_story_spine.md`

Thiết kế central question, selected opening direction, 6–10 beats và direct ending/callback. Mỗi beat cũng xác định technical concept nào được introduce, viewer sẽ hiểu nó bằng cách nào và label có thật sự cần giữ hay không.

Hook đã chọn là opening direction. Writer có thể polish wording nhưng không âm thầm đổi mechanism.

### Gate B

PASS khi hook selection đã rõ, opening dẫn tự nhiên vào story, 6–10 beats tạo thành transformation/causal/chronological chain và ending có direct answer.

Nếu 3–4 beats có thể đổi chỗ tự do mà logic không đổi, revise Story Spine.

---

## Stage 4 — Full Draft

Prompt: `prompts/v2/04_draft.md`

Artifact: `04_draft.md`

Ưu tiên spoken, concrete, causal và comprehensible. Draft target khoảng ±10% target words.

Technical concept dùng `meaning first, label second`; giải thích function trước taxonomy; CORE term giải thích ở first use; DISPENSABLE jargon ưu tiên bỏ label.

Giữ opening mechanism đã chọn; không biến nó thành generic question-answer scaffold chỉ vì dễ viết.

---

## Stage 5 — Fact Audit

Prompt: `prompts/v2/05_fact_audit.md`

Artifact: `05_fact_audit.md`

Audit high-risk claims: number/date/quote, named study/person/institution, first/oldest/only/largest, causal/consensus/current claims, cinematic detail kể như fact, và plain-language explanation/analogy có nguy cơ làm sai technical meaning.

Actions: `KEEP | QUALIFY | REWRITE | REMOVE | VERIFY`.

`VERIFY` còn tồn tại = FAIL.

---

## Stage 6 — Final Edit

Prompt: `prompts/v2/06_final_edit.md`

Artifact: `06_final_script.md`

Áp dụng Fact Audit, cắt repetition/padding, làm prose dễ nói, giữ concrete cases mạnh, giữ selected hook mechanism, chạy cold-reader jargon pass và đưa final về ±7% target words.

---

## Final Validation

```bash
python scripts/check_project.py projects/<slug>
```

Hard FAIL cho `simple_v2` khi:

- thiếu artifact bắt buộc;
- Hook Lab chưa có selection;
- Fact Audit chưa PASS;
- final lệch quá ±7% target;
- final còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Template-like hook phrase chỉ WARN, không hard fail.

---

## State — simple_v2

```json
{
  "pipeline_version": "simple_v2",
  "current_stage": "input",
  "hook_selection": "PENDING",
  "selected_hook": "",
  "selected_hook_mechanism": "",
  "target_words": 0,
  "draft_words": 0,
  "final_words": 0,
  "fact_audit": "PENDING",
  "timing_gate": "PENDING"
}
```

---

## Rerun rules

- Research thiếu support → sửa Stage 1.
- Hook candidates quá giống nhau → rerun Hook Lab, không ép user chọn trong một batch yếu.
- User muốn hook khác/hybrid → revise Hook Lab và chỉ tiếp tục sau explicit selection.
- Story rời rạc → sửa Stage 3.
- Draft dài/ngắn vì thiếu substance → sửa Story Spine/Research, không filler.
- Fact Audit FAIL → sửa Research/Draft rồi audit lại.
- Final chỉ cần prose/timing cleanup → sửa Stage 6.

Project `simple_v1` cũ vẫn được checker hỗ trợ.
