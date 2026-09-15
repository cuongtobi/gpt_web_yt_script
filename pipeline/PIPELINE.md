# Pipeline

## Stage 0 — Intake

File: `00_input.md`

Chuẩn hóa topic, language, duration, audience, tone, title/angle nếu có. Tính target word budget. Viết một câu `viewer_promise`: xem hết video, người xem sẽ hiểu hoặc nhìn khác điều gì?

Không research sâu ở stage này.

## Stage 1 — Research Ledger

Prompt: `prompts/01_research.md`

Mục tiêu không phải tạo encyclopedia. Mục tiêu là thu thập đúng evidence cần cho central question **và một inventory đủ mạnh để kể story**.

Research theo các nhóm:

1. origin / before-state;
2. mechanism;
3. turning points;
4. concrete cases / objects / experiments / people;
5. reframe / counterevidence / reversal;
6. scale-expansion evidence;
7. modern consequence / why it matters.

Mỗi claim cần factual metadata + story metadata:

- status/source/support/limits;
- story role;
- story value;
- visual potential;
- playable scene/concrete anchor;
- human-scale example;
- scale potential;
- escalation value.

Research Ledger là factual boundary + story inventory, không phải narration order.

Output: `01_research_ledger.md`.

### Gate

Không sang architecture nếu thesis chính dựa trên claim `UNVERIFIED`.

## Stage 2 — Story Architecture

Prompt: `prompts/02_architecture.md`

Thiết kế câu chuyện trước khi viết câu chữ.

Bắt buộc có:

- central contradiction;
- hook archetype: ưu tiên Transformation Hook hoặc World-Before-X Hook khi phù hợp;
- central question;
- 4–5 Act Architecture;
- viewer-question chain;
- causal ladder 5–9 bước;
- Scale Escalation Map;
- Story Expansion Test;
- Reveal Ladder R1→R5;
- Curiosity Debt Map;
- historical/explanatory detours có chức năng;
- Visual Scene Density Map;
- uncertainty map;
- ending answer + reframe + implication + callback.

### Act rule

Mỗi act phải có:

- entry question/belief;
- payoff;
- scale/stakes/depth increase;
- consequence mở act kế.

Act chỉ gom các fact cùng chủ đề = fail.

### Causal rule

Causal ladder phải đọc được:

`A → therefore B → creates C → response D → consequence E`.

Nếu chỉ `A happened, then B, then C`, chưa đạt.

### Scale rule

Scale vocabulary:

`object → individual → community → institution → civilization → global/system`

Không cần tăng tuyến tính nhưng mỗi 2–3 beats phải có intentional zoom hoặc lý do giữ scale.

Output: `02_story_architecture.md`.

## Stage 3 — Retention Outline

Prompt: `prompts/03_outline.md`

Chia video thành acts + beats có timestamp/word budget.

Mỗi beat phải ghi:

- act;
- viewer question;
- evidence;
- playable scene / physical sequence;
- human-scale element;
- reveal/payoff;
- meaning;
- consequence;
- curiosity handoff;
- scale + zoom direction;
- story expansion function;
- visual anchor;
- open loops;
- reveal level R1–R5;
- novelty/stakes.

### Story Expansion rule

Mỗi beat phải ít nhất một:

- deepens mechanism;
- widens scale;
- changes interpretation;
- raises stakes.

Không có function → cut/compress/fold.

### Retention cadence

- 0:00–0:45: hook + contradiction + central question;
- 10–15% đầu: real payoff;
- 25–40%: mechanism/reframe đầu;
- 45–65%: evidence/case mạnh hơn opening;
- 60–80%: R3/R4 nếu topic hỗ trợ;
- 80–90%: hội tụ;
- cuối: answer → reframe → implication → callback.

### Scene density

Topic giàu visual evidence: khoảng 60–90 giây nên có playable scene hoặc physical sequence. Không để >2 phút chỉ abstraction nếu có cách kể cụ thể hơn.

Output: `03_outline.md`.

## Stage 4 — Draft

Prompt: `prompts/04_draft.md`

Viết theo outline nhưng ưu tiên spoken rhythm và story momentum.

Draft rules:

- claim factual chỉ dùng từ Research Ledger;
- mỗi beat phải có story expansion function;
- giữ act turns và scale movement;
- reward trước qualification khi accuracy cho phép;
- sau abstraction, quay về concrete/human-scale consequence;
- detour chỉ giữ nếu tăng scale/scene/reframe/stakes hoặc causal proof;
- không spam generic cliffhanger;
- không nhồi citation;
- CTA nếu có ngắn và không phá narrative.

### Dramatization doctrine

**Dramatize structure, never facts.**

Được reorder/delay/reveal/contrast/zoom/compress attribution.
Không được bịa dialogue, emotion, exact historical action, sensory detail, motive hoặc certainty.

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
- current fact;
- cinematic/sensory detail kể như fact.

Đánh dấu `KEEP`, `QUALIFY`, `REWRITE`, `REMOVE`, `VERIFY`.

Zero tolerance:

- invented probability;
- invented citation;
- unsupported quote;
- theory stated as settled fact;
- invented cinematic detail;
- current number không có nguồn hiện hành.

Output: `05_fact_audit.md`.

## Stage 6 — Retention / Story Momentum Audit

Prompt: `prompts/06_retention_audit.md`

Đọc draft như viewer lần đầu.

Audit:

- first 3 minutes;
- act progression / act turns;
- viewer-question chain;
- story expansion per beat;
- curiosity handoff;
- payoff cadence;
- Scale Escalation;
- intentional zoom-in/zoom-out;
- Reveal Ladder R1–R5;
- R3/R4 model change;
- playable scene density;
- research-order leak;
- methodology drag;
- decorative detours;
- transition/template repetition;
- compression;
- weakest-60-seconds test.

Retention score dùng thang `/40` trong `QUALITY_GATES.md`.

Output: `06_retention_audit.md`.

## Stage 7 — Final Rewrite

Prompt: `prompts/07_rewrite_final.md`

Áp dụng cả Fact Audit và Retention Audit ở cấp structure, act, scale, scene và prose.

Thứ tự ưu tiên:

1. factual integrity;
2. viewer-question chain;
3. central question/payoff;
4. act progression + causal coherence;
5. scale escalation + reveal ladder;
6. playable scene density;
7. spoken clarity;
8. duration;
9. style.

Không giữ câu hay nếu sai/overstated.

Final phải đạt:

- first 3 minutes pass;
- act progression pass;
- scale escalation pass;
- scene density pass;
- reveal ladder pass;
- Fact Audit pass;
- Retention/Story Momentum pass;
- timing pass.

Output: `07_final_script.md`.

## State

Cập nhật `project_state.json` sau mỗi stage:

- `current_stage`;
- `target_words`;
- `draft_words`;
- `final_words`;
- `fact_audit`;
- `retention_audit`;
- `first_3_minutes`;
- `architecture_gate`;
- `timing_gate`;
- `blocked_claims`;
- `updated_at`.

Có thể thêm:

- `act_progression`;
- `scale_escalation`;
- `scene_density`;
- `reveal_ladder`.

## Rerun rules

- Fact Audit fail → sửa Research Ledger hoặc Draft trước, không polish trực tiếp.
- Retention fail vì structure → quay lại Architecture/Outline.
- `FLAT ACT`, scale stagnation, weak R4 → sửa Stage 2/3 trước.
- Scene density fail → sửa Outline rồi Draft; không bịa scene.
- Duration fail >10% → rebudget Outline trước khi cắt/thêm ngẫu nhiên.
