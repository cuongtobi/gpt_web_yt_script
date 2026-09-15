# Pipeline

## Stage 0 — Intake

File: `00_input.md`

Chuẩn hóa topic, language, duration, audience, tone, title/angle nếu có. Tính target word budget. Viết một câu `viewer_promise`: xem hết video, người xem sẽ hiểu hoặc nhìn khác điều gì?

Không research sâu ở stage này.

## Stage 1 — Research Ledger

Prompt: `prompts/01_research.md`

Mục tiêu không phải tạo encyclopedia. Mục tiêu là thu thập đúng bằng chứng cần cho central question và causal ladder.

Research theo 5 nhóm:

1. origin / before-state;
2. mechanism;
3. turning points;
4. concrete cases / objects / experiments / people;
5. modern consequence / why it matters now.

Mỗi claim cần: claim, status, source, source type, support excerpt/notes, story use, visual potential.

Output: `01_research_ledger.md`.

### Gate

Không sang architecture nếu thesis chính dựa trên claim `UNVERIFIED`.

## Stage 2 — Story Architecture

Prompt: `prompts/02_architecture.md`

Thiết kế câu chuyện trước khi viết câu chữ.

Bắt buộc có:

- opening image;
- central question;
- surprising contrast;
- before-state;
- causal ladder 5–9 bước;
- escalation map;
- macro open loop;
- 2–4 major payoffs;
- ending callback;
- uncertainty map.

Causal ladder phải đọc được theo dạng:

`A → therefore B → which creates C → so humans/systems respond with D → which changes E`.

Nếu chỉ có `A happened, then B happened, then C happened`, architecture chưa đạt.

Output: `02_story_architecture.md`.

## Stage 3 — Retention Outline

Prompt: `prompts/03_outline.md`

Chia video thành beats có timestamp/word budget.

Mỗi beat phải ghi:

- question being answered;
- evidence;
- meaning;
- consequence;
- visual anchor;
- transition/open loop;
- approximate words/seconds;
- novelty/stakes level 1–5.

Rule mặc định:

- 0:00–0:45: hook + central question;
- trước ~15% video: viewer phải hiểu stakes và hướng trả lời;
- mỗi 60–120 giây nên có pattern change: new case, mechanism, reveal, scale shift hoặc question;
- giữa video phải có ít nhất một reframe lớn;
- 80–90%: bắt đầu hội tụ về answer;
- cuối: answer → meaning → callback.

Output: `03_outline.md`.

## Stage 4 — Draft

Prompt: `prompts/04_draft.md`

Viết theo outline, nhưng ưu tiên spoken rhythm hơn việc bám câu chữ outline.

Draft rule:

- claim factual chỉ dùng từ Research Ledger;
- không nhồi citation trong narration;
- source attribution chỉ nêu khi nó tạo giá trị story hoặc cần để qualify claim;
- mỗi paragraph phải làm ít nhất một việc: advance plot, explain mechanism, raise stakes, pay off question, create visual, or bridge to next beat;
- xóa paragraph chỉ paraphrase đoạn trước;
- tránh intro CTA trước khi hook được payoff tối thiểu một lần;
- CTA nếu có phải ngắn và không làm đứt narrative.

Output: `04_draft.md`.

## Stage 5 — Fact Audit

Prompt: `prompts/05_fact_audit.md`

Audit từng claim có rủi ro:

- number/date/statistic;
- named study/person/institution;
- quotation;
- “first/oldest/largest/only”;
- causal claim;
- consensus claim;
- probability;
- current fact.

Đánh dấu `KEEP`, `QUALIFY`, `REWRITE`, `REMOVE`, `VERIFY`.

Zero tolerance:

- invented probability;
- invented citation;
- unsupported quote;
- theory stated as settled fact;
- current number không có nguồn hiện hành.

Output: `05_fact_audit.md`.

## Stage 6 — Retention Audit

Prompt: `prompts/06_retention_audit.md`

Đọc draft như viewer lần đầu.

Audit:

- 30 giây đầu có visual + tension + question không?
- có đoạn 45–90 giây không tạo thông tin/ý nghĩa mới không?
- micro open loop có được payoff không?
- escalation có tăng hay phẳng?
- có quá nhiều proper nouns/dates liên tiếp không?
- có abstract block khó dựng hình không?
- transition có lặp template không?
- one-liner có bị spam không?
- có thể cắt 10% mà không mất gì không? Nếu có, draft còn padding.
- ending có chỉ recap hay thực sự reframe/callback?

Output: `06_retention_audit.md`.

## Stage 7 — Final Rewrite

Prompt: `prompts/07_rewrite_final.md`

Áp dụng cả hai audit.

Thứ tự ưu tiên khi conflict:

1. factual integrity;
2. central question clarity;
3. causal coherence;
4. retention;
5. duration;
6. stylistic flourish.

Không được giữ câu hay nếu câu đó sai hoặc overstated.

Output: `07_final_script.md`.

## State

Cập nhật `project_state.json` sau mỗi stage:

- `current_stage`;
- `target_words`;
- `draft_words`;
- `fact_audit`;
- `retention_audit`;
- `blocked_claims`;
- `updated_at`.

## Rerun rules

- Fact Audit fail → sửa Research Ledger hoặc Draft trước, không polish trực tiếp.
- Retention fail nhưng fact pass → sửa Architecture/Outline nếu vấn đề structural; sửa Draft nếu chỉ prose-level.
- Duration fail >10% → rebudget Outline trước khi cắt/thêm ngẫu nhiên.
