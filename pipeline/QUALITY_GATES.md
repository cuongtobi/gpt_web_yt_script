# Quality Gates

## Gate A — Research readiness

PASS khi:

- central question có đủ bằng chứng để trả lời;
- mỗi causal step quan trọng có ít nhất một source/support note phù hợp;
- các claim gây tranh luận đã có certainty label;
- không thesis nào dựa trên nguồn không kiểm chứng;
- các claim quan trọng đã có Story role / Story value / Visual potential khi phù hợp;
- có đủ evidence để tạo ít nhất một reframe/reversal nếu topic thực sự hỗ trợ.

FAIL nếu script chỉ có nhiều fact nhưng không có evidence cho causal chain.

## Gate B — Architecture

Chấm 0–2 mỗi mục:

1. opening image/contrast cụ thể;
2. central contradiction mạnh;
3. central question rõ;
4. hook archetype có transformation hoặc world-before-X tension;
5. act architecture có progression;
6. viewer-question chain tự nhiên;
7. causal ladder thay vì timeline dump;
8. early payoff trong 10–15%;
9. curiosity handoff giữa beats;
10. reveal ladder R1→R5;
11. có R3 và R4 nếu evidence/topic hỗ trợ;
12. scale escalation map;
13. story expansion ở mỗi beat;
14. playable scene density plan;
15. visual/scale variety;
16. ending answer + reframe + callback.

PASS: >= 26/32 và không mục nào 0 ở central question, act progression, viewer-question chain, causal ladder, early payoff, scale escalation, ending.

FAIL tự động nếu:

- 2–3 phút đầu chủ yếu là methodology/setup mà chưa có real payoff;
- 4+ beats có thể đổi chỗ tự do mà không ảnh hưởng causal/story progression;
- act structure chỉ là chronology labels;
- story không có scale movement dù topic rõ ràng cho phép.

## Gate C — Draft integrity

PASS khi:

- độ dài draft trong ±10% target;
- không paragraph nào chỉ lặp lại ý trước;
- không có 3 đoạn abstract liên tiếp;
- không có 2 beat methodology/caveat-heavy liên tiếp nếu chưa payoff;
- source/name/date chỉ xuất hiện khi cần;
- CTA không phá hook;
- script nói thành tiếng tự nhiên;
- mỗi beat có story function rõ;
- mỗi beat deepens mechanism, widens scale, changes interpretation hoặc raises stakes;
- act turns có payoff/consequence;
- không có decorative factual detail unsupported;
- không dùng invented historical/sensory detail để đạt cinematic density.

## Gate D — Fact Audit

PASS khi:

- 100% precise numbers quan trọng có support;
- 100% quote quan trọng được verify hoặc đã paraphrase;
- 100% “first/oldest/only/largest” có support đủ mạnh hoặc đã qualify;
- không có fabricated probability;
- theory ≠ fact;
- current facts có nguồn phù hợp với thời điểm project;
- cinematic/sensory detail trình bày như fact cũng phải có support;
- dramatization chỉ nằm ở structure/presentation, không ở evidence.

Bất kỳ fabricated source/number/quote nào = FAIL tự động.

## Gate E — Retention / Story Momentum Audit

Score 0–2 mỗi mục:

1. hook visual + central contradiction;
2. transformation/world-before-X tension;
3. central question;
4. first meaningful payoff early;
5. act progression;
6. strong act turns;
7. viewer-question chain;
8. curiosity handoffs;
9. payoff cadence;
10. causal escalation;
11. story expansion per beat;
12. scale escalation;
13. intentional zoom-in/zoom-out;
14. major reframe/reversal;
15. reveal ladder clarity;
16. playable scene density;
17. no research-order/methodology drag;
18. no padding/decorative detours;
19. transition/rhetorical diversity;
20. ending answer + reframe + callback.

PASS: >= 33/40 và các mục 1, 4, 5, 7, 10, 12, 16, 18, 20 không được 0.

