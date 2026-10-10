content = open('views/index.ejs', encoding='utf-8').read()

# Define the text block
text_block = '''          <div>
            <span class="section-badge">
              <span class="lang-mr">??????? ? ??????????? ?????</span>
              <span class="lang-en">President & Executive Message</span>
            </span>
            <h2 class="section-title" style="margin-top: 0.5rem;">
              <span class="lang-mr">??????? ? ?????? ????????</span>
              <span class="lang-en">Warm Welcome & Divine Blessings</span>
            </h2>
            <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1.5rem;">
              <span class="lang-mr">????? ????? ???????? ?????? ?????? ????? ??????????? ???? ?????? ???.</span>
              <span class="lang-en">Welcome to the official digital temple portal of Dagdi Chawl Chi Aai Mauli.</span>
            </p>

            <!-- Pull Quote Style Emphasis -->
            <blockquote class="pres-quote"
              style="border-left: 4px solid #C9A227; padding-left: 1.2rem; margin: 1.5rem 0; font-family: var(--font-mr-head); font-size: 1.25rem; color: #6B1414; font-style: italic;">
              <span class="lang-mr">"???????, ???? ??? ??????? ???????? ?? ????? ????? ???? ??????? ?????? ?????????
                ????."</span>
              <span class="lang-en">"Faith, service, and social commitment are the core pillars of Dagdi Chawl Chi Aai Mauli
                Mandal."</span>
            </blockquote>

            <div
              style="display: flex; gap: 1.5rem; border-left: 3px solid var(--royal-gold); padding-left: 1.5rem; background: rgba(212, 175, 55, 0.05); padding: 1.2rem 1.5rem; border-radius: var(--radius-sm);">
              <div>
                <h4 style="margin: 0; color: var(--temple-maroon); font-size: 1.15rem;">
                  <span class="lang-mr">????. ???? ???</span><span class="lang-en">Mr. Paresh Parab</span>
                </h4>
                <p style="margin: 0; font-size: 0.88rem; color: var(--primary-saffron); font-weight: 700;">
                  <span class="lang-mr">???????, ???? ???, ???? ?????, ???? ??? ???, ????? ??? (??????), ????? - ??????
                    ????</span><span class="lang-en">President, Ganesh Chowk, Bhaji Galli, Shankar Sheth Road, Grant
                    Road (W), Mumbai - 400007 Mandal</span>
                </p>
              </div>
            </div>
          </div>'''

# Define the image block
image_block = '''          <div style="position: relative;">
            <div class="gold-motion-frame">
              <picture>
                <img src="/images/president.jpg" alt="President" class="president-img" width="600" height="460"
                  loading="lazy"
                  style="width: 100%; height: auto; display: block; border-radius: 8px;">
              </picture>
            </div>
          </div>'''

# The original sequence is text_block followed by image_block
original = text_block + '\n\n' + image_block
swapped = image_block + '\n\n' + text_block

if original in content:
    content = content.replace(original, swapped)
    open('views/index.ejs', 'w', encoding='utf-8').write(content)
    print('Successfully swapped!')
else:
    print('Failed to find exact block. Check line endings or spacing.')
