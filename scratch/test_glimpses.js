const http = require('http');

http.get('http://127.0.0.1:3000/glimpses', (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const matches = data.match(/\/images\/glimpses\/2026_new_[0-9]\.(jpg|png)/g);
    console.log('Matches:', matches);
    process.exit(0);
  });
}).on('error', err => {
  console.error('Error:', err.message);
  process.exit(1);
});
