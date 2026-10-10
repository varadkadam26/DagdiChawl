require('dotenv').config();

// In-memory fallback data store for offline / demo execution
const mockStore = {
  passes: [],
  donations: [],
  offline_excel_sheets: [],
  offline_excel_rows: [],
  yatra_status: {
    current_day: 3,
    total_days: 10,
    current_location: 'Tulsiwadi Pandal, Dagdi Chawl (Mandap Darshan Open)',
    next_location: 'Maha Aarti & Evening Mahaprasad (8:00 PM)',
    distance_covered_km: 100,
    total_distance_km: 100,
    active_varkaris: 35000,
    meals_served_today: 18500,
    last_updated: new Date()
  },
  logs: [
    { id: 1, type: 'SYSTEM', message: 'Dagdi Chawl Chi Aai Mauli Portal Initialized', timestamp: new Date() }
  ]
};

async function initDB() {
  console.log('✅ Running with high-performance In-Memory Data Store (Google Sheets backed). MySQL omitted.');
}

function safeJsonParse(value, fallback) {
  try { return JSON.parse(value); } catch (e) { return fallback; }
}

// Data Access API
module.exports = {
  initDB,
  isMock: () => true,
  mockStore,

  async getPasses() {
    return mockStore.passes;
  },

  async getPassByCode(code) {
    return mockStore.passes.find(p => p.pass_code.toUpperCase() === code.toUpperCase());
  },

  async getPassByPhone(phone) {
    return mockStore.passes.find(p => p.phone === phone);
  },

  async createPass(passData) {
    const newPass = {
      id: mockStore.passes.length + 1,
      ...passData,
      created_at: new Date()
    };
    mockStore.passes.unshift(newPass);
    return newPass;
  },

  async getDonations() {
    return mockStore.donations;
  },

  async getDonationByReceipt(receiptNo) {
    return mockStore.donations.find(d => d.receipt_no.toUpperCase() === receiptNo.toUpperCase());
  },

  async createDonation(donationData) {
    const newDonation = {
      id: mockStore.donations.length + 1,
      ...donationData,
      created_at: new Date()
    };
    mockStore.donations.unshift(newDonation);
    return newDonation;
  },

  async updateDonationStatus(receiptNo, status) {
    const d = mockStore.donations.find(item => item.receipt_no.toUpperCase() === receiptNo.toUpperCase());
    if (d) {
      d.status = status;
    }
    return d;
  },

  async getOfflineExcelSheets() {
    return mockStore.offline_excel_sheets || [];
  },

  async getOfflineExcelRows(sheetId = null) {
    const rows = mockStore.offline_excel_rows || [];
    return sheetId ? rows.filter(r => Number(r.sheet_id) === Number(sheetId)) : rows;
  },

  async getOfflineRecords(recordType = null) {
    const sheets = await this.getOfflineExcelSheets();
    const filteredSheets = recordType ? sheets.filter(s => s.record_type === recordType) : sheets;
    const result = [];
    for (const sheet of filteredSheets) {
      const rows = await this.getOfflineExcelRows(sheet.id);
      for (const row of rows) result.push({ ...row, sheet_name: sheet.sheet_name, record_type: sheet.record_type, columns: sheet.columns });
    }
    return result;
  },

  async createOfflineExcelSheet({ sheet_name, record_type, original_filename, columns, rows }) {
    const sheetId = (mockStore.offline_excel_sheets || []).length + 1;
    const sheet = {
      id: sheetId,
      sheet_name,
      record_type,
      original_filename,
      columns,
      uploaded_at: new Date()
    };
    mockStore.offline_excel_sheets.unshift(sheet);
    for (const row of rows) {
      mockStore.offline_excel_rows.push({
        id: mockStore.offline_excel_rows.length + 1,
        sheet_id: sheetId,
        row_number: row.row_number,
        data: row.data,
        amount: row.amount || 0,
        quantity: row.quantity || 1,
        created_at: new Date()
      });
    }
    return sheet;
  },

  async deleteOfflineExcelSheet(sheetId) {
    mockStore.offline_excel_sheets = (mockStore.offline_excel_sheets || []).filter(s => Number(s.id) !== Number(sheetId));
    mockStore.offline_excel_rows = (mockStore.offline_excel_rows || []).filter(r => Number(r.sheet_id) !== Number(sheetId));
    return true;
  },

  async getOfflineDonations() {
    return this.getOfflineRecords('donation');
  },

  getYatraStatus() {
    return mockStore.yatra_status;
  },

  addLog(type, message) {
    const log = { id: mockStore.logs.length + 1, type, message, timestamp: new Date() };
    mockStore.logs.unshift(log);
    return log;
  },

  getLogs() {
    return mockStore.logs;
  },

  async clearAllData() {
    mockStore.passes = [];
    mockStore.donations = [];
    mockStore.offline_excel_sheets = [];
    mockStore.offline_excel_rows = [];
  }
};
