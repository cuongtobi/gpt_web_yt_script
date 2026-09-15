# GPT Web YouTube Script Pipeline

Pipeline viết YouTube documentary/explainer theo hướng **story-first**: người xem luôn có lý do cụ thể để muốn biết chuyện gì xảy ra tiếp theo.

Core flow:

**cinematic hook → transformation/central contradiction → central question → early payoff → consequence → stronger question → act progression → scale expansion → concrete scene → deeper mechanism → reframe/reversal → synthesis → thematic callback**

Repo được thiết kế để dùng trực tiếp với **Codex** hoặc **ChatGPT Web + GitHub**. Mỗi video là một workspace riêng trong `projects/<slug>/`.

---

## Mục tiêu

- Đầu vào tối thiểu: **chủ đề + ngôn ngữ + độ dài video**.
- Đầu ra: YouTube video script hoàn chỉnh, bám sát thời lượng yêu cầu.
- Viết để nói/voice-over, không viết như bài luận.
- Hook mạnh trong 30–45 giây đầu.
- Có payoff thật trong 10–15% đầu.
- Có 4–5 acts hoặc progression tương đương.
- Có viewer-question chain: answer này tự sinh question tiếp theo.
- Có causal chain thay vì timeline/fact dump.
- Mỗi beat phải deepens mechanism, widens scale, changes interpretation hoặc raises stakes.
- Có Scale Escalation: object/individual/community/institution/civilization/global-system khi phù hợp.
- Có Reveal Ladder R1→R5, gồm reframe/reversal nếu evidence hỗ trợ.
- Có playable scene/physical sequence đủ dày cho editor dựng video.
- Research là factual boundary, không phải narration order.
- Không bịa nguồn, số liệu, quote, xác suất, historical action hay sensory detail.
- Dramatize structure/presentation, không dramatize evidence.
- Giảm dấu vết template/AI.

---

## Pipeline

```text
00_input
   ↓
01_research_ledger
   ↓
02_story_architecture
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
```

Bên trong Stage 2–3 có các controller chính:

```text
Central Contradiction
↓
Hook Archetype
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

Final:

```text
projects/<slug>/07_final_script.md
```

Chi tiết:

```text
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
```

---

# 1. Cách dùng với Codex

## 1.1 Clone repo

```bash
git clone https://github.com/cuongtobi/gpt_web_yt_script.git
cd gpt_web_yt_script
```

Repo không yêu cầu package Python ngoài cho helper scripts hiện tại.

```bash
python --version
```

---

## 1.2 Mở repo bằng Codex

Mở Codex tại root repo.

Agent phải đọc:

```text
AGENTS.md
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
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
- Architecture phải có Act Architecture, Scale Escalation, Story Expansion, Reveal Ladder và Scene Density Map;
- mỗi beat phải tạo consequence/câu hỏi tiếp theo;
- tự sửa nếu audit FAIL;
- final nằm trong projects/<slug>/07_final_script.md;
- cuối cùng chạy scripts/check_project.py và chỉ coi hoàn tất khi PASS.
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

```bash
python scripts/check_project.py how-did-humans-invent-money
```

Checker hiện kiểm tra các lỗi cơ bản như:

