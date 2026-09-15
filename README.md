# GPT Web YouTube Script Pipeline

Pipeline viết YouTube documentary/explainer theo hướng **story-first + evidence-grounded + anti-template**: người xem luôn có lý do cụ thể để muốn biết chuyện gì xảy ra tiếp theo, nhưng các video trong cùng series không bị lặp cùng một “bộ khung AI” ở bề mặt.

Core flow:

**hook độc đáo → central contradiction → central question → early payoff → consequence → stronger question → act progression → scale expansion → concrete scene → deeper mechanism → reframe/reversal → synthesis → callback**

Repo được thiết kế để dùng trực tiếp với **Codex** hoặc **ChatGPT Web + GitHub**. Mỗi video là một workspace riêng trong `projects/<slug>/`.

---

## Mục tiêu

- Đầu vào tối thiểu: **chủ đề + ngôn ngữ + độ dài video**.
- Đầu ra: YouTube documentary/explainer script hoàn chỉnh, bám sát thời lượng yêu cầu.
- Viết để nói/voice-over, không viết như bài luận.
- Hook mạnh trong 30–45 giây đầu nhưng không lặp surface form của các video gần nhất.
- Có payoff thật trong 10–15% đầu.
- Có 4–5 acts hoặc progression tương đương.
- Có viewer-question chain: answer này tự sinh question tiếp theo.
- Có causal chain thay vì timeline/fact dump.
- Mỗi beat phải ít nhất một: `deepens mechanism`, `widens scale`, `changes interpretation`, `raises stakes`.
- Có Scale Escalation: object → individual → community → institution → civilization → global/system khi phù hợp.
- Có Reveal Ladder R1→R5, gồm reframe/reversal nếu evidence hỗ trợ.
- Có playable scene/physical sequence đủ dày cho editor dựng video.
- Research là factual boundary, không phải narration order.
- Không bịa nguồn, số liệu, quote, xác suất, historical action hay sensory detail.
- Dramatize structure/presentation, không dramatize evidence.
- Giảm dấu vết AI/template **trong một script và giữa nhiều project**.

---

# Pipeline

```text
00_input
   ↓
01_research_ledger
   ↓
02_story_architecture
   ├─ Hook Strategy Registry
   ├─ Hook Candidate Tournament
   └─ Cross-project style avoidance
   ↓
03_outline
   ↓
04_draft
   ↓
05_fact_audit
   ↓
06_retention_audit
   ↓
07_final_script
   ├─ Remove Narrator Scaffolding pass
   └─ Surface-form cleanup
   ↓
check_project.py
   ├─ structural/fact/timing gates
   └─ Gate G: Cross-Project Anti-Template
```

Bên trong Stage 2–3 có các controller chính:

```text
Central Contradiction
↓
Hook Strategy Selection
↓
Hook Candidate Tournament
↓
Act Architecture
↓
Viewer-Question Chain
↓
Causal Ladder
↓
Scale Escalation Map
↓
Story Expansion Test
↓
Reveal Ladder R1→R5
↓
Visual Scene Density Map
↓
Retention Outline
```

Final narration:

```text
projects/<slug>/07_final_script.md
```

Tài liệu quan trọng:

```text
AGENTS.md
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
docs/HOOK_STRATEGY_REGISTRY.md
prompts/00_orchestrator.md
```

---

# 1. Cách dùng với Codex

## 1.1 Clone repo

```bash
git clone https://github.com/cuongtobi/gpt_web_yt_script.git
cd gpt_web_yt_script
```

Repo hiện không yêu cầu package Python ngoài cho helper scripts.

```bash
python --version
```

---

## 1.2 Mở repo bằng Codex

Agent phải đọc:

```text
AGENTS.md
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
docs/HOOK_STRATEGY_REGISTRY.md
prompts/00_orchestrator.md
```

`AGENTS.md` là source of truth cho behavior, story doctrine, factual rules và Definition of Done.

---

## 1.3 Giao toàn bộ video cho Codex

