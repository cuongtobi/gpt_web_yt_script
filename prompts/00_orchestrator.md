# Master Orchestrator — Simple Documentary Pipeline v2

Dùng prompt này khi bắt đầu một YouTube documentary/explainer mới.

## Input tối thiểu

```text
topic: <chủ đề>
language: <ngôn ngữ>
duration: <phút>
```

Optional: title, angle, audience, tone, must_include, must_avoid, sources, hook_choice.

## Nhiệm vụ

Bạn đang làm việc trong repo `cuongtobi/gpt_web_yt_script`.

1. Đọc `AGENTS.md`, `pipeline/PIPELINE.md`, `pipeline/QUALITY_GATES.md`, `docs/STYLE_DNA.md` và `docs/LANGUAGE_COMPREHENSION.md`. Chọn profile tương ứng với output language.
2. Tạo slug và khởi tạo `projects/<slug>/` từ `templates/project_v2/`.
3. Điền `00_input.md`, target WPM và target words.
4. Chạy Stage 1 Research → `01_research.md`.
5. Chạy Stage 2 Hook Lab theo `prompts/v2/02_hook_lab.md` → `02_hook_lab.md`.
6. Cập nhật state thành `awaiting_hook_selection`, trình bày 10 candidate H1–H10 cho user và **DỪNG**.
7. Chỉ khi user explicit chọn H1–H10 hoặc tên mechanism:
   - cập nhật Selection trong `02_hook_lab.md`;
   - đặt `hook_selection = SELECTED` cùng `selected_hook` và `selected_hook_mechanism` trong state;
   - chạy Stage 3 Story Spine → `03_story_spine.md`;
   - Stage 4 Full Draft → `04_draft.md`; sau khi draft xong, scan lại mọi technical/academic/foreign term thực tế phát sinh;
   - Stage 5 Fact Audit → `05_fact_audit.md`, bắt buộc có Draft Term Inventory + Language comprehension audit;
   - nếu audit FAIL, sửa Research/Draft rồi audit lại;
   - Stage 6 Final Edit → `06_final_script.md`, chạy native cold-reader pass theo output language.
8. Cập nhật `project_state.json` sau mỗi stage.
9. Cuối cùng chạy `python scripts/check_project.py projects/<slug>` và chỉ coi project hoàn tất khi PASS.

Nếu input ban đầu đã có `hook_choice`, vẫn tạo Hook Lab để trace alternatives nhưng có thể ghi selection ngay và tiếp tục mà không dừng.

## Hook Lab doctrine

Hook Lab luôn tạo đúng 10 **entry mechanisms** khác nhau:

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

Đây không phải 10 sentence templates. Mỗi candidate phải khác thật sự về đường vào story.

Không mặc định:

- `scene → direct question → Câu trả lời...`;
- `Câu trả lời là...`;
- `Câu trả lời bắt đầu...`;
- `Câu trả lời ngắn gọn...`;
- `The answer is...`;
- `The short answer is...`;
- `Hãy tưởng tượng...` / `Imagine...`.

Central question phải rõ trong planning nhưng không bắt buộc xuất hiện trực tiếp trong hook. Sau tension/question, ưu tiên fact, evidence, mechanism, contradiction hoặc consequence.

### Human choice is mandatory

Không tự xếp hạng rồi chọn hộ user. Có thể ghi ngắn trade-off của từng candidate trong artifact, nhưng completion message sau Hook Lab chỉ cần đưa 10 lựa chọn rõ ràng và yêu cầu user chọn.

Nếu user chưa chọn, **không chạy Story Spine trở đi**, dù user ban đầu dùng cụm “chạy toàn bộ pipeline”. Hook selection là intentional human gate của pipeline v2.

## Story target

Sau selection, Story Spine ưu tiên một causal/chronological/mechanistic chain rõ. Không ép một north-star flow duy nhất cho mọi topic.

Ưu tiên bốn phẩm chất:

- **spoken** — nghe như narration, không như essay;
- **concrete** — thường xuyên có người/vật/địa điểm/action/mechanism cụ thể;
- **causal** — đoạn sau xuất hiện vì đoạn trước tạo consequence hoặc câu hỏi thật;
- **native-comprehensible** — nghe tự nhiên với general native viewer của output language, không phải bản dịch của một narration style khác.

Selected hook là opening direction. Có thể polish exact wording nhưng không đổi mechanism chỉ vì một skeleton khác dễ viết hơn.

## Factual doctrine

Research là factual boundary. `docs/LANGUAGE_COMPREHENSION.md` là comprehension/register boundary cho supported languages.

Không bịa source, quote, statistic, probability, exact historical action, sensory detail hoặc causal certainty. High-risk claims phải được kiểm tra lại ở Fact Audit, ưu tiên original/primary source.

## Message sau Hook Lab

Báo ngắn:

- project path;
- Research readiness;
- H1–H10: mechanism + nguyên văn hook candidate;
- câu nhắc: `Chọn H1–H10 (hoặc tên mechanism). Sau khi bạn chọn, pipeline sẽ tiếp tục từ Story Spine.`

Không báo project hoàn tất ở bước này.

## Completion message sau Final

Báo ngắn:

- project path;
- selected hook + mechanism;
- final words / target;
- estimated duration;
- Fact Audit verdict;
- checker verdict;
- 2–4 điểm nổi bật của Story Spine;
- uncertainty quan trọng còn giữ trong final.
