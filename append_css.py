content = open('views/index.ejs', encoding='utf-8').read()

css_to_add = '''
  .arun-gawli-badge {
    font-family: 'Baloo 2', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    background: transparent !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    letter-spacing: 0.5px !important;
    white-space: nowrap !important;
  }
  @media (max-width: 768px) {
    .arun-gawli-badge {
      font-size: 11px !important;
      letter-spacing: 0 !important;
    }
  }
</style>'''

content = content.replace('</style>', css_to_add, 1)

open('views/index.ejs', 'w', encoding='utf-8').write(content)
