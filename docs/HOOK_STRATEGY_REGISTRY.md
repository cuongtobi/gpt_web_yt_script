# Hook Strategy Registry — Anti-Template Surface Control

Mục tiêu của tài liệu này là giữ **story architecture mạnh** nhưng tránh để nhiều video liên tiếp lộ cùng một bề mặt AI/template.

Phân biệt hai khái niệm:

- `hook_strategy`: logic kể chuyện bên dưới opening.
- `hook_surface_form`: cách opening xuất hiện trên câu chữ.

Hai video có thể dùng cùng logic như contradiction hoặc world-before-X, nhưng **không được mặc định dùng cùng surface form**.

## Registry

### H01 — ACTION_FIRST
Mở bằng một hành động vật lý cụ thể đang xảy ra.

Ví dụ abstract: một vật bị cắt, một máy dừng, một người chạm vào thứ gì đó, một quá trình bắt đầu.

### H02 — OBJECT_FIRST
Mở bằng một vật thể cụ thể rồi dùng vật đó để mở contradiction lớn hơn.

### H03 — COLD_FACT
Mở bằng một fact ngắn, trực tiếp, có bằng chứng và tự nó tạo tension.

Không dùng số liệu chỉ để shock nếu con số đó không quan trọng với thesis.

### H04 — CONTRADICTION_FIRST
Đặt hai điều cùng đúng nhưng khó hòa giải cạnh nhau ngay từ đầu.

### H05 — RESULT_FIRST
Mở bằng hậu quả hoặc trạng thái cuối rồi quay lại câu hỏi “làm sao đến đây?”.

### H06 — DIRECT_QUESTION
Mở thẳng bằng câu hỏi trung tâm hoặc một phiên bản cụ thể hơn của nó.

Không dùng như default cho mọi video.

### H07 — EVIDENCE_FIRST
Mở bằng một bằng chứng nhìn thấy được: vật thể, di tích, bản đồ, ảnh scan, tài liệu, dấu vết, kết quả thí nghiệm.

### H08 — MECHANISM_FIRST
Mở bằng một cơ chế vật lý/sinh học/kinh tế đang vận hành và để consequence tạo câu hỏi.

### H09 — PERSON_OR_CASE_FIRST
Mở bằng một case/person/event có source support thật sự và liên quan trực tiếp tới central question.

Không bịa cảm xúc, lời thoại hay chi tiết scene.

### H10 — BEFORE_AFTER
Đặt before/after cạnh nhau nhưng không cần dùng imperative imagination.

### H11 — DATA_OR_PATTERN_FIRST
Mở bằng một pattern rõ trong data hoặc repeated observation, rồi hỏi mechanism phía sau.

### H12 — SCENE_FIRST
Mở bằng một scene factual/concrete có place/object/action đủ dựng hình.

Scene không đồng nghĩa với “Hãy tưởng tượng…”. Nếu là reconstruction, phải giữ đúng epistemic boundary.

## Surface forms

Surface form phải được ghi riêng trong `02_story_architecture.md` và `project_state.json`.

Các family tham khảo:

- `imperative_imagination` — “Hãy tưởng tượng…”, “Hãy thử…”, “Imagine…”, “Picture this…”
- `direct_statement`
- `direct_question`
- `action_sentence`
- `object_description`
- `fact_statement`
- `result_statement`
- `evidence_description`
- `person_case_intro`
- `before_after_statement`

`imperative_imagination` **không bị cấm tuyệt đối**, nhưng không được dùng như opening mặc định. Nếu đã xuất hiện trong một trong các project gần nhất thì phải chọn surface khác, trừ khi user yêu cầu rõ.

## Cross-project selection rule

Trước khi chốt Architecture:

1. Đọc `project_state.json` của tối đa 5 project hoàn tất gần nhất trong `projects/`.
2. Ghi lại `hook_strategy`, `hook_surface_form`, `opening_signature`.
3. Không lặp `hook_surface_form` của 2 project gần nhất.
4. Không lặp cùng `opening_signature` với 2 project gần nhất.
5. Nếu cùng `hook_strategy` với nhiều project gần đây, chỉ được giữ khi surface form và opening sequence thực sự khác.
6. Nếu topic tự nhiên chỉ phù hợp một strategy, giữ strategy nhưng thay surface.

## Hook Candidate Tournament

Architecture phải tạo **ít nhất 4 candidate hooks khác nhau về cấu trúc**, không phải chỉ paraphrase.

Mỗi candidate ghi:

- strategy ID;
- surface form;
- opening signature;
- concrete anchor;
- contradiction/tension;
- early payoff path;
- similarity risk với recent projects.

Chọn candidate thắng theo thứ tự ưu tiên:

1. factual integrity;
2. central-question clarity;
3. curiosity;
4. playable visual;
5. uniqueness so với recent projects;
6. spoken naturalness.

## Opening signature

`opening_signature` là mô tả ngắn sequence chức năng của 30–45 giây đầu, ví dụ:

- `object -> contradiction -> payoff -> question`
- `action -> mechanism -> contradiction -> question`
- `evidence -> implication -> question`
- `result -> rewind -> mechanism`

Không dùng wording của script làm signature.

## Anti-template principle

Backend có thể giữ story logic mạnh như:

`contradiction -> payoff -> consequence -> stronger question`

Nhưng final prose không được liên tục tự báo cấu trúc bằng các câu kiểu:

- “Đây là bước ngoặt.”
- “Bây giờ câu chuyện trở nên lớn hơn.”
- “Nhưng câu hỏi tiếp theo là…”
- “Và đây là điều thú vị.”

Structure phải được **cảm nhận qua evidence và consequence**, không cần narrator liên tục chỉ dẫn viewer rằng một beat đang là reveal/reframe/turn.
