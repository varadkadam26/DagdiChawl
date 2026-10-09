import codecs
import re

with codecs.open('views/index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the CSS for hd-devi, hd-devi-wrapper, and add new lighting layers
new_css = """
  .hd-devi-wrapper {
    position: absolute;
    /* initial percentages (will be overridden by JS) */
    top: 12.31%;
    left: 50.58%;
    width: 34.86%;
    z-index: 5;
    pointer-events: none;
    /* REMOVED huge drop-shadows to prevent pasted outline look */
  }

  .hd-devi {
    display: block;
    width: 100%;
    height: auto;
    /* Subtle warm amber/golden color grading matching the cave's exposure */
    filter: sepia(0.25) brightness(0.92) contrast(1.08) saturate(1.15) hue-rotate(-3deg);
  }

  /* Contact shadow at the base to ground the idol without outlining the whole shape */
  .idol-contact-shadow {
    position: absolute;
    bottom: -2%;
    left: 10%;
    width: 80%;
    height: 10%;
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.5) 40%, transparent 70%);
    z-index: -1;
    border-radius: 50%;
    filter: blur(8px);
  }

  /* Shared masking for lighting layers */
  .lighting-layer {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    -webkit-mask-image: url('/devi-idol.png');
    mask-image: url('/devi-idol.png');
    -webkit-mask-size: 100% 100%;
    mask-size: 100% 100%;
    -webkit-mask-repeat: no-repeat;
    mask-repeat: no-repeat;
    pointer-events: none;
    z-index: 6;
  }

  /* Warm golden rim highlights from the cave lanterns */
  .lighting-layer-highlights {
    background: 
      radial-gradient(ellipse at -5% 55%, rgba(255, 170, 50, 0.45) 0%, transparent 35%),
      radial-gradient(ellipse at 105% 55%, rgba(255, 160, 40, 0.4) 0%, transparent 35%),
      linear-gradient(180deg, rgba(255,200,100,0.15) 0%, transparent 20%);
    mix-blend-mode: color-dodge;
  }

  /* Soft natural shadows on the sides facing away from light and at the bottom */
  .lighting-layer-shadows {
    background: 
      linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 15%, transparent 35%),
      radial-gradient(ellipse at 50% -10%, rgba(0,0,0,0.2) 0%, transparent 40%);
    mix-blend-mode: multiply;
  }

  /* Animated subtle ambient firelight overlay */
  .devi-interactive-light {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    -webkit-mask-image: url('/devi-idol.png');
    mask-image: url('/devi-idol.png');
    -webkit-mask-size: 100% 100%;
    mask-size: 100% 100%;
    -webkit-mask-repeat: no-repeat;
    mask-repeat: no-repeat;
    background: radial-gradient(circle at 10% 60%, rgba(255, 160, 40, 0.15) 0%, transparent 60%),
                radial-gradient(circle at 90% 60%, rgba(255, 160, 40, 0.15) 0%, transparent 60%);
    mix-blend-mode: overlay;
    z-index: 7;
    animation: fire-flicker-no-move 3s infinite alternate;
  }

  @keyframes fire-flicker-no-move {
    0% { opacity: 0.6; }
    25% { opacity: 0.7; }
    50% { opacity: 0.95; }
    75% { opacity: 0.8; }
    100% { opacity: 0.9; }
  }
"""

# Replace old CSS with new CSS
text = re.sub(
    r'\.hd-devi-wrapper\s*\{.*?(?=\s*\.hd-text-container|\s*@media)',
    new_css,
    text,
    flags=re.DOTALL
)

# 2. Update HTML structure of hd-devi-wrapper
new_html = """
    <!-- Razor-sharp HD Devi Idol seamlessly blended into the cave -->
    <div class="hd-devi-wrapper" id="hd-devi-wrapper">
      <div class="idol-contact-shadow"></div>
      <img src="/devi-idol.png" alt="HD Devi" class="hd-devi" id="hd-devi-img" />
      <div class="lighting-layer lighting-layer-highlights"></div>
      <div class="lighting-layer lighting-layer-shadows"></div>
      <div class="devi-interactive-light"></div>
    </div>
"""

text = re.sub(
    r'<!-- Razor-sharp HD Devi Idol overlaid EXACTLY on top -->\s*<div class="hd-devi-wrapper">.*?</div>',
    new_html,
    text,
    flags=re.DOTALL
)

# 3. Add JS to perfectly align the idol in both desktop and mobile
# It calculates the scaled width/height of the background image due to object-fit: cover,
# then maps the exact idol coordinates onto the screen.
js_script = """
<script>
  function alignCutout() {
    const bgImg = document.getElementById('devi-bg-img');
    const wrapper = document.getElementById('hd-devi-wrapper');
    if (!bgImg || !wrapper) return;

    // Natural dimensions of the background image
    const nw = 1200; // bgImg.naturalWidth fallback
    const nh = 675;  // bgImg.naturalHeight fallback

    const cw = bgImg.clientWidth;
    const ch = bgImg.clientHeight;
    if (cw === 0 || ch === 0) return;

    const imgRatio = nw / nh;
    const conRatio = cw / ch;

    let renderW, renderH, offsetX, offsetY;

    if (conRatio > imgRatio) {
      // Container is wider than image aspect ratio -> image is cropped top/bottom
      renderW = cw;
      renderH = cw / imgRatio;
      
      // object-position: 79% center means horizontal shift is 79%, but since width matches, X offset is 0.
      // vertical is center, so Y offset is (ch - renderH) / 2
      offsetX = 0;
      offsetY = (ch - renderH) / 2;
    } else {
      // Container is taller than image aspect ratio -> image is cropped left/right
      renderW = ch * imgRatio;
      renderH = ch;
      
      // object-position is 79% center on X axis!
      // This means the left edge of the image is at 79% of the extra space.
      const extraX = cw - renderW; // This is negative
      offsetX = extraX * 0.79;
      offsetY = 0;
    }

    // Exact bounding box of the idol in the original 1200x675 image:
    // left: 50.58%, top: 12.31%, width: 34.86%
    const idolLeftPct = 0.5058;
    const idolTopPct = 0.1231;
    const idolWidthPct = 0.3486;

    // Map to screen pixels
    const pixelLeft = offsetX + (idolLeftPct * renderW);
    const pixelTop = offsetY + (idolTopPct * renderH);
    const pixelWidth = idolWidthPct * renderW;

    wrapper.style.left = pixelLeft + 'px';
    wrapper.style.top = pixelTop + 'px';
    wrapper.style.width = pixelWidth + 'px';
  }

  window.addEventListener('load', alignCutout);
  window.addEventListener('resize', alignCutout);
  // Run once immediately just in case
  alignCutout();
</script>
</body>
"""

text = text.replace('</body>', js_script)

with codecs.open('views/index.ejs', 'w', encoding='utf-8') as f:
    f.write(text)
