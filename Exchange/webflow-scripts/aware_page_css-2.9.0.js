document.head.insertAdjacentHTML('beforeend','<style>' + `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500&display=swap');

.aw-page *{box-sizing:border-box;margin:0;padding:0;}
.aw-page a{text-decoration:none;color:inherit;}
.aw-page img{display:block;}

/* Container */
.aw-container{max-width:1100px;margin:0 auto;padding:0 32px;}

/* ── 1. Announcement ── */
.aw-announce{background:#040404;color:white;padding:11px;text-align:center;font-family:'Inter',sans-serif;font-size:0.8rem;font-weight:400;letter-spacing:0.02em;}
.aw-announce a{color:white;text-decoration:underline;}

/* ── 2. Nav ── */
.aw-nav{position:sticky;top:0;z-index:1000;background:white;border-bottom:1px solid #CDC9DD;}
.aw-nav-inner{max-width:1100px;margin:0 auto;padding:0 32px;height:68px;display:flex;align-items:center;justify-content:space-between;}
.aw-nav-logo img{height:28px;}
.aw-nav-links{display:flex;gap:32px;font-family:'Inter',sans-serif;font-size:0.875rem;font-weight:400;color:#040404;}
.aw-nav-links a{color:#040404;transition:opacity .2s;}
.aw-nav-links a:hover{opacity:.5;}
.aw-nav-right{display:flex;align-items:center;gap:20px;}
.aw-lang{font-family:'Inter',sans-serif;font-size:0.875rem;color:#605E64;cursor:pointer;}

/* CTA pills */
.aw-cta-pill{display:inline-flex;align-items:center;justify-content:center;padding:14px 28px;border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.85rem;font-weight:500;letter-spacing:0.04em;cursor:pointer;transition:opacity .2s;white-space:nowrap;}
.aw-cta-pill:hover{opacity:.85;}
.aw-cta-dark{background:#040404;color:white;}
.aw-cta-white{background:white;color:#040404;}
.aw-cta-ghost{background:transparent;border:1px solid rgba(255,255,255,0.5);color:white;}
.aw-cta-outline{background:transparent;border:1px solid #040404;color:#040404;}

/* ── 3. Hero ── */
.aw-hero{min-height:100vh;background:#040404;position:relative;display:flex;align-items:center;overflow:hidden;}.aw-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:220px;background:linear-gradient(to bottom,transparent 0%,#040404 100%);z-index:1;pointer-events:none;}.aw-hero-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;pointer-events:none;}
.aw-hero::before{content:'';position:absolute;inset:0;background:linear-gradient(to right,rgba(4,4,4,.30) 0%,rgba(4,4,4,.15) 55%,rgba(4,4,4,.05) 100%);z-index:0;}
.aw-hero .aw-container{position:relative;z-index:1;}
.aw-hero-inner{max-width:620px;padding:120px 0;}
.aw-eyebrow{font-family:'Inter',sans-serif;font-size:0.65rem;font-weight:500;letter-spacing:0.15em;text-transform:uppercase;display:block;margin-bottom:24px;}
.aw-eyebrow-white{color:rgba(255,255,255,.6);}
.aw-eyebrow-muted{color:#605E64;}.aw-social-proof .aw-eyebrow-muted,.aw-testimonials .aw-eyebrow-muted{color:rgba(255,255,255,0.55);}
.aw-hero-h1{font-family:'Playfair Display',serif;font-size:clamp(2.8rem,5vw,4.5rem);font-weight:400;color:white;line-height:1.05;margin-bottom:24px;}
.aw-hero-h1 em{font-style:italic;}
.aw-hero-sub{font-family:'Inter',sans-serif;font-weight:300;font-size:1.1rem;color:rgba(255,255,255,.65);line-height:1.7;margin-bottom:36px;}
.aw-hero-ctas{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:40px;}
.aw-trust-badge{display:inline-flex;align-items:center;padding:10px 18px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);backdrop-filter:blur(8px);border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.8rem;color:white;font-weight:400;}

/* ── 4. Social Proof ── */
.aw-social-proof{background:#0a0a0a;padding:80px 32px;text-align:center;}
.aw-social-inner{max-width:640px;margin:0 auto;}
.aw-stars-blue{color:white;font-size:1.1rem;margin-bottom:16px;letter-spacing:.05em;}
.aw-quote{text-align:center;font-family:'Playfair Display',serif;font-style:italic;font-size:1.4rem;font-weight:400;color:white;line-height:1.6;margin-bottom:20px;}
.aw-attribution{text-align:center;font-family:'Inter',sans-serif;font-size:0.8rem;color:rgba(255,255,255,0.6);}

/* ── 4b. Testimonial Carousel ── */
.aw-testimonials{background:#0a0a0a;padding:0 0 100px;}
.aw-testimonials-track{display:flex;gap:20px;flex-wrap:wrap;justify-content:center;padding:0 32px 12px;}
.aw-testimonials-track::-webkit-scrollbar{display:none;}
.aw-tcard{flex:0 0 260px;max-width:300px;background:white;border:none;border-radius:16px;padding:28px 24px;position:relative;box-shadow:0 4px 24px rgba(0,0,0,0.18);}
.aw-tcard-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;}
.aw-tcard-stars{color:#486EF6;font-size:0.75rem;letter-spacing:.05em;}
.aw-tcard-tag{border:1px solid #CDC9DD;border-radius:9999px;font-size:0.6rem;letter-spacing:.1em;text-transform:uppercase;padding:3px 10px;color:#605E64;font-family:'Inter',sans-serif;white-space:nowrap;}
.aw-tcard-quote{text-align:left;font-family:'Playfair Display',serif;font-style:italic;font-size:1rem;color:#040404;line-height:1.6;margin-bottom:20px;}
.aw-tcard-author{text-align:left;font-family:'Inter',sans-serif;font-size:0.8rem;color:#605E64;}

/* ── 5. Marquee ── */
.aw-marquee{background:#040404;padding:20px 0;overflow:hidden;}
.aw-marquee-track{display:flex;white-space:nowrap;animation:aw-scroll 30s linear infinite;}
.aw-marquee-item{font-family:'Inter',sans-serif;font-weight:300;font-size:0.85rem;color:white;letter-spacing:.06em;padding:0 20px;}
.aw-marquee-dot{color:rgba(255,255,255,.3);padding:0 4px;}
@keyframes aw-scroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}

/* ── 6. Categories ── */
.aw-categories{background:white;padding:120px 0 80px;}
.aw-section-header{text-align:center;margin-bottom:52px;padding:0 32px;}
.aw-h2{font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3rem);font-weight:400;color:#040404;line-height:1.1;margin-top:12px;}
.aw-h2 em{font-style:italic;}
.aw-cards-track{display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 32px 16px;-webkit-overflow-scrolling:touch;scrollbar-width:none;justify-content:center;}
.aw-cards-track::-webkit-scrollbar{display:none;}
.aw-cat-card{flex:0 0 240px;height:480px;border-radius:20px;overflow:hidden;position:relative;scroll-snap-align:start;background:#111;}
.aw-cat-card-bg{position:absolute;inset:0;background-size:cover;background-position:center;transition:transform .4s ease;}
.aw-cat-card:hover .aw-cat-card-bg{transform:scale(1.04);}
.aw-cat-card-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(4,4,4,.78) 0%,rgba(4,4,4,.1) 50%,transparent 100%);}
.aw-cat-pill{position:absolute;top:20px;left:20px;border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.65rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;padding:5px 12px;color:white;}
.aw-cat-bottom{position:absolute;bottom:24px;left:20px;right:20px;}
.aw-cat-title{font-family:'Playfair Display',serif;font-style:italic;font-size:1.3rem;font-weight:400;color:white;margin-bottom:16px;line-height:1.2;}
.aw-cat-cta{display:inline-flex;align-items:center;padding:8px 18px;border-radius:9999px;border:1px solid rgba(255,255,255,.5);color:white;font-family:'Inter',sans-serif;font-size:0.75rem;font-weight:400;background:rgba(255,255,255,.08);}

/* ── 7. AwarePro ── */
.aw-pro{background:linear-gradient(135deg,#0a0a1a 0%,#1a1035 50%,#0f0f20 100%);padding:120px 32px;}
.aw-pro-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;}
.aw-phone-mockup{display:flex;justify-content:center;}
.aw-phone-frame{width:260px;height:520px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);border-radius:40px;backdrop-filter:blur(20px);position:relative;padding:28px 22px 28px;overflow:hidden;}
.aw-phone-notch{width:72px;height:22px;background:rgba(255,255,255,.08);border-radius:0 0 14px 14px;margin:0 auto 20px;}
.aw-phone-metric{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:14px 16px;margin-bottom:10px;}
.aw-phone-metric-label{font-family:'Inter',sans-serif;font-size:0.6rem;color:rgba(255,255,255,.45);letter-spacing:.1em;text-transform:uppercase;margin-bottom:3px;}
.aw-phone-metric-value{font-family:'Playfair Display',serif;font-size:1.5rem;color:white;font-weight:400;}
.aw-phone-badge-ok{display:inline-block;background:rgba(72,199,120,.18);color:#48C778;border:1px solid rgba(72,199,120,.3);border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.58rem;letter-spacing:.08em;text-transform:uppercase;padding:2px 9px;margin-top:4px;}
.aw-phone-chart{height:44px;background:rgba(72,110,246,.08);border-radius:8px;margin:10px 0 0;position:relative;overflow:hidden;}
.aw-phone-chart::after{content:'';position:absolute;bottom:10px;left:0;right:0;height:2px;background:linear-gradient(to right,rgba(72,110,246,.2),#486EF6,rgba(72,110,246,.2));border-radius:1px;}
.aw-phone-alert{position:absolute;right:16px;border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.6rem;padding:4px 10px;font-weight:500;}
.aw-phone-alert-red{bottom:130px;background:rgba(239,68,68,.22);color:#ef4444;border:1px solid rgba(239,68,68,.28);}
.aw-phone-alert-ora{bottom:94px;background:rgba(251,146,60,.22);color:#fb923c;border:1px solid rgba(251,146,60,.28);}
.aw-pro-eyebrow{display:inline-block;border:1px solid rgba(255,255,255,.2);border-radius:9999px;font-family:'Inter',sans-serif;font-size:0.6rem;letter-spacing:.12em;text-transform:uppercase;padding:5px 14px;color:rgba(255,255,255,.55);margin-bottom:22px;}
.aw-pro-h2{font-family:'Playfair Display',serif;font-size:clamp(2rem,3.5vw,2.8rem);font-weight:400;color:white;line-height:1.1;margin-bottom:14px;}
.aw-pro-h2 em{font-style:italic;color:#A480F2;}
.aw-pro-price{font-family:'Inter',sans-serif;font-weight:300;font-size:1.8rem;color:rgba(255,255,255,.88);margin-bottom:30px;}
.aw-pro-features{list-style:none;margin-bottom:36px;}
.aw-pro-features li{display:flex;align-items:flex-start;gap:12px;font-family:'Inter',sans-serif;font-size:0.88rem;color:rgba(255,255,255,.72);line-height:1.55;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.07);}.aw-pro-features li:last-child{border-bottom:none;}
.aw-pro-check{color:#A480F2;font-size:1rem;flex-shrink:0;margin-top:1px;}
.aw-pro-ctas{display:flex;gap:14px;flex-wrap:wrap;}
.aw-cta-pro-ghost{background:transparent;border:1px solid rgba(255,255,255,.3);color:white;}

/* ── 8. How It Works ── */
.aw-how{background:white;padding:120px 0;}
.aw-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;max-width:1100px;margin:0 auto;padding:0 32px;}
.aw-step{padding:36px 28px;border:1px solid #CDC9DD;border-radius:16px;}
.aw-step-num{font-family:'Playfair Display',serif;font-size:2.5rem;font-weight:400;color:#CDC9DD;margin-bottom:20px;}
.aw-step-title{font-family:'Inter',sans-serif;font-weight:500;font-size:0.95rem;color:#040404;margin-bottom:8px;}
.aw-step-body{font-family:'Inter',sans-serif;font-weight:300;font-size:0.85rem;color:#605E64;line-height:1.6;}

/* ── 9. Comparison ── */
.aw-compare{background:#F6F5FC;padding:120px 0;}
.aw-compare-table{max-width:900px;margin:0 auto;padding:0 32px;}
.aw-table{width:100%;border-collapse:collapse;font-family:'Inter',sans-serif;font-size:0.88rem;}
.aw-table th{padding:14px 20px;text-align:left;border-bottom:2px solid #CDC9DD;}
.aw-table th:first-child{color:#040404;font-weight:500;}
.aw-table th:nth-child(2){color:#486EF6;font-weight:600;}
.aw-table th:nth-child(3){color:#605E64;font-weight:400;}
.aw-table td{padding:13px 20px;border-bottom:1px solid #CDC9DD;}
.aw-table td:first-child{color:#040404;font-weight:400;}
.aw-table td:nth-child(2){color:#486EF6;font-weight:500;}
.aw-table td:nth-child(3){color:#605E64;}
.aw-table tr:last-child td{border-bottom:none;}

/* ── 10. Trust ── */
.aw-trust{background:white;padding:120px 0;}
.aw-trust-badges{display:flex;gap:20px;flex-wrap:wrap;justify-content:center;margin-top:52px;}
.aw-badge{padding:28px 36px;border:1px solid #CDC9DD;border-radius:16px;text-align:center;font-family:'Inter',sans-serif;}
.aw-badge-icon{display:none;}
.aw-badge-label{font-size:0.875rem;color:#605E64;font-weight:500;}
.aw-trust-stats{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:700px;margin:40px auto 0;}
.aw-stat-card{padding:36px;border:1px solid #CDC9DD;border-radius:16px;text-align:center;}
.aw-stat-big{font-family:'Playfair Display',serif;font-size:3rem;font-weight:400;color:#040404;}
.aw-stat-label{font-family:'Inter',sans-serif;font-size:0.82rem;color:#605E64;margin-top:6px;}

/* ── 11. Stats bar ── */
.aw-stats-bar{background:#040404;padding:80px 32px;}
.aw-stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;max-width:1100px;margin:0 auto;}
.aw-stat-item{text-align:center;padding:40px 24px;border-right:1px solid rgba(255,255,255,.08);}
.aw-stat-item:last-child{border-right:none;}
.aw-stat-number{font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:400;color:white;}
.aw-stat-unit{font-family:'Inter',sans-serif;font-size:0.75rem;color:rgba(255,255,255,.4);letter-spacing:.1em;text-transform:uppercase;margin-top:8px;}

/* ── 12. FAQ ── */
.aw-faq{background:white;padding:120px 0;}
.aw-faq-list{max-width:760px;margin:52px auto 0;padding:0 32px;}
.aw-faq-item{border-bottom:1px solid #CDC9DD;}
.aw-faq-q{width:100%;display:flex;align-items:center;justify-content:space-between;padding:22px 0;cursor:pointer;font-family:'Inter',sans-serif;font-size:0.95rem;font-weight:500;color:#040404;background:none;border:none;text-align:left;}
.aw-faq-icon{flex-shrink:0;width:24px;height:24px;border:1px solid #CDC9DD;border-radius:9999px;display:flex;align-items:center;justify-content:center;font-size:1rem;color:#605E64;transition:transform .25s;}
.aw-faq-item.open .aw-faq-icon{transform:rotate(45deg);}
.aw-faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease,padding .3s ease;}
.aw-faq-item.open .aw-faq-a{max-height:400px;}
.aw-faq-a-inner{padding:0 0 22px;font-family:'Inter',sans-serif;font-weight:300;font-size:0.88rem;color:#605E64;line-height:1.7;}

/* ── 13. Footer CTA ── */
.aw-footer-cta{background:#F6F5FC;padding:120px 32px;text-align:center;}
.aw-footer-cta-inner{max-width:640px;margin:0 auto;}
.aw-footer-cta h2{font-family:'Playfair Display',serif;font-size:clamp(2.2rem,4vw,3.2rem);font-weight:400;color:#040404;line-height:1.1;margin-bottom:20px;}
.aw-footer-cta h2 em{font-style:italic;}
.aw-footer-cta p{font-family:'Inter',sans-serif;font-weight:300;font-size:1rem;color:rgba(4,4,4,.5);line-height:1.7;margin-bottom:36px;}
.aw-footer{background:#040404;padding:64px 32px 40px;}
.aw-footer-inner{max-width:1100px;margin:0 auto;}
.aw-footer-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:52px;}
.aw-footer-brand p{font-family:'Inter',sans-serif;font-weight:300;font-size:0.85rem;color:rgba(255,255,255,.45);line-height:1.7;margin-top:16px;max-width:240px;}
.aw-footer-col h4{font-family:'Inter',sans-serif;font-weight:500;font-size:0.75rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:16px;}
.aw-footer-col ul{list-style:none;}
.aw-footer-col li{margin-bottom:10px;}
.aw-footer-col a{font-family:'Inter',sans-serif;font-size:0.85rem;color:rgba(255,255,255,.6);font-weight:300;}
.aw-footer-col a:hover{color:white;}
.aw-footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding-top:28px;display:flex;align-items:center;justify-content:space-between;font-family:'Inter',sans-serif;font-size:0.8rem;color:rgba(255,255,255,.3);}
.aw-footer-bottom-links{display:flex;gap:24px;}
.aw-footer-bottom-links a{color:rgba(255,255,255,.3);}
.aw-footer-bottom-links a:hover{color:rgba(255,255,255,.7);}

/* Responsive */
@media(max-width:768px){
  .aw-nav-links{display:none;}
  .aw-pro-inner{grid-template-columns:1fr;}
  .aw-phone-mockup{display:none;}
  .aw-steps{grid-template-columns:1fr 1fr;}
  .aw-stats-grid{grid-template-columns:1fr 1fr;}
  .aw-footer-top{grid-template-columns:1fr 1fr;}
  .aw-hero-h1{font-size:2.4rem;}
}
@media(max-width:480px){
  .aw-steps{grid-template-columns:1fr;}
  .aw-footer-top{grid-template-columns:1fr;}
  .aw-stats-grid{grid-template-columns:1fr 1fr;}
  .aw-trust-stats{grid-template-columns:1fr;}
}
` + '</style>');