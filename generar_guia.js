const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument({
  size: 'A4',
  margins: { top: 50, bottom: 50, left: 45, right: 45 },
  info: { Title: 'Guía para Autónomos - Crecimiento Financiero Global' }
});

doc.pipe(fs.createWriteStream('Guia_Autonomos.pdf'));

const azul = '#0a1f44';
const amarillo = '#b8960a';
const gris = '#4a5563';

function titulo(t) { doc.fontSize(22).font('Helvetica-Bold').fillColor(azul).text(t, { align: 'center' }); doc.moveDown(0.25); }
function subtitulo(t) { doc.fontSize(11).font('Helvetica').fillColor(gris).text(t, { align: 'center' }); doc.moveDown(0.5); }
function seccion(num, tit, txt) {
  doc.fontSize(12).font('Helvetica-Bold').fillColor(azul).text(`${num}. ${tit}`);
  doc.fontSize(10).font('Helvetica').fillColor('#333').text(txt, { indent: 14 });
  doc.moveDown(0.35);
}
function cierre(t) { doc.fontSize(11).font('Helvetica-Oblique').fillColor(azul).text(t, { align: 'center' }); }

titulo('Guía para Autónomos');
subtitulo('Protege tu negocio · Crecimiento Financiero Global');

doc.fontSize(10).font('Helvetica').fillColor('#333')
  .text('Te ayudamos a elegir la mejor cobertura para tu actividad. Esta guía resume los seguros esenciales para autónomos en España.', { align: 'left' });
doc.moveDown(0.5);

seccion(1, 'Responsabilidad Civil', 'Cubre daños a terceros por tu actividad profesional. Obligatorio en muchas profesiones (arquitectos, abogados, sanitarios) y muy recomendable para cualquier autónomo.');
seccion(2, 'Seguro de Salud', 'Acceso a medicina privada sin listas de espera. Ideal para autónomos que no pueden permitirse días perdidos. Las primas son deducibles en el IRPF.');
seccion(3, 'Seguro de Hogar', 'Protege tu vivienda y, si trabajas desde casa, tu equipamiento profesional (ordenador, mobiliario, herramientas).');
seccion(4, 'Seguro de Vida', 'Garantiza la estabilidad de tu familia si faltas. Indemnización para cubrir deudas, hipoteca o gastos del día a día.');
seccion(5, 'Ahorro e Inversión', 'Planes de pensiones, PIAS, unit linked. Ventajas fiscales para autónomos en productos de ahorro a largo plazo.');

doc.moveDown(0.5);
cierre('¿Quieres un plan personalizado?');
doc.fontSize(10).font('Helvetica').fillColor(amarillo)
  .text('info@crecimientofinancieroglobal.com', { align: 'center', link: 'mailto:info@crecimientofinancieroglobal.com' });
doc.fontSize(9).font('Helvetica').fillColor(gris)
  .text('www.crecimientofinancieroglobal.com', { align: 'center' });

doc.end();
console.log('✅ PDF generado');
