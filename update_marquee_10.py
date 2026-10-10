with open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# Marquee HTML with all 10 images
marquee_html = '''<div style="overflow: hidden; margin-bottom: 1rem;">
        <div class="marquee-track-right" style="animation-duration: 40s;">
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
          <picture>
            <img src="/images/marquee/new_6.jpg" alt="Dagdi Chawl Event 6" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_7.jpg" alt="Dagdi Chawl Event 7" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_8.png" alt="Dagdi Chawl Event 8" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_9.jpg" alt="Dagdi Chawl Event 9" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_10.jpg" alt="Dagdi Chawl Event 10" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
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
          <picture>
            <img src="/images/marquee/new_6.jpg" alt="Dagdi Chawl Event 6" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_7.jpg" alt="Dagdi Chawl Event 7" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_8.png" alt="Dagdi Chawl Event 8" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_9.jpg" alt="Dagdi Chawl Event 9" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
          <picture>
            <img src="/images/marquee/new_10.jpg" alt="Dagdi Chawl Event 10" width="400" height="300" loading="lazy" decoding="async" class="img-marquee">
          </picture>
        </div>
      </div>'''

start_idx = text.find('<div style="overflow: hidden; margin-bottom: 1rem;">')
if start_idx != -1:
    end_idx = text.find('</section>', start_idx)
    text = text[:start_idx] + marquee_html + '\n    ' + text[end_idx:]

with open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done replacing marquee with 10 images!')
