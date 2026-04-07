#!/usr/bin/env python3
"""Generate and deploy Aware Health outcome pages for all packages."""

import base64, json, urllib.request, os

TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = 'aware-agent/aware-agent'
OUTPUT_DIR = '/Users/awareagents/AwareAgents/Exchange/Generic Quiz Funnel'

def deploy(filename, html_content):
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    sha = None
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{REPO}/contents/{filename}')
        req.add_header('Authorization', f'token {TOKEN}')
        req.add_header('Accept', 'application/vnd.github.v3+json')
        with urllib.request.urlopen(req) as resp:
            sha = json.loads(resp.read())['sha']
    except:
        pass
    data = {'message': f'Add {filename}', 'content': encoded}
    if sha:
        data['sha'] = sha
    req2 = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/contents/{filename}',
        data=json.dumps(data).encode('utf-8'),
        method='PUT'
    )
    req2.add_header('Authorization', f'token {TOKEN}')
    req2.add_header('Accept', 'application/vnd.github.v3+json')
    req2.add_header('Content-Type', 'application/json')
    with urllib.request.urlopen(req2) as resp:
        result = json.loads(resp.read())
        print(f'Deployed: {filename} → https://aware-agent.github.io/aware-agent/{filename}')


CSS = """
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #fff;
    color: #1A1A1A;
    font-size: 16px;
    line-height: 1.5;
    padding: 0;
  }

  .page { max-width: 560px; margin: 0 auto; padding: 24px 20px 48px; }

  /* ── HERO ── */
  .hero {
    text-align: center;
    padding: 32px 0 24px;
    border-bottom: 1px solid #F0F0F0;
    margin-bottom: 28px;
  }
  .hero-label {
    display: inline-block;
    background: #F5F3FF;
    color: #A480F2;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
  }
  .hero h1 {
    font-size: 26px;
    font-weight: 800;
    line-height: 1.25;
    margin-bottom: 10px;
  }
  .hero p {
    font-size: 15px;
    color: #666;
  }

  /* ── PRIMARY CARD ── */
  .product-card {
    border: 2px solid #A480F2;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 12px;
    position: relative;
    background: #fff;
  }
  .product-card.recommended::before {
    content: "✓ Für dich empfohlen";
    position: absolute;
    top: -13px;
    left: 20px;
    background: #A480F2;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 999px;
  }

  .card-inner { padding-left: 0; }
  .card-title {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 4px;
  }
  .card-tagline {
    font-size: 14px;
    color: #555;
    margin-bottom: 16px;
    line-height: 1.4;
  }
  .card-reasons {
    list-style: none;
    margin-bottom: 16px;
  }
  .card-reasons li {
    font-size: 14px;
    color: #333;
    padding: 4px 0 4px 22px;
    position: relative;
    line-height: 1.4;
  }
  .card-reasons li::before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #486EF6;
    font-weight: 700;
  }
  .marker-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 20px;
  }
  .chip {
    background: #F0EDFF;
    color: #7B5CF0;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 999px;
    white-space: nowrap;
  }
  .chip.blue { background: #EEF2FF; color: #486EF6; }
  .chip.green { background: #EDFDF5; color: #059669; }
  .chip.teal { background: #ECFEFF; color: #0891B2; }
  .chip.orange { background: #FFF7ED; color: #EA580C; }
  .card-price {
    font-size: 15px;
    color: #888;
    margin-bottom: 14px;
  }
  .card-price strong {
    font-size: 20px;
    color: #1A1A1A;
    font-weight: 800;
  }
  .btn-primary {
    display: block;
    width: 100%;
    background: #1A1A1A;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    text-align: center;
    padding: 16px 20px;
    border-radius: 10px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: opacity 0.15s;
  }
  .btn-primary:hover { opacity: 0.85; }

  /* ── PRODUCT SELECTION ── */
  .section-title {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #999;
    margin: 28px 0 14px;
  }
  .product-grid {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 8px;
  }
  .product-alt {
    border: 1.5px solid #E5E5E5;
    border-radius: 12px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.15s;
  }
  .product-alt:hover { border-color: #A480F2; }
  .alt-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .alt-info { flex: 1; }
  .alt-name {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 2px;
  }
  .alt-desc {
    font-size: 13px;
    color: #777;
    line-height: 1.3;
  }
  .alt-price {
    font-size: 14px;
    font-weight: 700;
    color: #1A1A1A;
    white-space: nowrap;
  }

  /* ── AWAREPRO BLOCK ── */
  .pro-block {
    background: #F9F7FF;
    border-radius: 14px;
    padding: 24px 20px;
    margin: 28px 0;
    border: 1.5px solid #E8E2FF;
  }
  .pro-badge {
    display: inline-block;
    font-size: 13px;
    font-weight: 800;
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
    background: linear-gradient(90deg, #FFD660 0%, #FF88BD 21%, #BA83FA 41%, #878BF1 58%, #66A9FF 84%, #5EFFB2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    box-shadow: inset 0 0 0 1.5px rgba(164,128,242,0.25);
  }
  .pro-headline {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 6px;
    line-height: 1.3;
    color: #1A1A1A;
  }
  .pro-headline .rainbow {
    background: linear-gradient(90deg, #FFD660 0%, #FF88BD 21%, #BA83FA 41%, #878BF1 58%, #66A9FF 84%, #5EFFB2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .pro-block .sub {
    font-size: 14px;
    color: #666;
    margin-bottom: 20px;
  }
  .pro-features {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 11px;
    margin-bottom: 22px;
  }
  .pro-features li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 14px;
    line-height: 1.4;
  }
  .pro-features .icon {
    font-size: 18px;
    flex-shrink: 0;
    margin-top: 1px;
  }
  .pro-features .feat-label { font-weight: 700; color: #1A1A1A; }
  .pro-features .feat-desc { color: #666; }
  .btn-pro {
    display: block;
    width: 100%;
    background: #1A1A1A;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    text-align: center;
    padding: 16px 20px;
    border-radius: 10px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    margin-bottom: 10px;
  }
  .pro-fine {
    text-align: center;
    font-size: 12px;
    color: #AAA;
  }

  /* ── INSIGHT BLOCK ── */
  .insight-grid {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 8px;
  }
  .insight-box {
    background: #FAFAFA;
    border-left: 3px solid #486EF6;
    border-radius: 0 10px 10px 0;
    padding: 14px 16px;
    font-size: 14px;
    color: #444;
    line-height: 1.5;
  }
  .insight-box strong {
    display: block;
    font-size: 13px;
    font-weight: 700;
    color: #486EF6;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  /* ── TRUST BLOCK ── */
  .trust-block {
    background: #FAFAFA;
    border-radius: 14px;
    padding: 20px;
    margin: 28px 0;
    text-align: center;
  }
  .trust-stats {
    display: flex;
    justify-content: space-around;
    gap: 8px;
    margin-bottom: 16px;
    flex-wrap: wrap;
  }
  .trust-stat { text-align: center; }
  .trust-stat .num {
    font-size: 20px;
    font-weight: 800;
    color: #1A1A1A;
    display: block;
  }
  .trust-stat .lbl {
    font-size: 12px;
    color: #888;
  }
  .trust-quote {
    font-size: 14px;
    color: #555;
    font-style: italic;
    line-height: 1.5;
    border-top: 1px solid #E8E8E8;
    padding-top: 14px;
  }
  .trust-quote cite {
    display: block;
    font-style: normal;
    font-weight: 600;
    color: #888;
    font-size: 13px;
    margin-top: 6px;
  }

  /* ── FAQ ── */
  .faq { margin: 8px 0 28px; }
  .faq-item {
    border-bottom: 1px solid #F0F0F0;
  }
  .faq-q {
    width: 100%;
    background: none;
    border: none;
    text-align: left;
    font-size: 15px;
    font-weight: 600;
    color: #1A1A1A;
    padding: 16px 0;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
  }
  .faq-q .arrow {
    font-size: 18px;
    color: #A480F2;
    flex-shrink: 0;
    transition: transform 0.2s;
  }
  .faq-a {
    font-size: 14px;
    color: #555;
    line-height: 1.6;
    padding-bottom: 16px;
    display: none;
  }
  .faq-item.open .faq-a { display: block; }
  .faq-item.open .arrow { transform: rotate(180deg); }

  /* ── FOOTER ── */
  .page-footer {
    text-align: center;
    font-size: 12px;
    color: #BBB;
    padding-top: 20px;
    border-top: 1px solid #F0F0F0;
  }
  .page-footer a { color: #AAA; }
"""

