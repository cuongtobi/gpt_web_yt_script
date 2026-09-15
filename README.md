# GPT Web YouTube Script Pipeline

Pipeline đơn giản để viết YouTube documentary/explainer theo kiểu **concrete + causal + evidence-grounded**.

Mục tiêu là tạo script có cảm giác một writer đang kể một chuỗi biến đổi có thật, không phải một model đang cố PASS hàng chục framework.

## Input

Tối thiểu:

```text
topic: <chủ đề>
language: <ngôn ngữ>
duration: <phút>
```

Optional: title, angle, audience, tone, must_include, must_avoid, sources.

## Output

```text
projects/<slug>/05_final_script.md
```

Default word budget:

```text
English:    158 words/minute
Vietnamese: 152 từ/phút
Other:      150 words/minute
```

Final tolerance mặc định: ±7% target words.

---

# Pipeline

```text
00_input.md
   ↓
01_research.md
   ↓
02_story_spine.md
   ↓
03_draft.md
   ↓
04_fact_audit.md
   ↓
05_final_script.md
```

Chỉ 5 stage thực sự:

## Stage 1 — Research

Tạo research pack vừa đủ để kể chuyện:

- 1–2 central question candidates;
- timeline / causal background;
- khoảng 10–20 core claims;
- 5–8 strong cases / objects / studies;
- useful numbers / quotes;
- important uncertainties.

Research quyết định **cái gì được phép nói**, không quyết định thứ tự narration.

## Stage 2 — Story Spine

Chỉ thiết kế:

- central question;
- opening cụ thể;
- 6–10 beats;
- direct ending + callback.

Mỗi beat trả lời:

```text
What happened / what do we learn?
Why does it matter?
What does it naturally lead to next?
Evidence / cases used:
```

Không ép Act score, R1→R5, Scale Escalation, Curiosity Debt hay scene quota.

## Stage 3 — Full Draft

Ba ưu tiên:

```text
spoken
concrete
causal
```

Chronology hoàn toàn hợp lệ nếu chronology chính là story.

Không lặp ý để kéo duration. Không đọc research notes thành literature review.

## Stage 4 — Fact Audit

Audit các claim có rủi ro cao:

- number / percentage / date;
- quote;
- named study/person/institution;
- first/oldest/only/largest;
- causal / consensus / current claims;
- cinematic/sensory detail kể như fact.

Actions:

```text
KEEP
QUALIFY
REWRITE
REMOVE
VERIFY
```

Còn `VERIFY` = chưa PASS.

## Stage 5 — Final Edit

- áp dụng Fact Audit;
- cắt repetition/padding;
- làm prose dễ nói;
- rút attribution/methodology dài;
- giữ concrete cases mạnh;
- sửa transition máy móc khi cần;
- đưa final về ±7%;
- trả central question rõ ở cuối.

Anti-template chỉ là **soft editorial check**. Không có cross-project similarity hard gate.

---

# Story DNA

North-star flow:

```text
concrete opening
→ big contrast / central question
→ before-state or origin
→ first change
→ consequence
→ next change
→ stronger case/evidence
→ larger transformation
→ modern form
→ direct answer
→ callback
```

Đây là guide, không phải template cứng.

Một section tốt thường làm viewer hiểu **vì sao bước tiếp theo xảy ra**.

## Opening

Không có opening phrase mặc định.

Không tự động dùng:

```text
Hãy tưởng tượng...
Bạn có bao giờ...
Imagine...
Picture this...
```

Nhưng nếu một cách mở như vậy thực sự là cách tốt nhất, vẫn được dùng. Naturalness quan trọng hơn artificial uniqueness.

## Evidence

Đưa evidence vào story đúng chỗ nó chứng minh claim.

Không authority-stack tên tác giả + trường + journal + năm liên tục nếu narration không cần.

## Ending

Ending cần:

- direct answer;
- synthesis của transformation;
- callback nếu tự nhiên.

Không mở research branch mới ở conclusion.

Chi tiết style: `docs/STYLE_DNA.md`.

---

# Factual rules

Không bịa:

- paper / author / journal / institution;
- date / statistic / probability;
- quote;
- DOI / URL;
- exact historical action;
- emotion / motive;
- sensory detail kể như fact;
- stronger causal certainty.

Không chuyển `likely`, `probably`, `evidence suggests` thành `%` tự chế.

High-risk claim ở Fact Audit nên quay lại original/primary source khi có thể.

---

# Cách dùng với Codex

Clone repo:

```bash
git clone https://github.com/cuongtobi/gpt_web_yt_script.git
cd gpt_web_yt_script
```

Tạo project:

```bash
python scripts/new_project.py \
  --topic "How Did Humans Invent Money?" \
  --language English \
  --duration 25
```

Windows PowerShell:

```powershell
python scripts/new_project.py --topic "How Did Humans Invent Money?" --language English --duration 25
```

Sau đó giao cho Codex:

```text
Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline cho project vừa tạo.
Research kỹ factual claims quan trọng.
Chỉ coi hoàn tất khi Fact Audit PASS và scripts/check_project.py PASS.
```

---

# Cách dùng với ChatGPT Web + GitHub

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Viết một YouTube documentary script mới.

topic: <TOPIC>
language: <LANGUAGE>
duration: <MINUTES> minutes

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline và lưu mọi artifact vào một project mới trong projects/.
```

Pipeline sẽ tạo:

```text
projects/<slug>/
  00_input.md
  01_research.md
  02_story_spine.md
  03_draft.md
  04_fact_audit.md
  05_final_script.md
  project_state.json
```

---

# Final validation

Chạy:

```bash
python scripts/check_project.py projects/<slug>
```

Hard FAIL chỉ khi:

- thiếu artifact;
- Fact Audit chưa PASS;
- final lệch quá ±7%;
- final còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Checker chỉ WARN, không FAIL, với:

- template-like transition lặp nhiều;
- opening kiểu `Hãy tưởng tượng...` / `Imagine...`;
- percentage claim cần double-check support.

Project legacy vẫn được checker nhận diện và kiểm tra theo schema cũ.

---

# Repo structure

```text
AGENTS.md
README.md

pipeline/
  PIPELINE.md
  QUALITY_GATES.md

docs/
  STYLE_DNA.md

prompts/
  00_orchestrator.md
  01_research.md
  02_story_spine.md
  03_draft.md
  04_fact_audit.md
  05_final_edit.md

scripts/
  new_project.py
  check_project.py

templates/project/
  00_input.md
  01_research.md
  02_story_spine.md
  03_draft.md
  04_fact_audit.md
  05_final_script.md
  project_state.json

projects/
  <mỗi video là một thư mục riêng>
```

---

# Definition of Done

Project mới hoàn tất khi:

- research đủ support cho thesis;
- Story Spine có central question và chuỗi 6–10 beat dễ theo;
- narration spoken/concrete/causal;
- Fact Audit = `PASS`;
- final nằm trong ±7% target;
- final không còn editor/verification notes;
- central question được trả lời rõ;
- `python scripts/check_project.py <project>` trả `RESULT: PASS`.

Không yêu cầu architecture score, retention score, scale score, reveal score hoặc cross-project anti-template score.
