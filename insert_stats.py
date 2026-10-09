content = open('views/about.ejs', encoding='utf-8').read()

stats_block = '''
    <!-- Animated Stat Counter Row -->
    <div class="grid-2" style="margin-bottom: 3rem; gap: 1.5rem;">
      <div class="stat-counter-card">
        <div class="stat-num-value" data-target="1973" data-no-comma="true">1973</div>
        <div class="stat-label-text">
          <span class="lang-mr">??????? ????</span><span class="lang-en">Founding Year</span>
        </div>
      </div>
      <div class="stat-counter-card">
        <div class="stat-num-value" data-target="53">53</div>
        <div class="stat-label-text">
          <span class="lang-mr">????? ?????? ?????</span><span class="lang-en">Years of Continuous Service</span>
        </div>
      </div>
    </div>
'''

content = content.replace('    <div class="grid-2" style="margin-bottom: 3rem;">', stats_block + '\n    <div class="grid-2" style="margin-bottom: 3rem;">')

open('views/about.ejs', 'w', encoding='utf-8').write(content)
print("Stats inserted")