AWAREPRO_BLOCK = """
  <!-- AWAREPRO UPSELL -->
  <div class="pro-block">
    <div class="pro-badge">⭐ AwarePro</div>
    <div class="pro-headline">Werde <span class="rainbow">AwarePro</span> Member</div>
    <p class="sub">Langfristig gesund — ab €129/Jahr</p>
    <ul class="pro-features">
      <li>
        <span class="icon">🔬</span>
        <span><span class="feat-label">Bis zu 99 Biomarker</span><br><span class="feat-desc">Zugang zu über 20 personalisierten Panels</span></span>
      </li>
      <li>
        <span class="icon">💰</span>
        <span><span class="feat-label">20% Rabatt</span><br><span class="feat-desc">auf alle Follow-up Checks</span></span>
      </li>
      <li>
        <span class="icon">📈</span>
        <span><span class="feat-label">Verlaufs-Tracking</span><br><span class="feat-desc">Alle Ergebnisse und Trends direkt in der App</span></span>
      </li>
      <li>
        <span class="icon">🧬</span>
        <span><span class="feat-label">Biologisches Alter</span><br><span class="feat-desc">Erfahre, wie alt dein Körper wirklich ist</span></span>
      </li>
      <li>
        <span class="icon">🩺</span>
        <span><span class="feat-label">TeleClinic Zugang</span><br><span class="feat-desc">Arztgespräch direkt über die App (DE)</span></span>
      </li>
    </ul>
    <a href="https://www.aware.app/de/shop/berlin-mitte" class="btn-pro">
      Jetzt AwarePro starten →
    </a>
    <div class="pro-fine">Jederzeit kündbar · Keine Vertragsbindung · Klarna verfügbar</div>
  </div>
"""

TRUST_BLOCK = """
  <!-- TRUST BLOCK -->
  <div class="trust-block">
    <div class="trust-stats">
      <div class="trust-stat">
        <span class="num">10.000+</span>
        <span class="lbl">Kunden getestet</span>
      </div>
      <div class="trust-stat">
        <span class="num">⭐ 4.7</span>
        <span class="lbl">aus 1.425 Bewertungen</span>
      </div>
      <div class="trust-stat">
        <span class="num">650k+</span>
        <span class="lbl">Werte analysiert</span>
      </div>
    </div>
  </div>
"""

def make_chips(biomarkers, colors=None):
    """Generate HTML chip elements for biomarkers."""
    color_classes = ['blue', 'blue', '', 'teal', 'green', 'orange', 'blue', '', 'teal', 'green']
    html = ''
    for i, b in enumerate(biomarkers):
        cls = color_classes[i % len(color_classes)] if colors is None else (colors[i] if i < len(colors) else 'blue')
        cls_attr = f' class="chip {cls}"' if cls else ' class="chip"'
        html += f'        <span{cls_attr}>{b}</span>\n'
    return html

def make_alts(alts):
    """Generate alternative product HTML."""
    dot_colors = ['#A480F2', '#7B5CF0', '#FFBE68', '#486EF6', '#059669']
    html = ''
    for i, (name, sku, price, desc) in enumerate(alts):
        color = dot_colors[i % len(dot_colors)]
        html += f'''    <a href="https://www.aware.app/de/shop/berlin-mitte/{sku}" class="product-alt">
      <div class="alt-dot" style="background:{color};"></div>
      <div class="alt-info">
        <div class="alt-name">{name}</div>
        <div class="alt-desc">{desc}</div>
      </div>
      <div class="alt-price">ab €{price}</div>
    </a>
'''
    return html

def make_insights(insights):
    """Generate insight boxes HTML."""
    labels = ['Wusstest du?', 'Die Verbindung', 'Oft übersehen']
    html = ''
    for i, text in enumerate(insights):
        label = labels[i % len(labels)]
        html += f'''    <div class="insight-box">
      <strong>{label}</strong>
      {text}
    </div>
'''
    return html

def make_faq(faq_items):
    """Generate FAQ HTML."""
    html = ''
    for q, a in faq_items:
        html += f'''    <div class="faq-item">
      <button class="faq-q" onclick="this.parentElement.classList.toggle('open')">
        {q}
        <span class="arrow">⌄</span>
      </button>
      <div class="faq-a">{a}</div>
    </div>
'''
    return html

def build_page(
    title,
    sku,
    hero_h1,
    hero_p,
    card_title,
    card_tagline,
    reasons,
    chips,
    price_oneoff,
    price_pro,
    cta_label,
    alts,
    insights,
    faq_items
):
    chips_html = make_chips(chips) if isinstance(chips[0], str) else make_chips([c[0] for c in chips], [c[1] for c in chips])
    alts_html = make_alts(alts)
    insights_html = make_insights(insights)
    faq_html = make_faq(faq_items)
    reasons_html = ''.join(f'        <li>{r}</li>\n' for r in reasons)

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Deine Empfehlung – Aware</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="page">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-label">Deine persönliche Empfehlung</div>
    <h1>{hero_h1}</h1>
    <p>{hero_p}</p>
  </div>

  <!-- PRIMARY PRODUCT CARD -->
  <div class="product-card recommended">
    <div class="card-inner">
      <div class="card-title">{card_title}</div>
      <div class="card-tagline">{card_tagline}</div>

      <ul class="card-reasons">
{reasons_html}      </ul>

      <div class="marker-chips">
{chips_html}      </div>

      <div class="card-price">ab <strong>€{price_oneoff}</strong> &nbsp;<span style="font-size:13px;color:#999;font-weight:500;">oder €{price_pro} mit <span style="font-weight:700;background:linear-gradient(90deg,#FFD660 0%,#FF88BD 21%,#BA83FA 41%,#878BF1 58%,#66A9FF 84%,#5EFFB2 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">AwarePro</span></span></div>
      <a href="https://www.aware.app/de/shop/berlin-mitte/{sku}" class="btn-primary">
        {cta_label} →
      </a>
    </div>
  </div>

  <!-- PRODUCT SELECTION -->
  <div class="section-title">Oder wähle selbst:</div>
  <div class="product-grid">
{alts_html}  </div>

