import re

with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# Marquee HTML to replace the old ones
marquee_html = '''<div style="overflow: hidden; margin-bottom: 1rem;">
        <div class="marquee-track-right">
          <picture>
            <img src="/images/marquee/new_1.jpg" alt="Dagdi Chawl Event 1" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_2.jpg" alt="Dagdi Chawl Event 2" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_3.png" alt="Dagdi Chawl Event 3" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_4.jpg" alt="Dagdi Chawl Event 4" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_5.jpg" alt="Dagdi Chawl Event 5" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>

          <!-- Duplicated for seamless scrolling -->
          <picture>
            <img src="/images/marquee/new_1.jpg" alt="Dagdi Chawl Event 1" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_2.jpg" alt="Dagdi Chawl Event 2" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_3.png" alt="Dagdi Chawl Event 3" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_4.jpg" alt="Dagdi Chawl Event 4" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_5.jpg" alt="Dagdi Chawl Event 5" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
        </div>
      </div>'''

start_idx = text.find('<div style="overflow: hidden; margin-bottom: 1rem;">')
if start_idx != -1:
    end_idx = text.find('</section>', start_idx)
    text = text[:start_idx] + marquee_html + '\n    ' + text[end_idx:]

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done replacing marquee!')
