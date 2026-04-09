import re

with open('backup.py', 'r') as f:
    text = f.read()

# 1. Update Grid CSS
css_old = r'''            .grid-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
                width: 100%;
                max-width: 1600px;
            }

            @media \(max-width: 991px\) {
                .grid-container {
                    grid-template-columns: 1fr;
                }
                .timer-display { font-size: 2.5rem; }
            }'''

css_new = r'''            .grid-container {
                display: grid;
                grid-template-columns: 350px 1fr;
                gap: 40px;
                width: 100%;
                max-width: 1800px;
            }

            @media (max-width: 1400px) {
                .grid-container {
                    grid-template-columns: 1fr 1.5fr;
                }
            }

            @media (max-width: 991px) {
                .grid-container {
                    grid-template-columns: 1fr;
                }
                .timer-display { font-size: 2.5rem; }
            }

            .right-column-grid {
                display: grid;
                grid-template-columns: minmax(320px, 1fr) 1.8fr;
                gap: 40px;
                align-items: stretch;
            }

            @media (max-width: 1200px) {
                .right-column-grid {
                    grid-template-columns: 1fr;
                }
            }'''

text = re.sub(css_old, css_new, text)

# 2. Update HTML Right Column
html_old = r'''                <!-- Right Column -->
                <div class="d-flex flex-column gap-4">'''

html_new = r'''                <!-- Right Column -->
                <div class="right-column-grid w-100">'''

text = re.sub(html_old, html_new, text)

# 3. Update HTML Empty State
empty_old = r'''                    <!-- Empty State -->
                    <div id="emptyState" class="glass-card p-4 p-xl-5 d-flex flex-column align-items-center justify-content-center text-center opacity-50">'''

empty_new = r'''                    <!-- Empty State -->
                    <div id="emptyState" class="glass-card p-4 p-xl-5 d-flex flex-column align-items-center justify-content-center text-center opacity-50" style="grid-column: 1 / -1;">'''

text = re.sub(empty_old, empty_new, text)

# 4. JS logic to span keysCard
js_logic_old = r'''                    if \(data.generating\) {
                        statusMessage.innerHTML = `Target Prefix: <span class="text-info fw-bold">\$\{data.prefix\}</span>`;
                        statusCard.classList.remove\('d-none'\);'''

js_logic_new = r'''                    if (data.generating) {
                        statusMessage.innerHTML = `Target Prefix: <span class="text-info fw-bold">${data.prefix}</span>`;
                        statusCard.classList.remove('d-none');
                        keysCard.style.gridColumn = "";'''

text = re.sub(js_logic_old, js_logic_new, text)

js_logic_old2 = r'''                    \} else \{
                        statusCard.classList.add\('d-none'\);
                        document.getElementById\('prefix'\).disabled = false;'''

js_logic_new2 = r'''                    } else {
                        statusCard.classList.add('d-none');
                        keysCard.style.gridColumn = "1 / -1";
                        document.getElementById('prefix').disabled = false;'''

text = re.sub(js_logic_old2, js_logic_new2, text)

with open('backup.py', 'w') as f:
    f.write(text)

print("Layout update applied to backup.py!")
