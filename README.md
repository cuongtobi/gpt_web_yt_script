# GPT Web YouTube Script Pipeline

Pipeline viết YouTube documentary/explainer theo kiểu **spoken + concrete + causal + comprehensible + evidence-grounded**.

Current pipeline: **simple_v2** — thêm Hook Lab để opening đa dạng và có **human choice gate** trước Story Spine.

## Input

```text
topic: <chủ đề>
language: <ngôn ngữ>
duration: <phút>
```

Optional: title, angle, audience, tone, must_include, must_avoid, sources, hook_choice.

Default word budget:

```text
English:    158 words/minute
Vietnamese: 152 từ/phút
Other:      150 words/minute
```

Final tolerance: ±7% target words.

---

# Pipeline v2

```text
00_input.md
   ↓
01_research.md
   ↓
02_hook_lab.md
   ↓
WAIT FOR USER TO CHOOSE H1–H10
   ↓
03_story_spine.md
   ↓
04_draft.md
   ↓
05_fact_audit.md
   ↓
06_final_script.md
```

## Stage 1 — Research

Tạo research pack vừa đủ để kể story: central question candidates, timeline/causal background, 10–20 core claims, 5–8 strong cases, useful numbers/quotes và important uncertainties.

Research quyết định **cái gì được phép nói**, không quyết định thứ tự narration. Research cũng tạo `Audience Vocabulary / Technical Term Map` để phân loại jargon thành `CORE | SUPPORTING | DISPENSABLE` và chuẩn bị plain-language explanation trước khi viết.

## Stage 2 — Hook Lab

Tạo 10 opening candidates theo 10 curiosity mechanisms:

1. **Contradiction**
2. **Concrete scene**
3. **Mystery / evidence first**
4. **Reverse assumption**
5. **Mechanism in motion**
6. **Before → after transformation**
7. **Object hook**
8. **Stakes hook**
9. **Timeline jump**
10. **Unexpected cause**

Đây là 10 **entry mechanisms**, không phải 10 sentence templates. Candidate phải khác thật về cách vào story, không chỉ rewrite cùng một đoạn bằng từ khác.

Central question có thể explicit hoặc implicit. Pipeline không mặc định `scene → question → answer` và không mặc định các scaffold như:

```text
Câu trả lời là...
Câu trả lời bắt đầu...
Câu trả lời ngắn gọn...
The answer is...
The short answer is...
```

Sau Hook Lab, pipeline **bắt buộc dừng** và để user chọn H1–H10. Model không tự chọn hộ.

## Stage 3 — Story Spine

Chỉ chạy sau khi user chọn hook.

Tạo 6–10 beats. Mỗi beat trả lời:

```text
What happened / what do we learn?
Why does it matter?
What does it naturally lead to next?
Evidence / cases used:
```

Selected hook là opening direction. Writer có thể polish wording nhưng không âm thầm đổi mechanism.

Story Spine xác định technical concepts xuất hiện ở beat nào, cách viewer phổ thông hiểu chúng và label nào có thể bỏ.

## Stage 4 — Full Draft

Ưu tiên:

```text
spoken
concrete
causal
```

Draft target khoảng ±10%. Không lặp ý để kéo duration. Không biến selected hook thành generic question-answer scaffold chỉ vì dễ viết.

Jargon control dùng hai nguyên tắc: **meaning first, label second** và **function before taxonomy**. CORE term phải giải thích ở first use; SUPPORTING term giải thích rất ngắn; DISPENSABLE jargon ưu tiên bỏ label.

## Stage 5 — Fact Audit

Audit cả opening và body:

- number / percentage / date;
- quote;
- named study/person/institution;
- first/oldest/only/largest;
- causal / consensus / current claims;
- cinematic/sensory detail kể như fact;
- plain-language technical explanation và analogy có làm sai meaning hay không.

Actions: `KEEP | QUALIFY | REWRITE | REMOVE | VERIFY`.

