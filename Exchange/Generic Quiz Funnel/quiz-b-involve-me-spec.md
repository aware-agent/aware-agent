# involve.me Spec: Aware Quiz Funnel — B-Version
**Sprache:** DE  
**Typ:** Outcome Quiz + Lead-Gen  
**Ziel:** E-Mail-Capture → Produktempfehlung → Ecommerce-Conversion  
**Slides:** 12 Quiz-Slides + 7 Outcome-Pages  
**Stand:** 2026-04-01

---

## Settings (involve.me Global)
- Type: **Outcome Quiz**
- Progress Bar: **Yes** (ab Slide 2, Farbe: #A18AFF)
- Language: DE
- Email Notifications: ja
- GDPR: Opt-in Checkbox on E-Mail slide

---

## QUIZ-SLIDES

---

### Slide 1 – Opener / Welcome

**Type:** Welcome Screen  
**Headline:** Dein Körper sendet Signale. Weißt du, was er meint?  
**Body:**  
In nur 2 Minuten findest du heraus, welche Blutwerte bei dir Aufschluss geben – und was dahintersteckt.

**Social Proof (Text unter Body):**  
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

### Slide 4 – EDU: Körper-System-Map (Infografik)

**Type:** Content / Statement Screen  
**Keine Frage, keine Eingabe – reiner Edu-Content**

**Headline:** So hängt das zusammen.

**Body-Text:**  
Dein Körper ist ein vernetztes System. Symptome wie Müdigkeit oder Stimmungsschwankungen entstehen selten aus einer einzigen Ursache – sie sind oft Signale aus mehreren biologischen Bereichen gleichzeitig.

**Infografik-Beschreibung für involve.me (als Bild hochladen oder als Text darstellen):**  
> Erstelle eine einfache Grafik mit 5 Kreisen: **Hormone · Stoffwechsel · Energie · Immunsystem · Herz/Gefäße**  
> Verbinde die Kreise mit gestrichelten Linien zu den häufigsten Symptomen.  
> Stil: Aware-Brand, Farben aus Health Zone Palette.  
> Alternativ: Einfache Textdarstellung in 2 Spalten mit Checkmarks.

**Inhalt alternativ als Text (wenn Bild nicht möglich):**

| Körpersystem | Typische Signale |
|---|---|
| 🔵 Hormone | PMS, Stimmung, Zyklusprobleme, Libido |
| 🟣 Stoffwechsel | Gewicht, Energie, Blutzucker |
| 🟢 Energie | Müdigkeit, Schlaf, Belastbarkeit |
| 🔷 Immunsystem | Infektanfälligkeit, Entzündungen |
| 🩷 Herz/Gefäße | Stress, Blutdruck, Ausdauer |

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

**Statement-Box (groß, zentriert):**  
> **7 von 10 Menschen** mit ähnlichen Symptomen  
> finden im Blutbild eine **biologische Ursache** –  
> die ohne Test unsichtbar geblieben wäre.

**Sub-Text:**  
Deine Angaben helfen uns jetzt, die relevantesten Systeme für dich zu identifizieren.

**Button:** Meine Analyse freischalten →

---

### Slide 11 – E-Mail-Capture (Lead Gen)

**Type:** Lead Form  
**Headline:** Dein personalisierter Gesundheits-Report ist bereit.

**Sub-Headline:**  
Gib deine E-Mail-Adresse an, um deine Empfehlung zu sehen – inklusive erklärender Einblicke in deine Biologie.

**Preview-Teaser (visuell als Karte darstellen, "verschwommen"):**  
> 🔒 Deine Empfehlung: [Name des Panels]  
> ✓ Die biologischen Ursachen deiner Symptome  
> ✓ Konkrete Handlungsschritte  
> ✓ Dein persönlicher Biomarker-Fahrplan

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

**Inhalt:**  
🔬 Wir ordnen deine Angaben jetzt zu…

**Animierter Fortschrittsbalken** (involve.me Timer nutzen)

**Texte die durchlaufen:**  
- "Symptome werden biologischen Systemen zugeordnet…"
- "Relevante Biomarker werden identifiziert…"
- "Deine persönliche Empfehlung wird erstellt…"

*(In involve.me: als Statement-Screen mit Timer 3s, dann Jump zu Outcome)*

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

**Hinweis für involve.me:** Logic Jumps von Slide 9 (depth) und Slide 3 (symptoms) + Slide 2 (gender) setzen. Reihenfolge: spezifischste Regel zuerst.

---

## OUTCOME-SEITEN

### ⚙️ Struktur jeder Outcome-Seite

Jede Outcome-Seite folgt diesem Aufbau:
1. **Hero** – Personalisierter Header
2. **Primary Product Card** – Empfohlenes Paket
3. **Insight Block** – Warum dieses Paket / Edu-Content
4. **Trust-Block** – Social Proof
5. **Weitere Pakete** – 2–3 Alternativen (Package Clustering)
6. **FAQ** – 3 aufklappbare Fragen

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

**Weitere Pakete:**
- Holistic Core – "Wenn du zusätzlich Organ- und Stoffwechsel-Werte im Blick behalten willst" → https://www.aware.app/de/shop/berlin-mitte/HC
- Holistic Advanced – "Für ein vollständiges Bild inkl. Schilddrüse, Cortisol und Entzündungsmarker" → https://www.aware.app/de/shop/berlin-mitte/HA
- Nutrition Check – "Wenn Müdigkeit auch durch Nährstoffmangel entstehen kann" → https://www.aware.app/de/shop/berlin-mitte/NUT

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

**Insight Block:**
- **Box 1:** "Ein 'normaler' Gesamt-Testosteronwert sagt oft nichts aus – wenn das Hormon gebunden und inaktiv ist. Freies Testosteron und SHBG zeigen erst das wahre Bild."
- **Box 2:** "Zu viel Östrogen bei Männern – durch Stress, Körperfett oder Ernährung – bremst Testosteron aus. Prolaktin sabotiert zusätzlich Libido und Antrieb."

**Trust-Block:** wie FH

**Weitere Pakete:**
- Holistic Core → HC
- Sports Check → SP
- Holistic Advanced → HA

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

**Insight Block:**
- **Box 1:** "Eine Fettleber oder Nierenschwäche spürt man oft erst, wenn es ernst wird. Frühzeitig erkennen, bevor Symptome entstehen."
- **Box 2:** "HbA1c misst den Langzeit-Blutzucker der letzten 3 Monate – der wichtigste Marker zur Diabetes-Prävention. Standard-Bluttests zeigen nur eine Momentaufnahme."

**Weitere Pakete:** HC, HA, FH oder MH je nach Gender

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

**Insight Block:**
- **Box 1:** "Eisenmangel ist der häufigste Grund für Leistungsabfall – auch bei Männern. Ferritin zeigt deinen Speicher, nicht nur das Eisen im Blut."
- **Box 2:** "Magnesium im Serum zu messen ist ungenau. Wir messen es in den Erythrozyten – das ist der 'wahre' Muskelwert."

**Weitere Pakete:** HC, NUT, MH

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

**Insight Block:**
- **Box 1:** "Fast jeder Mensch in Mitteleuropa hat einen Vitamin-D-Mangel – besonders im Winter. Das drückt auf Stimmung, Immunsystem und Schlaf."
- **Box 2:** "Eisenmangel erkennt man erst zuverlässig über Ferritin – nicht über einfaches Eisen im Blut. Oft der unentdeckte Grund für anhaltende Müdigkeit."

**Weitere Pakete:** HC, LTH, SP

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

**Insight Block:**
- **Box 1:** "ApoB ist der Goldstandard für Herzgesundheit – präziser als LDL-Cholesterin. Standard-Checks messen ihn fast nie."
- **Box 2:** "Nüchtern-Insulin und HOMA-Index zeigen Insulinresistenz, lange bevor sich der Blutzucker verändert – der Schlüssel zur Prävention."

**Weitere Pakete:** HA, LTH, FH oder MH je nach Gender

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

**Insight Block:**
- **Box 1:** "Cortisol ist das Stresshormon, das deinen Antrieb stilllegen kann. Es wird in Standard-Tests nie gemessen – im Holistic Advanced schon."
- **Box 2:** "Q10 und Holo-Transcobalamin (aktives B12) zeigen, ob Energie in deinen Zellen wirklich ankommt – nicht nur ob sie im Blut vorhanden ist."
- **Box 3:** "Homocystein ist ein unterschätzter Risikomarker für Herz, Gehirn und Gefäße – und lässt sich durch gezielte Supplementierung senken."

**Weitere Pakete:** HC (als "Einstieg"), FH oder MH je nach Gender

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

---

*Ende der Spezifikation | Quiz B-Version | Aware Health | 2026-04-01*
