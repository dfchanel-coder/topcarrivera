const {test} = require('node:test');
const assert = require('node:assert/strict');
const {workshopStatus} = require('../js/main.js');
// 2026-10-26 is Monday. Dates have an explicit shop offset, independent of host TZ.
for (const [when,open,text] of [
 ['2026-10-26T00:00:00-03:00',false,'hoy'],
 ['2026-10-26T08:29:00-03:00',false,'hoy'],
 ['2026-10-26T08:30:00-03:00',true,'cierra 18:30'],
 ['2026-10-26T18:29:00-03:00',true,'cierra 18:30'],
 ['2026-10-26T18:30:00-03:00',false,'mañana'],
 ['2026-10-30T18:30:00-03:00',false,'lunes'],
 ['2026-10-31T10:00:00-03:00',false,'lunes'],
 ['2026-11-01T20:00:00-03:00',false,'mañana'],
 ['2026-10-27T01:00:00Z',false,'mañana']
]) test(when,()=>{const result=workshopStatus(new Date(when));assert.equal(result.open,open);assert.ok(result.text.includes(text),result.text);});
test('Portuguese follows the same local schedule',()=>{
 assert.equal(workshopStatus(new Date('2026-10-26T08:00:00-03:00'),true).text,'Fechado · abre hoje às 8h30');
 assert.equal(workshopStatus(new Date('2026-10-30T19:00:00-03:00'),true).text,'Fechado · abre segunda às 8h30');
});
