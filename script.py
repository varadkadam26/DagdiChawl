import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Address
text = text.replace('<span class="lang-mr">गणेश चौक, भाजी गल्ली, शंकर शेट रोड, ग्रँट रोड (पश्चिम), मुंबई - ४००००७.</span>', '<span class="lang-mr">७१४, दगडी चाळ, बापूराव जगताप मार्ग, भायखळा (पश्चिम), मुंबई - ४०००११.</span>')
text = text.replace('<span class="lang-en">Ganesh Chowk, Bhaji Galli, Shankar Sheth Road, Grant Road (W), Mumbai - 400007.</span>', '<span class="lang-en">714, Dagdi Chawl, Bapurao Jagtap Marg, Byculla (W), Mumbai - 400011.</span>')
text = text.replace('<span class="lang-en">Ganesh Chowk, Bhaji Galli, Shankar Sheth Road, Grant Road (W), Mumbai -\n                400007.</span>', '<span class="lang-en">714, Dagdi Chawl, Bapurao Jagtap Marg, Byculla (W), Mumbai -\n                400011.</span>')

# 2. Maps link
text = text.replace('href="https://www.google.com/maps/place/XR77%2B6R8+Malabar+Hill+Cha+Raja,+Shankar+Sheth+Ln,+Bhaji+Galli,+Grant+Road+West,+Grant+Road+(W),+Grant+Road,+Mumbai,+Maharashtra+400007/data=!4m2!3m1!1s0x3be7cf87d09dfb77:0xdfbb25d99102747e"', 'href="https://www.google.com/maps/search/Dagdi+Chawl,+Bapurao+Jagtap+Marg,+Byculla+West,+Mumbai+400011"')
text = text.replace('src="https://www.google.com/maps?q=Malabar+Hill+Cha+Raja,+Shankar+Sheth+Ln,+Bhaji+Galli,+Grant+Road+West,+Mumbai-400007&output=embed"', 'src="https://www.google.com/maps?q=Dagdi+Chawl,+Bapurao+Jagtap+Marg,+Byculla+West,+Mumbai-400011&output=embed"')

# 3. Arun Gawli golden text
text = text.replace('<p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1rem;">', '<p style="color: #FFD700; text-shadow: 0 0 8px rgba(255, 215, 0, 0.6); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1rem; font-weight: 500;">')
text = text.replace('<p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1.5rem;">\n              <span class="lang-mr">या पवित्र उत्सवाच्या निमित्ताने सर्व भाविक भक्तांना मनःपूर्वक शुभेच्छा! आई माऊलीची कृपा आपल्या सर्वांवर सदैव राहो आणि प्रत्येकाच्या जीवनात सुख, शांती व समृद्धी नांदो, हीच आईच्या चरणी प्रार्थना.</span>', '<p style="color: #FFD700; text-shadow: 0 0 8px rgba(255, 215, 0, 0.6); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1.5rem; font-weight: 500;">\n              <span class="lang-mr">या पवित्र उत्सवाच्या निमित्ताने सर्व भाविक भक्तांना मनःपूर्वक शुभेच्छा! आई माऊलीची कृपा आपल्या सर्वांवर सदैव राहो आणि प्रत्येकाच्या जीवनात सुख, शांती व समृद्धी नांदो, हीच आईच्या चरणी प्रार्थना.</span>')
text = text.replace('color: #6B1414; font-weight: bold; font-style: italic;">', 'color: #FFD700; text-shadow: 0 0 10px rgba(255, 215, 0, 0.8); font-weight: bold; font-style: italic;">')

# 4. Remove Animated Stats Row
text = re.sub(r'<!-- Animated Stat Counter Row -->.*?</div>\s*</div>\s*</div>\s*', '', text, flags=re.DOTALL)

# 5. Ganpati to Devi info
ganpati_block = '''<source srcset="/images/malabar_ganpati_05.webp" type="image/webp">
              <img src="/images/malabar_ganpati_05.jpg" alt="Malabar Hill Cha Raja Peshwa Craft" width="600"
                height="480" loading="lazy"
                style="width: 100%; height: 100%; object-fit: cover; object-position: center 15%;">'''
devi_block = '''<img src="/images/devi-info.jpg" alt="Dagdi Chawl Chi Aai Mauli" width="600"
                height="480" loading="lazy"
                style="width: 100%; height: 100%; object-fit: cover; object-position: center 15%;">'''
text = text.replace(ganpati_block, devi_block)