```text
Hãy làm việc trong repo này và chạy toàn bộ YouTube script pipeline.

Input:
topic: How Did Humans Invent Money?
language: English
duration: 25 minutes

Yêu cầu:
- đọc AGENTS.md và prompts/00_orchestrator.md trước;
- tự tạo project mới trong projects/;
- research trước factual claim quan trọng;
- chạy đủ Research Ledger → Architecture → Outline → Draft → Fact Audit → Retention Audit → Final;
- Stage 2 phải dùng Hook Strategy Registry và tránh lặp opening của project gần nhất;
- Architecture phải có Act Architecture, Scale Escalation, Story Expansion, Reveal Ladder và Scene Density Map;
- mỗi beat phải tạo consequence/câu hỏi tiếp theo;
- Stage 7 phải chạy Remove Narrator Scaffolding pass;
- tự sửa nếu audit hoặc Gate G FAIL;
- final nằm trong projects/<slug>/07_final_script.md;
- cuối cùng chạy scripts/check_project.py với style state và chỉ coi hoàn tất khi PASS.
```

Bạn không cần ra lệnh từng stage. Orchestrator tự chạy toàn pipeline.

---

## 1.4 Tạo project bằng helper script

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

Kết quả:

```text
projects/how-did-humans-invent-money/
  00_input.md
  01_research_ledger.md
  02_story_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_final_script.md
  project_state.json
```

Sau đó:

```text
Tiếp tục project projects/how-did-humans-invent-money/.
Đọc AGENTS.md và toàn bộ artifacts hiện có.
Chạy từ stage chưa hoàn thành tiếp theo cho tới final.
Không reset research đã được xác nhận nếu không cần.
```

---

## 1.5 Tham số `new_project.py`

Tối thiểu:

```bash
python scripts/new_project.py \
  --topic "<topic>" \
  --language "<language>" \
  --duration <minutes>
```

Optional:

```text
--slug
--title
--angle
--audience
--wpm
```

Ví dụ:

```bash
python scripts/new_project.py \
  --topic "Why Do Humans Dream?" \
  --language English \
  --duration 18 \
  --title "Why Do Humans Dream?" \
  --angle "evolution, neuroscience, unresolved theories" \
  --audience "general curious audience"
```

Default:

```text
English:    158 words/minute
Vietnamese: 152 từ/phút
Other:      150 words/minute
```

---

## 1.6 Input nâng cao

Có thể thêm:

```text
title:
angle:
audience:
tone:
must_include:
must_avoid:
sources:
```

Ví dụ:

```text
topic: Why Did Humans Start Using Money?
language: English
duration: 22 minutes
audience: adults interested in history and economics
tone: cinematic documentary, curious, grounded
angle: money as a solution to trust, accounting and scale
must_include: Mesopotamian accounting, coins, paper money, banking
must_avoid: crypto speculation
```

---

## 1.7 Chạy kiểm tra cuối

Với project mới, chạy:

```bash
python scripts/check_project.py how-did-humans-invent-money --write-style-state
python scripts/check_project.py how-did-humans-invent-money
```

Lệnh đầu:

- chạy toàn bộ checker;
- tính style fingerprint từ final;
- so sánh opening với các project gần nhất;
- ghi kết quả Gate G vào `project_state.json`.

Lệnh thứ hai xác nhận state đã được lưu và project vẫn PASS.

Checker hiện kiểm tra:

- đủ file bắt buộc;
- final trong tolerance ±7%;
- Fact Audit = PASS;
- Retention Audit = PASS;
- story gates trong `project_state.json`;
- final không còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`;
- transition template lặp;
- percentage claims cần ledger support;
- style fingerprint;
- narrator scaffolding;
- cross-project opening similarity;
- surface-form repeat;
- opening-signature repeat.

Kết quả mong muốn:

```text
RESULT: PASS
```

---

## 1.8 Tiếp tục / rewrite project cũ

```text
Đọc project projects/how-did-humans-invent-money/.
Tôi muốn tăng retention ở 5 phút giữa nhưng không thay đổi thesis chính.
Đọc Research Ledger, Architecture, Outline, Draft và Retention Audit hiện tại.
Sửa từ stage phù hợp, cập nhật downstream artifacts và chạy check_project.py lại.
```

Nếu vấn đề nằm ở act/scale/reversal/scene density, quay về Stage 2 hoặc 3; không chỉ sửa câu ở final.

Nếu vấn đề là opening/template similarity, sửa từ Stage 2 Hook Strategy Selection rồi propagate xuống Stage 3/4/7.

---

# 2. Cách dùng với ChatGPT Web

## 2.1 Prompt ngắn nhất

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Viết một YouTube documentary script mới.

topic: How Did Humans Invent Money?
language: English
duration: 25 minutes

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline và lưu mọi artifact vào một project mới trong projects/.
```

---

## 2.2 Prompt khuyến nghị

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Tạo project YouTube script mới với input:

