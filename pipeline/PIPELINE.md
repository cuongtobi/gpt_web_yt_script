# Simple YouTube Documentary Pipeline

Pipeline này cố ý **đơn giản**. Mục tiêu là tạo script có cảm giác như một documentary writer đang kể một chuỗi biến đổi có thật, không phải một model đang hoàn thành hàng chục controller.

## Stage 0 — Input

Artifact: `00_input.md`

Chuẩn hóa:

- topic;
- language;
- duration;
- audience / title / angle nếu user cung cấp;
- target WPM;
- target words.

Không research sâu ở Stage 0.

---

## Stage 1 — Research

Prompt: `prompts/01_research.md`

Artifact: `01_research.md`

Research pack gồm:

- 1–2 central question candidates;
- timeline / causal background cần thiết;
- khoảng 10–20 core claims;
- 5–8 strong cases / objects / studies;
- useful numbers / quotes;
- important uncertainties.

Research là factual boundary, không phải narration order.

### Gate

Không sang Story Spine nếu thesis chính dựa trên claim `UNVERIFIED` hoặc các bước lớn của câu chuyện chưa có support.

---

## Stage 2 — Story Spine

Prompt: `prompts/02_story_spine.md`

Artifact: `02_story_spine.md`

Chỉ thiết kế:

- central question;
- một opening cụ thể;
- 6–10 beats;
- direct ending + callback.

Mỗi beat trả lời:

```text
What happened / what do we learn?
Why does it matter to the central question?
What does it naturally lead to next?
Evidence / cases used:
```

Không ép R1–R5, acts, scale map, curiosity debt, scene quota hoặc hook archetype.

### Gate

Nếu 3–4 beats có thể đổi chỗ tự do mà logic không đổi, Story Spine còn quá modular. Sắp lại cho causal/chronological transformation rõ hơn.

---

## Stage 3 — Full Draft

Prompt: `prompts/03_draft.md`

Artifact: `03_draft.md`

Writer ưu tiên:

1. spoken;
2. concrete;
3. causal.

Chronology được phép nếu chronology chính là story.

Draft target khoảng ±10% target words.

Không thêm filler chỉ để đủ từ.

---

## Stage 4 — Fact Audit

Prompt: `prompts/04_fact_audit.md`

Artifact: `04_fact_audit.md`

Audit high-risk claims:

- precise number / percentage / date;
- quotes;
- named study/person/institution;
- first/oldest/only/largest;
- causal / consensus / current claims;
- cinematic or sensory detail told as fact.

Actions:

`KEEP | QUALIFY | REWRITE | REMOVE | VERIFY`

`VERIFY` còn tồn tại = FAIL.

Fact Audit tập trung factual integrity, không redesign story nếu không cần.

---

## Stage 5 — Final Edit

Prompt: `prompts/05_final_edit.md`

Artifact: `05_final_script.md`

Final Edit:

- áp dụng Fact Audit;
- cắt repetition/padding;
- làm prose dễ nói;
- rút methodology/attribution dài;
- giữ concrete cases mạnh;
- sửa transition máy móc khi cần;
- đưa final về ±7% target words;
- trả central question rõ ở cuối.

Anti-template là soft editorial check, không phải hard gate.

---

## Final Validation

Chạy:

```bash
python scripts/check_project.py projects/<slug>
```

Hard FAIL chỉ khi:

- thiếu artifact bắt buộc;
- Fact Audit chưa PASS;
- final lệch quá ±7% target;
- final còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Template-like prose chỉ WARN.

---

## State

`project_state.json` của project mới dùng:

```json
{
  "pipeline_version": "simple_v1",
  "current_stage": "input",
  "target_words": 0,
  "draft_words": 0,
  "final_words": 0,
  "fact_audit": "PENDING",
  "timing_gate": "PENDING"
}
```

Có thể lưu thêm `blocked_claims`, `important_uncertainties`, `stage_history`.

---

## Rerun rules

- Research thiếu support → sửa Stage 1.
- Story bị rời rạc → sửa Stage 2.
- Draft dài/ngắn vì thiếu substance → sửa Story Spine/Research, không filler.
- Fact Audit FAIL → sửa Research/Draft rồi audit lại.
- Final chỉ cần prose/timing cleanup → sửa Stage 5.

Không quay về architecture framework phức tạp trừ khi user yêu cầu phân tích riêng.
