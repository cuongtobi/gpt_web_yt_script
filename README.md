# GPT Web YouTube Script Pipeline

Pipeline viết YouTube documentary/explainer script theo cấu trúc kể chuyện giữ chân người xem:

**cinematic hook → central question → causal chain → evidence → meaning → consequence → open loop → payoff → thematic callback**

Repo được thiết kế để dùng trực tiếp với **Codex** hoặc **ChatGPT Web + GitHub**. Mỗi video là một workspace riêng trong `projects/<slug>/` để có thể nghiên cứu, viết, audit và tiếp tục chỉnh sửa mà không mất context.

---

## Mục tiêu

- Đầu vào tối thiểu: **chủ đề + ngôn ngữ + độ dài video**.
- Đầu ra: YouTube video script hoàn chỉnh, bám sát thời lượng yêu cầu.
- Viết để **nói/voice-over**, không viết như bài luận.
- Hook mạnh trong 30–45 giây đầu.
- Thông tin quan trọng xuất hiện sớm.
- Có macro open loop xuyên video và micro open loops giữa các phần.
- Tổ chức nội dung bằng **chuỗi nguyên nhân–hệ quả**, không chỉ liệt kê timeline/fact.
- Script phải tạo được hình ảnh/B-roll rõ ràng.
- Không lặp ý để kéo thời lượng.
- Phân biệt rõ fact, theory, interpretation và uncertainty.
- Không bịa nguồn, số liệu, quote, xác suất hoặc false precision.
- Giảm dấu vết template/AI bằng kiểm soát transition, sentence rhythm và rhetorical patterns.

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

File đầu ra cuối cùng:

```text
projects/<slug>/07_final_script.md
```

Chi tiết logic từng stage xem:

```text
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
```

---

# 1. Cách dùng với Codex

Codex là cách thuận tiện nhất nếu bạn muốn agent trực tiếp đọc repo, tạo project, sửa file, chạy helper script và hoàn thành toàn bộ pipeline.

## 1.1 Clone repo

Trên máy local:

```bash
git clone https://github.com/cuongtobi/gpt_web_yt_script.git
cd gpt_web_yt_script
```

Repo không yêu cầu package Python ngoài. Hai helper script hiện tại chỉ dùng Python standard library.

Kiểm tra Python:

```bash
python --version
```

Hoặc trên một số máy:

```bash
python3 --version
```

---

## 1.2 Mở repo bằng Codex

Mở Codex tại thư mục root của repo.

Agent phải đọc các file điều khiển chính trước khi viết:

```text
AGENTS.md
pipeline/PIPELINE.md
pipeline/QUALITY_GATES.md
docs/STYLE_DNA.md
prompts/00_orchestrator.md
```

`AGENTS.md` là source of truth về behavior, word budget, epistemic rules, anti-AI rules và definition of done.

---

## 1.3 Cách nhanh nhất: giao toàn bộ video cho Codex

Prompt mẫu:

```text
Hãy làm việc trong repo này và chạy toàn bộ YouTube script pipeline.

Input:
topic: How Did Humans Invent Money?
language: English
duration: 25 minutes

Yêu cầu:
- đọc AGENTS.md và prompts/00_orchestrator.md trước;
- tự tạo project mới trong projects/;
- research trước khi viết factual claim quan trọng;
- chạy đủ Research Ledger → Architecture → Outline → Draft → Fact Audit → Retention Audit → Final;
- tự sửa nếu audit FAIL;
- final phải nằm trong projects/<slug>/07_final_script.md;
- cuối cùng chạy scripts/check_project.py và chỉ coi hoàn tất khi PASS.
```

Bạn không cần ra lệnh từng stage. Khi user yêu cầu “viết script”, orchestrator được thiết kế để agent tự chạy toàn pipeline.

---

## 1.4 Tạo project thủ công bằng helper script

Có thể khởi tạo workspace trước:

```bash
python scripts/new_project.py \
  --topic "How Did Humans Invent Money?" \
  --language English \
  --duration 25
```

Windows PowerShell có thể dùng một dòng:

```powershell
python scripts/new_project.py --topic "How Did Humans Invent Money?" --language English --duration 25
```

Kết quả ví dụ:

```text
projects/how-did-humans-invent-money/
```

