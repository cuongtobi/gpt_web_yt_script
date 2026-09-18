# Fact Audit

- Verdict: PASS

## Selected hook audit

**Selected hook:** H1 — Contradiction

Premise cốt lõi được support: capsaicin gây burning pain bằng cách kích hoạt sensory neurons qua receptor TRPV1; receptor này cũng được hoạt hóa bởi nhiệt trong vùng noxious. Vì vậy contradiction “một hệ cảnh báo đau/nhiệt trở thành thứ ta chủ động tìm trong đồ ăn” là hợp lệ.

Primary source:
- Caterina MJ et al. *The capsaicin receptor: a heat-activated ion channel in the pain pathway.* Nature 389, 816–824 (1997). DOI: 10.1038/39807.

**Action:** KEEP mechanism, REWRITE chi tiết phụ ở final để loại các phản ứng cơ thể cụ thể không cần thiết cho premise (“toát mồ hôi, chảy nước mắt, tìm nước”). Opening final vẫn giữ contradiction và câu callback “một hệ cảnh báo đã biến thành gia vị”.

## Required changes

1. **Opening:** bỏ các chi tiết sweating/tearing không cần thiết; giữ capsaicin → TRPV1 → burning contradiction.
2. **Wasabi/mù tạt:** bỏ mô tả time-course “bốc lên mũi nhanh/rút nhanh hơn ớt” vì research pack không audit riêng claim so sánh thời gian; chỉ giữ isothiocyanates → TRPA1 → pungency.
3. **Carbonation:** wording cụ thể theo Wang et al. 2010: CO2 có thể đi vào tế bào, gây intracellular acidification và TRPA1 là một thành phần quan trọng của nociceptive response. Không nói TRPA1 giải thích toàn bộ cảm giác ga.
4. **Endorphin/dopamine:** không dùng như causal thesis. Chỉ nói research pack không support một chuỗi đơn giản “đau → endorphin → thích cay”.
5. **Culture:** giữ wording association/contribution; không viết childhood/culture như causation tuyệt đối.
6. **Benign masochism:** gọi rõ là psychological framework/theory, không settled neural mechanism.
7. **Personality:** giữ “correlates/associated”, không suy ra người thích cay là người liều lĩnh nói chung.
8. **Ecology:** giữ wording “capsaicin có thể/selectively discourages một số vertebrate predators mà không deterring effective seed dispersers”; không nói nó tiến hóa “để chống con người”.
9. **Chimpanzee case:** giữ caveat n=2 và không suy rộng thành conclusion về human evolution.
10. **Culinary history:** bỏ claim chưa research như “con người mang ớt đi khắp thế giới/chọn giống” khỏi final; chỉ giữ việc con người chủ động dùng ớt trong thực phẩm.

## Claim audit

