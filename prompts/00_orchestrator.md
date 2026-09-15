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
8. Nếu research tool/web không khả dụng, không tự bịa nguồn. Ghi claim chưa kiểm chứng là `UNVERIFIED` và viết final chỉ từ phần có support đáng tin cậy đã được user cung cấp hoặc repo có sẵn.
9. Nếu Fact Audit FAIL, sửa trước khi chạy final.
10. Nếu Retention Audit FAIL vì structural issue, quay lại Architecture/Outline thay vì chỉ polish câu chữ.
11. Final phải đạt timing tolerance hoặc giải thích rõ exception trong state.

## Interaction policy

- Không hỏi lại điều user đã cung cấp.
- Nếu chỉ thiếu preference phụ, tự dùng default trong `AGENTS.md`.
- Chỉ hỏi khi thiếu thông tin khiến không thể xác định task, ví dụ không có topic.
- Khi user yêu cầu “viết script”, tự chạy toàn pipeline; không bắt user ra lệnh từng stage.
- Khi user yêu cầu sửa một project đang có, đọc artifacts hiện tại và tiếp tục từ stage phù hợp, không reset project vô cớ.

## Story target

Không clone câu chữ của video tham khảo. Tạo cùng cấp độ chất lượng bằng các cơ chế:

`cinematic/concrete hook → surprising contrast → central question → before-state → causal ladder → evidence/case → meaning → consequence → new question → escalation/reframe → answer → larger implication → callback`

Mỗi section phải trả lời được: **vì sao người xem cần đoạn này để hiểu câu hỏi trung tâm?**

## Completion message

Khi hoàn thành, báo ngắn:

- project path;
- final word count / target;
- estimated duration;
- Fact Audit verdict;
- Retention Audit score/verdict;
- 2–4 điểm story architecture nổi bật;
- bất kỳ uncertainty quan trọng nào còn giữ trong final.
