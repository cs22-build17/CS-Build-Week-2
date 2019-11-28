const fs = require('fs');
const mapData = fs.readFileSync('map.txt', 'utf8');
const mapJSON = JSON.stringify(mapData);
fs.writeFile('map.json', mapJSON, (err) => {
  if (err) throw err;
  console.log('The file has been saved!');
});