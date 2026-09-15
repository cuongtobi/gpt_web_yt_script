# Master Orchestrator Prompt

Dùng prompt này khi bắt đầu một video mới bằng ChatGPT Web/Codex.

## Input từ user

Tối thiểu:

```text
topic: <chủ đề>
language: <ngôn ngữ>
duration: <phút>
```

Có thể có thêm title, angle, audience, tone, must_include, must_avoid, sources.

## Nhiệm vụ

Bạn đang làm việc trong repo `cuongtobi/gpt_web_yt_script`.

1. Đọc `AGENTS.md`, `pipeline/PIPELINE.md`, `pipeline/QUALITY_GATES.md` và `docs/STYLE_DNA.md`.
2. Tạo slug ngắn, dễ đọc cho video.
3. Khởi tạo `projects/<slug>/` từ `templates/project/`.
4. Điền `00_input.md`, tính target WPM và target words.
5. Chạy tuần tự Stage 1 → 7 bằng prompt tương ứng trong `prompts/`.
6. Sau mỗi stage, lưu artifact vào project và cập nhật `project_state.json`.
7. Không bỏ qua Research Ledger đối với factual documentary/explainer.
8. Research Ledger là factual boundary, **không phải thứ tự kể chuyện**.
9. Architecture và Outline phải được thiết kế từ viewer-question chain: mỗi payoff tạo consequence/câu hỏi tiếp theo.
10. Trong 10–15% đầu phải có real payoff; không để first 2–3 minutes thành methodology/setup lecture.
11. Khi accuracy cho phép, ưu tiên `reveal → evidence → meaning → qualification` thay vì `methodology → caveat → answer`.
12. Nếu research tool/web không khả dụng, không tự bịa nguồn. Ghi claim chưa kiểm chứng là `UNVERIFIED` và viết final chỉ từ phần có support đáng tin cậy đã được user cung cấp hoặc repo có sẵn.
13. Nếu Fact Audit FAIL, sửa trước khi chạy final.
14. Nếu Retention Audit FAIL vì structural issue, quay lại Architecture/Outline và reorder thay vì chỉ polish câu chữ.
15. Final phải đạt timing tolerance hoặc giải thích rõ exception trong state.

## Interaction policy

- Không hỏi lại điều user đã cung cấp.
- Nếu chỉ thiếu preference phụ, tự dùng default trong `AGENTS.md`.
- Chỉ hỏi khi thiếu thông tin khiến không thể xác định task, ví dụ không có topic.
- Khi user yêu cầu “viết script”, tự chạy toàn pipeline; không bắt user ra lệnh từng stage.
- Khi user yêu cầu sửa một project đang có, đọc artifacts hiện tại và tiếp tục từ stage phù hợp, không reset project vô cớ.

## Story target

Không clone câu chữ của video tham khảo. Tạo cùng cấp độ hấp dẫn bằng logic:

`cinematic/concrete hook → central contradiction → central question → early payoff → consequence → stronger question → causal discovery → concrete evidence → reveal → reframe/reversal → synthesis → callback`

Mỗi section phải trả lời cả hai câu:

1. **Vì sao viewer cần đoạn này để hiểu câu hỏi trung tâm?**
2. **Sau đoạn này, viewer tự nhiên muốn biết điều gì tiếp theo?**

Nếu câu trả lời thứ hai không rõ, story handoff bị gãy.

## Completion message

Khi hoàn thành, báo ngắn:

- project path;
- final word count / target;
- estimated duration;
- Fact Audit verdict;
- Retention Audit score/verdict;
- First 3 minutes verdict;
- 2–4 điểm story architecture nổi bật;
- bất kỳ uncertainty quan trọng nào còn giữ trong final.