Trong đó có sẵn:

```text
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

Sau đó nói với Codex:

```text
Tiếp tục project projects/how-did-humans-invent-money/.
Đọc AGENTS.md và toàn bộ artifacts hiện có.
Chạy pipeline từ stage chưa hoàn thành tiếp theo cho tới final.
Không reset hoặc ghi đè research đã được xác nhận nếu không cần thiết.
```

---

## 1.5 Các tham số hỗ trợ của `new_project.py`

Tối thiểu:

```bash
python scripts/new_project.py \
  --topic "<topic>" \
  --language "<language>" \
  --duration <minutes>
```

Có thể thêm:

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

Default tốc độ đọc hiện tại:

```text
English:    158 words/minute
Vietnamese: 152 từ/phút
Other:      150 words/minute
```

Có thể override bằng `--wpm`.

---

## 1.6 Input nâng cao

Ngoài ba trường bắt buộc, có thể đưa thêm cho Codex:

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

Nếu thiếu các preference phụ, agent dùng default trong `AGENTS.md`; không cần dừng pipeline chỉ để hỏi những chi tiết không thiết yếu.

---

## 1.7 Chạy kiểm tra cuối

Sau khi có final:

```bash
python scripts/check_project.py how-did-humans-invent-money
```

Hoặc truyền đường dẫn:

```bash
python scripts/check_project.py projects/how-did-humans-invent-money
```

Checker hiện kiểm tra:

- đủ file bắt buộc;
- final có nằm trong tolerance độ dài ±7%;
- Fact Audit có `PASS`;
- Retention Audit có `PASS`;
- final không còn note kiểu `[VERIFY]`, `[TODO]`, `[SOURCE]`, `[CHECK]`;
- cảnh báo transition mang tính template nếu lặp quá nhiều;
- cảnh báo mọi claim có `%` để bắt buộc kiểm tra support trong Research Ledger.

Kết quả mong muốn:

```text
RESULT: PASS
```

Nếu `FAIL`, yêu cầu Codex đọc lỗi, sửa stage liên quan và chạy checker lại.

Prompt mẫu:

```text
Chạy python scripts/check_project.py <slug>.
Nếu FAIL, đọc toàn bộ lỗi và sửa đúng stage gây lỗi.
Không chỉ sửa bề mặt final nếu lỗi nằm ở research, architecture hoặc outline.
Lặp lại cho tới khi RESULT: PASS.
```

---

## 1.8 Tiếp tục hoặc rewrite project cũ

Không cần tạo project mới nếu chỉ muốn sửa script hiện có.

Ví dụ:

```text
Đọc project projects/how-did-humans-invent-money/.
Tôi muốn tăng retention ở 5 phút giữa nhưng không thay đổi thesis chính.
Hãy đọc Research Ledger, Architecture, Outline, Draft và Retention Audit hiện tại.
Sửa từ stage phù hợp, cập nhật downstream artifacts và chạy check_project.py lại.
```

Hoặc:

```text
Đọc project projects/how-did-humans-invent-money/.
Rút video từ 25 phút xuống 18 phút.
Giữ central question và causal ladder chính.
Cập nhật word budget, outline, draft, audits và final.
```

Nguyên tắc: **không reset toàn bộ project vô cớ**. Tiếp tục từ stage sớm nhất thực sự bị ảnh hưởng.

---

# 2. Cách dùng với ChatGPT Web

Repo cũng được thiết kế để chạy trực tiếp trong ChatGPT Web khi ChatGPT có quyền truy cập GitHub repo này.

## 2.1 Bắt đầu chat mới

Trong ChatGPT Web, kết nối/chọn GitHub và repo:

```text
cuongtobi/gpt_web_yt_script
```

Sau đó gửi yêu cầu trực tiếp.

Prompt ngắn nhất:

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Viết một YouTube documentary script mới.

topic: How Did Humans Invent Money?
language: English
duration: 25 minutes

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline và lưu mọi artifact vào một project mới trong projects/.
```

ChatGPT phải tự đọc rule của repo và chạy các stage theo thứ tự.

---

## 2.2 Prompt khuyến nghị cho ChatGPT Web

