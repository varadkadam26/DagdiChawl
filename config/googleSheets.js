const { google } = require('googleapis');
const path = require('path');
const fs = require('fs');
require('dotenv').config();

const SCOPES = ['https://www.googleapis.com/auth/spreadsheets'];
const CREDENTIALS_PATH = path.join(__dirname, '..', 'credentials.json');
const SPREADSHEET_ID = process.env.GOOGLE_SHEET_ID || '';

// Tab definitions with their headers
const TABS = {
  DONATION: {
    name: 'Donations',
    headers: ['Receipt No', 'Donor Name', 'Phone', 'Email', 'Amount (₹)', 'Category', 'PAN Number', 'Payment ID', 'Order ID', 'Status', 'Date & Time']
  },
  CONTACT: {
    name: 'Contact Us',
    headers: ['Name', 'Contact (Email/Phone)', 'Message', 'Date & Time']
  }
};
let sheetsClient = null;
let initPromise = null;

async function getClient() {
  if (sheetsClient) return sheetsClient;

  if (initPromise) return initPromise;

  initPromise = (async () => {
    try {
      let authOptions = { scopes: SCOPES };

      if (process.env.GOOGLE_CREDENTIALS) {
        // Production: load credentials from env var (JSON string)
        const credentials = JSON.parse(process.env.GOOGLE_CREDENTIALS);
        if (credentials.private_key) {
          credentials.private_key = credentials.private_key.replace(/\\n/g, '\n');
        }
        authOptions.credentials = credentials;
      } else if (fs.existsSync(CREDENTIALS_PATH)) {
        // Local dev: load from file
        authOptions.keyFile = CREDENTIALS_PATH;
      } else {
        console.log('⚠️ No Google credentials found (no file or env var). Sheets sync disabled.');
        initPromise = null;
        return null;
      }

      const auth = new google.auth.GoogleAuth(authOptions);
      const authClient = await auth.getClient();
      sheetsClient = google.sheets({ version: 'v4', auth: authClient });
      console.log('✅ Google Sheets API client authenticated successfully.');
      return sheetsClient;
    } catch (err) {
      console.error('⚠️ Google Sheets authentication failed:', err.message);
      initPromise = null;
      return null;
    }
  })();

  return initPromise;
}

async function ensureTabs() {
  if (!SPREADSHEET_ID) {
    console.log('⚠️ GOOGLE_SHEET_ID not set in .env — skipping Google Sheets sync.');
    return false;
  }

  const client = await getClient();
  if (!client) return false;

  try {
    const spreadsheet = await client.spreadsheets.get({ spreadsheetId: SPREADSHEET_ID });
    const existingSheets = spreadsheet.data.sheets.map(s => s.properties.title);

    for (const tab of Object.values(TABS)) {
      if (!existingSheets.includes(tab.name)) {
        await client.spreadsheets.batchUpdate({
          spreadsheetId: SPREADSHEET_ID,
          requestBody: {
            requests: [{
              addSheet: {
                properties: { title: tab.name }
              }
            }]
          }
        });

        await client.spreadsheets.values.update({
          spreadsheetId: SPREADSHEET_ID,
          range: `'${tab.name}'!A1`,
          valueInputOption: 'RAW',
          requestBody: {
            values: [tab.headers]
          }
        });

        console.log(`✅ Created Google Sheet tab: "${tab.name}" with headers.`);
      }
    }

    return true;
  } catch (err) {
    console.error('⚠️ Error ensuring Google Sheet tabs:', err.message);
    return false;
  }
}

async function appendRow(tabName, rowData) {
  if (!SPREADSHEET_ID) return;

  const client = await getClient();
  if (!client) return;

  try {
    await client.spreadsheets.values.append({
      spreadsheetId: SPREADSHEET_ID,
      range: `'${tabName}'!A:Z`,
      valueInputOption: 'USER_ENTERED',
      insertDataOption: 'INSERT_ROWS',
      requestBody: {
        values: [rowData]
      }
    });
    console.log(`✅ Appended row to Google Sheet tab: "${tabName}"`);
  } catch (err) {
    console.error(`⚠️ Failed to append row to "${tabName}":`, err.message);
  }
}

async function appendDonation(donation) {
  const row = [
    donation.receipt_no || '',
    donation.donor_name || '',
    donation.phone || '',
    donation.email || '',
    donation.amount || 0,
    donation.category || '',
    donation.pan_number || '',
    donation.payment_id || '',
    donation.order_id || '',
    donation.status || 'SUCCESS',
    new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
  ];
  await appendRow(TABS.DONATION.name, row);
}

async function appendContactInquiry(contact) {
  const row = [
    contact.name || '',
    contact.email || contact.contact || '',
    contact.message || '',
    new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
  ];
  await appendRow(TABS.CONTACT.name, row);
}

async function clearAllSheetsData() {
  if (!SPREADSHEET_ID) {
    console.log('⚠️ GOOGLE_SHEET_ID not set in .env — skipping Google Sheets clear.');
    return false;
  }

  const client = await getClient();
  if (!client) return false;

  try {
    for (const tab of Object.values(TABS)) {
      await client.spreadsheets.values.clear({
        spreadsheetId: SPREADSHEET_ID,
        range: `'${tab.name}'!A2:Z1000`
      });
      console.log(`✅ Cleared data rows from Google Sheet tab: "${tab.name}"`);
    }
    return true;
  } catch (err) {
    console.error('⚠️ Error clearing Google Sheets data rows:', err.message);
    return false;
  }
}

module.exports = {
  ensureTabs,
  appendDonation,
  appendContactInquiry,
  clearAllSheetsData
};
