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

1. Đọc `AGENTS.md`, `pipeline/PIPELINE.md`, `pipeline/QUALITY_GATES.md`, `docs/STYLE_DNA.md` và `docs/HOOK_STRATEGY_REGISTRY.md`.
2. Tạo slug ngắn, dễ đọc cho video.
3. Khởi tạo `projects/<slug>/` từ `templates/project/`.
4. Điền `00_input.md`, tính target WPM và target words.
5. Trước Stage 2, đọc `project_state.json` của tối đa 5 project hoàn tất gần nhất để lấy `style_fingerprint` và tránh lặp opening surface/signature.
6. Chạy tuần tự Stage 1 → 7 bằng prompt tương ứng trong `prompts/`.
7. Sau mỗi stage, lưu artifact vào project và cập nhật `project_state.json`.
8. Không bỏ qua Research Ledger đối với factual documentary/explainer.
9. Research Ledger là factual boundary + story inventory, **không phải thứ tự kể chuyện**.
10. Architecture phải thiết kế đủ:
   - central contradiction;
   - hook archetype;
   - Hook Strategy Registry selection;
   - Hook Candidate Tournament;
   - cross-project anti-template check;
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
11. Outline phải chuyển architecture thành word/time budget nhưng giữ act turns, scale movement và playable scene density.
12. Trong 10–15% đầu phải có real payoff; không để first 2–3 minutes thành methodology/setup lecture.
13. Khi accuracy cho phép, ưu tiên `reveal → evidence → meaning → qualification` thay vì `methodology → caveat → answer`.
14. Mỗi beat phải ít nhất một: `deepens mechanism`, `widens scale`, `changes interpretation`, `raises stakes`.
15. Mỗi 2–3 beats phải có intentional scale movement hoặc lý do rõ để giữ scale.
16. Với topic giàu visual evidence, khoảng 60–90 giây nên có playable scene/physical sequence; không bịa chi tiết để đạt scene density.
17. Chủ động tìm R3 reframe và R4 reversal nếu evidence/topic hỗ trợ; không tạo fake reversal bằng dramatic wording.
18. Historical/explanatory detours chỉ giữ nếu tăng scale, scene value, causal proof, reframe/reversal hoặc stakes.
19. Draft/Final được phép dramatize structure/presentation, **không dramatize evidence**.
20. Stage 7 phải chạy **Remove Narrator Scaffolding Pass** và cập nhật `style_fingerprint`.
21. Nếu research tool/web không khả dụng, không tự bịa nguồn. Ghi claim chưa kiểm chứng `UNVERIFIED` và chỉ dùng phần có support đáng tin cậy.
22. Nếu Fact Audit FAIL, sửa trước khi final.
23. Nếu Retention Audit FAIL vì structural issue, quay lại Architecture/Outline và reorder; không chỉ polish câu.
24. Final phải đạt timing tolerance hoặc giải thích rõ exception trong state.
25. Sau khi có final, chạy:

```bash
python scripts/check_project.py projects/<slug> --write-style-state
```

26. Nếu checker FAIL vì anti-template gate, quay lại Stage 2/7 để đổi opening surface/signature hoặc loại narrator scaffolding; không chỉ sửa vài từ cho qua checker.
27. Chạy checker lại không có `--write-style-state` và chỉ hoàn tất khi RESULT = PASS.

## Interaction policy

- Không hỏi lại điều user đã cung cấp.
- Nếu chỉ thiếu preference phụ, tự dùng default trong `AGENTS.md`.
- Chỉ hỏi khi thiếu thông tin khiến không thể xác định task, ví dụ không có topic.
- Khi user yêu cầu “viết script”, tự chạy toàn pipeline; không bắt user ra lệnh từng stage.
- Khi user yêu cầu sửa một project đang có, đọc artifacts hiện tại và tiếp tục từ stage phù hợp, không reset project vô cớ.

## Story target

Không clone câu chữ của video tham khảo. Tạo cùng cấp độ hấp dẫn bằng logic story, nhưng **không để surface form lặp thành template**.

Backend có thể dùng logic:

`concrete hook → contradiction → central question → early payoff → consequence → stronger question → causal discovery → scale expansion → reframe/reversal → synthesis → callback`

Nhưng final không được liên tục tự báo skeleton bằng các câu kiểu “Đây là bước ngoặt”, “Bây giờ câu chuyện lớn hơn”, “Nhưng câu hỏi tiếp theo là…”.

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
- Hook strategy + surface form;
- Cross-project similarity verdict;
- Narrator scaffolding verdict;
- 2–4 điểm story architecture nổi bật;
- bất kỳ uncertainty quan trọng nào còn giữ trong final.