topic: <TOPIC>
language: <LANGUAGE>
duration: <MINUTES> minutes

Optional:
title: <TITLE>
angle: <ANGLE>
audience: <AUDIENCE>
tone: <TONE>
must_include: <ITEMS>
must_avoid: <ITEMS>

Yêu cầu:
1. Đọc AGENTS.md, pipeline/PIPELINE.md, pipeline/QUALITY_GATES.md, docs/STYLE_DNA.md, docs/HOOK_STRATEGY_REGISTRY.md và prompts/00_orchestrator.md.
2. Khởi tạo projects/<slug>/ từ template.
3. Chạy đủ Research Ledger → Story Architecture → Outline → Draft → Fact Audit → Retention/Story Momentum Audit → Final.
4. Stage 2 đọc fingerprint/opening của project gần nhất, tạo ít nhất 4 hook candidate khác cấu trúc và chọn hook không lặp surface/signature.
5. Architecture phải có 4–5 acts, Scale Escalation Map, Story Expansion Test, Reveal Ladder R1→R5 và Visual Scene Density Map.
6. Research/verify factual claim quan trọng trước khi dùng.
7. Không bịa source, statistic, quote, probability, historical action hoặc sensory detail.
8. Dramatize structure, never facts.
9. Nếu Fact Audit FAIL, sửa claim/source trước.
10. Nếu Retention Audit FAIL vì structure, quay lại Architecture/Outline.
11. Stage 7 chạy Remove Narrator Scaffolding pass.
12. Final phải đạt duration target, story gates và Gate G Anti-Template.
13. Cập nhật project_state.json, gồm style_fingerprint.
14. Khi hoàn thành, báo word count, duration, Fact Audit, Retention score, First 3 Minutes, Act Progression, Scale Escalation, Scene Density, Reveal Ladder và Cross-Project Anti-Template verdict.
```

---

## 2.3 Output project

```text
projects/<slug>/
  00_input.md
  01_research_ledger.md
  02_story_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_final_script.md
  project_state.json
```

Voice-over lấy từ:

```text
07_final_script.md
```

---

## 2.4 Tiếp tục project trong chat khác

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Tiếp tục project:
projects/how-did-humans-invent-money/

Đọc toàn bộ artifacts và project_state.json trước.
Xác định stage hiện tại rồi tiếp tục từ đó.
Không tạo project mới.
```

---

# 3. Story DNA

Pipeline không clone câu chữ video mẫu. Nó học **logic engine**, nhưng không để logic engine lộ ra thành cùng một surface template ở mọi video.

```text
Distinct opening surface
        ↓
Transformation / central contradiction
        ↓
Central question
        ↓
Early payoff
        ↓
Consequence → stronger question
        ↓
Act progression
        ↓
Scale expansion / zoom in-out
        ↓
Concrete scene / physical evidence
        ↓
Deeper mechanism
        ↓
Reframe / reversal
        ↓
Larger consequence
        ↓
Central answer
        ↓
Larger implication
        ↓
Callback to opening
```

Nguyên tắc lõi:

> **Question → Evidence → Reveal → Meaning → Consequence → New Question**

Nếu đoạn chỉ đưa fact mà không làm viewer hiểu sâu hơn, story lớn hơn, interpretation thay đổi hoặc stakes tăng, đoạn đó chưa hoàn thành nhiệm vụ.

---

# 4. Các controller quan trọng

## 4.1 Hook Strategy Registry

File:

```text
docs/HOOK_STRATEGY_REGISTRY.md
```

Stage 2 không được mặc định mở bằng cùng một công thức như:

```text
“Hãy tưởng tượng...”
“Hãy thử...”
“Imagine...”
“Picture this...”
```

Pipeline phân biệt:

- **hook strategy** — logic kể chuyện ở cấp architecture;
- **hook surface form** — hình thức câu mở đầu thực tế;
- **opening signature** — fingerprint ngắn của opening pattern.

Một strategy có thể được dùng lại khi topic phù hợp, nhưng **surface/signature gần nhau không được lặp liên tiếp**.

Stage 2 phải:

1. đọc tối đa 5 project gần nhất nếu có;
2. xem `style_fingerprint` và opening của chúng;
3. tạo ít nhất 4 hook candidate khác cấu trúc;
4. chọn candidate mạnh về curiosity + visuality + factual integrity + uniqueness;
5. lưu Strategy ID, Surface form và Opening signature vào Architecture/state.

---

## 4.2 Act Architecture

Default 4–5 acts:

