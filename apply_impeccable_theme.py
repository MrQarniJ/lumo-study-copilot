import re

def update_lumo():
    with open('lumo-prototype.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update :root design system tokens
    old_root = """  /* ===== Lumo Senior Product Design System (Restrained, Tasteful, Purposeful) ===== */
  :root {
    --bg-app: #FAF9F6;
    --bg-surface: #FFFFFF;
    --bg-subtle: #F3EFE6;
    
    --brand-indigo: #2D275A;
    --brand-indigo-hover: #221D47;
    --accent-violet: #6D28D9;
    
    --semantic-green: #10B981;
    --semantic-green-bg: #ECFDF5;
    --semantic-green-text: #065F46;

    --semantic-amber: #F59E0B;
    --semantic-amber-bg: #FFFBEB;
    --semantic-amber-text: #92400E;

    --semantic-rose: #F43F5E;
    --semantic-rose-bg: #FFF1F2;
    --semantic-rose-text: #9F1239;

    --text-primary: #1C1929;
    --text-secondary: #635F74;
    --text-muted: #9591A5;
    
    --border: #E8E4DA;
    --border-light: #F1EDE5;

    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.03);
    --shadow-card: 0 2px 6px rgba(45, 39, 90, 0.04);
    --shadow-modal: 0 16px 40px rgba(0, 0, 0, 0.16);

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-pill: 9999px;
  }"""

    new_root = """  /* ===== Lumo Senior Product Design System (Impeccable Senior Editorial Spec) ===== */
  :root {
    /* Base Surfaces */
    --bg-app: #FAF9F6;
    --bg-surface: #FFFFFF;
    --bg-subtle: #F4EFE6;
    --bg-elevated: #FFFFFF;
    
    /* Academic Oxford Indigo Brand */
    --brand-indigo: #241E4E;
    --brand-indigo-hover: #1A153A;
    --accent-violet: #6366F1;
    --accent-violet-bg: #EEF2FF;
    --accent-violet-border: #C7D2FE;
    --accent-violet-text: #3730A3;
    
    /* Semantic Colors (Calibrated WCAG AA Compliant on Warm Cream & Pure White) */
    --semantic-green: #059669;
    --semantic-green-bg: #F0FDF4;
    --semantic-green-border: #BBF7D0;
    --semantic-green-text: #166534;

    --semantic-amber: #D97706;
    --semantic-amber-bg: #FFFBEB;
    --semantic-amber-border: #FDE68A;
    --semantic-amber-text: #92400E;

    --semantic-rose: #E11D48;
    --semantic-rose-bg: #FFF1F2;
    --semantic-rose-border: #FECDD3;
    --semantic-rose-text: #9F1239;

    /* Editorial Text Hierarchy */
    --text-primary: #181528;
    --text-secondary: #58536E;
    --text-muted: #79748D;
    
    /* Hairline Crisp Border System */
    --border: #E8E4DA;
    --border-light: #F1EDE5;

    /* Multi-layered Color-Matched Elevation (Ambient + Key Light) */
    --shadow-sm: 0 1px 2px rgba(24, 21, 40, 0.04);
    --shadow-card: 0 1px 3px rgba(24, 21, 40, 0.04), 0 6px 16px -4px rgba(24, 21, 40, 0.05);
    --shadow-hover: 0 3px 6px rgba(24, 21, 40, 0.04), 0 12px 24px -6px rgba(24, 21, 40, 0.08);
    --shadow-modal: 0 20px 48px -8px rgba(17, 14, 34, 0.22);

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-pill: 9999px;
  }"""

    assert old_root in content, "old_root not found"
    content = content.replace(old_root, new_root)

    # 2. Browser surface styling & font rendering
    old_box_star = "* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }"
    new_box_star = """* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  ::selection {
    background: #241E4E;
    color: #FFFFFF;
  }
  input, textarea, select {
    caret-color: #241E4E;
  }
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: #D8D4C8; border-radius: 9999px; }
  ::-webkit-scrollbar-thumb:hover { background: #BDB7A6; }

  /* Tabular Numerals for Precision Metrics */
  .tabular-nums,
  .status-bar,
  .stat-box-clean .num,
  .analysis-metric-headline,
  .banner-readiness-row,
  .readiness-pct-label,
  .task-time-pill,
  .audio-duration,
  .settings-row .val,
  .topic-action-badge,
  .day-lbl {
    font-variant-numeric: tabular-nums;
  }"""
    assert old_box_star in content, "old_box_star not found"
    content = content.replace(old_box_star, new_box_star)

    # 3. Replace AI sloppy .slide-quote-highlight (Remove border-left: 3px)
    old_quote = """.slide-quote-highlight {
    background: #FFFBEB;
    border-left: 3px solid var(--semantic-amber);
    padding: 8px 10px;
    border-radius: 0 6px 6px 0;
    margin: 8px 0;
    font-style: italic;
    color: var(--text-primary);
  }"""
    new_quote = """.slide-quote-highlight {
    background: var(--semantic-amber-bg);
    border: 1px solid var(--semantic-amber-border);
    padding: 10px 12px;
    border-radius: var(--radius-sm);
    margin: 8px 0;
    font-style: normal;
    color: var(--semantic-amber-text);
    line-height: 1.5;
  }"""
    assert old_quote in content, "old_quote not found"
    content = content.replace(old_quote, new_quote)

    # 4. Replace AI sloppy .takeaway-clean-box (Remove border-left: 3px)
    old_takeaway = """.takeaway-clean-box {
    background: #F4EFFC;
    border-left: 3px solid var(--accent-violet);
    padding: 10px 12px;
    border-radius: 0 8px 8px 0;
    font-size: 12px;
    color: #4C1D95;
    margin: 8px 0;
  }"""
    new_takeaway = """.takeaway-clean-box {
    background: var(--accent-violet-bg);
    border: 1px solid var(--accent-violet-border);
    padding: 11px 14px;
    border-radius: var(--radius-sm);
    font-size: 12px;
    line-height: 1.5;
    color: var(--accent-violet-text);
    margin: 10px 0;
  }"""
    assert old_takeaway in content, "old_takeaway not found"
    content = content.replace(old_takeaway, new_takeaway)

    # 5. Elevate Hero Banner to Oxford Editorial Gradient with Inner Highlight
    old_hero = """.hero-banner-simple {
    background: var(--brand-indigo);
    border-radius: var(--radius-lg);
    padding: 18px 20px;
    color: #FFFFFF;
    margin-bottom: 16px;
  }"""
    new_hero = """.hero-banner-simple {
    background: linear-gradient(145deg, #241E4E 0%, #1A153A 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12), 0 8px 24px -4px rgba(26, 21, 58, 0.25);
    border-radius: var(--radius-lg);
    padding: 20px 22px;
    color: #FFFFFF;
    margin-bottom: 18px;
    position: relative;
    overflow: hidden;
  }"""
    assert old_hero in content, "old_hero not found"
    content = content.replace(old_hero, new_hero)

    # 6. Elevate status-indicator-dot and topic badges
    old_dot_css = """.status-indicator-dot {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9px;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1;
  }
  .dot-red { background: var(--semantic-rose); }
  .dot-amber { background: var(--semantic-amber); }
  .dot-green { background: var(--semantic-green); }

  .topic-title-clean { font-size: 14px; font-weight: 700; color: var(--text-primary); }
  .topic-sub-clean { font-size: 12px; color: var(--text-secondary); margin-top: 1px; }
  .topic-action-badge {
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: var(--radius-pill);
    text-align: right;
  }
  .badge-red { background: var(--semantic-rose-bg); color: var(--semantic-rose-text); }
  .badge-amber { background: var(--semantic-amber-bg); color: var(--semantic-amber-text); }
  .badge-green { background: var(--semantic-green-bg); color: var(--semantic-green-text); }"""

    new_dot_css = """.status-indicator-dot {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 1;
  }
  .dot-red { background: var(--semantic-rose-bg); color: var(--semantic-rose); border: 1px solid var(--semantic-rose-border); }
  .dot-amber { background: var(--semantic-amber-bg); color: var(--semantic-amber); border: 1px solid var(--semantic-amber-border); }
  .dot-green { background: var(--semantic-green-bg); color: var(--semantic-green); border: 1px solid var(--semantic-green-border); }

  .topic-title-clean { font-size: 14px; font-weight: 700; color: var(--text-primary); }
  .topic-sub-clean { font-size: 12px; color: var(--text-secondary); margin-top: 1px; }
  .topic-action-badge {
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: var(--radius-pill);
    text-align: right;
  }
  .badge-red { background: var(--semantic-rose-bg); color: var(--semantic-rose-text); border: 1px solid var(--semantic-rose-border); }
  .badge-amber { background: var(--semantic-amber-bg); color: var(--semantic-amber-text); border: 1px solid var(--semantic-amber-border); }
  .badge-green { background: var(--semantic-green-bg); color: var(--semantic-green-text); border: 1px solid var(--semantic-green-border); }"""

    assert old_dot_css in content, "old_dot_css not found"
    content = content.replace(old_dot_css, new_dot_css)

    # 7. Replace Unicode character icons with clean SVG icons in Screen 2
    old_topic_1 = '<div class="status-indicator-dot dot-red" title="Weak Concept">!</div>'
    new_topic_1 = '<div class="status-indicator-dot dot-red" title="Weak Concept"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="14"></line><line x1="12" y1="18" x2="12.01" y2="18"></line></svg></div>'
    assert old_topic_1 in content, "old_topic_1 not found"
    content = content.replace(old_topic_1, new_topic_1)

    old_topic_2 = '<div class="status-indicator-dot dot-amber" title="Due for Review">↻</div>'
    new_topic_2 = '<div class="status-indicator-dot dot-amber" title="Due for Review"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><polyline points="23 4 23 10 17 10"></polyline><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path></svg></div>'
    # There are two amber topics
    assert content.count(old_topic_2) == 2, f"expected 2 amber dots, found {content.count(old_topic_2)}"
    content = content.replace(old_topic_2, new_topic_2)

    old_topic_4 = '<div class="status-indicator-dot dot-green" title="Mastered">✔</div>'
    new_topic_4 = '<div class="status-indicator-dot dot-green" title="Mastered"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>'
    assert old_topic_4 in content, "old_topic_4 not found"
    content = content.replace(old_topic_4, new_topic_4)

    # 8. Elevate recall buttons with semantic hover & selected states
    old_recall_css = """.recall-btn {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 10px 4px;
    text-align: center;
    cursor: pointer;
    font-size: 12px;
    font-weight: 700;
    transition: background 0.12s ease, border-color 0.12s ease, transform 0.1s ease;
  }
  .recall-btn:active { transform: scale(0.96); }
  .recall-btn.selected {
    border-color: var(--brand-indigo);
    background: #F1ECE1;
  }"""

    new_recall_css = """.recall-btn {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 10px 4px;
    text-align: center;
    cursor: pointer;
    font-size: 12px;
    font-weight: 700;
    box-shadow: var(--shadow-sm);
    transition: background 0.12s ease, border-color 0.12s ease, transform 0.1s ease, box-shadow 0.12s ease;
  }
  .recall-btn:hover { background: #FAF9F6; }
  .recall-btn:active { transform: scale(0.96); }
  .recall-btn.selected {
    border-color: var(--brand-indigo);
    background: #F4EFE6;
  }
  .recall-btn.recall-again.selected { background: var(--semantic-rose-bg); border-color: var(--semantic-rose-border); }
  .recall-btn.recall-hard.selected { background: var(--semantic-amber-bg); border-color: var(--semantic-amber-border); }
  .recall-btn.recall-good.selected { background: var(--semantic-green-bg); border-color: var(--semantic-green-border); }
  .recall-btn.recall-easy.selected { background: var(--accent-violet-bg); border-color: var(--accent-violet-border); }"""

    assert old_recall_css in content, "old_recall_css not found"
    content = content.replace(old_recall_css, new_recall_css)

    # 9. Add semantic classes to recall buttons in Screen 3 HTML
    old_grid_html = """      <div class="recall-buttons-grid">
        <div class="recall-btn" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-rose-text);">Again</span>
            <span class="kbd-hint">1</span>
          </div>
          <span class="recall-sub">&lt; 1m</span>
        </div>
        <div class="recall-btn" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-amber-text);">Hard</span>
            <span class="kbd-hint">2</span>
          </div>
          <span class="recall-sub">12h</span>
        </div>
        <div class="recall-btn selected" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-green-text);">Good</span>
            <span class="kbd-hint">3</span>
          </div>
          <span class="recall-sub">2d</span>
        </div>
        <div class="recall-btn" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--brand-indigo);">Easy</span>
            <span class="kbd-hint">4</span>
          </div>
          <span class="recall-sub">6d</span>
        </div>
      </div>"""

    new_grid_html = """      <div class="recall-buttons-grid">
        <div class="recall-btn recall-again" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-rose-text);">Again</span>
            <span class="kbd-hint">1</span>
          </div>
          <span class="recall-sub">&lt; 1m</span>
        </div>
        <div class="recall-btn recall-hard" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-amber-text);">Hard</span>
            <span class="kbd-hint">2</span>
          </div>
          <span class="recall-sub">12h</span>
        </div>
        <div class="recall-btn recall-good selected" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--semantic-green-text);">Good</span>
            <span class="kbd-hint">3</span>
          </div>
          <span class="recall-sub">2d</span>
        </div>
        <div class="recall-btn recall-easy" onclick="rateCard(this, true)">
          <div style="display:flex; justify-content:center; align-items:center;">
            <span style="color:var(--brand-indigo);">Easy</span>
            <span class="kbd-hint">4</span>
          </div>
          <span class="recall-sub">6d</span>
        </div>
      </div>"""

    assert old_grid_html in content, "old_grid_html not found"
    content = content.replace(old_grid_html, new_grid_html)

    # 10. Add hairline borders to gain pills in Screen 6 and 7
    old_gain_badge = 'style="font-size:12px; font-weight:700; color:var(--semantic-green-text); background:var(--semantic-green-bg); padding:3px 8px; border-radius:var(--radius-pill);"'
    new_gain_badge = 'style="font-size:12px; font-weight:700; color:var(--semantic-green-text); background:var(--semantic-green-bg); border:1px solid var(--semantic-green-border); padding:3px 8px; border-radius:var(--radius-pill);"'
    assert old_gain_badge in content, "old_gain_badge not found"
    content = content.replace(old_gain_badge, new_gain_badge)

    old_week_badge = 'style="font-size:11px; font-weight:700; color:var(--semantic-green-text); background:var(--semantic-green-bg); padding:2px 8px; border-radius:var(--radius-pill);"'
    new_week_badge = 'style="font-size:11px; font-weight:700; color:var(--semantic-green-text); background:var(--semantic-green-bg); border:1px solid var(--semantic-green-border); padding:2px 8px; border-radius:var(--radius-pill);"'
    assert old_week_badge in content, "old_week_badge not found"
    content = content.replace(old_week_badge, new_week_badge)

    # Write out updated file
    with open('lumo-prototype.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('lumo-prototype.html updated successfully with all Impeccable theme polish!')

if __name__ == '__main__':
    update_lumo()
