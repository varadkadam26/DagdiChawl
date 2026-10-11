const fs = require('fs');
const path = require('path');

const srcDir = 'C:\\Users\\Manish\\.gemini\\antigravity-ide\\brain\\8b48d514-085d-423f-9f74-6affb060217e\\.user_uploaded';
const files = [
  'media_1791717853346.png',
  'media_1791717864385.jpg',
  'media_1791717876679.jpg',
  'media_1791717884454.jpg'
];

const destDir = path.join(__dirname, '..', 'public', 'images', 'glimpses');
if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

files.forEach((f, idx) => {
  const ext = path.extname(f);
  const src = path.join(srcDir, f);
  const dest = path.join(destDir, `2026_new_${idx + 1}${ext}`);
  fs.copyFileSync(src, dest);
  console.log(`Copied ${f} -> 2026_new_${idx + 1}${ext} (${fs.statSync(dest).size} bytes)`);
});
