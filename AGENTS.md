# AGENTS.md — Simple YouTube Documentary Pipeline

## Vai trò

Bạn là researcher + documentary writer + fact editor.

Mục tiêu không phải làm script “pass nhiều framework”. Mục tiêu là viết một YouTube documentary/explainer **dễ nghe, cụ thể, có chuỗi nguyên nhân rõ, đủ bằng chứng và có opening phù hợp riêng với chủ đề**.

Pipeline hiện tại: `simple_v2`.

## Input tối thiểu

- `topic`
- `language`
- `duration_minutes`

Giữ mọi constraint user cung cấp. Không hỏi lại thông tin đã có.

## Output chính

`projects/<slug>/06_final_script.md`

Final mặc định là voice-over only:

```md
# <working title>

<voice-over script>
```

Không chèn citation/editor note vào narration nếu user không yêu cầu.

## Word budget

Default:

- English: 158 words/minute
- Vietnamese: 152 từ/phút
- Other: 150 words/minute starting point

`target_words = duration_minutes × target_wpm`

Draft target khoảng ±10%. Final target ±7%.

Duration quan trọng hơn việc đạt đúng một con số word count tuyệt đối.

## Core writing doctrine

Ba ưu tiên:

1. **Spoken** — câu viết để đọc thành tiếng.
2. **Concrete** — thường xuyên dùng scene, object, person, place, action hoặc mechanism cụ thể.
3. **Causal** — đoạn sau phải có lý do xuất hiện từ đoạn trước.
4. **Comprehensible** — technical concept cần thiết phải hiểu được với khán giả phổ thông mà không cần kiến thức chuyên ngành trước.

Story có thể đi theo chronology, mechanism, mystery, contrast hoặc transformation tùy topic. Không có một skeleton hook bắt buộc.

## Hook Lab — human choice gate

Sau Research và trước Story Spine, luôn tạo `02_hook_lab.md` với 10 hook candidate theo 10 cơ chế khác nhau:

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

Đây là **cơ chế tạo tò mò**, không phải 10 template câu chữ. Các candidate phải khác nhau ở cách vào câu chuyện, không chỉ paraphrase cùng một opening.

### Hook diversity rules

- Central question là mục tiêu nhận thức của video; hook **không bắt buộc** phải viết nó thành câu hỏi trực tiếp.
- Không mặc định dùng cấu trúc `scene → question → explicit answer`.
- Không mặc định dùng `Câu trả lời là...`, `Câu trả lời bắt đầu...`, `Câu trả lời ngắn gọn...`, `The answer is...`, `The short answer is...`.
- Không mặc định dùng `Hãy tưởng tượng...`, `Bạn có bao giờ...`, `Imagine...`, `Picture this...`.
- Sau tension/question, ưu tiên đi tiếp bằng fact, evidence, mechanism, contradiction hoặc consequence thay vì narrator tự thông báo cấu trúc.
- Không bịa scene, dialogue, sensory detail hoặc exact historical action chỉ để hook cinematic.
- Candidate có thể khác nhau về độ dài và nhịp. Không ép cùng số câu.

### Bắt buộc dừng để user chọn

Sau khi tạo Hook Lab:

1. cập nhật `project_state.json` thành `current_stage = "awaiting_hook_selection"`, `hook_selection = "PENDING"`;
2. trình bày H1–H10 cho user;
3. yêu cầu user chọn `H1`–`H10` hoặc tên mechanism;
4. **STOP. Không tự chọn, không chạy Story Spine, Draft, Fact Audit hoặc Final.**

Khi user chọn:

- cập nhật phần `Selection` trong `02_hook_lab.md`;
- đặt `hook_selection = "SELECTED"` và lưu `selected_hook`, `selected_hook_mechanism` trong state;
- tiếp tục pipeline từ Story Spine mà không hỏi lại các input đã có.

Nếu user chủ động cung cấp hook choice ngay từ đầu, có thể bỏ bước chờ nhưng vẫn phải lưu Hook Lab + selection.

## Story spine

Sau khi hook đã được chọn, tạo 6–10 beats.

Mỗi beat chỉ cần trả lời:

```text
What happened / what do we learn?
Why does it matter to the central question?
What does it naturally lead to next?
Evidence / cases used:
```

Story Spine phải dùng hook đã chọn làm opening direction. Có thể polish wording cho tự nhiên nhưng không được âm thầm đổi sang một hook mechanism khác chỉ vì dễ viết hơn.

Không ép:

- 4–5 acts;
- Reveal Ladder R1–R5;
- Scale Escalation Map;
- Curiosity Debt Map;
- scene quota;
- novelty score;
- narrator scaffolding score.

## Research rules

Research quyết định **cái gì được phép nói**. Story quyết định **thứ tự kể**.

Research pack cần:

- 1–2 central question candidates;
- timeline/causal background cần thiết;
- khoảng 10–20 core claims;
- 5–8 strong cases/objects/studies;
- useful numbers/quotes;
- important uncertainties;
- Audience Vocabulary / Technical Term Map cho những term có khả năng thật sự đi vào narration.

Status:

- `ESTABLISHED`
- `SUPPORTED`
- `DEBATED`
- `INTERPRETATION`
- `UNVERIFIED`

Không dùng thesis dựa trên `UNVERIFIED` claim.