FAIL tự động nếu:

- first 3 minutes chủ yếu là setup/methodology;
- có 2+ `BROKEN HANDOFF` nghiêm trọng liên tiếp;
- major reveal bị chôn sau đoạn explanation có thể reorder mà không ảnh hưởng accuracy;
- script có nhiều đoạn đúng nhưng viewer không có lý do cụ thể để tiếp tục;
- có `FLAT ACT` lớn không được sửa;
- 3+ beats liên tiếp cùng abstract scale mà topic có cách zoom in/out rõ;
- >2 phút abstraction không có playable scene/concrete physical sequence khi topic hỗ trợ;
- weakest-60-seconds test không trả lời được bằng lý do cụ thể.

## Gate F — Final timing

Default PASS khi final word count nằm trong ±7% target.

Nếu voice/TTS profile có tốc độ đo thực tế, dùng estimated audio duration thay cho word count.

## Gate G — Cross-Project Anti-Template

Áp dụng cho project có `anti_template_version >= 1`.

PASS khi:

- `style_fingerprint` đã finalized;
- có `hook_strategy`, `hook_surface_form`, `opening_signature`;
- surface form không lặp với 2 project gần nhất;
- `imperative_imagination` kiểu “Hãy tưởng tượng… / Hãy thử… / Imagine…” không lặp trong recent window;
- opening signature không lặp exact với 2 project gần nhất;
- opening similarity với 5 project gần nhất dưới hard threshold của checker;
- final không drift từ surface đã chọn trong Architecture quay về một template quen thuộc;
- `narrator_scaffolding_gate = PASS`;
- `cross_project_similarity_gate.verdict = PASS`.

Checker thực thi:

```bash
python scripts/check_project.py projects/<slug> --write-style-state
python scripts/check_project.py projects/<slug>
```

Hard FAIL khi:

- opening similarity >= 0.68 với một recent project;
- hook surface lặp theo rule trên;
- opening signature lặp exact với một trong 2 project gần nhất;
- narrator scaffolding marker >= 7;
- style fingerprint chưa finalized hoặc thiếu field bắt buộc.

Soft WARN khi:

- opening similarity >= 0.54 nhưng < 0.68;
- narrator scaffolding marker từ 4 đến 6.

Legacy project không có `anti_template_version` chỉ WARN để tránh phá archive cũ.

## Anti-pattern checklist

Tự động flag nếu có:

- 3+ lần một transition phrase giống nhau;
- 3+ đoạn dùng cùng rhetorical skeleton;
- 2 đoạn liên tiếp mở bằng câu hỏi rhetorical;
- 4+ proper nouns mới trong một phút narration;
- nhiều ngày tháng không ảnh hưởng causal story;
- đoạn citation-heavy nghe như literature review;
- claim định lượng không có ledger support;
- “obviously”, “everyone knows”, “scientists proved” cho claim phức tạp;
- “the reason is simple” khi thực tế có nhiều nguyên nhân;
- conclusion thêm claim mới chưa được research;
- methodology/caveat xuất hiện trước first reward dù có thể dời xuống;
- beat chỉ tồn tại vì research có fact đó, không phải vì story cần nó;
- beat không deepens/widens/changes/raises bất kỳ thứ gì;
- generic cliffhanger không có consequence thật;
- >90 giây không có reveal/case/mechanism/consequence/reversal/scene;
- >2 phút abstraction không có visual/human-scale anchor;
- 3+ beats cùng scale mà không có intentional reason;
- detour không có scale/scene/reframe/stakes value;
- R4 chỉ là dramatic wording, không làm viewer sửa model;
- act transition không đổi question, scale, stakes hoặc interpretation;
- opening surface/signature lặp với recent project;
- narrator liên tục tự báo “đây là bước ngoặt / đây là nơi / câu hỏi tiếp theo là…” thay vì để evidence tạo turn.
