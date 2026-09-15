# Master Orchestrator — Simple Documentary Pipeline

Dùng prompt này khi bắt đầu một YouTube documentary/explainer mới.

## Input tối thiểu

```text
topic: <chủ đề>
language: <ngôn ngữ>
duration: <phút>
```

Optional: title, angle, audience, tone, must_include, must_avoid, sources.

## Nhiệm vụ

Bạn đang làm việc trong repo `cuongtobi/gpt_web_yt_script`.

1. Đọc `AGENTS.md`, `pipeline/PIPELINE.md`, `pipeline/QUALITY_GATES.md` và `docs/STYLE_DNA.md`.
2. Tạo slug và khởi tạo `projects/<slug>/` từ `templates/project/`.
3. Điền `00_input.md`, target WPM và target words.
4. Chạy tuần tự 5 stage:
   - Stage 1 Research → `01_research.md`
   - Stage 2 Story Spine → `02_story_spine.md`
   - Stage 3 Full Draft → `03_draft.md`
   - Stage 4 Fact Audit → `04_fact_audit.md`
   - Stage 5 Final Edit → `05_final_script.md`
5. Cập nhật `project_state.json` sau mỗi stage.
6. Nếu Fact Audit FAIL, sửa Research/Draft rồi audit lại trước Final Edit.
7. Cuối cùng chạy `python scripts/check_project.py projects/<slug>` và chỉ coi project hoàn tất khi PASS.

## Story target

Pipeline không cố tối ưu hàng chục controller. Mục tiêu là một story spine rõ:

```text
concrete opening
→ big contrast / central question
→ before-state or origin
→ change
→ consequence
→ next change
→ stronger evidence/case
→ larger transformation
→ modern form
→ direct answer
→ callback
```

Chronology được phép nếu chronology chính là story.

## Writing doctrine

Ưu tiên ba phẩm chất:

- **spoken** — nghe như narration, không như essay;
- **concrete** — thường xuyên có người/vật/địa điểm/action/mechanism cụ thể;
- **causal** — đoạn sau xuất hiện vì đoạn trước tạo consequence hoặc câu hỏi thật.

Không ép:

- R1→R5;
- Scale Escalation Map;
- Curiosity Debt Map;
- scene quota;
- hook archetype quota;
- cross-project similarity hard gate;
- narrator-scaffolding score.

Những thứ này có thể là editorial observations, không phải bài kiểm tra writer phải vượt qua.

## Factual doctrine

Research là factual boundary.

Không bịa source, quote, statistic, probability, exact historical action, sensory detail hoặc causal certainty.

High-risk claims phải được kiểm tra lại ở Fact Audit, ưu tiên original/primary source.

## Completion message

Báo ngắn:

- project path;
- final words / target;
- estimated duration;
- Fact Audit verdict;
- checker verdict;
- 2–4 điểm nổi bật của Story Spine;
- uncertainty quan trọng còn giữ trong final.