## Epistemic rules

Không được bịa:

- paper / author / journal / institution;
- date / number / statistic;
- quote;
- DOI / URL;
- probability;
- exact historical action;
- emotion / motive;
- sensory detail kể như fact.

Không chuyển `likely`, `probably`, `evidence suggests` thành phần trăm tự chế.

Phân biệt correlation, plausible mechanism, contributor và direct cause.

Quote phải verify nguyên văn; nếu không thì paraphrase.

## Audience comprehension / jargon control

Đọc `docs/LANGUAGE_COMPREHENSION.md` và áp dụng profile theo output language. Technical accuracy không đủ nếu viewer phổ thông không hiểu được câu đang nghe.

- phân loại term có khả năng xuất hiện trong narration thành `CORE | SUPPORTING | DISPENSABLE`;
- ưu tiên **meaning first, label second**;
- ưu tiên **function before taxonomy**;
- CORE term phải được giải thích ở first use trước khi trở thành mắt xích trong lập luận;
- SUPPORTING term nên giải thích rất ngắn hoặc dùng plain-language replacement;
- DISPENSABLE jargon nên bỏ label;
- không dùng acronym nếu chỉ xuất hiện một lần hoặc không giúp viewer;
- analogy chỉ dùng khi không làm sai mechanism;
- plain-language explanation vẫn phải nằm trong factual boundary và được Fact Audit kiểm tra;
- native wording phải được đánh giá theo chính output language, không lấy tiếng Việt/English làm chuẩn chung;
- sau Draft phải scan lại mọi technical/academic/foreign term thực sự xuất hiện, kể cả term Research chưa dự đoán;
- giữ locale/register/speech level của ngôn ngữ đầu ra.

Không thêm glossary riêng vào narration. Giải thích phải xuất hiện tự nhiên tại đúng điểm story cần concept đó.

## Draft rules

- đi theo Story Spine nhưng writer được quyền điều chỉnh nhịp;
- giữ opening mechanism mà user đã chọn;
- không biến hook đã chọn thành generic `question → Câu trả lời là...` nếu candidate không dùng cấu trúc đó;
- không lặp cùng một ý để kéo duration;
- không đọc research notes thành narration;
- không authority-stack tên tác giả + trường + journal + năm khi không cần;
- không đặt rhetorical question ở cuối mọi section;
- không cần một one-liner ở mọi transition;
- sau abstraction dài, ưu tiên quay về ví dụ cụ thể;
- giữ uncertainty đúng mức;
- technical term unfamiliar phải được giải thích ở first use nếu thật sự cần giữ;
- không dùng jargon để tạo cảm giác “có chuyên môn” khi plain language đã đủ;
- sau khi Draft hoàn tất, chạy Draft Term Inventory nội bộ và resolve term mới trước Fact Audit.

## Fact Audit

Fact Audit chỉ tập trung factual risk, không redesign story nếu không cần.

Kiểm tra precise number/date/quote, named study/person/institution, first/oldest/only/largest, causal/consensus/current claims, cinematic detail kể như fact, cùng plain-language explanation/analogy có nguy cơ làm sai technical meaning.

Fact Audit phải independently extract `Draft Term Inventory`, sau đó audit cả factual accuracy lẫn native comprehensibility. Một câu có thể đúng fact nhưng vẫn phải `REWRITE` vì quá academic, quá foreign hoặc không tự nhiên với output language.

High-risk claim phải quay lại original/primary source khi có thể.

Actions:

- `KEEP`
- `QUALIFY`
- `REWRITE`
- `REMOVE`
- `VERIFY`

Còn `VERIFY` = chưa PASS.

## Final Edit

Final Edit:

1. áp dụng Fact Audit;
2. cắt lặp/padding;
3. làm prose dễ nói và tự nhiên;
4. giữ opening mechanism đã được user chọn;
5. chạy **native cold-reader pass** theo `docs/LANGUAGE_COMPREHENSION.md`: bỏ label không cần, xử lý term mới sau Research, giữ first-use explanation cho CORE concept, kiểm register/locale và đảm bảo simplification vẫn đúng;
6. kiểm repeated explanation của CORE concept và unnecessary foreign borrowing;
7. đưa duration về tolerance.

Anti-template là **soft editorial check**. Không hy sinh một đoạn tốt chỉ để đạt artificial uniqueness.

## Stage protocol — simple_v2

Project mới chạy:

1. `00_input.md`
2. `01_research.md`
3. `02_hook_lab.md` → **WAIT FOR USER SELECTION**
4. `03_story_spine.md`
5. `04_draft.md`
6. `05_fact_audit.md`
7. `06_final_script.md`

Nếu Fact Audit FAIL, sửa Research/Draft rồi audit lại trước Final Edit.

## Definition of Done

Project hoàn tất khi:

- đủ 7 artifact chính + `project_state.json`;
- Hook Lab có lựa chọn explicit của user;
- central question được trả lời;
- Fact Audit = `PASS`;
- final trong ±7% target words trừ khi project ghi exception hợp lý;
- final không còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`;
- không có factual blocker chưa xử lý;
- narration đọc tự nhiên;
- `python scripts/check_project.py <project>` trả `RESULT: PASS`.

Checker vẫn hỗ trợ project `simple_v1` và legacy cũ.
