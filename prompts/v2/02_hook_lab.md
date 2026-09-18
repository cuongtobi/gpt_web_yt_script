# Stage 2 — Hook Lab

Đọc `00_input.md` và `01_research.md`.

Mục tiêu: tạo nhiều **đường vào câu chuyện thực sự khác nhau** để user chọn opening direction trước khi Story Spine được viết.

Lưu vào `02_hook_lab.md`.

## Bắt buộc tạo 10 candidate

Tạo đúng một candidate cho mỗi mechanism:

### H1 — Contradiction
Mở bằng hai fact/truth tưởng như khó cùng đúng, rồi để tension kéo viewer vào story.

### H2 — Concrete scene
Mở bằng scene/object/action cụ thể có evidence. Nếu scene chỉ là minh họa giả định, phải wording rõ là hypothetical. Không bịa historical action, dialogue, weather, emotion hoặc sensory detail.

### H3 — Mystery / evidence first
Mở bằng artifact, experiment, measurement, archaeological evidence hoặc hiện tượng chưa được giải thích ngay.

### H4 — Reverse assumption
Mở bằng cách sửa một trực giác/hiểu lầm phổ biến, nhưng phải đủ nuance để không biến thành clickbait sai.

### H5 — Mechanism in motion
Mở bằng cơ thể, máy móc, thị trường, hệ sinh thái, quy trình hoặc causal mechanism đang hoạt động.

### H6 — Before → after transformation
Đặt hai trạng thái trước/sau cạnh nhau để viewer muốn biết bước chuyển xảy ra bằng cách nào.

### H7 — Object hook
Dùng một vật nhỏ/cụ thể mang theo câu chuyện lớn: artifact, coin, seed, bone, tool, molecule, document, device...

### H8 — Stakes hook
Mở bằng hậu quả thực sự nếu vấn đề không được giải quyết hoặc mechanism thất bại. Không phóng đại stakes ngoài evidence.

### H9 — Timeline jump
Đặt hai thời điểm xa nhau cạnh nhau để tạo contrast lịch sử hoặc tiến hóa.

### H10 — Unexpected cause
Mở bằng một nguyên nhân/driver ít trực giác nhưng có support, khiến viewer phải cập nhật cách hiểu ban đầu.

## Diversity rules

10 mechanism là **creative constraints**, không phải 10 sentence templates.

Bắt buộc:

- H1–H10 phải khác nhau về first move, logic tò mò và nhịp;
- không chỉ thay noun/verb rồi giữ cùng skeleton;
- không bắt buộc candidate nào cũng có direct question;
- không bắt buộc central question xuất hiện nguyên văn;
- candidate có thể dài/ngắn khác nhau; thường đủ 2–6 câu để user đánh giá, nhưng đây không phải quota;
- sau setup/tension, ưu tiên đi tiếp bằng fact/evidence/mechanism/consequence;
- mọi factual premise phải trace được về `01_research.md`;
- hook không được phụ thuộc vào jargon mà khán giả phổ thông chưa hiểu;
- nếu technical label buộc phải xuất hiện trong hook, meaning phải rõ ngay trong cùng nhịp mở đầu hoặc label phải được thay bằng plain language.

Không mặc định dùng các scaffold:

- `Câu trả lời là...`
- `Câu trả lời bắt đầu...`
- `Câu trả lời ngắn gọn...`
- `The answer is...`
- `The answer starts with...`
- `The short answer is...`
- `Để hiểu điều này, trước hết...`
- `To understand this, we need to...`
- `Nhưng câu hỏi là...`
- `Hãy tưởng tượng...`
- `Imagine...`

Các phrase trên không phải banned forever trong toàn script; Hook Lab tránh dùng chúng như default scaffolding để bảo vệ diversity.

## Candidate format

Với mỗi H1–H10:

```md
### H1 — <Mechanism>

**Hook**
<actual narration candidate>

**Evidence anchors**
- C# / case / source already present in 01_research.md

**Bridge**
<1 câu: candidate này tự nhiên dẫn vào bước nào của story>
```

Không xếp hạng Best/Winner. Không tự chọn.

Dùng `Audience Vocabulary / Technical Term Map` trong Research để tránh đưa CORE/SUPPORTING term vào hook như một nhãn trống. Curiosity phải đến từ contradiction, evidence, mechanism hoặc consequence — không phải từ việc viewer không biết một từ chuyên ngành nghĩa là gì.

## Selection section

Kết thúc file bằng:

```md
## Selection

- Status: PENDING
- Selected ID:
- Selected mechanism:
- User note:
```

Sau khi user chọn, update section thành `Status: SELECTED` và điền lựa chọn chính xác.

## Human gate

Sau khi lưu Hook Lab:

1. update state:
   - `current_stage = "awaiting_hook_selection"`
   - `hook_selection = "PENDING"`
2. hiển thị H1–H10 cho user;
3. yêu cầu chọn H1–H10 hoặc tên mechanism;
4. **STOP. Không chạy Story Spine hoặc bất kỳ downstream stage nào.**

Nếu user muốn sửa một candidate hoặc kết hợp ý, revise Hook Lab trước. Downstream chỉ chạy sau khi user explicit chốt một selected hook.
