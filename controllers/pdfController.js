const PDFDocument = require('pdfkit');
const path = require('path');
const fs = require('fs');

const logoPath = path.join(__dirname, '../public/images/logo.png');

// Helper: draw subtle background logo watermark
const drawWatermark = (doc) => {
  if (fs.existsSync(logoPath)) {
    try {
      doc.save();
      doc.opacity(0.07);
      doc.image(logoPath, (595 - 260) / 2, 230, { width: 260 });
      doc.restore();
    } catch (err) {
      console.error('PDF watermark error:', err.message);
    }
  }
};

// Helper: draw a labeled field pair (label above, bold value below)
const makeDrawField = (doc) => (label, value, x, y, width = 220) => {
  doc.fillColor('#7A3B3B').fontSize(8).font('Helvetica-Bold').text(label.toUpperCase(), x, y);
  doc.fillColor('#1a1a1a').fontSize(11).font('Helvetica-Bold').text(value || 'N/A', x, y + 13, { width });
};

// Helper: draw the shared Dagdi Chawl receipt header
const drawHeader = (doc) => {
  doc.rect(40, 40, 515, 105).fill('#7B1A1A');
  doc.fillColor('#FFD700').fontSize(10).font('Helvetica-Oblique')
    .text('|| JAI AAI MAULI ||', 55, 52, { align: 'center', width: 485 });
  doc.fillColor('#FFD700').fontSize(20).font('Helvetica-Bold')
    .text('DAGDI CHAWLICHI AAI MAULI', 55, 68, { align: 'center', width: 485 });
  doc.fillColor('#F5E0C3').fontSize(11).font('Helvetica')
    .text('BHAYKHAALA DAGDI CHAWL SARVAJANIK NAVRATROTSAV MANDAL', 55, 94, { align: 'center', width: 485 });
  doc.fillColor('#E8C98A').fontSize(8).font('Helvetica')
    .text('Address: Dagdi Chawl, B.J. Marg, Byculla West, Mumbai - 400011    |    Website: dagdichawlichiaaimauli.in',
      55, 116, { align: 'center', width: 485 });
  doc.moveTo(40, 148).lineTo(555, 148).lineWidth(2).strokeColor('#D4AF37').stroke();
};

// Helper: draw the receipt title strip
const drawReceiptTitleStrip = (doc, receiptNo, date) => {
  doc.rect(40, 155, 515, 30).fill('#FFF8F0');
  doc.rect(40, 155, 515, 30).lineWidth(1).strokeColor('#C09040').stroke();
  doc.fillColor('#7B1A1A').fontSize(11).font('Helvetica-Bold')
    .text('OFFICIAL DONATION RECEIPT', 55, 165);
  doc.fillColor('#444').fontSize(9).font('Helvetica')
    .text('Receipt No: ' + receiptNo + '    Date: ' + date, 55, 165, { align: 'right', width: 485 });
};

