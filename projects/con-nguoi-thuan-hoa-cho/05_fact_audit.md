# Fact Audit

- Verdict: PASS

## Selected hook audit

H1 — Contradiction giữ được premise cốt lõi: dogs are the earliest known domesticated animal and securely predate agriculture. Tuy nhiên câu “một nhánh sói ... và từ đó không quay lại” có thể khiến người nghe hiểu lịch sử chó là một lineage đơn giản, trong khi ancient DNA cho thấy ancestry phức tạp và có wolf-related admixture. Final phải giữ contradiction nhưng rewrite câu này.

Primary checks:
- Marsh et al., Nature 2026: genetically confirmed dogs at Pınarbaşı (~15.8 ka) and Gough’s Cave (~14.3 ka), showing Palaeolithic western Eurasian distribution. https://www.nature.com/articles/s41586-026-10170-x
- Bergström et al., Nature 2022: 72 ancient wolf genomes; dogs closer overall to ancient eastern Eurasian wolves, but no sampled wolf is a direct match; at least two wolf-related ancestry sources are required for dog population history. https://www.nature.com/articles/s41586-022-04824-9

## Required changes

1. **REWRITE opening lineage wording:** thay “một nhánh sói ... và từ đó không quay lại” bằng wording thừa nhận grey-wolf origin nhưng không ngụ ý một lineage đơn giản không admixture.
2. **REWRITE vague time sentence:** bỏ “đẩy mốc chắc chắn của câu chuyện về sâu hơn 10.000 năm trước”; dùng mốc cụ thể ~15.800 năm và giải thích nó đặt genetically confirmed dogs sâu vào Palaeolithic.
3. **QUALIFY Bonn-Oberkassel disease:** giữ “pathology compatible with / likely canine distemper” và “authors argue survival probably required substantial human care”; không nói diagnosis tuyệt đối và không suy diễn love/emotion như fact.
4. **QUALIFY AMY2B:** final phải nói increased AMY2B copy number became widespread mainly after the agricultural transition and varied among ancient/modern dogs; không trình bày starch adaptation như trigger ban đầu của domestication.
5. **REMOVE/QUALIFY unsupported utility speculation:** hunting, guarding, warmth, hauling chỉ được nêu như possible later functions; không gán một function cụ thể cho earliest dogs.
6. **KEEP origin uncertainty explicit:** exact time, exact geography, single-vs-multiple domestication, and initial commensal-vs-cooperative pathway remain unresolved.

## Claim audit

| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
| Dogs derive from grey-wolf ancestry | Medium | Bergström et al. 2022 | KEEP | Chó có nguồn gốc từ ancestry của sói xám; quần thể tổ tiên trực tiếp chưa được xác định. |
| Dogs existed before agriculture | Medium | Marsh et al. 2026; dog domestication reviews | KEEP | Chó đã tồn tại cùng hunter-gatherers trước khi agriculture trở thành nền tảng sinh kế phổ biến. |
| Pınarbaşı dog ~15.8 ka | High: precise date/current discovery | Marsh et al. 2026 | KEEP | Khoảng 15.800 năm trước; calibrated range in paper 15,915–15,669 cal BP. |
| Gough’s Cave dog ~14.3 ka | High: precise date | Marsh et al. 2026 | KEEP | Khoảng 14.300 năm trước; paper range 14,793–14,090 cal BP. |
| Gough’s Cave also yielded wolf genome | Medium | Marsh et al. 2026 | KEEP | Nghiên cứu cũng xác định một wolf individual khoảng 14.3 ka from the site/context. |
| Western Eurasian Palaeolithic dogs were widespread/genetically related | High | Marsh et al. 2026 | KEEP | Một dog population genetically related was broadly distributed across western Eurasia. |
| 72 ancient wolf genomes | High: exact number | Bergström et al. 2022 | KEEP | Study analysed 72 ancient wolf genomes spanning ~100,000 years. |
| Dogs closer overall to eastern than sampled western Eurasian ancient wolves | Medium | Bergström et al. 2022 | KEEP | Giữ “nhìn chung gần hơn”; không biến thành exact origin claim. |
| No sampled ancient wolf genome is direct progenitor match | Medium | Bergström et al. 2022 | KEEP | Không genome wolf được phân tích nào khớp trực tiếp với progenitor populations. |
| At least two wolf-related ancestry sources | Medium | Bergström et al. 2022 | KEEP | Dữ liệu phù hợp với eastern-related ancestry plus a western/southwestern-related contribution in some dogs; independent domestication vs later admixture unresolved. |
| Bonn-Oberkassel ~14.2 ka, co-burial with humans | High | Janssens et al. 2018, Journal of Archaeological Science | KEEP | Khoảng 14.200 năm; juvenile dog buried with two humans. https://www.sciencedirect.com/science/article/abs/pii/S0305440318300049 |
| Bonn dog had distemper and required care | High: diagnosis/causality | Janssens et al. 2018 | QUALIFY | Pathology was interpreted as likely morbillivirus/canine distemper; authors argue survival without intensive human assistance would have been unlikely. |
| Commensal scavenging started domestication | High: causal theory | Research C9; no direct archaeological sequence | QUALIFY | Một model plausible, không phải event đã chứng minh trực tiếp. |
| Cooperative relationship started domestication | High: causal theory | Research C10 | QUALIFY | Alternative/possibly overlapping model; trigger unknown. |
| AMY2B/starch adaptation | High: chronology | Axelsson et al. 2013; Arendt et al. 2016; ancient dog genome work | REWRITE | Many dogs show starch-digestion adaptation; high AMY2B copy number largely spread after agriculture and was not universal. https://www.nature.com/articles/nature11837 ; https://www.nature.com/articles/hdy201648 |
| Exact domestication place/date known | High | Bergström 2022; Marsh 2026 | REMOVE | Không đưa exact place/date; explicitly state unresolved. |
| Modern dog social-cue sensitivity proves Palaeolithic behavior | High inference | Research C12 | QUALIFY | Modern traits show selection on behavior matters, but do not reconstruct exact Palaeolithic behavior. |

## Final audit notes

- No direct quotation is used in narration.
- No fabricated percentage/probability is used.
- No cinematic dialogue, weather, emotion or exact historical action is narrated as fact.
- Selected H1 mechanism survives all required factual qualifications.
- No `VERIFY` blocker remains.