| Claim | Risk | Evidence/source | Action | Final wording |
|---|---|---|---|---|
| Capsaicin kích hoạt hệ cảm giác đau/nhiệt qua TRPV1 | HIGH — selected hook premise | Caterina et al. 1997, Nature, DOI 10.1038/39807 | KEEP | Capsaicin kích hoạt TRPV1; receptor này cũng đáp ứng noxious heat. |
| “Cay” không phải basic taste; burning thuộc chemesthesis | MEDIUM | Viana 2011, ACS Chem Neurosci, DOI 10.1021/cn100102c | KEEP | Burning/pungency là chemesthetic/somatosensory component của flavor. |
| Capsaicin không cần làm mô nóng như đồ ăn nóng để tạo “nóng” | MEDIUM | Caterina et al. 1997 | KEEP | Chemical activation của TRPV1 có thể tạo burning sensation dù nguồn kích thích không phải nhiệt vật lý tương đương. |
| Wasabi/mù tạt: isothiocyanates kích hoạt TRPA1 | HIGH | Jordt et al. 2004, Nature, DOI 10.1038/nature02282 | KEEP | Wasabi/horseradish/mustard pungency liên quan isothiocyanates và TRPA1. |
| Carbonation có nociceptive sting liên quan TRPA1 | HIGH | Wang, Chang & Liman 2010, J Neurosci, DOI 10.1523/JNEUROSCI.2715-10.2010 | QUALIFY | TRPA1 là một thành phần quan trọng của nociceptive response to high CO2; không nói là toàn bộ cảm giác carbonation. |
| Repeated low-dose capsaicin exposure gây desensitization ở người | HIGH | Nolden et al. 2024, Physiol Behav, PMID 38135109, DOI 10.1016/j.physbeh.2023.114447 | KEEP | 17-day protocol cho thấy capsaicin group giảm oral burn ratings. |
| Desensitization do giảm TRPV1 expression | HIGH causal | Nolden et al. 2024 | REWRITE | Study không tìm thấy evidence rằng giảm TRPV1 mRNA giải thích effect; mechanism vẫn chưa rõ. |
| Exposure có thể tăng liking của chili burn | HIGH | Stevenson & Yeomans 1995, Appetite, PMID 7611746, DOI 10.1016/S0195-6663(95)99328-2 | KEEP | Trong meal context, liking tăng tuyến tính qua exposure ở một số capsaicin concentrations. |
| Liking tăng chỉ vì burn giảm | HIGH causal | Stevenson & Yeomans 1995 | REWRITE | Study cho thấy increase in liking không phụ thuộc đơn giản vào changes in rated burn intensity/arousal. |
| Culture/childhood/repeated exposure là determinant lớn | MEDIUM | Siebert, Lee & Prescott 2022 review, PMCID PMC9795841 | QUALIFY | Review cho thấy environment và repeated exposure là những influences mạnh; không causalize quá mức. |
| Benign masochism giải thích liking spicy food | HIGH theory-vs-fact | Rozin et al. 2013, JDM, DOI 10.1017/S1930297500005295 | QUALIFY | Đây là interpretive framework: enjoyment of negative reactions in a safe context / “mind over body”. |
| Nhiều người thích intensity ngay dưới intolerable | MEDIUM | Rozin et al. 2013 | KEEP WITH SCOPE | “Nhiều người trong các mẫu/studies”, không universal. |
| Sensation seeking liên quan liking spicy food | MEDIUM | Byrnes & Hayes 2016, Appetite, PMID 27137410 | KEEP WITH CORRELATIONAL WORDING | “có tương quan/liên quan”, không “gây ra”. |
| Capsaicin selectively discourages vertebrate seed predators | HIGH ecological causal | Tewksbury & Nabhan 2001, Nature, DOI 10.1038/35086653 | KEEP | Dùng đúng mức: selective deterrence trong hệ thống nghiên cứu, không anthropomorphize plant intent. |
| Hai chimpanzees acquire preference for chili crackers | MEDIUM small-n | Rozin & Kennel 1983, Appetite, PMID 6625565 | QUALIFY | N=2, captive study; curiosity only, no evolutionary generalization. |
| Endorphin/dopamine là nguyên nhân chính của thích cay | HIGH unsupported simplification | Không có direct support đủ mạnh trong research pack | REMOVE AS THESIS | Chỉ nhắc như popular oversimplification mà script không dựa vào. |

## Precise numbers / dates audit

- **1997** TRPV1/capsaicin receptor paper: verified.
- **2024 / 17-day protocol / Study 1 n=51 / Study 2 n=45:** verified from Nolden et al. abstract. Final không cần n hoặc percentage, giảm factual clutter.
- **1995 repeated-exposure liking study:** verified.
- **2022 review / 38 studies:** verified. Final dùng con số 38.
- **2013 benign masochism paper / 29 initially aversive activities:** research source verified; final không cần số 29.
- **1983 chimpanzee study / two chimpanzees:** verified.
- Không có direct quote trong narration.
- Không có fabricated probability.

## Final audit verdict

**PASS.** Không còn blocker. Các Required changes là wording/qualification edits và không làm mất selected H1 Contradiction mechanism.