Dùng mẫu này khi muốn kiểm soát chặt hơn:

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
3. Chạy đủ Research Ledger → Story Architecture → Outline → Draft → Fact Audit → Retention Audit → Final.
4. Với factual claim quan trọng, research/verify trước khi đưa vào final.
5. Không bịa nguồn, số liệu, quote hoặc xác suất.
6. Nếu Fact Audit FAIL, sửa claim/source trước.
7. Nếu Retention Audit FAIL vì cấu trúc, quay lại Architecture/Outline trước khi rewrite.
8. Final phải bám duration target trong tolerance mặc định của repo.
9. Cập nhật project_state.json.
10. Khi hoàn thành, báo project path, word count, estimated duration và kết quả hai audit.
```

---

## 2.3 ChatGPT Web sẽ tạo những gì?

Ví dụ topic tạo slug `how-did-humans-invent-money`:

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

Bạn chỉ cần lấy nội dung để voice-over từ:

```text
07_final_script.md
```

Research/source không cần chèn vào narration; chúng được giữ riêng trong Research Ledger để script sạch và dễ đọc TTS.

---

## 2.4 Tiếp tục project trong chat khác

Không cần phụ thuộc vào lịch sử chat trước nếu artifacts đã nằm trong GitHub.

Prompt:

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Tiếp tục project:
projects/how-did-humans-invent-money/

Đọc toàn bộ artifacts và project_state.json trước.
Xác định stage hiện tại rồi tiếp tục từ đó.
Không tạo project mới.
```

Đây là lý do mỗi video lưu toàn bộ state trong repo thay vì chỉ giữ trong conversation.

---

## 2.5 Chỉ sửa final nhưng vẫn giữ tính nhất quán

Ví dụ:

```text
@GitHub đọc project projects/how-did-humans-invent-money/.

Rewrite final để voice-over tự nhiên hơn và giảm cảm giác AI.
Không thay đổi fact hoặc causal claim nếu Research Ledger không support.
Sau rewrite, cập nhật Retention Audit và 07_final_script.md.
```

Nếu yêu cầu thay thesis, angle hoặc cấu trúc lớn, nên cho agent quay lại `02_story_architecture.md` hoặc `03_outline.md` thay vì chỉ sửa câu chữ ở final.

---

## 2.6 Yêu cầu một stage riêng

Mặc định khi nói “viết script”, agent nên chạy toàn pipeline.

Nhưng có thể chỉ yêu cầu một stage:

```text
@GitHub đọc project projects/<slug>/.
Chỉ audit factual accuracy của draft hiện tại.
Cập nhật 05_fact_audit.md, chưa rewrite final.
```

Hoặc:

```text
@GitHub đọc project projects/<slug>/.
Chỉ phân tích retention và cập nhật 06_retention_audit.md.
Không thay đổi script.
```

---

# 3. Story DNA của pipeline

Pipeline không sao chép câu chữ của bất kỳ video mẫu nào. Nó học ở cấp cấu trúc.

Một video tốt thường đi theo logic:

```text
Concrete/cinematic opening
        ↓
Surprising contrast
        ↓
Central question
        ↓
Before-state
        ↓
Causal ladder
        ↓
Evidence / case / mechanism
        ↓
Meaning
        ↓
Consequence
        ↓
New question
        ↓
Escalation / reframe
        ↓
Answer
        ↓
Larger implication
        ↓
Callback to opening
```

Nguyên tắc lõi:

> **Question → Evidence → Meaning → Consequence → New Question**

Nếu một đoạn chỉ đưa fact mà không làm thay đổi hiểu biết của người xem, đoạn đó chưa hoàn thành nhiệm vụ.

---

# 4. Research và factual integrity

Research Ledger phân loại claim thành:

```text
ESTABLISHED
SUPPORTED
DEBATED
INTERPRETATION
SPECULATIVE
```

Pipeline phải giữ nguyên mức certainty phù hợp khi chuyển claim vào script.

Ví dụ không được làm:

```text
Nguồn: "likely"
Script: "There is a 90% chance..."
```

Không tự tạo confidence score hoặc phần trăm từ lập luận định tính.

Không được bịa:

- paper;
- tác giả;
- journal;
- institution;
- năm;
- DOI/URL;
- quote;
- statistic;
- xác suất.