- đủ file bắt buộc;
- final trong tolerance ±7%;
- Fact Audit = PASS;
- Retention Audit = PASS;
- final không còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`;
- cảnh báo transition template lặp;
- cảnh báo `%` để bắt kiểm tra ledger support.

Các story gate sâu hơn nằm trong `pipeline/QUALITY_GATES.md` và `06_retention_audit.md`:

- First 3 Minutes;
- Act Progression;
- Scale Escalation;
- Scene Density;
- Reveal Ladder;
- Story Expansion;
- Weakest-60-Seconds.

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
1. Đọc AGENTS.md, pipeline/PIPELINE.md, pipeline/QUALITY_GATES.md, docs/STYLE_DNA.md và prompts/00_orchestrator.md.
2. Khởi tạo projects/<slug>/ từ template.
3. Chạy đủ Research Ledger → Story Architecture → Outline → Draft → Fact Audit → Retention/Story Momentum Audit → Final.
4. Architecture phải có 4–5 acts, Scale Escalation Map, Story Expansion Test, Reveal Ladder R1→R5 và Visual Scene Density Map.
5. Research/verify factual claim quan trọng trước khi dùng.
6. Không bịa source, statistic, quote, probability, historical action hoặc sensory detail.
7. Dramatize structure, never facts.
8. Nếu Fact Audit FAIL, sửa claim/source trước.
9. Nếu Retention Audit FAIL vì structure, quay lại Architecture/Outline.
10. Final phải đạt duration target và tất cả story gates.
11. Cập nhật project_state.json.
12. Khi hoàn thành, báo word count, duration, Fact Audit, Retention score, First 3 Minutes, Act Progression, Scale Escalation, Scene Density và Reveal Ladder verdict.
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

## 2.5 Chỉ sửa một stage

```text
@GitHub đọc project projects/<slug>/.
Chỉ phân tích retention/story momentum và cập nhật 06_retention_audit.md.
Không thay đổi script.
```

Hoặc:

```text
@GitHub đọc project projects/<slug>/.
Audit lại Act Architecture + Scale Escalation + Reveal Ladder.
Chỉ cập nhật 02_story_architecture.md và 03_outline.md.
```

---

# 3. Story DNA

Pipeline không clone câu chữ video mẫu. Nó học **logic engine**.

```text
Concrete/cinematic opening
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

## 4.1 Act Architecture

Default 4–5 acts:

```text
Act 1 — The mystery / before-state
Act 2 — How it began
Act 3 — How humans/systems pushed it further
Act 4 — Unexpected consequence / reversal
Act 5 — What it became / what it means
```

Tên/số acts được thay đổi theo topic. Mỗi act phải có entry question, payoff, escalation và consequence mở act kế.

## 4.2 Scale Escalation

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

## 4.3 Story Expansion

Mỗi beat phải ít nhất một:

```text
deepens mechanism
widens scale
changes interpretation
raises stakes
```

Không có → cut/compress/fold.

## 4.4 Reveal Ladder

```text
R1 — orientation payoff
R2 — mechanism payoff
R3 — reframe
R4 — major reveal/reversal
R5 — synthesis
```

R4 phải làm viewer sửa model, không chỉ là câu dramatic.

## 4.5 Visual Scene Density

Phân biệt:

- visual anchor = chart/map/object;
- playable scene = sequence có place/object/person/action/mechanism.

Với topic giàu visual evidence, target mềm khoảng 60–90 giây có một playable scene/physical sequence.

## 4.6 Detours

Historical/explanatory detour chỉ giữ nếu tăng ít nhất một:

```text
scale
scene value
causal proof
pattern interrupt
reframe/reversal
stakes/consequence
```

## 4.7 Dramatization

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

# 6. Anti-AI / anti-template

Tránh:

- spam “Here’s the thing”;
- spam “Think about that”;
- spam “This is where it gets interesting”;
- liên tục “Not X. Y.”;
- quoteable one-liner ở mọi paragraph;
- authority stacking;
- mọi beat cùng một rhetorical skeleton;
- generic cliffhanger;
- abstract explanation kéo dài không scene/scale shift;
- lặp luận điểm để đủ thời lượng.

Giữ logic engine ổn định nhưng thay surface form theo topic.

---

# 7. Word budget

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

# 8. Cấu trúc repo

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
  02_architecture.md
  03_outline.md
  04_draft.md
  05_fact_audit.md
  06_retention_audit.md
  07_rewrite_final.md

scripts/
  new_project.py
  check_project.py

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

# 9. Workflow khuyến nghị

```text
1. topic + language + duration
2. Research Ledger + story metadata
3. Central contradiction + hook archetype
4. Act Architecture
5. Viewer-question chain + causal ladder
6. Scale Escalation + Story Expansion
7. Reveal Ladder + Scene Density Map
8. Retention Outline
9. Draft
10. Fact Audit
11. Retention / Story Momentum Audit
12. Final Rewrite
13. check_project.py
14. lấy 07_final_script.md khi PASS
```

---

# 10. Definition of Done

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
- Fact Audit = `PASS`;
- Retention / Story Momentum Audit >= `33/40` và `PASS`;
- `scripts/check_project.py` trả `RESULT: PASS`.

Artifact sản xuất:

```text
projects/<slug>/07_final_script.md
```