info_block = '''<span class="lang-mr">राजेशाही पेहराव व मूर्तिकला</span><span class="lang-en">Royal Attire & Sculpture
                Craft</span>
            </span>
            <h2 class="section-title">
              <span class="lang-mr">२४ फुटांची भव्यता आणि सुवर्ण सजावट</span>
              <span class="lang-en">24-Feet Grandeur & Golden Decoration</span>
            </h2>
            <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1.5rem;">
              <span class="lang-mr">२४ फूट उंच, मलबार हिलचा राजाचे दिव्य हास्य आणि तेजस्वी डोळे लाखो भाविकांना आकर्षित
                करतात.</span>
              <span class="lang-en">Standing 24 feet tall, the divine smile and radiant eyes of Malabar Hill Cha Raja
                captivate millions of visiting devotees.</span>
            </p>
            <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 2rem;">
              <span class="lang-mr">लाकडी आणि सोन्याच्या सिंहासनावर विराजमान असलेली ही मूर्ती दरवर्षी विशिष्ट
                महाराष्ट्रीय सांस्कृतिक थीमवर साकारली जाते.</span>
              <span class="lang-en">Seated on carved wooden and golden thrones, the idol form is crafted according to
                unique Maharashtrian cultural themes every single year.</span>
            </p>

            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <div
                style="background: #FFFFFF; border: 1.5px solid var(--royal-gold); padding: 1rem 1.5rem; border-radius: var(--radius-md); flex: 1;">
                <div
                  style="font-size: 1.8rem; font-weight: 800; color: var(--primary-saffron); font-family: var(--font-en-head);">
                  <span class="lang-mr">२४ फूट</span><span class="lang-en">24 Feet</span>
                </div>
                <div style="font-size: 0.82rem; font-weight: 700; color: var(--text-muted);">
                  <span class="lang-mr">भव्य मूर्तीची उंची</span><span class="lang-en">Grand Idol Height</span>
                </div>
              </div>
              <div
                style="background: #FFFFFF; border: 1.5px solid var(--royal-gold); padding: 1rem 1.5rem; border-radius: var(--radius-md); flex: 1;">
                <div
                  style="font-size: 1.8rem; font-weight: 800; color: var(--primary-saffron); font-family: var(--font-en-head);">
                  <span class="lang-mr">५३+ वर्षे</span><span class="lang-en">53+ Yrs</span>
                </div>
                <div style="font-size: 0.82rem; font-weight: 700; color: var(--text-muted);">
                  <span class="lang-mr">शुद्ध भक्तीची परंपरा</span><span class="lang-en">Legacy of Pure Devotion</span>
                </div>
              </div>
            </div>'''
devi_info_block = '''<span class="lang-mr">दिव्य मूर्ती व सौंदर्य</span><span class="lang-en">Divine Idol & Beauty</span>
            </span>
            <h2 class="section-title">
              <span class="lang-mr">आई माऊलीचे मनमोहक रूप</span>
              <span class="lang-en">The Enchanting Form of Aai Mauli</span>
            </h2>
            <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 1.5rem;">
              <span class="lang-mr">दगडी चाळीच्या आई माऊलीचे अत्यंत लोभस आणि तेजस्वी रूप भाविकांच्या मनाला भुरळ घालते. तिचे दिव्य हास्य आणि वात्सल्यपूर्ण दृष्टी सर्वांना एक अनोखी शांती आणि ऊर्जा प्रदान करते.</span>
              <span class="lang-en">The incredibly charming and radiant form of Dagdi Chawl Chi Aai Mauli captivates the hearts of devotees. Her divine smile and affectionate gaze bestow unique peace and energy upon everyone.</span>
            </p>
            <p style="color: var(--text-muted); font-size: 1.08rem; line-height: 1.85; margin-bottom: 2rem;">
              <span class="lang-mr">नवरात्रीच्या पवित्र उत्सवादरम्यान, आई माऊलीची मूर्ती अतिशय सुंदर दागिन्यांनी आणि आकर्षक फुलांच्या सजावटीने सजवली जाते, जी भक्ती आणि श्रद्धेचे प्रतीक आहे.</span>
              <span class="lang-en">During the holy festival of Navratri, the idol of Aai Mauli is adorned with beautiful jewelry and stunning floral decorations, serving as a true symbol of devotion and faith.</span>
            </p>'''
text = text.replace(info_block, devi_info_block)

# 6. Remove Historic Golden Moments Section
historic_start = text.find('<section style="padding: 6rem 0;">')
historic_end = text.find('</section>', historic_start)
if historic_start != -1 and historic_end != -1:
    text = text[:historic_start] + text[historic_end + len('</section>'):]

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