Còn `VERIFY` = chưa PASS. Nếu premise cốt lõi của selected hook không support, quay lại Hook Lab thay vì lén đổi opening.

## Stage 6 — Final Edit

Áp dụng Fact Audit, cắt repetition/padding, làm prose dễ nói, giữ concrete cases mạnh, giữ selected hook mechanism, chạy cold-reader jargon pass và đưa final về ±7%.

Output chính:

```text
projects/<slug>/06_final_script.md
```

---

# Hook diversity doctrine

Hook không được định nghĩa bằng câu chữ; hook được định nghĩa bằng **động lực tò mò**.

Không bắt buộc mọi opening phải:

- có direct question;
- nói central question nguyên văn;
- reveal thesis ngay;
- có cùng số câu;
- kết bằng `Câu trả lời là...`.

Scene hook phải dựa trên evidence hoặc phrasing rõ là hypothetical. Không bịa dialogue, weather, emotion, exact historical action hoặc sensory detail chỉ để cinematic.

Nếu bỏ label H1–H10 mà nhiều candidate vẫn có cùng skeleton, Hook Lab cần viết lại.

Chi tiết: `docs/STYLE_DNA.md` và `prompts/v2/02_hook_lab.md`.

---

# Cách dùng với Codex

```bash
git clone https://github.com/cuongtobi/gpt_web_yt_script.git
cd gpt_web_yt_script
python scripts/new_project.py --topic "How Did Humans Invent Money?" --language English --duration 25
```

Sau đó:

```text
Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy pipeline cho project vừa tạo.
Dừng sau Hook Lab để tôi chọn hook.
```

Sau khi nhận H1–H10, trả lời ví dụ:

```text
Chọn H4
```

Pipeline sẽ tiếp tục Story Spine → Draft → Fact Audit → Final.

---

# Cách dùng với ChatGPT Web + GitHub

Turn 1:

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Viết một YouTube documentary script mới.

topic: <TOPIC>
language: <LANGUAGE>
duration: <MINUTES> minutes

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy pipeline và lưu mọi artifact vào một project mới trong projects/.
```

Assistant sẽ research, tạo `02_hook_lab.md`, đưa H1–H10 và **dừng để bạn chọn**.

Turn 2:

```text
Chọn H7
```

Assistant ghi selection và chạy phần còn lại của pipeline.

Nếu bạn đã có lựa chọn mechanism ngay từ đầu, có thể thêm:

```text
hook_choice: Object hook
```

Hook Lab vẫn được tạo để trace alternatives, nhưng pipeline không cần dừng.

---

# Final validation

```bash
python scripts/check_project.py projects/<slug>
```

Hard FAIL cho `simple_v2` khi:

- thiếu artifact;
- Hook Lab chưa có explicit selection;
- Fact Audit chưa PASS;
- final lệch quá ±7%;
- final còn `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`.

Checker chỉ WARN với template-like transitions, generic imagination openings, early-answer scaffold như `Câu trả lời là...` / `The short answer is...`, và percentage claims cần double-check.

Checker vẫn hỗ trợ `simple_v1` và legacy projects.

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
  ...v1 prompts remain for compatibility...
  v2/
    02_hook_lab.md
    03_story_spine.md
    04_draft.md
    05_fact_audit.md
    06_final_edit.md

scripts/
  new_project.py
  check_project.py

templates/
  project/        # simple_v1 compatibility
  project_v2/     # current default

projects/
  <mỗi video là một thư mục riêng>
```

---

# Definition of Done

Project `simple_v2` hoàn tất khi:

- research đủ support cho thesis;
- Hook Lab có 10 candidate khác mechanism và explicit user selection;
- Story Spine có 6–10 beat dễ theo;
- narration spoken/concrete/causal;
- selected hook mechanism được giữ qua Draft/Final;
- Fact Audit = `PASS`;
- final nằm trong ±7% target;
- final không còn editor/verification notes;
- central question được trả lời rõ;
- `python scripts/check_project.py <project>` trả `RESULT: PASS`.