Nếu chưa verify được, đánh dấu `UNVERIFIED` trong research và không trình bày nó như fact chắc chắn trong final.

---

# 5. Anti-AI / anti-template

Pipeline chủ động tránh các pattern dễ khiến script nghe như AI:

- spam “Here’s the thing”;
- spam “Think about that”;
- spam “This is where it gets interesting”;
- liên tục dùng “Not X. Y.”;
- paragraph nào cũng cố tạo một quoteable one-liner;
- authority stacking tên tác giả + trường + journal + năm khi không cần;
- câu nào cũng có cùng độ dài và nhịp;
- abstract explanation kéo dài mà không có visual anchor;
- lặp cùng một luận điểm để kéo đủ thời lượng.

Với video documentary 20–30 phút, chỉ nên có một số câu nhấn thật sự đáng nhớ, không biến toàn script thành chuỗi slogan.

---

# 6. Word budget và thời lượng

Mặc định:

```text
English documentary:    target 158 WPM
Vietnamese documentary: target 152 từ/phút
Other languages:        starting point 150 WPM
```

Công thức:

```text
target_words = duration_minutes × target_wpm
```

Ví dụ video English 25 phút:

```text
25 × 158 = 3,950 words
```

Draft có thể lệch rộng hơn trong quá trình viết, nhưng final mặc định phải về trong tolerance **±7%**.

Nếu TTS thực tế của kênh nhanh/chậm hơn, dùng `--wpm` khi tạo project hoặc cập nhật `00_input.md` + `project_state.json`.

---

# 7. Cấu trúc repo

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

# 8. Workflow khuyến nghị

Cho video mới, workflow ngắn nhất là:

```text
1. Gửi topic + language + duration.
2. Agent đọc AGENTS.md + orchestrator.
3. Tạo project.
4. Research có chọn lọc.
5. Xây causal story architecture.
6. Tạo retention outline.
7. Viết draft.
8. Fact Audit.
9. Retention Audit.
10. Rewrite final.
11. Chạy check_project.py.
12. Chỉ lấy 07_final_script.md khi PASS.
```

Không nên bỏ Research Ledger với factual documentary/explainer.

Không nên viết thẳng final từ topic nếu mục tiêu là chất lượng ổn định cho video dài.

---

# 9. Ví dụ hoàn chỉnh

## Codex

```text
Làm việc trong repo hiện tại.

Tạo một YouTube documentary mới:

topic: How Did Humans Invent Debt?
language: English
duration: 24 minutes
audience: general curious audience
tone: cinematic, intelligent, conversational
angle: debt as a social/accounting technology before modern money

Đọc AGENTS.md và prompts/00_orchestrator.md.
Chạy toàn bộ pipeline.
Research factual claims trước khi dùng.
Tự sửa mọi audit FAIL.
Cuối cùng chạy scripts/check_project.py và lưu final vào 07_final_script.md.
```

## ChatGPT Web

```text
@GitHub làm việc với repo cuongtobi/gpt_web_yt_script

Tạo một YouTube documentary mới:

topic: How Did Humans Invent Debt?
language: English
duration: 24 minutes
audience: general curious audience
tone: cinematic, intelligent, conversational
angle: debt as a social/accounting technology before modern money

Đọc AGENTS.md và prompts/00_orchestrator.md rồi tự chạy toàn bộ pipeline.
Không bỏ Research Ledger.
Nếu audit FAIL, sửa rồi audit lại trước khi final.
```

---

# 10. Definition of done

Một project chỉ được xem là hoàn thành khi:

- word/duration budget đạt;
- central question được trả lời;
- causal ladder rõ;
- không section nào chỉ là fact dump;
- factual claim quan trọng có support trong Research Ledger;
- không còn unsupported precise number;
- theory/interpretation được gắn certainty đúng;
- hook và ending liên kết về cùng thematic question;
- không lặp ý để kéo thời lượng;
- narration đọc thành tiếng tự nhiên;
- Fact Audit = `PASS`;
- Retention Audit = `PASS`;
- `scripts/check_project.py` trả về `RESULT: PASS`.

Khi tất cả điều kiện trên đạt, artifact dùng để sản xuất video là:

```text
projects/<slug>/07_final_script.md
```
