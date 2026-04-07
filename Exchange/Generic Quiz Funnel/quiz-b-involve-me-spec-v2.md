# involve.me Spec: Aware Quiz Funnel — B-Version v2
**Sprache:** DE  
**Typ:** Outcome Quiz + Lead-Gen  
**Ziel:** E-Mail-Capture → Produktempfehlung → Ecommerce-Conversion  
**Slides:** 12 Quiz-Slides + 7 Outcome-Pages  
**Stand:** 2026-04-02 (v2 — AwarePro-Block, Auswahlmöglichkeit auf Ergebnisseiten, Visual Upgrades)

---

## Settings (involve.me Global)
- Type: **Outcome Quiz**
- Progress Bar: **Yes** (ab Slide 2, Farbe: #A18AFF)
- Language: DE
- Email Notifications: ja
- GDPR: Opt-in Checkbox on E-Mail slide

---

## VISUAL UPGRADE ÜBERSICHT (NEU in v2)

> Diese Übersicht zeigt alle visuellen Verbesserungen gegenüber v1. Details sind inline in den jeweiligen Slides beschrieben.

| # | Element | Upgrade |
|---|---------|---------|
| Slide 1 | Social Proof | Sterne-Rating + Zahlen-Chips (4.7★ · 10k+ · 650k+ Werte) |
| Slide 1 | Trust-Badges | Logo-Bar (z.B. "Bekannt aus" oder Lab-Partner-Logos) |
| Slide 4 | Infografik | Körper-System-Netzwerk als echte Grafik statt Tabelle |
| Slide 10 | Stat-Card | Große animierte Zahl (7/10) als visuelles Element |
| Slide 11 | E-Mail-Gate | "Blurred preview" Card als Teaser-Grafik |
| Slide 12 | Loading | Animierter Biomarker-Scan mit Fortschrittsbalken |
| Alle Outcomes | Hero | Personalisierter Headline mit Symptom-Rückspiegelung |
| Alle Outcomes | Produkt-Karten | Echte Auswahlmöglichkeit (3er-Grid mit Highlight) |
| Alle Outcomes | AwarePro | Dedizierter Upsell-Block (nach Primary Card) |
| Alle Outcomes | Biomarker-Chips | Farbige, zone-codierte Chips mit Icon |

---

## QUIZ-SLIDES

---

### Slide 1 – Opener / Welcome

**Type:** Welcome Screen  
**Headline:** Dein Körper sendet Signale. Weißt du, was er meint?  
**Body:**  
In nur 2 Minuten findest du heraus, welche Blutwerte bei dir Aufschluss geben – und was dahintersteckt.

**[VISUAL UPGRADE v2] Social Proof Bar (direkt unter der Headline):**
> Drei Chips nebeneinander, gut lesbar:
> - ⭐ **4.7 / 5** (App Store & Google Play)
> - 👥 **10.000+ Kunden** getestet
> - 🔬 **650.000+ Werte** analysiert
>
> Design: Kleine Pill-Buttons, grau/weiß, inline, kein Ablenkungspotenzial.

**[VISUAL UPGRADE v2] Trust-Badges unterhalb der Chips:**
> Kleine Logos oder Text-Labels: z.B. Partnerlab-Logos, "Medizinisch validiert", TÜV-Siegel o.ä.
> Alternativ: "Bekannt aus [Logo1] [Logo2]" falls Presseerwähnungen vorhanden.

**Bestehender Social Proof (kleinere Schrift, unter Badges):**  
✓ 10.000+ Menschen haben bereits ihre Werte gecheckt  
✓ Medizinisch validiert  
✓ Ergebnis in 48h

**Button:** Jetzt starten →

---

### Slide 2 – Gender

**Type:** Single Choice  
**Frage:** Wie lautet dein biologisches Geschlecht?  
**Variable:** `gender`  
**Optionen:**
- Weiblich → `female`
- Männlich → `male`

**Routing:** Kein Jump, weiter zu Slide 3

---

### Slide 3 – Symptome / Concerns

**Type:** Multiple Choice (max. 4 Auswahlen)  
**Frage:** Was ist in deinem Körper zuletzt passiert, das dich aufmerksam gemacht hat?  
**Hinweis:** Wähle bis zu 4 Optionen aus  
**Variable:** `symptoms` (Multi-Array)  
**Optionen:**
- ⚡ Plötzliche Energietiefs → `energie`
- ⚖️ Gewichtsschwankungen → `gewicht`
- 🌙 Schlafstörungen → `schlaf`
- 🧠 Stimmung oder Fokus → `stimmung`
- 🔄 PMS / Zyklusveränderungen → `pms`
- 💪 Trainingsplateaus → `training`
- 😤 Stressreaktionen → `stress`
- ❓ Sonstiges → `sonstiges`

**Button:** Weiter →

---

### Slide 4 – EDU: Körper-System-Map

**Type:** Content / Statement Screen  
**Keine Frage, keine Eingabe – reiner Edu-Content**

**Headline:** So hängt das zusammen.

**Body-Text:**  
Dein Körper ist ein vernetztes System. Symptome wie Müdigkeit oder Stimmungsschwankungen entstehen selten aus einer einzigen Ursache – sie sind oft Signale aus mehreren biologischen Bereichen gleichzeitig.

**[VISUAL UPGRADE v2] Infografik — Körper-System-Netzwerk:**
> **Empfohlen als echte Grafik (PNG/SVG hochladen in involve.me):**
>
> Zentraler Kreis: "Dein Körper"  
> 5 äußere Kreise (farbig nach Zone-Palette):  
> - 🔵 Hormone (#486EF6) — PMS · Stimmung · Libido  
> - 🟣 Stoffwechsel (#A480F2) — Gewicht · Energie · Blutzucker  
> - 🟢 Energie (#6AF0B6) — Müdigkeit · Schlaf · Belastbarkeit  
> - 🩵 Immunsystem (#02ADB8) — Infektanfälligkeit · Entzündungen  
> - 🩷 Herz/Gefäße (#FF6B8A) — Stress · Blutdruck · Ausdauer  
>
> Gestrichelte Linien verbinden die Kreise, signalisieren Vernetzung.  
> Unter jedem Kreis: 2–3 Symptom-Tags als kleine Chips.  
> Stil: Aware-Brand, cleane Linien, mobile-optimiert (vertikal stapelbar).
>
> **Fallback (wenn Grafik nicht möglich):** Tabelle wie in v1.

**CTA-Text:** Jetzt schauen, welche Werte für dich relevant sind

**Button:** Weiter →

---

### Slide 5 – Wichtigkeit (Slider)

**Type:** Rating Scale / Slider  
**Frage:** Wie wichtig ist es dir, zu verstehen, was hinter diesen Signalen steckt?  
**Skala:** 0 (Weniger wichtig) → 10 (Sehr wichtig)  
**Variable:** `importance`  
**Button:** Weiter →

---

### Slide 6 – Warum jetzt?

**Type:** Single Choice  
**Frage:** Warum ist dieses Thema gerade jetzt wichtig für dich?  
**Variable:** `why_now`  
**Optionen:**
- Ich will verstehen, was wirklich los ist → `verstehen`
- Ich will nicht länger raten → `raten`
- Ich fühle mich nicht wie ich selbst → `identity`
- Ich will bessere Entscheidungen treffen → `entscheidungen`
- Ich will wieder Kontrolle → `kontrolle`
- Sonstiges → `sonstiges`

**Button:** Weiter →

---

### Slide 7 – Ziele in 12 Wochen

**Type:** Multiple Choice (max. 4 Auswahlen)  
**Frage:** Wo möchtest du in 12 Wochen stehen?  
**Variable:** `goals` (Multi-Array)  
**Optionen:**
- ⚡ Mehr Energie und Belastbarkeit → `energie`
- ⚖️ Ausgeglichener Hormonspiegel → `hormone`
- 🔥 Besserer Stoffwechsel → `stoffwechsel`
- 🏃 Mehr Leistung beim Sport → `sport`
- 😊 Ausgeglichene Stimmung → `stimmung`
- 😴 Erholsamerer Schlaf → `schlaf`

**Button:** Weiter →

---

### Slide 8 – Was hält dich zurück?

**Type:** Single Choice  
**Frage:** Was hält dich aktuell am stärksten davon ab?  
**Variable:** `blocker`  
**Optionen:**
- Ich kenne die Ursache nicht → `ursache`
- Mein Körper sendet widersprüchliche Signale → `widerspruch`
- Ich brauche Zahlen und Fakten → `fakten`
- Die Symptome verändern sich → `veraenderung`
- Maßnahmen haben bisher nicht geholfen → `massnahmen`
- Sonstiges → `sonstiges`

**Button:** Weiter →

---

### Slide 9 – Gewünschte Detailtiefe

**Type:** Single Choice  
**Frage:** Was erwartest du konkret von den Ergebnissen?  
**Variable:** `depth`  
**Optionen:**
- Überblick über die wichtigsten Werte → `ueberblick`
- Klare Ursachen und mittlere Detailtiefe → `mittel`
- Vollständige medizinische Detailtiefe → `vollstaendig`
- Alles davon + regelmäßige Verlaufsdaten → `alles`

**Logic Jump:**
- `vollstaendig` oder `alles` → setzt Outcome-Tendenz auf HA
- `ueberblick` → setzt Outcome-Tendenz auf LTH

**Button:** Weiter →

---

### Slide 10 – STAT-CARD (Cliffhanger)

**Type:** Statement / Content Screen  
**Keine Frage**

**Headline:** Fast da. Noch eine wichtige Information.

**[VISUAL UPGRADE v2] Große animierte Statistik-Karte:**
> Zentrierte Karte, großer Schriftzug:
>
> **"7 von 10"**  
> *(Zahl in sehr großer, fetter Schrift, lila/Aware-Brandfarbe)*
>
> Darunter:  
> Menschen mit ähnlichen Symptomen finden im Blutbild eine biologische Ursache — die ohne Test unsichtbar geblieben wäre.
>
> Optional: Kleine Piktogramm-Icons (7 ausgefüllte Menschen, 3 leere), um die Ratio visuell darzustellen.

**Sub-Text:**  
Deine Angaben helfen uns jetzt, die relevantesten Systeme für dich zu identifizieren.

**Button:** Meine Analyse freischalten →

---

### Slide 11 – E-Mail-Capture (Lead Gen)

**Type:** Lead Form  
**Headline:** Dein personalisierter Gesundheits-Report ist bereit.

**Sub-Headline:**  
Gib deine E-Mail-Adresse an, um deine Empfehlung zu sehen – inklusive erklärender Einblicke in deine Biologie.

**[VISUAL UPGRADE v2] Blurred Preview Card:**
> Grafische Karte (verschwommen/unscharf dargestellt), zeigt:
>
> 🔒 Deine Empfehlung: ████████ Check  
> ✓ Die biologischen Ursachen deiner Symptome  
> ✓ Konkrete Handlungsschritte  
> ✓ Dein persönlicher Biomarker-Fahrplan  
>
> Effekt: Blur via CSS oder als statisches Bild mit Unschärfe-Overlay.  
> Ziel: Neugier und Verlangen wecken — das Ergebnis ist "gleich da".

**Felder:**
- Vorname (optional, Text)
- E-Mail (Pflichtfeld, E-Mail-Validierung)
- Bundesland (verstecktes Feld, z.B. via URL-Parameter)

**DSGVO Opt-in (Checkbox, Pflicht):**  
"Ich bin einverstanden, den Aware Newsletter zu erhalten und meinen Fortschritt zu tracken. Abmeldung jederzeit möglich. [Datenschutzerklärung]"

**Button:** Meine Empfehlung anzeigen →

---

### Slide 12 – Loading / Verarbeitung

**Type:** Content Screen mit Timer  
**Dauer:** 2–3 Sekunden, dann auto-weiter zu Outcome  

**[VISUAL UPGRADE v2] Animierter Scan-Effekt:**
> Fortschrittsbalken (lila, Aware-Brand) läuft von 0–100%.  
> Daneben oder darunter: Scanlinien-Animation oder Biomarker-Icons die "eingelesen" werden.  
> Texte die sequenziell durchlaufen:
> - "Symptome werden biologischen Systemen zugeordnet…"
> - "Relevante Biomarker werden identifiziert…"
> - "Deine persönliche Empfehlung wird erstellt…"
>
> Hinweis für involve.me: Statement-Screen + Timer 3s, dann Jump zu Outcome.

---

## ROUTING-LOGIK (Logic Jumps)

Nach Slide 12 wird anhand der gesammelten Variablen das Outcome bestimmt:

```
WENN gender = female UND symptoms enthält (pms ODER stimmung ODER energie)
  → OUTCOME: FH (Female Hormone Check)

WENN gender = male UND symptoms enthält (energie ODER stimmung ODER training)
  → OUTCOME: MH (Male Hormone Check)

SONST WENN symptoms enthält training ODER goals enthält sport
  → OUTCOME: SP (Sports Check)

SONST WENN symptoms enthält gewicht ODER goals enthält stoffwechsel
  → OUTCOME: NUT (Nutrition Check)

SONST WENN depth = vollstaendig ODER depth = alles
  → OUTCOME: HA (Holistic Advanced)

SONST WENN depth = ueberblick
  → OUTCOME: LTH (Long-Term Health Check)

DEFAULT → OUTCOME: HC (Holistic Core)
```

---

## OUTCOME-SEITEN

### ⚙️ Struktur jeder Outcome-Seite (v2)

1. **Hero** – Personalisierter Header mit Symptom-Rückspiegelung
2. **Primary Product Card** – Empfohlenes Paket (hervorgehoben)
3. **[NEU] Produkt-Auswahl-Block** – 3er-Grid mit allen relevanten Checks
4. **[NEU] AwarePro Upsell-Block** – auf allen Outcome-Seiten identisch
5. **Insight Block** – Edu-Content / Warum dieser Check?
6. **Trust-Block** – Social Proof
7. **FAQ** – 3 aufklappbare Fragen

---

### [NEU] Produkt-Auswahl-Block (Template — auf allen Outcomes)

> Nach der Primary Card kommt dieser Block, der dem Nutzer echte Wahlfreiheit gibt.

**Headline:** Oder wähle selbst den passenden Check:

**Layout:** 3 Karten nebeneinander (auf Mobile: vertikal gestapelt)  
- Empfohlener Check: **Highlighted** (Rahmen in Brandfarbe, Badge "Für dich empfohlen")  
- 2 Alternativen: Normal, aber mit Preis + 1-Satz-Beschreibung + CTA-Link  

**Karten-Inhalt je Check:**
- Name + Preisrange  
- 1 Satz was er abdeckt  
- 3–4 Key-Marker Chips (farbig, zone-codiert)  
- Button: "Mehr erfahren" → Link zur Shop-Seite

**Hinweis für involve.me:** Als Text-Block mit Buttons umsetzen oder als Bild-Karten mit Links. Spacing beachten.

---

### [NEU] AwarePro Upsell-Block (Template — auf allen Outcomes, identisch)

> Direkt nach dem Produkt-Auswahl-Block, vor dem Insight Block.

**Hintergrund:** Leicht getönter Block (z.B. #F5F3FF — helles Lila), abgesetzt vom Rest.

**Badge oben links:** ⭐ AwarePro

**Headline:** Hol noch mehr raus — mit AwarePro

**Subline:** Einmal buchen, dauerhaft profitieren.

**Vorteile (als Icon-Liste):**
- 🧬 **Bio Age** — Erfahre, wie alt dein Körper biologisch wirklich ist
- 💰 **20% Rabatt** auf alle Follow-up Checks
- 📈 **Verlaufs-Tracking** — Sieh wie sich deine Werte über Zeit entwickeln
- ⚡ **Priority Lab** — Schnellere Verarbeitung deiner Proben
- 🤝 **Persönlicher Health Coach** — Deine Werte erklärt, nicht nur gezeigt

**CTA-Button:** Jetzt AwarePro dazubuchen → (Link: https://www.aware.app/de/pro oder relevante URL)

**Kleindruck:** Kann jederzeit gekündigt werden · Keine Vertragsbindung

---

### OUTCOME 1 – FH: Female Hormone Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/FH  
**Zone-Farbe:** #486EF6 (Hormones)

**Hero:**
- Headline: Dein Körper zeigt klare Signale – hier ist was wir empfehlen.
- Sub: Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.

**Primary Card:**
- **Titel:** Female Hormone Check
- **Tagline:** Verstehe deinen Rhythmus. Klarheit über PMS, Energie und hormonelles Gleichgewicht.
- **Akzentfarbe links:** #486EF6
- **"Für dich empfohlen, weil:"**
  - Du hast Veränderungen in Stimmung, Energie oder Zyklus beschrieben
  - Hormonelle Ungleichgewichte erklären genau diese Symptome – oft ohne dass Standard-Tests etwas zeigen
  - Der Female Hormone Check analysiert die feine Abstimmung zwischen deinen Hormonen
- **Key-Marker Chips:** Östradiol · Progesteron · Testosteron · LH · FSH · SHBG
- **Preis:** ab €129
- **CTA-Button:** Jetzt Female Hormone Check buchen → (Link: https://www.aware.app/de/shop/berlin-mitte/FH)

**Produkt-Auswahl-Block:**
- Empfohlen: **FH** (Female Hormone Check, €129)
- Alternative 1: **HC** (Holistic Core, €149) — "Zusätzlich Organ- & Stoffwechselwerte"
- Alternative 2: **HA** (Holistic Advanced, €299) — "Das vollständigste Bild deiner Biologie"

**AwarePro Upsell-Block:** *(Standard-Template, siehe oben)*

**Insight Block:**
- **Box 1 – Wusstest du?**  
  "Östrogendominanz betrifft schätzungsweise 1 von 3 Frauen zwischen 25 und 45 Jahren – und ist eine der häufigsten ungeklärten Ursachen für PMS, Müdigkeit und Gewichtszunahme."
- **Box 2 – Die Verbindung:**  
  "Stimmungsschwankungen und Energietiefs entstehen oft nicht durch Stress allein – sie entstehen, weil Progesteron und Östrogen aus dem Gleichgewicht geraten sind. Ein einfaches Blutbild beim Hausarzt misst das nicht."
- **Box 3:**  
  "Testosteron ist auch bei Frauen wichtig – für Energie, Antrieb und Libido. Zu wenig davon bleibt oft unentdeckt."

**Trust-Block:**
- 10.000+ Kunden · NPS 72 · Lab Score 4.78/5
- Quote: *"Endlich hatte ich Zahlen, die erklären, warum ich mich so gefühlt habe. Die Empfehlungen waren konkret und direkt umsetzbar."* – Lea M., Berlin

**FAQ:**
- Q: Wie funktioniert die Blutabnahme?  
  A: Keine Terminbuchung nötig. Du gehst einfach zu einem unserer Partner-Standorte (z.B. Berlin Mitte, dm-Märkte), gibst dein Blut ab und bekommst deine Ergebnisse in 48h in der Aware App.
- Q: Wann erhalte ich meine Ergebnisse?  
  A: In der Regel innerhalb von 48 Stunden nach deiner Blutabnahme.
- Q: Für wen ist der Female Hormone Check geeignet?  
  A: Für alle Frauen, die Veränderungen in Stimmung, Zyklus, Energie oder Libido bemerken – egal ob jung, in der Perimenopause oder danach.

---

### OUTCOME 2 – MH: Male Hormone Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/MH  
**Zone-Farbe:** #486EF6 (Hormones)

**Hero:**
- Headline: Dein Körper zeigt klare Signale – hier ist was wir empfehlen.

**Primary Card:**
- **Titel:** Male Hormone Check
- **Tagline:** Hol dir deinen Antrieb zurück. Kein Erraten mehr – harte Daten zu deiner Energie und Vitalität.
- **"Für dich empfohlen, weil:"**
  - Du hast sinkende Energie, Trainingsplateaus oder Stimmungsveränderungen beschrieben
  - Testosteron und seine Begleitmarker erklären genau diese Symptome bei Männern
  - Ein Standard-Test zeigt nur Gesamt-Testosteron – wir schauen tiefer
- **Key-Marker Chips:** Testosteron · Freies Testosteron · SHBG · Estradiol · LH · DHEA-S
- **Preis:** ab €149
- **CTA-Button:** Jetzt Male Hormone Check buchen → (Link: https://www.aware.app/de/shop/berlin-mitte/MH)

**Produkt-Auswahl-Block:**
- Empfohlen: **MH** (Male Hormone Check, €149)
- Alternative 1: **SP** (Sports Check, €129) — "Leistung, Regeneration und Energiestoffwechsel"
- Alternative 2: **HA** (Holistic Advanced, €299) — "Das vollständigste Bild deiner Biologie"

**AwarePro Upsell-Block:** *(Standard-Template)*

**Insight Block:**
- **Box 1:** "Ein 'normaler' Gesamt-Testosteronwert sagt oft nichts aus – wenn das Hormon gebunden und inaktiv ist. Freies Testosteron und SHBG zeigen erst das wahre Bild."
- **Box 2:** "Zu viel Östrogen bei Männern – durch Stress, Körperfett oder Ernährung – bremst Testosteron aus. Prolaktin sabotiert zusätzlich Libido und Antrieb."

**Trust-Block:** wie FH

**FAQ:** identisch mit FH, Punkt 3 angepasst für Männer

---

### OUTCOME 3 – LTH: Long-Term Health Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/LTH  
**Zone-Farbe:** #02ADB8 (Liver/Organ)

**Primary Card:**
- **Titel:** Long-Term Health Check
- **Tagline:** Dein jährlicher TÜV für den Körper. Umfassender als beim Hausarzt – direkt per App.
- **"Für dich empfohlen, weil:"**
  - Du möchtest einen klaren Überblick ohne zu viel Detailtiefe
  - Der Long-Term Check prüft deine Organfunktionen, deinen Zucker und dein Immunsystem
  - Perfekt als Basis-Check oder jährliches Monitoring
- **Key-Marker Chips:** HbA1c · Leber (GGT, ALAT) · Nieren (eGFR) · Immunsystem · Differentialblutbild
- **Preis:** ab €99
- **CTA-Button:** Jetzt Long-Term Health buchen →

**Produkt-Auswahl-Block:**
- Empfohlen: **LTH** (Long-Term Health, €99)
- Alternative 1: **HC** (Holistic Core, €149) — "Tiefere Einblicke in Stoffwechsel und Herzgesundheit"
- Alternative 2: **HA** (Holistic Advanced, €299) — "Das vollständigste Bild deiner Biologie"

**AwarePro Upsell-Block:** *(Standard-Template)*

**Insight Block:**
- **Box 1:** "Eine Fettleber oder Nierenschwäche spürt man oft erst, wenn es ernst wird. Frühzeitig erkennen, bevor Symptome entstehen."
- **Box 2:** "HbA1c misst den Langzeit-Blutzucker der letzten 3 Monate – der wichtigste Marker zur Diabetes-Prävention. Standard-Bluttests zeigen nur eine Momentaufnahme."

**Trust-Block + FAQ:** wie FH, Punkt 3 angepasst

---

### OUTCOME 4 – SP: Sports Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/SP  
**Zone-Farbe:** #6AF0B6 (Zinc/Energy)

**Primary Card:**
- **Titel:** Sports Check
- **Tagline:** Optimiere deinen Motor. Biologische Ursachen für Müdigkeit, Plateaus und fehlende Erholung.
- **"Für dich empfohlen, weil:"**
  - Du hast Trainingsplateaus oder Leistungsstagnation beschrieben
  - Eisenmangel, Magnesium und Entzündungsmarker sind die häufigsten unentdeckten Leistungsbremsen
  - Der Sports Check findet, was Standard-Tests übersehen
- **Key-Marker Chips:** Ferritin · Magnesium (RBC) · Omega-3-Index · hs-CRP · Hämoglobin · B12
- **Preis:** ab €129
- **CTA-Button:** Jetzt Sports Check buchen →

**Produkt-Auswahl-Block:**
- Empfohlen: **SP** (Sports Check, €129)
- Alternative 1: **NUT** (Nutrition Check, €99) — "Nährstoffversorgung und Treibstoff-Audit"
- Alternative 2: **HC** (Holistic Core, €149) — "Zusätzlich Stoffwechsel und Herzgesundheit"

**AwarePro Upsell-Block:** *(Standard-Template)*

**Insight Block:**
- **Box 1:** "Eisenmangel ist der häufigste Grund für Leistungsabfall – auch bei Männern. Ferritin zeigt deinen Speicher, nicht nur das Eisen im Blut."
- **Box 2:** "Magnesium im Serum zu messen ist ungenau. Wir messen es in den Erythrozyten – das ist der 'wahre' Muskelwert."

**Trust-Block + FAQ:** wie FH, Punkt 3 angepasst für Sportler

---

### OUTCOME 5 – NUT: Nutrition Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/NUT  
**Zone-Farbe:** #FFBE68 (Potassium/Vitamins)

**Primary Card:**
- **Titel:** Nutrition Check
- **Tagline:** Dein Treibstoff-Audit. Gut essen reicht nicht – wenn dein Körper die Nährstoffe nicht aufnimmt.
- **"Für dich empfohlen, weil:"**
  - Du hast Müdigkeit, Gewichtsschwankungen oder Konzentrationsprobleme beschrieben
  - Nährstoffmängel sind häufig versteckt und werden selten getestet
  - Besonders relevant bei vegetarischer/veganer Ernährung oder Stress
- **Key-Marker Chips:** Ferritin · Vitamin D · B12 · Folsäure · B6 · B2
- **Preis:** ab €99
- **CTA-Button:** Jetzt Nutrition Check buchen →

**Produkt-Auswahl-Block:**
- Empfohlen: **NUT** (Nutrition Check, €99)
- Alternative 1: **LTH** (Long-Term Health, €99) — "Zusätzlich Organ- und Immunsystem-Check"
- Alternative 2: **HC** (Holistic Core, €149) — "Tiefere Einblicke in Stoffwechsel und Herzgesundheit"

**AwarePro Upsell-Block:** *(Standard-Template)*

**Insight Block:**
- **Box 1:** "Fast jeder Mensch in Mitteleuropa hat einen Vitamin-D-Mangel – besonders im Winter. Das drückt auf Stimmung, Immunsystem und Schlaf."
- **Box 2:** "Eisenmangel erkennt man erst zuverlässig über Ferritin – nicht über einfaches Eisen im Blut. Oft der unentdeckte Grund für anhaltende Müdigkeit."

**Trust-Block + FAQ:** wie FH

---

### OUTCOME 6 – HC: Holistic Core Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/HC  
**Zone-Farbe:** #A480F2 (Metabolism)

**Primary Card:**
- **Titel:** Holistic Core Check
- **Tagline:** Dein Gesundheits-Fundament. Mehr als ein Hausarzt-Check – weniger als eine Vollanalyse.
- **"Für dich empfohlen, weil:"**
  - Du möchtest ein solides Bild deiner Gesundheit ohne zu viel Komplexität
  - Der Holistic Core schließt die Lücke zwischen Standard und Vollanalyse
  - Ideal als Erst-Check oder jährliches Monitoring
- **Key-Marker Chips:** ApoB · HOMA-Index · Nüchtern-Insulin · hs-CRP · Leber · Nieren · TSH
- **Preis:** ab €149
- **CTA-Button:** Jetzt Holistic Core buchen →

**Produkt-Auswahl-Block:**
- Empfohlen: **HC** (Holistic Core, €149)
- Alternative 1: **LTH** (Long-Term Health, €99) — "Einstieg, weniger Detailtiefe"
- Alternative 2: **HA** (Holistic Advanced, €299) — "Das vollständigste Bild deiner Biologie"

**AwarePro Upsell-Block:** *(Standard-Template)*

**Insight Block:**
- **Box 1:** "ApoB ist der Goldstandard für Herzgesundheit – präziser als LDL-Cholesterin. Standard-Checks messen ihn fast nie."
- **Box 2:** "Nüchtern-Insulin und HOMA-Index zeigen Insulinresistenz, lange bevor sich der Blutzucker verändert – der Schlüssel zur Prävention."

**Trust-Block + FAQ:** wie FH

---

### OUTCOME 7 – HA: Holistic Advanced Check

**URL:** https://www.aware.app/de/shop/berlin-mitte/HA  
**Zone-Farbe:** #A480F2 (Metabolism) + Gradient

**Primary Card:**
- **Titel:** Holistic Advanced Check
- **Tagline:** Dein Körper, komplett entschlüsselt. Das umfassendste Bild deiner Biologie.
- **"Für dich empfohlen, weil:"**
  - Du möchtest vollständige medizinische Detailtiefe und regelmäßige Verlaufsdaten
  - Du willst nicht nur Symptome behandeln, sondern verstehen wie dein System funktioniert
  - Der Holistic Advanced liefert Antworten, die kein Standard-Check geben kann
- **Key-Marker Chips:** ApoB · Homocystein · fT3 · fT4 · Cortisol · Omega-3 · Q10 · Holo-TC (aktives B12)
- **Preis:** ab €299
- **Premium Badge:** ⭐ Unser umfassendster Check
- **CTA-Button:** Jetzt Holistic Advanced buchen →

**Produkt-Auswahl-Block:**
- Empfohlen: **HA** (Holistic Advanced, €299)
- Alternative 1: **HC** (Holistic Core, €149) — "Weniger Detailtiefe, guter Einstieg"
- Alternative 2: **FH oder MH** (je nach Gender) — "Fokus auf Hormone"

**AwarePro Upsell-Block:** *(Standard-Template — hier besonders relevant, da Nutzer schon hohes Interesse an Tiefe signalisiert hat)*

**Insight Block:**
- **Box 1:** "Cortisol ist das Stresshormon, das deinen Antrieb stilllegen kann. Es wird in Standard-Tests nie gemessen – im Holistic Advanced schon."
- **Box 2:** "Q10 und Holo-Transcobalamin (aktives B12) zeigen, ob Energie in deinen Zellen wirklich ankommt – nicht nur ob sie im Blut vorhanden ist."
- **Box 3:** "Homocystein ist ein unterschätzter Risikomarker für Herz, Gehirn und Gefäße – und lässt sich durch gezielte Supplementierung senken."

**Trust-Block + FAQ:** wie FH

---

## GLOBALE ELEMENTE (auf allen Outcome-Seiten)

### Trust-Block (überall gleich)
```
10.000+ Kunden getestet
NPS 72  |  Lab Score 4.78/5  |  App Score 4.53/5
"Endlich Klarheit über meine Werte – die Empfehlungen waren konkret und umsetzbar." – Lea M., Berlin
```

### FAQ-Akkordeon (überall gleich, außer Frage 3)
**Q1:** Wie funktioniert die Blutabnahme?  
**A1:** Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 10 Minuten.

**Q2:** Wann erhalte ich meine Ergebnisse?  
**A2:** In der Regel innerhalb von 48 Stunden nach der Blutabnahme, direkt in der Aware App.

**Q3:** Für wen ist dieser Check geeignet?  
**A3:** [Je nach Outcome angepasst – Alter, Geschlecht, Beschwerden]

### DSGVO-Footer (auf allen Seiten)
Deine Daten werden gemäß DSGVO verarbeitet. [Datenschutzerklärung] · [Impressum]

---

## HINWEISE FÜR DEN AUFBAU IN involve.me

1. **Outcome-Zuweisung:** Nutze "Outcome Quiz" Type, weise jeder Antwort Punkte zu und definiere Punkt-Ranges für jedes Outcome. Alternativ: Logic Jumps für spezifischeres Routing.

2. **Logic Jumps Priorität:**
   - Slide 2 (gender) + Slide 3 (symptoms) setzen erste Tendenz
   - Slide 9 (depth) kann Outcome überschreiben
   - Immer spezifischste Regel gewinnt

3. **Fortschrittsbalken:** In involve.me Settings aktivieren, beginnt ab Slide 2

4. **Loading Screen (Slide 12):** Statement-Screen + Timer 3 Sekunden

5. **E-Mail-Feld:** Pflichtfeld, GDPR-Checkbox ebenfalls Pflicht

6. **Outcome-Pages:** Können in involve.me als "Result Pages" gebaut werden mit vollem Content-Editor. Nutze Buttons, Text-Blöcke, Divider.

7. **UTM/Tracking:** CTA-Buttons auf Outcome-Pages mit UTM-Parametern versehen: `?utm_source=quiz&utm_medium=funnel&utm_campaign=generic-quiz`

8. **[NEU] Produkt-Auswahl-Block:** Entweder als 3-spaltige Bild-Karten mit eingebetteten Links, oder als nebeneinander gestellte Button-Blöcke. involve.me unterstützt Multi-Column Layouts im Result Page Editor.

9. **[NEU] AwarePro-Block:** Als farblich hervorgehobener Textblock mit Icon-Liste. Hintergrundfarbe leicht lila (#F5F3FF). Immer nach dem Produkt-Auswahl-Block, vor dem Insight Block.

10. **[NEU] Grafiken für Slide 4 + Slide 10:** Als PNG/SVG hochladen. Empfohlen: Aware Design Team erstellt die Körper-System-Infografik und die 7/10-Statistik-Karte nach Spec.

---

*Ende der Spezifikation | Quiz B-Version v2 | Aware Health | 2026-04-02*
