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
8. Research Ledger là factual boundary + story inventory, **không phải thứ tự kể chuyện**.
9. Architecture phải thiết kế đủ:
   - central contradiction;
   - hook archetype;
   - 4–5 act progression;
   - viewer-question chain;
   - causal ladder;
   - Scale Escalation Map;
   - Story Expansion Test;
   - Reveal Ladder R1→R5;
   - Curiosity Debt Map;
   - Visual Scene Density Map;
   - detours có chức năng;
   - ending callback.
10. Outline phải chuyển architecture thành word/time budget nhưng giữ act turns, scale movement và playable scene density.
11. Trong 10–15% đầu phải có real payoff; không để first 2–3 minutes thành methodology/setup lecture.
12. Khi accuracy cho phép, ưu tiên `reveal → evidence → meaning → qualification` thay vì `methodology → caveat → answer`.
13. Mỗi beat phải ít nhất một: `deepens mechanism`, `widens scale`, `changes interpretation`, `raises stakes`.
14. Mỗi 2–3 beats phải có intentional scale movement hoặc lý do rõ để giữ scale.
15. Với topic giàu visual evidence, khoảng 60–90 giây nên có playable scene/physical sequence; không bịa chi tiết để đạt scene density.
16. Chủ động tìm R3 reframe và R4 reversal nếu evidence/topic hỗ trợ; không tạo fake reversal bằng dramatic wording.
17. Historical/explanatory detours chỉ giữ nếu tăng scale, scene value, causal proof, reframe/reversal hoặc stakes.
18. Draft/Final được phép dramatize structure/presentation, **không dramatize evidence**.
19. Nếu research tool/web không khả dụng, không tự bịa nguồn. Ghi claim chưa kiểm chứng `UNVERIFIED` và chỉ dùng phần có support đáng tin cậy.
20. Nếu Fact Audit FAIL, sửa trước khi final.
21. Nếu Retention Audit FAIL vì structural issue, quay lại Architecture/Outline và reorder; không chỉ polish câu.
22. Final phải đạt timing tolerance hoặc giải thích rõ exception trong state.

## Interaction policy

- Không hỏi lại điều user đã cung cấp.
- Nếu chỉ thiếu preference phụ, tự dùng default trong `AGENTS.md`.
- Chỉ hỏi khi thiếu thông tin khiến không thể xác định task, ví dụ không có topic.
- Khi user yêu cầu “viết script”, tự chạy toàn pipeline; không bắt user ra lệnh từng stage.
- Khi user yêu cầu sửa một project đang có, đọc artifacts hiện tại và tiếp tục từ stage phù hợp, không reset project vô cớ.

## Story target

Không clone câu chữ của video tham khảo. Tạo cùng cấp độ hấp dẫn bằng logic:

`cinematic/concrete hook → transformation/central contradiction → central question → early payoff → consequence → stronger question → causal discovery → scale expansion → concrete scene → deeper mechanism → reframe/reversal → larger consequence → synthesis → callback`

Mỗi section phải trả lời:

1. **Vì sao viewer cần đoạn này để hiểu câu hỏi trung tâm?**
2. **Sau đoạn này, viewer tự nhiên muốn biết gì tiếp?**
3. **Đoạn này làm story sâu hơn, lớn hơn, khác đi hoặc quan trọng hơn ở đâu?**
4. **Viewer có thể nhìn thấy/dựng được gì?**

Nếu câu 2 không rõ → handoff gãy.
Nếu câu 3 không rõ → beat không có story expansion.
Nếu câu 4 liên tục không rõ → visual density yếu.

## Completion message

Khi hoàn thành, báo ngắn:

- project path;
- final word count / target;
- estimated duration;
- Fact Audit verdict;
- Retention/Story Momentum score + verdict;
- First 3 minutes verdict;
- Act progression verdict;
- Scale escalation verdict;
- Scene density verdict;
- Reveal ladder verdict;
- 2–4 điểm story architecture nổi bật;
- bất kỳ uncertainty quan trọng nào còn giữ trong final.
