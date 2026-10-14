const nodemailer = require('nodemailer');
require('dotenv').config();

const SMTP_USER = process.env.SMTP_USER || '';
const SMTP_APP_PASSWORD = process.env.SMTP_APP_PASSWORD || '';

let transporter = null;

try {
  if (SMTP_USER && SMTP_APP_PASSWORD) {
    transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: SMTP_USER,
        pass: SMTP_APP_PASSWORD
      }
    });
    console.log('✅ Gmail SMTP transporter configured.');
  } else {
    console.log('⚠️ SMTP credentials not set in .env — email sending disabled.');
  }
} catch (err) {
  console.error('⚠️ SMTP transporter creation error:', err.message);
}

const MANDAL_NAME = 'Dagdi Chawlichi Aai Mauli — Byculla Navratrotsav Mandal';
const MANDAL_SHORT = 'दगडी चाळीची आई माऊली';
const MANDAL_EMAIL_FROM = `"दगडी चाळीची आई माऊली" <${SMTP_USER}>`;

/**
 * Send contact form inquiry email
 */
async function sendContactEmail({ name, email, contact, message }) {
  if (!transporter) {
    console.log('⚠️ SMTP transporter not available — skipping email.');
    return false;
  }

  const userEmail = (email || contact || '').trim();
  const toAddresses = ['byculladagadichawlnavratri1973@gmail.com', SMTP_USER];
  const isEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userEmail);
  const ccList = isEmail ? [userEmail] : [];

  const htmlBody = `
    <div style="font-family:'Segoe UI',Arial,sans-serif;max-width:600px;margin:0 auto;border:2px solid #C0972D;border-radius:12px;overflow:hidden;">
      <div style="background:linear-gradient(135deg,#7B1A1A,#5C0015);padding:24px;text-align:center;">
        <h2 style="color:#F5D98E;margin:0;font-size:22px;">🙏 नवीन संपर्क संदेश</h2>
        <p style="color:#E8C86E;margin:6px 0 0;font-size:14px;">New Contact Inquiry — ${MANDAL_NAME}</p>
      </div>
      <div style="padding:28px;background:#FFF9F0;">
        <table style="width:100%;border-collapse:collapse;">
          <tr>
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;width:140px;vertical-align:top;">नाव / Name:</td>
            <td style="padding:10px 12px;color:#333;">${name}</td>
          </tr>
          <tr style="background:#FEF3E2;">
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;vertical-align:top;">ईमेल / Email:</td>
            <td style="padding:10px 12px;color:#333;">${userEmail}</td>
          </tr>
          <tr>
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;vertical-align:top;">संदेश / Message:</td>
            <td style="padding:10px 12px;color:#333;line-height:1.6;">${message.replace(/\n/g, '<br>')}</td>
          </tr>
        </table>
      </div>
      <div style="background:#7B1A1A;padding:14px;text-align:center;">
        <p style="color:#E8C86E;margin:0;font-size:12px;">${MANDAL_SHORT} | भायखळा, मुंबई | जय आई माऊली 🙏</p>
      </div>
    </div>
  `;

  const mailOptions = {
    from: MANDAL_EMAIL_FROM,
    to: toAddresses.join(', '),
    cc: ccList.length ? ccList.join(', ') : undefined,
    subject: `नवीन संपर्क संदेश — ${name} | दगडी चाळीची आई माऊली`,
    html: htmlBody
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('✅ Contact email sent:', info.messageId);
    return true;
  } catch (err) {
    console.error('⚠️ Failed to send contact email:', err.message);
    return false;
  }
}

/**
 * Send donation approval email with PDF receipt attached
 */
async function sendDonationApprovalEmail(donation, pdfBuffer) {
  if (!transporter) {
    console.log('⚠️ SMTP transporter not available — skipping email.');
    return false;
  }

  const donorEmail = (donation.email || '').trim();
  if (!donorEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(donorEmail)) {
    console.log('⚠️ Invalid or missing donor email — skipping email dispatch.');
    return false;
  }

  const htmlBody = `
    <div style="font-family:'Segoe UI',Arial,sans-serif;max-width:600px;margin:0 auto;border:2px solid #C0972D;border-radius:12px;overflow:hidden;">
      <div style="background:linear-gradient(135deg,#7B1A1A,#5C0015);padding:24px;text-align:center;">
        <h2 style="color:#F5D98E;margin:0;font-size:22px;">🌺 देणगी पावती मंजूर!</h2>
        <p style="color:#E8C86E;margin:6px 0 0;font-size:14px;">Donation Approved — दगडी चाळीची आई माऊली</p>
      </div>
      <div style="padding:28px;background:#FFF9F0;">
        <p style="font-size:16px;color:#7B1A1A;font-weight:700;margin-top:0;">जय आई माऊली! सस्नेह नमस्कार ${donation.donor_name},</p>
        <p style="color:#333;line-height:1.6;">भायखळा दगडी चाळ सार्वजनिक नवरात्रौत्सव मंडळाला आपण दिलेल्या <strong>₹ ${parseFloat(donation.amount).toLocaleString('en-IN')}</strong> च्या देणगीची यशस्वी पडताळणी झाली असून आपली अधिकृत PDF पावती या ईमेलसोबत जोडलेली (Attached) आहे.</p>

        <table style="width:100%;border-collapse:collapse;margin:20px 0;background:#FFFFFF;border:1px solid #E8C86E;border-radius:8px;">
          <tr>
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;width:160px;">पावती क्र. / Receipt No:</td>
            <td style="padding:10px 12px;color:#333;font-weight:700;">${donation.receipt_no}</td>
          </tr>
          <tr style="background:#FEF3E2;">
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;">देणगीदार / Donor:</td>
            <td style="padding:10px 12px;color:#333;">${donation.donor_name}</td>
          </tr>
          <tr>
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;">रक्कम / Amount:</td>
            <td style="padding:10px 12px;color:#7B1A1A;font-size:18px;font-weight:800;">₹ ${parseFloat(donation.amount).toLocaleString('en-IN')}</td>
          </tr>
          <tr style="background:#FEF3E2;">
            <td style="padding:10px 12px;font-weight:700;color:#7B1A1A;">UTR No / Ref:</td>
            <td style="padding:10px 12px;color:#333;font-family:monospace;">${donation.payment_id || donation.payment_utr || 'N/A'}</td>
          </tr>
        </table>

        <p style="color:#555;font-size:14px;line-height:1.6;">माऊलीचा आशीर्वाद आपल्या व आपल्या कुटुंबावर सदैव राहो हीच आई माऊलीच्या चरणी प्रार्थना! 🙏</p>
      </div>
      <div style="background:#7B1A1A;padding:14px;text-align:center;">
        <p style="color:#E8C86E;margin:0;font-size:12px;">${MANDAL_SHORT} | भायखळा, मुंबई | dagdichawlichiaaimauli.in 🙏</p>
      </div>
    </div>
  `;

  const mailOptions = {
    from: MANDAL_EMAIL_FROM,
    to: donorEmail,
    subject: `देणगी पावती — ${donation.receipt_no} | दगडी चाळीची आई माऊली`,
    html: htmlBody,
    attachments: [
      {
        filename: `DagdiChawl_Donation_Receipt_${donation.receipt_no}.pdf`,
        content: pdfBuffer,
        contentType: 'application/pdf'
      }
    ]
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('✅ Donation approval email sent to', donorEmail, ':', info.messageId);
    return true;
  } catch (err) {
    console.error('⚠️ Failed to send donation email to', donorEmail, ':', err.message);
    return false;
  }
}

module.exports = {
  sendContactEmail,
  sendDonationApprovalEmail
};
