[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/reemar128/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/reemar128/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# Wednesday 25 November 2026 — the world in one day, 36 stories

A make.fun bounty entry for
[news-image-20261125](https://make.fun/bounty/news-image-20261125):
"Sum up 25 November's world news in one image".

The program draws a dense newspaper front page for Wednesday 25 November
2026: a dark-teal masthead, a six-stat numbers strip, seven featured stories
with decks beside a drawn world map, a UTC timeline, and a three-column
region-grouped list of the remaining stories. Every story on the page was
verified as a Wednesday 25 November 2026 event in a reputable outlet
(Reuters, AP, BBC, BEA, Destatis and others). Stories from Tuesday 24
November or earlier were checked and left out — the research was re-verified
twice, and 21 wrong-day items were removed before building.

## The 36 stories

1. Shenzhou-24 launches, Pakistan's first astronaut to Tiangong
2. Three bodies found in flooded West Java gold mine; 26 miners trapped
3. Cartagena hostage siege ends with all freed, one captor killed
4. Bangladesh garment wage rises 36% to 17,000 taka a month
5. Ukrainian drones strike Samara refineries (Syzran + Kuibyshev)
6. Australia signs Solomon Islands security treaty, A$740m over 10 years
7. Shein Europe sales sink 27.6% to $2.98bn
8. US market close: Dow 50,182.95 (+0.33%), S&P 7,182.78, Nasdaq 23,585.80
9. North Korea expels Swiss office head, 48 hours to leave
10. Saudi coalition hits Hodeidah, Saada, Amran; Houthis threaten Jeddah
11. Gaza al-Shati airstrike kills a family of four
12. Germany Q3 GDP +0.1% (revised down from 0.2%)
13. Australia October CPI +4.9% y/y
14. Estonia FM Margus Tsahkna arrives in Kyiv
15. China pledges to help Thailand and Myanmar fight Mekong pollution
16. US PCE inflation +3.8% headline, core +3.3% YoY
17. US Q3 GDP, 2nd estimate, +4.3% annualised
18. US jobless claims 189,000; durable goods +0.2%
19. Trump preparing new tariffs — China 20%, potentially 40%
20. Deere misses, FY2027 guidance $4.5–5.25bn
21. Dell beats hugely, shares still fall 5–7%
22. Eurostar strike cancels London–Paris–Brussels trains
23. Germany's Merz defends Ukraine aid in Bundestag
24. Ramaphosa wins Phala Phala court battle
25. UK energy bills +26% from January, Ofgem cap £2,166
26. Two men charged over Anmer Hall break-in
27. Malaysia Airlines parent orders 10 Boeing 787-10 Dreamliners
28. Australia passes Digital Duty of Care Act for Big Tech
29. Two tankers hit mines in Hormuz, Iran warns vessels
30. ESA Hera reveals stadium-sized crater on Dimorphos after DART
31. Brazil Operation Húbris vs R$2bn illegal iron-ore scheme
32. Puerto Rico Supreme Court voids LUMA grid contract 5–4
33. Africa CDC + WHO launch $1.576bn Congo Ebola plan
34. Nollywood actor Pete Edochie dies at 79
35. Iraq Federal Supreme Court: Baghdad may deploy troops to Kurdistan border
36. NBA Cup: 76ers 111–104 Heat (LeBron's first triple-double as a 76er)

## How to run

```sh
python3 build_image.py   # writes entry.png (1024x1024, deterministic)
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` uses only the Python standard library. `build_image.py` needs
Pillow. Running `build_image.py` twice produces byte-identical output.

## License

MIT — see LICENSE.

---
Built with [make.fun](https://make.fun/r/arsk6sc9) — ref=arsk6sc9