```text
Act 1 — The mystery / before-state
Act 2 — How it began
Act 3 — How humans/systems pushed it further
Act 4 — Unexpected consequence / reversal
Act 5 — What it became / what it means
```

Tên/số acts được thay đổi theo topic. Mỗi act phải có entry question, payoff, escalation và consequence mở act kế.

---

## 4.3 Scale Escalation

```text
object
→ individual
→ community
→ institution
→ civilization
→ global/system
```

Không đi tuyến tính bắt buộc. Documentary tốt thường zoom in rồi zoom out.

Mỗi 2–3 beats phải có intentional scale movement hoặc lý do giữ scale.

---

## 4.4 Story Expansion

Mỗi beat phải ít nhất một:

```text
deepens mechanism
widens scale
changes interpretation
raises stakes
```

Không có → cut/compress/fold.

---

## 4.5 Reveal Ladder

```text
R1 — orientation payoff
R2 — mechanism payoff
R3 — reframe
R4 — major reveal/reversal
R5 — synthesis
```

R4 phải làm viewer sửa model, không chỉ là câu dramatic.

---

## 4.6 Visual Scene Density

Phân biệt:

- visual anchor = chart/map/object;
- playable scene = sequence có place/object/person/action/mechanism.

Với topic giàu visual evidence, target mềm khoảng 60–90 giây có một playable scene/physical sequence.

---

## 4.7 Detours

Historical/explanatory detour chỉ giữ nếu tăng ít nhất một:

```text
scale
scene value
causal proof
pattern interrupt
reframe/reversal
stakes/consequence
```

---

## 4.8 Dramatization

> **Dramatize structure, never facts.**

Được reorder/reveal/contrast/zoom/compress attribution.
Không được bịa dialogue, emotion, motive, sensory detail, exact ancient action hoặc certainty.

---

# 5. Research và factual integrity

Research Ledger phân loại:

```text
ESTABLISHED
SUPPORTED
DEBATED
INTERPRETATION
SPECULATIVE
UNVERIFIED
```

Ngoài factual metadata, mỗi claim có:

```text
Story role
Story value
Visual potential
Playable scene / concrete anchor
Human-scale example
Scale potential
Escalation value
```

Không tự tạo confidence score hoặc phần trăm từ lập luận định tính.

Không bịa:

- paper;
- tác giả;
- journal;
- institution;
- năm;
- DOI/URL;
- quote;
- statistic;
- probability;
- historical action;
- sensory detail.

---

# 6. Anti-AI / Anti-Template System

Pipeline xử lý template leakage ở bốn lớp chính.

## 6.1 Hook Strategy Registry

Không để nhiều video cùng mở bằng một pattern như:

```text
Hãy tưởng tượng...
Hãy thử...
Bạn có bao giờ...
Có một điều kỳ lạ...
Imagine...
Picture this...
```

Cấm “đổi từ nhưng giữ cùng skeleton” để lách gate.

---

## 6.2 Cross-Project Similarity Gate

Validator:

```text
scripts/anti_template.py
```

Được gọi từ:

```text
scripts/check_project.py
```

Mặc định so opening với **5 project gần nhất**.

Ngưỡng hiện tại:

```text
opening similarity >= 0.68  → FAIL
0.54 <= similarity < 0.68  → WARN
```

Ngoài similarity score, Gate G còn kiểm tra:

- lặp `hook_surface_form` gần đây;
- lặp `opening_signature` trong 2 project gần nhất;
- final drift trở lại `imperative_imagination` dù Architecture đã chọn surface khác;
- narrator scaffolding quá dày.

Các threshold này là heuristic bảo vệ series, không phải tuyên bố rằng một script có similarity thấp là “không AI”.

---

## 6.3 Remove Narrator Scaffolding Pass

Stage 7 có pass riêng để xóa hoặc rewrite những câu đang **thuyết minh cấu trúc của chính script**, ví dụ:

```text
Đây là bước ngoặt...
Đây là nơi...
Và đây là điều thú vị...
Bây giờ câu chuyện...
Nhưng câu hỏi tiếp theo là...
Câu trả lời đầu tiên...
This is the turning point...
This is where...
The next question is...
```

Rule quan trọng:

> Không đổi một scaffolding phrase thành một scaffolding phrase khác chỉ để qua checker.

Nếu evidence/consequence đã tự tạo act turn, narrator nên để nội dung tự làm việc.

Scaffolding thresholds hiện tại:

