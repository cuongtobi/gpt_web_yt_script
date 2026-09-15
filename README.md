# GPT Web YouTube Script Pipeline

Pipeline viết YouTube documentary/explainer script theo cấu trúc kể chuyện giữ chân người xem: cinematic hook → central question → causal chain → evidence → implication → open loop → thematic callback.

Repo được thiết kế để dùng trực tiếp với ChatGPT Web / Codex + GitHub. Mỗi video là một workspace riêng trong `projects/<slug>/`.

## Mục tiêu

- Đầu vào tối thiểu: chủ đề, ngôn ngữ, độ dài video.
- Đầu ra: YouTube video script hoàn chỉnh, độ dài bám sát thời lượng yêu cầu.
- Viết để nói, không phải để đọc như bài luận.
- Hook mạnh trong 30–45 giây đầu.
- Thông tin quan trọng xuất hiện sớm.
- Mức độ hấp dẫn tăng dần, có macro open loop và micro open loops.
- Script phải tạo được hình ảnh/B-roll rõ ràng.
- Không kéo dài bằng cách lặp ý.
- Phân biệt fact, theory, interpretation và uncertainty.
- Cấm tự bịa xác suất, số liệu, nguồn hoặc “false precision”.
- Giảm dấu vết template/AI bằng kiểm soát transition, sentence rhythm và rhetorical patterns.

## Cách dùng nhanh

1. Đọc `AGENTS.md`.
2. Tạo thư mục `projects/<slug>/` từ `templates/project/`.
3. Điền `00_input.md`.
4. Chạy tuần tự các stage trong `pipeline/PIPELINE.md`.
5. Chỉ xuất bản `07_final_script.md` khi vượt qua Fact Audit và Retention Audit.

## Pipeline

`00_input` → `01_research_ledger` → `02_story_architecture` → `03_outline` → `04_draft` → `05_fact_audit` → `06_retention_audit` → `07_final_script`

Chi tiết xem `pipeline/PIPELINE.md`.

## DNA storytelling

Pipeline không sao chép câu chữ của bất kỳ video mẫu nào. Nó học ở cấp cấu trúc:

- mở bằng một cảnh cụ thể hoặc nghịch lý có thể hình dung;
- làm một thứ quen thuộc trở nên lạ để tạo câu hỏi;
- tổ chức nội dung theo chuỗi nguyên nhân–hệ quả thay vì danh sách fact;
- mỗi phần phải trả lời một câu hỏi và mở ra câu hỏi tiếp theo;
- dùng evidence để dẫn tới meaning, không dùng authority stacking;
- thay đổi scale và loại hình ảnh để tránh nhịp đều;
- cuối video trả lời câu hỏi trung tâm và callback tới hình ảnh mở đầu.

## Cấu trúc repo

```text
AGENTS.md
README.md
pipeline/
  PIPELINE.md
  QUALITY_GATES.md
prompts/
  01_research.md
  02_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_rewrite_final.md
templates/project/
  00_input.md
  01_research_ledger.md
  02_story_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_final_script.md
  project_state.json
```

## Nguyên tắc quan trọng nhất

**Question → Evidence → Meaning → Consequence → New Question.**

Nếu một đoạn chỉ đưa fact mà không làm thay đổi hiểu biết của người xem, đoạn đó chưa hoàn thành nhiệm vụ.
