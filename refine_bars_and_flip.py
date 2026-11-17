with open('lumo-prototype.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Provide default heights for profile bar fills so they render beautifully in all states
old_bars = """        <!-- 7-Day Velocity Bar Graph -->
        <div class="retention-bar-chart">
          <div class="bar-col" onclick="inspectDay('Monday', '68%', 18, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="68%"></div></div>
            <span class="day-lbl">M</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Tuesday', '76%', 24, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="76%"></div></div>
            <span class="day-lbl">T</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Wednesday', '84%', 30, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="84%"></div></div>
            <span class="day-lbl">W</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Thursday', '92%', 28, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="92%"></div></div>
            <span class="day-lbl">T</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Friday', '78%', 16, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="78%"></div></div>
            <span class="day-lbl">F</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Saturday', '88%', 32, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" data-h="88%"></div></div>
            <span class="day-lbl">S</span>
          </div>
          <div class="bar-col active-today selected" onclick="inspectDay('Sunday (Today)', '94%', 36, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert target" data-h="94%"></div></div>
            <span class="day-lbl">S</span>
          </div>
        </div>"""

new_bars = """        <!-- 7-Day Velocity Bar Graph -->
        <div class="retention-bar-chart">
          <div class="bar-col" onclick="inspectDay('Monday', '68%', 18, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:68%;" data-h="68%"></div></div>
            <span class="day-lbl">M</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Tuesday', '76%', 24, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:76%;" data-h="76%"></div></div>
            <span class="day-lbl">T</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Wednesday', '84%', 30, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:84%;" data-h="84%"></div></div>
            <span class="day-lbl">W</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Thursday', '92%', 28, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:92%;" data-h="92%"></div></div>
            <span class="day-lbl">T</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Friday', '78%', 16, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:78%;" data-h="78%"></div></div>
            <span class="day-lbl">F</span>
          </div>
          <div class="bar-col" onclick="inspectDay('Saturday', '88%', 32, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert" style="height:88%;" data-h="88%"></div></div>
            <span class="day-lbl">S</span>
          </div>
          <div class="bar-col active-today selected" onclick="inspectDay('Sunday (Today)', '94%', 36, this)">
            <div class="bar-track-vert"><div class="bar-fill-vert target" style="height:94%;" data-h="94%"></div></div>
            <span class="day-lbl">S</span>
          </div>
        </div>"""

assert old_bars in html, "old_bars not found"
html = html.replace(old_bars, new_bars)

# 2. Update hash router for clean immediate flip capture
old_router = """    else if (hash === '#screen-3-back') { goTo(3); setTimeout(flipCard, 100); }"""
new_router = """    else if (hash === '#screen-3-back') {
      goTo(3);
      const card = document.getElementById('flip-card-element');
      if (card) {
        card.style.transition = 'none';
        card.classList.add('is-flipped');
        setTimeout(() => { card.style.transition = ''; }, 50);
      }
    }"""
assert old_router in html, "old_router not found"
html = html.replace(old_router, new_router)

with open('lumo-prototype.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Refinements applied successfully!')