```text
0–3 markers → PASS
4–6 markers → WARN
>= 7 markers → FAIL
```

---

## 6.4 Style Fingerprint trong `project_state.json`

Project mới có:

```json
{
  "anti_template_version": 1,
  "style_fingerprint": {
    "hook_strategy": "",
    "hook_surface_form": "",
    "opening_signature": "",
    "opening_first_words": "",
    "narrator_scaffolding_hits": 0,
    "rhetorical_question_count": 0,
    "finalized": false
  },
  "narrator_scaffolding_gate": "PENDING",
  "cross_project_similarity_gate": {
    "verdict": "PENDING",
    "compared_projects": [],
    "closest_project": "",
    "max_opening_similarity": 0,
    "surface_form_repeat": false,
    "opening_signature_repeat": false
  }
}
```

Sau final, chạy:

```bash
python scripts/check_project.py <slug> --write-style-state
```

để ghi fingerprint thực tế và kết quả Gate G.

Project cũ không có `anti_template_version: 1` được coi là **legacy**: anti-template violations chỉ WARN để không phá lịch sử repo. Project mới dùng template hiện tại phải PASS Gate G.

---

# 7. Quality Gates

Chi tiết đầy đủ nằm trong:

```text
pipeline/QUALITY_GATES.md
```

Các gate chính:

```text
Gate A — Research readiness
Gate B — Architecture
Gate C — Draft integrity
Gate D — Fact Audit
Gate E — Retention / Story Momentum
Gate F — Final timing
Gate G — Cross-Project Anti-Template
```

Gate G không thay Fact/Retention gate. Một script có opening độc đáo nhưng research yếu vẫn FAIL; một script factual tốt nhưng copy surface template của hai video trước cũng chưa hoàn thành.

---

# 8. Word budget

```text
English documentary:    158 WPM
Vietnamese documentary: 152 từ/phút
Other languages:        150 WPM starting point
```

```text
target_words = duration_minutes × target_wpm
```

Final mặc định ±7%.

---

# 9. Cấu trúc repo

```text
AGENTS.md
README.md

pipeline/
  PIPELINE.md
  QUALITY_GATES.md

docs/
  STYLE_DNA.md
  HOOK_STRATEGY_REGISTRY.md

prompts/
  00_orchestrator.md
  01_research.md
  02_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_rewrite_final.md

scripts/
  new_project.py
  check_project.py
  anti_template.py

templates/project/
  00_input.md
  01_research_ledger.md
  02_story_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_final_script.md
  project_state.json

projects/
  <mỗi video là một thư mục riêng>
```

---

# 10. Workflow khuyến nghị

```text
1. topic + language + duration
2. Research Ledger + story metadata
3. đọc fingerprint/opening của recent projects
4. Hook Strategy Registry + 4+ hook candidates
5. Central contradiction + selected hook
6. Act Architecture
7. Viewer-question chain + causal ladder
8. Scale Escalation + Story Expansion
9. Reveal Ladder + Scene Density Map
10. Retention Outline
11. Draft
12. Fact Audit
13. Retention / Story Momentum Audit
14. Final Rewrite
15. Remove Narrator Scaffolding pass
16. check_project.py --write-style-state
17. check_project.py
18. lấy 07_final_script.md khi tất cả gate PASS
```

---

# 11. Definition of Done

Project chỉ hoàn thành khi:

- word/duration đạt;
- central question được trả lời;
- First 3 Minutes = PASS;
- Act Progression = PASS;
- Viewer-question chain không gãy nghiêm trọng;
- mỗi beat có Story Expansion function;
- Scale Escalation = PASS;
- Scene Density = PASS khi topic hỗ trợ;
- Reveal Ladder = PASS;
- có R3 và R4 nếu evidence/topic hỗ trợ;
- không section chỉ fact dump;
- factual claim quan trọng có ledger support;
- không unsupported precise number;
- theory/interpretation đúng certainty;
- không unsupported cinematic detail;
- không decorative detour/padding;
- narration tự nhiên;
- narrator scaffolding dưới hard threshold;
- `style_fingerprint.finalized = true` đối với project anti-template v1;
- Cross-Project Similarity Gate = PASS;
- không lặp recent hook surface/signature bị cấm;
- Fact Audit = `PASS`;
- Retention / Story Momentum Audit >= `33/40` và `PASS`;
- Timing Gate = `PASS`;
- `scripts/check_project.py` trả `RESULT: PASS`.

Artifact sản xuất:

```text
projects/<slug>/07_final_script.md
```