{AWAREPRO_BLOCK}

  <!-- INSIGHT BLOCK -->
  <div class="section-title">Warum dieser Check?</div>
  <div class="insight-grid">
{insights_html}  </div>

{TRUST_BLOCK}

  <!-- FAQ -->
  <div class="section-title">Häufige Fragen</div>
  <div class="faq">
{faq_html}  </div>

  <!-- FOOTER -->
  <div class="page-footer">
    Deine Daten werden gemäß DSGVO verarbeitet. &nbsp;·&nbsp;
    <a href="https://www.aware.app/de/datenschutz">Datenschutzerklärung</a> &nbsp;·&nbsp;
    <a href="https://www.aware.app/de/impressum">Impressum</a>
  </div>

</div>
</body>
</html>"""


# ─── PACKAGE DEFINITIONS ────────────────────────────────────────────────────

pages = []

# MH – Male Hormones
pages.append(('outcome-mh.html', build_page(
    title='Male Hormones',
    sku='MH',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Male Hormone Check',
    card_tagline='Verstehe deine männlichen Hormone. Klarheit über Energie, Libido und hormonelles Gleichgewicht.',
    reasons=[
        'Du hast Veränderungen in Energie, Libido oder Stimmung beschrieben',
        'Hormonelle Ungleichgewichte bei Männern bleiben häufig unentdeckt — Standard-Bluttests messen Testosteron nicht',
        'Der Male Hormone Check analysiert 9 Schlüsselwerte für dein vollständiges hormonelles Profil',
    ],
    chips=['Testosteron', 'Freies Testosteron', 'DHEA-S', 'FSH', 'LH', 'SHBG', 'Östradiol', 'Prolaktin'],
    price_oneoff=189,
    price_pro=149,
    cta_label='Jetzt Male Hormone Check buchen',
    alts=[
        ('Holistic Core', 'HOC', 149, 'Zusätzlich Organ- & Stoffwechselwerte'),
        ('Metabolism Core', 'MBC', 125, 'Wenn Gewicht, Energie & Blutzucker dich beschäftigen'),
        ('Holistic Advanced', 'HOA', 499, 'Das vollständigste Bild deiner Biologie'),
    ],
    insights=[
        'Ein niedriger Testosteronspiegel betrifft schätzungsweise 1 von 4 Männern über 30 — ohne dass klassische Bluttests beim Hausarzt ihn erkennen.',
        'Östradiol ist kein "weibliches Hormon" — auch Männer brauchen es für Knochen, Stimmung und Libido. Zu viel davon ist ein häufiger Grund für Müdigkeit und Stimmungstiefs.',
        'SHBG bindet freies Testosteron und macht es biologisch inaktiv. Ein erhöhter SHBG-Wert kann trotz "normalem" Testosteron zu echtem Mangel führen.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden nach der Blutabnahme, direkt in der Aware App.'),
        ('Muss ich nüchtern zur Blutabnahme kommen?', 'Für den Male Hormone Check solltest du idealerweise zwischen 7 und 10 Uhr morgens zur Abnahme kommen, da Testosteron morgens am höchsten ist.'),
        ('Für wen ist der Male Hormone Check geeignet?', 'Für Männer, die Veränderungen in Energie, Libido, Stimmung oder Muskelaufbau bemerken — egal ob mit 25 oder 55.'),
    ],
)))

# HOC – Holistic Core
pages.append(('outcome-hoc.html', build_page(
    title='Holistic Core',
    sku='HOC',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Holistic Core',
    card_tagline='Dein umfassender Gesundheitsüberblick. 51 Biomarker für alle wichtigen Körpersysteme.',
    reasons=[
        'Du möchtest einen vollständigen Überblick über deinen Gesundheitszustand',
        'Standard-Checks beim Hausarzt decken nur einen Bruchteil ab — der Holistic Core geht tiefer',
        'Von Schilddrüse über Leber bis Stoffwechsel: alle wichtigen Systeme auf einen Blick',
    ],
    chips=['Blutbild', 'Cholesterin', 'Leber (AST/ALT/GGT)', 'HbA1c', 'Glukose', 'Insulin', 'TSH', 'CRP', 'Kreatinin', 'eGFR'],
    price_oneoff=149,
    price_pro=129,
    cta_label='Jetzt Holistic Core buchen',
    alts=[
        ('Female Hormones', 'FH', 189, 'Wenn Zyklus, PMS oder Stimmung ein Thema sind'),
        ('Holistic Advanced', 'HOA', 499, 'Das vollständigste Bild mit 99 Biomarkern'),
        ('Nutrition Check', 'NUT', 149, 'Wenn Müdigkeit durch Nährstoffmangel entstehen kann'),
    ],
    insights=[
        'Insulinresistenz entwickelt sich oft über Jahre still und unbemerkt — lange bevor ein Arzt Diabetes diagnostiziert. Der Holistic Core misst Insulin und HOMA-Index, die ein Hausarzt selten bestimmt.',
        'Leberwerte wie ALT und GGT reagieren auf Alkohol, Medikamente und Fettleber — oft bereits Jahre vor echten Symptomen. Frühzeitig erkannt, ist das vollständig umkehrbar.',
        'Die Schilddrüse steuert Energie, Gewicht und Stimmung. TSH allein reicht als Screening, und der Holistic Core liefert dir genau das als Teil des umfassenden Bildes.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — bitte mindestens 12 Stunden nüchtern erscheinen, damit Glukose, Triglyzeride und Insulin korrekt gemessen werden.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden nach der Blutabnahme, direkt in der Aware App.'),
        ('Was unterscheidet den Holistic Core vom Holistic Advanced?', 'Der Holistic Advanced umfasst 99 Biomarker — inkl. Vitamine, Omega-3-Fettsäuren, Hormone und erweiterte Stoffwechselmarker. Der Core ist ideal für den regelmäßigen Jahrescheck.'),
    ],
)))

# HOA – Holistic Advanced
pages.append(('outcome-hoa.html', build_page(
    title='Holistic Advanced',
    sku='HOA',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Holistic Advanced',
    card_tagline='Das vollständigste Bild deiner Biologie. 99 Biomarker — von Hormonen bis Fettsäuren.',
    reasons=[
        'Du willst das tiefste mögliche Verständnis deines Körpers',
        '99 Biomarker inkl. Vitamine, Hormone, Fettsäuren, Entzündungsmarker und Organfunktionen',
        'Ideal für Menschen, die ihre Gesundheit ernsthaft optimieren — nicht nur kontrollieren',
    ],
    chips=['Alle Organsysteme', 'Hormone', 'Vitamine B2/B6/B9/B12/D', 'Omega-3-Index', 'Cortisol', 'Homocystein', 'Parathormon', 'Ferritin'],
    price_oneoff=499,
    price_pro=449,
    cta_label='Jetzt Holistic Advanced buchen',
    alts=[
        ('Holistic Core', 'HOC', 149, 'Der umfassende Einstieg mit 51 Biomarkern'),
        ('Metabolism Advanced', 'MBA', 689, 'Wenn Stoffwechsel, Hormone & Vitamine im Fokus stehen'),
        ('Female Hormones', 'FH', 189, 'Wenn hormonelle Balance ein zentrales Thema ist'),
    ],
    insights=[
        'Homocystein ist ein unterschätzter Risikofaktor für Herz-Kreislauf-Erkrankungen und kognitivem Abbau — und wird in den meisten Standard-Checks gar nicht gemessen.',
        'Der Omega-3-Index zeigt, wie gut dein Körper mit entzündungshemmenden Fettsäuren versorgt ist. Unter 8% gilt als erhöhtes kardiovaskuläres Risiko — die meisten Deutschen liegen darunter.',
        'Cortisol und seine Auswirkungen auf Schlaf, Gewicht und Immunsystem bleiben oft unsichtbar. Im Holistic Advanced sehen wir das komplette Bild — inkl. Entzündung, Schilddrüse und Fettsäureprofil.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 15 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — bitte mindestens 12 Stunden nüchtern erscheinen und 24–48 Stunden vor der Abnahme keine Nahrungsergänzungsmittel einnehmen.'),
        ('Wie lange dauert es bis zu den Ergebnissen?', 'Die meisten Werte sind innerhalb von 48 Stunden verfügbar. Für Fettsäuren (Omega-3) kann es bis zu 10 Werktage dauern.'),
        ('Ist das wirklich nötig oder reicht der Holistic Core?', 'Für einen Jahres-Check reicht der Core oft. Für tiefgehende Optimierung, unklare Symptome oder echte Longevity-Arbeit ist der Advanced die richtige Wahl.'),
    ],
)))

# LTH – Long Term Health Check
pages.append(('outcome-lth.html', build_page(
    title='Long Term Health Check',
    sku='LTH',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Long Term Health Check',
    card_tagline='Dein jährlicher Gesundheitscheck. 44 Biomarker für nachhaltige Prävention.',
    reasons=[
        'Regelmäßige Checks sind der beste Schutz — Prävention schlägt jede Behandlung',
        'Mit 44 Biomarkern erfasst der LTH alle wichtigen Organsysteme und Risikomarker',
        'Ideal als jährlicher Basischeck, um Veränderungen früh zu erkennen',
    ],
    chips=['Blutbild', 'Leber (AST/ALT/GGT)', 'Cholesterin', 'HbA1c', 'Glukose', 'TSH', 'Kreatinin', 'Eisen', 'Kalzium'],
    price_oneoff=125,
    price_pro=99,
    cta_label='Jetzt Long Term Health Check buchen',
    alts=[
        ('Holistic Core', 'HOC', 149, 'Mehr Tiefe mit 51 Biomarkern inkl. Insulin & CRP'),
        ('Nutrition Check', 'NUT', 149, 'Wenn Vitamine und Mikronährstoffe fehlen'),
        ('Thyroid Health', 'TH', 49, 'Gezielter Schilddrüsen-Check als Ergänzung'),
    ],
    insights=[
        'Chronische Krankheiten wie Typ-2-Diabetes, Herzerkrankungen oder Niereninsuffizienz entwickeln sich jahrelang ohne Symptome. Jährliche Blutchecks können diese Entwicklung frühzeitig aufdecken.',
        'Der HbA1c-Wert zeigt den durchschnittlichen Blutzucker der letzten 3 Monate — er ist damit viel aussagekräftiger als eine einmalige Glukosemessung.',
        'Eisen und TSH sind häufig die stillen Ursachen für anhaltende Müdigkeit. Beide sind im Long Term Health Check enthalten — und werden beim Hausarzt oft nicht bestimmt.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — bitte mindestens 12 Stunden nüchtern erscheinen, da Glukose und Triglyzeride im Panel enthalten sind.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden nach der Blutabnahme, direkt in der Aware App.'),
        ('Wie oft sollte ich den LTH machen?', 'Einmal pro Jahr ist ideal. Bei bekannten Risikofaktoren oder nach Lifestyle-Änderungen auch häufiger.'),
    ],
)))

# NUT – Nutrition
pages.append(('outcome-nut.html', build_page(
    title='Nutrition',
    sku='NUT',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Nutrition Check',
    card_tagline='Verstehe deine Nährstoffversorgung. Klarheit über Vitamine, Eisen und Energie.',
    reasons=[
        'Du fühlst dich müde oder antriebslos — obwohl du genug schläfst',
        'Nährstoffmängel sind eine der häufigsten, unentdeckten Ursachen für Erschöpfung und Konzentrationsprobleme',
        'Der Nutrition Check analysiert 9 entscheidende Vitamine und Mineralien, die Standard-Tests übersehen',
    ],
    chips=['Ferritin', 'Eisen', 'Transferrin', 'Vitamin B12', 'Vitamin D', 'Vitamin B9', 'Vitamin B2', 'Vitamin B6'],
    price_oneoff=149,
    price_pro=119,
    cta_label='Jetzt Nutrition Check buchen',
    alts=[
        ('Immune Health', 'IMH', 139, 'Wenn du dein Immunsystem unterstützen willst'),
        ('Sleep & Recovery', 'SLP', 139, 'Wenn Schlafprobleme und Erschöpfung im Vordergrund stehen'),
        ('Holistic Core', 'HOC', 149, 'Umfassender Überblick inkl. Organ- und Stoffwechselwerte'),
    ],
    insights=[
        'Über 70% der Deutschen haben einen suboptimalen Vitamin-D-Spiegel — besonders in den Wintermonaten. Vitamin D beeinflusst Immunsystem, Stimmung, Schlaf und Muskelfunktion.',
        'Ferritin ist der bessere Eisenmarker: Es zeigt die Eisenspeicher im Körper und sinkt oft Monate vor dem eigentlichen Mangel. Ein normales Blutbild schließt Eisenmangel nicht aus.',
        'Vitamin B12-Mangel entwickelt sich schleichend und kann zu Konzentrationsproblemen, Taubheitsgefühlen und Stimmungstiefs führen — besonders bei veganer oder vegetarischer Ernährung.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Soll ich meine Supplements vor der Abnahme absetzen?', 'Ja — bitte 24–48 Stunden vor der Blutabnahme keine Nahrungsergänzungsmittel einnehmen, um verfälschte Ergebnisse zu vermeiden.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48–72 Stunden. Einige B-Vitamine können bis zu 4 Werktage benötigen.'),
        ('Für wen ist der Nutrition Check besonders geeignet?', 'Für alle, die sich müde fühlen, sich pflanzlich ernähren, Sport treiben oder einfach sicherstellen wollen, dass ihre Nährstoffversorgung optimal ist.'),
    ],
)))

# SPO – Sport
pages.append(('outcome-spo.html', build_page(
    title='Sport',
    sku='SPO',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Sport Check',
    card_tagline='Optimiere deine Performance. 30 Biomarker für Ausdauer, Erholung und Regeneration.',
    reasons=[
        'Du trainierst regelmäßig, aber kommst nicht weiter oder erholst dich schlecht',
        'Mikronährstoffmängel wie Eisen, Magnesium oder Omega-3 limitieren Performance oft mehr als das Training selbst',
        'Der Sport Check zeigt dir genau, was deinen Körper antreibt — und was ihn bremst',
    ],
    chips=['Blutbild', 'Ferritin', 'Eisen', 'Magnesium', 'Omega-3-Index', 'Vitamin B12', 'CRP (hs)', 'Harnsäure'],
    price_oneoff=125,
    price_pro=99,
    cta_label='Jetzt Sport Check buchen',
    alts=[
        ('Nutrition Check', 'NUT', 149, 'Wenn Vitaminmangel die Ursache sein könnte'),
        ('Metabolism Core', 'MBC', 125, 'Wenn Stoffwechsel und Energie im Vordergrund stehen'),
        ('Holistic Core', 'HOC', 149, 'Umfassender Überblick für alle Körpersysteme'),
    ],
    insights=[
        'Eisenmangel ohne Anämie ist die häufigste unentdeckte Ursache für schlechte Ausdauerleistung. Der Ferritinwert zeigt die Eisenspeicher — selbst wenn das Blutbild noch "normal" aussieht.',
        'Ein Omega-3-Index unter 6% erhöht die Entzündungsneigung und verlangsamt die Regeneration. Ausdauersportler profitieren besonders von einem optimalen EPA/DHA-Status.',
        'Magnesium in Erythrozyten ist genauer als Serum-Magnesium und zeigt den echten intrazellulären Status. Magnesiummangel führt zu Krämpfen, schlechtem Schlaf und eingeschränkter Muskelkontraktion.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Wann sollte ich zur Blutabnahme kommen?', 'Mindestens 12 Stunden nüchtern. Am besten nicht direkt nach intensivem Training — 24 Stunden Abstand ist ideal für akkurate Werte.'),
        ('Wann erhalte ich meine Ergebnisse?', 'Die meisten Werte innerhalb von 48 Stunden. Omega-3 kann bis zu 10 Werktage dauern.'),
        ('Für wen ist der Sport Check geeignet?', 'Für aktive Menschen — egal ob Freizeitläufer, Kraftsportler oder ambitionierte Ausdauersportler — die ihre Leistung datenbasiert verbessern wollen.'),
    ],
)))

# MBC – Metabolism Core
pages.append(('outcome-mbc.html', build_page(
    title='Metabolism Core',
    sku='MBC',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Metabolism Core',
    card_tagline='Verstehe deinen Stoffwechsel. 37 Biomarker für Blutzucker, Leber und Metabolismus.',
    reasons=[
        'Gewichtszunahme, Energieschwankungen oder Heißhunger können Zeichen eines gestörten Stoffwechsels sein',
        'Insulinresistenz und Fettleber entwickeln sich still — lange bevor sie im Arztgespräch auffallen',
        'Der Metabolism Core zeigt dir Blutzucker, Insulin, Leberwerte und Nierenfunktion im Zusammenhang',
    ],
    chips=['HbA1c', 'Glukose', 'Insulin', 'HOMA-Index', 'Cholesterin', 'Leber (AST/ALT/GGT)', 'Kreatinin', 'Ferritin', 'Cystatin C'],
    price_oneoff=125,
    price_pro=99,
    cta_label='Jetzt Metabolism Core buchen',
    alts=[
        ('Metabolism Plus', 'MBP', 279, 'Mehr Tiefe: + Schilddrüse, Vitamin D & Omega-3'),
        ('Long Term Health Check', 'LTH', 125, 'Breiter Jahrescheck für alle Organsysteme'),
        ('Holistic Core', 'HOC', 149, 'Inkl. Immunsystem und vollständiges Blutbild'),
    ],
    insights=[
        'HOMA-Index und Insulinresistenz: Bis zu 40% der Erwachsenen in Deutschland haben eine subklinische Insulinresistenz — die meisten wissen es nicht, weil der Arzt nur Glukose misst, nicht Insulin.',
        'Cystatin C ist ein präziserer Nierenwert als Kreatinin und erkennt eingeschränkte Nierenfunktion früher. Der Metabolism Core ist eines der wenigen Panels, das ihn standardmäßig enthält.',
        'Der FIB-4-Index gibt Auskunft über Leberfibrose — eine oft unterschätzte Folge von Fettleber. Frühzeitig erkannt, ist sie vollständig reversibel.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — mindestens 12 Stunden nüchtern, damit Glukose, Insulin und HOMA-Index korrekt gemessen werden.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden in der Aware App.'),
        ('Was unterscheidet Metabolism Core von Metabolism Plus?', 'Der Plus-Plan ergänzt Schilddrüse (TSH), Vitamin D, Vitamin B12, Omega-3 und Cortisol — für ein noch vollständigeres Stoffwechselbild.'),
    ],
)))

# MBP – Metabolism Plus
pages.append(('outcome-mbp.html', build_page(
    title='Metabolism Plus',
    sku='MBP',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Metabolism Plus',
    card_tagline='Erweitertes Stoffwechselprofil. 48 Biomarker inkl. Schilddrüse, Cortisol und Omega-3.',
    reasons=[
        'Dein Stoffwechsel, Energiehaushalt und deine Hormonbalance hängen eng zusammen',
        'Cortisol, Schilddrüse und Vitamin D beeinflussen Gewicht, Stimmung und Schlaf — und werden selten gemeinsam gemessen',
        'Der Metabolism Plus gibt dir ein vollständiges Bild mit 48 Biomarkern',
    ],
    chips=['HbA1c', 'Insulin', 'HOMA-Index', 'TSH', 'Cortisol', 'Vitamin D', 'Omega-3-Index', 'ApoB', 'Zink', 'CRP (hs)'],
    price_oneoff=279,
    price_pro=219,
    cta_label='Jetzt Metabolism Plus buchen',
    alts=[
        ('Metabolism Core', 'MBC', 125, 'Einstieg ohne Hormone und Vitamine'),
        ('Metabolism Advanced', 'MBA', 689, 'Das vollständigste Stoffwechselprofil'),
        ('Holistic Advanced', 'HOA', 499, 'Alle 99 Biomarker inklusive Fettsäureprofil'),
    ],
    insights=[
        'Cortisol ist der Stresshormonspiegel — und beeinflusst direkt, wie dein Körper Fett speichert, Muskeln abbaut und schläft. Dauerhaft erhöhtes Cortisol bleibt meist unentdeckt.',
        'Apolipoprotein B (ApoB) ist präziser als LDL-Cholesterin als Herzrisikofaktor. Viele Menschen mit "normalem" LDL haben ein erhöhtes ApoB — und damit ein unterschätztes Risiko.',
        'Zink beeinflusst Insulinsensitivität, Immunfunktion und Hormonstoffwechsel. Mangel ist häufig bei Menschen mit hohem Stresslevel oder einseitiger Ernährung.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — mindestens 12 Stunden nüchtern und 24–48 Stunden ohne Nahrungsergänzungsmittel.'),
        ('Wann erhalte ich meine Ergebnisse?', 'Die meisten Werte innerhalb von 48 Stunden. Omega-3 kann bis zu 10 Werktage dauern.'),
        ('Was ist der Unterschied zum Metabolism Advanced?', 'Der Advanced enthält zusätzlich ein vollständiges Hormonsystem (Testosteron, Östradiol, DHEA-S), Selen, Holotranscobalamin und Adipokine (Leptin/Adiponectin).'),
    ],
)))

# MBA – Metabolism Advanced
pages.append(('outcome-mba.html', build_page(
    title='Metabolism Advanced',
    sku='MBA',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Metabolism Advanced',
    card_tagline='Das tiefste Stoffwechselprofil. 68 Biomarker: Hormone, Vitamine, Fettsäuren und mehr.',
    reasons=[
        'Du willst die tiefsten Einblicke in deinen Stoffwechsel — von Insulin bis Leptin',
        '68 Biomarker kombinieren Stoffwechsel, Hormone, Vitamine, Fettsäuren und Entzündung',
        'Ideal für Menschen, die ihre Gesundheit mit Datenpräzision langfristig optimieren',
    ],
    chips=['HOMA-Index', 'Testosteron', 'Östradiol', 'DHEA-S', 'Cortisol', 'Leptin', 'Adiponectin', 'Omega-3-Index', 'Selen', 'Homocystein (via HOA)'],
    price_oneoff=689,
    price_pro=549,
    cta_label='Jetzt Metabolism Advanced buchen',
    alts=[
        ('Metabolism Plus', 'MBP', 279, 'Etwas schlanker, aber sehr ähnliches Profil'),
        ('Holistic Advanced', 'HOA', 499, 'Alle 99 Biomarker inkl. erweitertes Fettsäureprofil'),
        ('Male Hormones', 'MH', 189, 'Wenn Hormone allein im Fokus stehen'),
    ],
    insights=[
        'Leptin und Adiponectin sind Adipokine — Hormone des Fettgewebes. Ihr Verhältnis sagt mehr über Entzündungsneigung und Insulinresistenz aus als jeder einzelne Standardwert.',
        'Selen schützt die Schilddrüse und ist essenziell für die Konversion von T4 zu T3. Mangel ist in Deutschland verbreitet und verursacht Erschöpfung, die sich nicht erklären lässt.',
        'Der Metabolism Advanced misst nicht nur Testosteron, sondern auch DHEA-S und Östradiol — das vollständige hormonelle Bild, das zeigt, wie dein Körper Energie und Körperzusammensetzung reguliert.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 15 Minuten.'),
        ('Muss ich nüchtern kommen?', 'Ja — mindestens 12 Stunden nüchtern und 24–48 Stunden ohne Nahrungsergänzungsmittel. Testosteron-Abnahme idealerweise zwischen 7 und 10 Uhr morgens.'),
        ('Wann erhalte ich meine Ergebnisse?', 'Die meisten Werte innerhalb von 48 Stunden. Omega-3 kann bis zu 10 Werktage dauern.'),
        ('Für wen ist das gedacht?', 'Für alle, die Gesundheitsoptimierung ernsthaft betreiben — ob Biohacker, Sportler oder Menschen mit komplexen Symptomen, für die normale Checks keine Antworten liefern.'),
    ],
)))

# IMH – Immune Health
pages.append(('outcome-imh.html', build_page(
    title='Immune Health',
    sku='IMH',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Immune Health Check',
    card_tagline='Verstehe deine Immunabwehr. 24 Biomarker für Immunsystem, Entzündung und Abwehrkraft.',
    reasons=[
        'Du bist häufig krank oder brauchst ungewöhnlich lange, um dich zu erholen',
        'Vitamin D, Zink und Selen sind die häufigsten Mikronährstoffmängel mit direktem Einfluss auf die Immunfunktion',
        'Der Immune Health Check zeigt dir, wo deine Immunabwehr stark ist — und wo sie Unterstützung braucht',
    ],
    chips=['Leukozyten', 'Lymphozyten', 'Neutrophile', 'IgG', 'Vitamin D', 'CRP (hs)', 'Zink', 'Selen', 'Holotranscobalamin'],
    price_oneoff=139,
    price_pro=109,
    cta_label='Jetzt Immune Health Check buchen',
    alts=[
        ('Nutrition Check', 'NUT', 149, 'Wenn Nährstoffmangel eine Rolle spielen könnte'),
        ('Sleep & Recovery', 'SLP', 139, 'Schlaf ist die Basis jeder Immunfunktion'),
        ('Holistic Core', 'HOC', 149, 'Umfassender Überblick für alle Körpersysteme'),
    ],
    insights=[
        'Vitamin D ist kein Vitamin, sondern ein Hormon — und reguliert über 200 immunrelevante Gene. Unter 30 ng/ml gilt als Mangel; über 50 ng/ml ist optimal. Die meisten Deutschen liegen zu niedrig.',
        'Selen ist essenziell für die Aktivität natürlicher Killerzellen und den Schutz vor oxidativem Stress. Deutsche Böden sind arm an Selen — ein stiller Mangel ist in Europa sehr verbreitet.',
        'IgG ist der häufigste Antikörpertyp und zeigt die langfristige Immunaktivität. Zusammen mit dem Differenzialblutbild entsteht ein vollständiges Bild der Immunantwort.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Soll ich meine Supplements vorher absetzen?', 'Ja — bitte 24–48 Stunden vor der Abnahme keine Vitamin-D-, Zink- oder Selenergänzungen einnehmen.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48–72 Stunden. Selen und Zink können bis zu 4 Werktage dauern.'),
        ('Was sagt mir das Ergebnis?', 'Die Aware App zeigt dir jeden Wert mit Einordnung, Referenzbereich und konkreten Handlungsempfehlungen.'),
    ],
)))

# SLP – Sleep & Recovery
pages.append(('outcome-slp.html', build_page(
    title='Sleep & Recovery',
    sku='SLP',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Sleep & Recovery Check',
    card_tagline='Finde die biologischen Ursachen für schlechten Schlaf und fehlende Erholung.',
    reasons=[
        'Du schläfst ausreichend, wachst aber trotzdem erschöpft auf',
        'Schilddrüsenhormone, Ferritin und Vitamin D sind häufig die stillen Schlafräuber — und werden selten getestet',
        'Der Sleep & Recovery Check deckt die häufigsten biologischen Ursachen für schlechten Schlaf auf',
    ],
    chips=['TSH', 'fT4', 'fT3', 'Ferritin', 'Vitamin D', 'HbA1c', 'CRP (hs)'],
    price_oneoff=139,
    price_pro=109,
    cta_label='Jetzt Sleep & Recovery Check buchen',
    alts=[
        ('Thyroid Health', 'TH', 49, 'Gezielter Schilddrüsen-Check als Ergänzung'),
        ('Nutrition Check', 'NUT', 149, 'Wenn Nährstoffmangel hinter der Erschöpfung steckt'),
        ('Holistic Core', 'HOC', 149, 'Umfassender Überblick für alle Organsysteme'),
    ],
    insights=[
        'Die Schilddrüse reguliert nicht nur den Stoffwechsel, sondern auch den Schlaf-Wach-Rhythmus. Eine leicht unterfunktive Schilddrüse (Hypothyreose) führt zu Schlafstörungen, Kältegefühl und Erschöpfung — selbst wenn der TSH noch "im Normbereich" liegt.',
        'Ferritin unter 30 ng/ml korreliert stark mit Restless-Legs-Syndrom und unterbrochenem Schlaf — auch wenn kein klassischer Eisenmangel vorliegt. Die meisten Ärzte testen Ferritin erst auf spezifische Anfrage.',
        'Chronische Entzündung (messbares CRP) stört den Schlafrhythmus direkt. Menschen mit erhöhtem hs-CRP schlafen weniger tief und erholen sich langsamer — ein Teufelskreis aus Schlafmangel und Entzündung.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich etwas vorbereiten?', 'Bitte 24–48 Stunden vorher keine Vitamin-D-Ergänzungen einnehmen.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden in der Aware App.'),
        ('Was ist wenn die Werte normal sind?', 'Auch das ist eine wichtige Information! Es bedeutet, dass biologische Ursachen für deinen Schlaf ausgeschlossen wurden und du andere Ansätze priorisieren kannst.'),
    ],
)))

# SKH – Skin Health
pages.append(('outcome-skh.html', build_page(
    title='Skin Health',
    sku='SKH',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Skin Health Check',
    card_tagline='Verstehe die biologischen Ursachen für dein Hautbild. 33 Biomarker für gesunde Haut von innen.',
    reasons=[
        'Unreine Haut, Akne, Haarausfall oder trockene Haut haben oft biologische Ursachen',
        'Omega-3, Zink, Vitamin D und Ferritin beeinflussen Hautzustand direkt — und werden selten zusammen gemessen',
        'Der Skin Health Check analysiert alle relevanten Biomarker für Haut, Haare und Nägel',
    ],
    chips=['Omega-3-Index', 'Zink', 'Ferritin', 'Vitamin D', 'TSH', 'CRP (hs)', 'HbA1c', 'Vitamin B12', 'Cholesterin'],
    price_oneoff=190,
    price_pro=150,
    cta_label='Jetzt Skin Health Check buchen',
    alts=[
        ('Nutrition Check', 'NUT', 149, 'Fokus auf Vitamine und Nährstoffversorgung'),
        ('Immune Health', 'IMH', 139, 'Wenn Entzündung und Immunreaktion im Vordergrund stehen'),
        ('Holistic Core', 'HOC', 149, 'Umfassender Überblick für alle Körpersysteme'),
    ],
    insights=[
        'Omega-3-Fettsäuren regulieren die Talgproduktion und Hautentzündung. Ein niedriger Omega-3-Index korreliert mit trockener, entzündlicher Haut — und ist bei den meisten Deutschen niedrig.',
        'Zink ist essenziell für die Wundheilung, Kollagensynthese und das Immungleichgewicht der Haut. Zinkmangel zeigt sich in Akne, Haarausfall und langsamer Hautregeneration.',
        'Die Schilddrüse beeinflusst die Hautfeuchtigkeit und Haarwachstum. Selbst eine leichte Hypothyreose kann zu trockener Haut, Haarausfall und brüchigen Nägeln führen.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Soll ich meine Supplements vorher absetzen?', 'Ja — bitte 24–48 Stunden vor der Abnahme keine Nahrungsergänzungen einnehmen.'),
        ('Wie lange dauern die Ergebnisse?', 'Die meisten Werte innerhalb von 48 Stunden. Omega-3 und Zink können bis zu 10 bzw. 4 Werktage dauern.'),
        ('Ist das auch für Haarausfall relevant?', 'Ja — Ferritin, Zink, TSH und Vitamin D sind die häufigsten messbaren Ursachen für diffusen Haarausfall und sind alle im Check enthalten.'),
    ],
)))

# AGE – Biological Age
pages.append(('outcome-age.html', build_page(
    title='Biological Age',
    sku='AGE',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Biological Age Check',
    card_tagline='Erfahre, wie alt dein Körper wirklich ist. 28 Biomarker für deinen biologischen Alterungsscore.',
    reasons=[
        'Dein biologisches Alter kann bis zu 20 Jahre von deinem Geburtsjahr abweichen',
        '28 Biomarker aus Blutbild, Leber, Niere, Entzündung und Stoffwechsel berechnen deinen Aging-Score',
        'Verstehe, welche Bereiche deinen Körper schneller oder langsamer altern lassen',
    ],
    chips=['RDW', 'Albumin', 'CRP (hs)', 'Glukose', 'Leber (AST/ALT/GGT)', 'Alkalische Phosphatase', 'Kreatinin', 'Blutbild'],
    price_oneoff=49,
    price_pro=39,
    cta_label='Jetzt Biological Age Check buchen',
    alts=[
        ('Long Term Health Check', 'LTH', 125, 'Umfassenderer Jahrescheck für alle Systeme'),
        ('Holistic Core', 'HOC', 149, 'Mehr Tiefe inkl. Insulin, Schilddrüse & mehr'),
        ('Thyroid Health', 'TH', 49, 'Als günztige Ergänzung zum Aging-Check'),
    ],
    insights=[
        'Der RDW (Erythrozytenverteilungsbreite) ist ein unterschätzter Aging-Marker: Er zeigt Variabilität in der Blutzellenproduktion und ist eines der stärksten Prädiktoren für biologisches Alter.',
        'Albumin ist das wichtigste Transportprotein und sinkt im Alter — bei schlechter Ernährung, chronischer Entzündung oder eingeschränkter Leberfunktion. Ein niedriger Albuminspiegel korreliert mit beschleunigtem Altern.',
        'Biologisches Alter ist keine fixe Zahl — es ist messbar und veränderbar. Menschen, die regelmäßig ihren Aging-Score tracken, können durch gezielte Interventionen messbar jünger werden.',
    ],
    faq_items=[
        ('Wie wird das biologische Alter berechnet?', 'Der Aware Algorithmus vergleicht deine 28 Biomarker mit altersoptimierten Referenzpopulationen und berechnet daraus deinen individuellen Alterungsindex.'),
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden in der Aware App.'),
        ('Wie oft sollte ich den Check wiederholen?', 'Halbjährlich oder jährlich — um zu sehen, ob Lifestyle-Änderungen dein biologisches Alter positiv beeinflussen.'),
    ],
)))

# TH – Thyroid Health
pages.append(('outcome-th.html', build_page(
    title='Thyroid Health',
    sku='TH',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Thyroid Health Check',
    card_tagline='Verstehe deine Schilddrüse vollständig. TSH, fT3 und fT4 — das komplette Bild.',
    reasons=[
        'Müdigkeit, Gewichtsprobleme oder Stimmungsschwankungen ohne klare Ursache',
        'TSH allein reicht nicht — fT3 und fT4 zeigen, ob die Schilddrüse wirklich optimal funktioniert',
        'Der Thyroid Health Check liefert das komplette Schilddrüsenprofil in einem günstigen Check',
    ],
    chips=['TSH', 'Freies Thyroxin (fT4)', 'Freies Trijodthyronin (fT3)'],
    price_oneoff=49,
    price_pro=39,
    cta_label='Jetzt Thyroid Health Check buchen',
    alts=[
        ('Sleep & Recovery', 'SLP', 139, 'Die Schilddrüse beeinflusst auch den Schlaf'),
        ('Long Term Health Check', 'LTH', 125, 'Umfassender Jahrescheck inkl. TSH'),
        ('Holistic Core', 'HOC', 149, 'Vollständiger Check für alle Organsysteme'),
    ],
    insights=[
        'TSH allein reicht nicht aus: Viele Menschen mit Hashimoto oder subklinischer Hypothyreose haben einen "normalen" TSH, aber erniedrigte fT3-Werte. Der Grund: Die Konversion von T4 zu T3 kann gestört sein.',
        'Die Schilddrüse steuert den gesamten Grundstoffwechsel. Eine leicht unterfunktive Schilddrüse kann Gewichtszunahme, Erschöpfung, Kältegefühl, Haarausfall und Stimmungstiefs verursachen — ohne dass ein Arzt etwas findet.',
        'Hashimoto ist die häufigste Autoimmunerkrankung in Deutschland — schätzungsweise 10% der Frauen sind betroffen. Der frühe Check schützt vor jahrelanger Odyssee.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte. Venöse Blutabnahme, dauert ca. 10 Minuten.'),
        ('Muss ich nüchtern sein?', 'Nicht zwingend — aber morgens testen ist ideal, da TSH morgens am stabilsten ist.'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden in der Aware App.'),
        ('Was wenn meine Werte "im Normbereich" sind aber ich Symptome habe?', 'Normalbereich ist nicht das Gleiche wie optimal. Die Aware App zeigt dir nicht nur ob ein Wert im Referenzbereich liegt, sondern auch wo er im optimalen Bereich wäre.'),
    ],
)))

# VITD – Vitamin D
pages.append(('outcome-vitd.html', build_page(
    title='Vitamin D',
    sku='VITD',
    hero_h1='Dein Körper zeigt klare Signale — hier ist was wir empfehlen.',
    hero_p='Basierend auf deinen Angaben haben wir den passenden Check für dich identifiziert.',
    card_title='Vitamin D Check',
    card_tagline='Dein Vitamin-D-Status auf einen Blick. Schnell, günstig, aussagekräftig.',
    reasons=[
        'Über 60% der Deutschen haben im Herbst und Winter einen zu niedrigen Vitamin-D-Spiegel',
        'Vitamin D beeinflusst Immunsystem, Knochen, Stimmung, Schlaf und Muskelkraft',
        'Ein einfacher Test gibt dir schnell Klarheit — und zeigt ob und wie viel du supplementieren solltest',
    ],
    chips=['Vitamin D (25-OH)'],
    price_oneoff=35,
    price_pro=25,
    cta_label='Jetzt Vitamin D Check buchen',
    alts=[
        ('Nutrition Check', 'NUT', 149, 'Vitamin D + alle weiteren Vitamine und Mineralien'),
        ('Immune Health', 'IMH', 139, 'Wenn das Immunsystem umfassend analysiert werden soll'),
        ('Sleep & Recovery', 'SLP', 139, 'Vitamin D + Schilddrüse + Ferritin für besseren Schlaf'),
    ],
    insights=[
        'Vitamin D ist streng genommen kein Vitamin, sondern ein Hormon — es beeinflusst über 200 Gene im Körper, darunter fast alle Immunprozesse, die Kalziumregulation und die Stimmung.',
        'Ein Wert über 50 ng/ml gilt als optimal — die meisten Deutschen liegen zwischen 20 und 30 ng/ml. Ohne Test weißt du nicht, ob deine Supplementierung ausreicht oder ob du unterdosierst.',
        'Besonders risikoreich: Menschen die viel drinnen sind, dunkle Haut haben oder im Norden leben. Aber auch im Sommer erreichen viele nicht den optimalen Spiegel.',
    ],
    faq_items=[
        ('Wie funktioniert die Blutabnahme?', 'Keine Terminbuchung nötig. Besuche einfach einen unserer Standorte (Berlin Mitte, dm-Märkte, Partnerstandorte bundesweit). Venöse Blutabnahme, dauert ca. 5 Minuten.'),
        ('Soll ich mein Vitamin D vorher absetzen?', 'Ja — bitte 24–48 Stunden vor der Abnahme kein Vitamin D einnehmen, um deinen tatsächlichen Status zu messen (nicht den unmittelbar supplementierten).'),
        ('Wann erhalte ich meine Ergebnisse?', 'In der Regel innerhalb von 48 Stunden in der Aware App.'),
        ('Wie viel Vitamin D sollte ich einnehmen?', 'Das hängt von deinem aktuellen Spiegel ab — genau deshalb lohnt sich der Test. Die App gibt dir personalisierte Empfehlungen basierend auf deinen Werten.'),
    ],
)))


# ─── GENERATE & DEPLOY ──────────────────────────────────────────────────────

print(f"Generating {len(pages)} HTML files...\n")

for filename, html in pages:
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved: {filepath}")

print(f"\nDeploying to GitHub Pages...\n")

for filename, html in pages:
    deploy(filename, html)

print("\n✅ All done!")
print("\nDeployed URLs:")
for filename, _ in pages:
    print(f"  - {filename} → https://aware-agent.github.io/aware-agent/{filename}")