module.exports = {

  // 1. DONATION RECEIPT for /download-receipt/:id
  generateDonationPDF(donation, res) {
    const doc = new PDFDocument({ size: 'A4', margin: 40 });
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', 'attachment; filename=DCM_Donation_Receipt_' + donation.receipt_no + '.pdf');
    doc.pipe(res);

    drawWatermark(doc);
    drawHeader(doc);

    const dateStr = new Date(donation.created_at || Date.now())
      .toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
    drawReceiptTitleStrip(doc, donation.receipt_no, dateStr);

    // DONOR DETAILS
    doc.rect(40, 195, 515, 130).lineWidth(1).strokeColor('#C09040').stroke();
    doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('DONOR DETAILS', 55, 208);
    doc.moveTo(55, 222).lineTo(540, 222).lineWidth(0.5).strokeColor('#D4AF37').stroke();

    const drawField = makeDrawField(doc);
    drawField('Donor Full Name', donation.donor_name, 55, 230);
    drawField('Contact Number', donation.phone ? '+91 ' + donation.phone : 'N/A', 310, 230);
    drawField('PAN Number', donation.pan_number || 'N/A', 55, 280);
    drawField('Seva Category / Purpose', donation.category || 'Navratri Utsav Mandal Seva', 310, 280);

    // AMOUNT HIGHLIGHT
    doc.rect(40, 340, 515, 75).fill('#FFFDF0');
    doc.rect(40, 340, 515, 75).lineWidth(1.5).strokeColor('#D4AF37').stroke();
    doc.fillColor('#7B3F00').fontSize(9).font('Helvetica-Bold')
      .text('CONTRIBUTION AMOUNT RECEIVED', 0, 355, { align: 'center', width: 595 });
    doc.fillColor('#8B1A1A').fontSize(26).font('Helvetica-Bold')
      .text('Rs. ' + parseFloat(donation.amount).toLocaleString('en-IN') + '/-', 0, 372, { align: 'center', width: 595 });
    const words = amountInWords(parseFloat(donation.amount));
    doc.fillColor('#555').fontSize(9).font('Helvetica-Oblique')
      .text('(' + words + ')', 0, 400, { align: 'center', width: 595 });

    // TRANSACTION BREAKDOWN
    doc.rect(40, 430, 515, 90).lineWidth(1).strokeColor('#C09040').stroke();
    doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('TRANSACTION BREAKDOWN', 55, 443);
    doc.moveTo(55, 458).lineTo(540, 458).lineWidth(0.5).strokeColor('#D4AF37').stroke();
    drawField('Payment Mode', 'UPI / Online', 55, 466);
    drawField('Payment UTR / Ref No.', donation.payment_id || donation.payment_utr || 'N/A', 230, 466);
    doc.fillColor('#7A3B3B').fontSize(8).font('Helvetica-Bold').text('PAYMENT STATUS', 430, 466);
    const status = (donation.status || 'SUCCESS').toUpperCase();
    const statusColor = (status === 'SUCCESS' || status === 'APPROVED') ? '#166534' : '#92400E';
    const statusBg = (status === 'SUCCESS' || status === 'APPROVED') ? '#D1FAE5' : '#FEF3C7';
    doc.rect(430, 479, 70, 18).fill(statusBg);
    doc.fillColor(statusColor).fontSize(9).font('Helvetica-Bold').text(status, 435, 483);

    // BLESSING QUOTE
    doc.rect(40, 540, 515, 55).fill('#FFF9F0');
    doc.rect(40, 540, 515, 55).lineWidth(0.5).strokeColor('#D4AF37').stroke();
    doc.fillColor('#7B1A1A').fontSize(9).font('Helvetica-Oblique')
      .text('"Maulichya krupaprasadane aapachya kutumbavar sadaiv sukh, samruddhi aani aarogya labho."', 55, 553, { align: 'center', width: 485 });
    doc.fillColor('#6B5C3E').fontSize(8).font('Helvetica')
      .text('All donations support sacred Navratri festival celebrations, cultural programs, and social welfare activities.', 55, 572, { align: 'center', width: 485 });

    // FOOTER
    doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('Dagdi Chawl Navratrotsav Mandal', 55, 630);
    doc.fillColor('#555').fontSize(8).font('Helvetica').text('This is a computer-generated receipt for online contribution.', 55, 644);
    doc.fillColor('#555').fontSize(8).font('Helvetica').text('No physical signature required.', 55, 656);
    doc.moveTo(380, 668).lineTo(540, 668).lineWidth(0.5).strokeColor('#999').stroke();
    doc.fillColor('#555').fontSize(9).font('Helvetica').text('Authorized Trustee / Treasurer', 380, 673);
    doc.fillColor('#aaa').fontSize(7.5).font('Helvetica')
      .text('Jai Aai Mauli  |  dagdichawlichiaaimauli.in  |  Instagram: @dagdichawlichiaaimauli', 40, 800, { align: 'center', width: 515 });

    doc.end();
  },

  // 2. T-SHIRT RECEIPT for /download-tshirt-receipt/:id
  generateTshirtPDF(order, res) {
    const doc = new PDFDocument({ size: 'A4', margin: 40 });
    res.setHeader('Content-Type', 'application/pdf');
    res.setHeader('Content-Disposition', 'attachment; filename=DCM_TShirt_Token_' + order.receipt_no + '.pdf');
    doc.pipe(res);

    drawWatermark(doc);
    drawHeader(doc);

    const dateStr = new Date(order.created_at || Date.now())
      .toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });

    // T-Shirt title strip
    doc.rect(40, 155, 515, 30).fill('#FFF8F0');
    doc.rect(40, 155, 515, 30).lineWidth(1).strokeColor('#C09040').stroke();
    doc.fillColor('#7B1A1A').fontSize(11).font('Helvetica-Bold').text('OFFICIAL T-SHIRT BOOKING TOKEN', 55, 165);
    doc.fillColor('#444').fontSize(9).font('Helvetica')
      .text('Token No: ' + order.receipt_no + '    Date: ' + dateStr, 55, 165, { align: 'right', width: 485 });

    // BUYER DETAILS
    doc.rect(40, 195, 515, 130).lineWidth(1).strokeColor('#C09040').stroke();
    doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('BUYER DETAILS', 55, 208);
    doc.moveTo(55, 222).lineTo(540, 222).lineWidth(0.5).strokeColor('#D4AF37').stroke();

    const drawField = makeDrawField(doc);
    drawField('Buyer Full Name', order.buyer_name, 55, 230);
    drawField('Contact Mobile', order.phone ? '+91 ' + order.phone : 'N/A', 310, 230);
    drawField('Selected Size', order.size || 'N/A', 55, 280);
    drawField('Color & Quantity', (order.color || 'N/A') + ' - ' + (order.quantity || 1) + ' Pc(s)', 310, 280);

    // AMOUNT
    doc.rect(40, 340, 515, 70).fill('#FFFDF0');
    doc.rect(40, 340, 515, 70).lineWidth(1.5).strokeColor('#D4AF37').stroke();
    doc.fillColor('#7B3F00').fontSize(9).font('Helvetica-Bold')
      .text('TOTAL AMOUNT PAID FOR T-SHIRT', 0, 353, { align: 'center', width: 595 });
    doc.fillColor('#8B1A1A').fontSize(26).font('Helvetica-Bold')
      .text('Rs. ' + parseFloat(order.total_amount || 0).toLocaleString('en-IN') + '/-', 0, 370, { align: 'center', width: 595 });

    // PICKUP INSTRUCTIONS
    doc.rect(40, 425, 515, 115).fill('#F0F8FF');
    doc.rect(40, 425, 515, 115).lineWidth(1).strokeColor('#93C5FD').stroke();
    doc.fillColor('#1E40AF').fontSize(10).font('Helvetica-Bold').text('T-SHIRT PICKUP INSTRUCTIONS', 55, 440);
    const instructions = [
      '1. Show this PDF token (digital or printed) at the Mandap Merchandise Desk.',
      '2. Pickup: Dagdi Chawl, B.J. Marg, Byculla West, Mumbai - 400011.',
      '3. For courier delivery queries, contact us via Instagram: @dagdichawlichiaaimauli',
      '4. Keep this receipt safe until you collect your T-Shirt.',
    ];
    let instY = 458;
    instructions.forEach(function(inst) {
      doc.fillColor('#1E3A8A').fontSize(9).font('Helvetica').text(inst, 55, instY, { width: 475 });
      instY += 18;
    });

    // FOOTER
    doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('Dagdi Chawl Navratrotsav Mandal', 55, 580);
    doc.fillColor('#555').fontSize(8).font('Helvetica').text('Computer-generated booking token. No physical signature required.', 55, 594);
    doc.moveTo(380, 616).lineTo(540, 616).lineWidth(0.5).strokeColor('#999').stroke();
    doc.fillColor('#555').fontSize(9).font('Helvetica').text('Authorized Trustee / Treasurer', 380, 621);
    doc.fillColor('#aaa').fontSize(7.5).font('Helvetica')
      .text('Jai Aai Mauli  |  dagdichawlichiaaimauli.in  |  Instagram: @dagdichawlichiaaimauli', 40, 800, { align: 'center', width: 515 });

    doc.end();
  },

  // 3. DONATION EMAIL BUFFER for email after admin approval
  generateDonationPDFBuffer(donation) {
    return new Promise(function(resolve, reject) {
      const doc = new PDFDocument({ size: 'A4', margin: 40 });
      const buffers = [];
      doc.on('data', function(chunk) { buffers.push(chunk); });
      doc.on('end', function() { resolve(Buffer.concat(buffers)); });
      doc.on('error', function(err) { reject(err); });

      drawWatermark(doc);
      drawHeader(doc);

      const dateStr = new Date(donation.created_at || Date.now())
        .toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
      drawReceiptTitleStrip(doc, donation.receipt_no, dateStr);

      // DONOR DETAILS
      doc.rect(40, 195, 515, 130).lineWidth(1).strokeColor('#C09040').stroke();
      doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('DONOR DETAILS', 55, 208);
      doc.moveTo(55, 222).lineTo(540, 222).lineWidth(0.5).strokeColor('#D4AF37').stroke();

      const drawField = makeDrawField(doc);
      drawField('Donor Full Name', donation.donor_name, 55, 230);
      drawField('Contact Number', donation.phone ? '+91 ' + donation.phone : 'N/A', 310, 230);
      drawField('Email Address', donation.email || 'N/A', 55, 280);
      drawField('Payment UTR / Ref No.', donation.payment_id || donation.payment_utr || 'N/A', 310, 280);
      drawField('Payment Status', 'APPROVED (SUCCESS)', 55, 315);
      drawField('Verification', 'MANDAL ADMIN VERIFIED', 310, 315);

      // AMOUNT
      doc.rect(40, 340, 515, 75).fill('#FFFDF0');
      doc.rect(40, 340, 515, 75).lineWidth(1.5).strokeColor('#D4AF37').stroke();
      doc.fillColor('#7B3F00').fontSize(9).font('Helvetica-Bold')
        .text('CONTRIBUTION AMOUNT RECEIVED', 0, 355, { align: 'center', width: 595 });
      doc.fillColor('#8B1A1A').fontSize(26).font('Helvetica-Bold')
        .text('Rs. ' + parseFloat(donation.amount).toLocaleString('en-IN') + '/-', 0, 372, { align: 'center', width: 595 });
      const words = amountInWords(parseFloat(donation.amount));
      doc.fillColor('#555').fontSize(9).font('Helvetica-Oblique')
        .text('(' + words + ')', 0, 400, { align: 'center', width: 595 });

      // BLESSING
      doc.rect(40, 435, 515, 55).fill('#FFF9F0');
      doc.rect(40, 435, 515, 55).lineWidth(0.5).strokeColor('#D4AF37').stroke();
      doc.fillColor('#7B1A1A').fontSize(9).font('Helvetica-Oblique')
        .text('"Maulichya krupaprasadane aapachya kutumbavar sadaiv sukh, samruddhi aani aarogya labho."', 55, 448, { align: 'center', width: 485 });
      doc.fillColor('#6B5C3E').fontSize(8).font('Helvetica')
        .text('All donations support sacred Navratri festival celebrations, cultural programs, and social welfare activities.', 55, 468, { align: 'center', width: 485 });

      // FOOTER
      doc.fillColor('#7B1A1A').fontSize(10).font('Helvetica-Bold').text('Dagdi Chawl Navratrotsav Mandal', 55, 540);
      doc.fillColor('#555').fontSize(8).font('Helvetica')
        .text('This is a computer-generated receipt for online contribution. No physical signature required.', 55, 554);
      doc.moveTo(380, 576).lineTo(540, 576).lineWidth(0.5).strokeColor('#999').stroke();
      doc.fillColor('#555').fontSize(9).font('Helvetica').text('Authorized Trustee / Treasurer', 380, 581);
      doc.fillColor('#aaa').fontSize(7.5).font('Helvetica')
        .text('Jai Aai Mauli  |  dagdichawlichiaaimauli.in  |  Instagram: @dagdichawlichiaaimauli', 40, 800, { align: 'center', width: 515 });

      doc.end();
    });
  }
};

// Utility: convert number to Indian English words
function amountInWords(num) {
  if (!num || isNaN(num)) return 'Amount Not Available';
  var a = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
    'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'];
  var b = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];
  function inWords(n) {
    if (n < 20) return a[n];
    if (n < 100) return b[Math.floor(n/10)] + (n%10 ? ' ' + a[n%10] : '');
    if (n < 1000) return a[Math.floor(n/100)] + ' Hundred' + (n%100 ? ' ' + inWords(n%100) : '');
    if (n < 100000) return inWords(Math.floor(n/1000)) + ' Thousand' + (n%1000 ? ' ' + inWords(n%1000) : '');
    if (n < 10000000) return inWords(Math.floor(n/100000)) + ' Lakh' + (n%100000 ? ' ' + inWords(n%100000) : '');
    return inWords(Math.floor(n/10000000)) + ' Crore' + (n%10000000 ? ' ' + inWords(n%10000000) : '');
  }
  var rupees = Math.floor(num);
  var paise = Math.round((num - rupees) * 100);
  var result = 'Rupees ' + inWords(rupees) + ' Only';
  if (paise > 0) result += ' and ' + inWords(paise) + ' Paise';
  return result;
}
