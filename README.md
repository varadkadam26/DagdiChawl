# 🙏 Dagdi Chawl Chi Aai Mauli — Official Website & Backend

> **भायखळा दगडी चाळ सार्वजनिक नवरात्रोत्सव मंडळ | Est. 1973 | Mumbai, Maharashtra**

The official website and backend management system for **Dagdi Chawl Chi Aai Mauli** — one of Mumbai's most iconic Ganpati mandals. Built with Node.js, Express, EJS, and integrated with Razorpay payments, Google Sheets real-time sync, Gmail SMTP, Twilio SMS, and PDFKit receipt generation.

---

## 🌟 Features

### 🎪 Public Website
| Feature | Description |
|---------|-------------|
| **Home & Hero** | Grand carousel showcase with GSAP animations, live yatra status, and mandal highlights |
| **About** | Mandal history since 1973, mission, and vision |
| **Glimpses Gallery** | Decade-wise photo gallery (1990–2025) with lightbox viewer |
| **Social Work** | Documentation of mandal's community service — food distribution, blind school visits, rain relief |
| **Festival Schedule** | Day-by-day Ganeshotsav event schedule with live status API |
| **Executive Committee** | Photo cards of all mandal committee members with designations |
| **Advertisement** | Digital advertising information and brochure download |
| **Contact Us** | Contact form with SMTP email delivery + embedded Google Maps |

- Official Collar Polo T-Shirt booking with size selection (Kids + Adults)
- **Razorpay payment gateway** integration — payment before receipt
- Auto-generated PDF pickup token receipt via PDFKit

### 💰 Online Donation Portal (`/donate`)
- Preset amounts (₹501, ₹1008, ₹2100, ₹5001) + custom amount
- **Razorpay checkout** with live order creation
-  Tax Exemption PDF receipt with PAN details
- Twilio SMS confirmation to donor
- Real-time sync to **Google Sheets** ("Donations" tab)

### 📬 Contact Form (`/contact`)
- Email sent via **Gmail SMTP** (Nodemailer)
  - **From**: `mitramsolutions@gmail.com`
  - **To**: `byculladagadichawlnavratri1973@gmail.com`
  - **CC**: User's email (if provided)
- Real-time sync to **Google Sheets** ("Contact Us" tab)

### 📊 Google Sheets Live Sync
All form submissions (T-Shirts, Donations, Contact) are automatically appended to a shared Google Spreadsheet using a **Google Cloud Service Account** — enabling the mandal committee to track everything in real-time without accessing the admin panel.

### 🔐 Admin Panel (`/admin`)
- Password-protected dashboard
- Real-time metrics — total donations, t-shirt orders, system logs
- Excel upload/export for offline records
- Combined online + offline data export

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Runtime** | Node.js (v18+) |
| **Framework** | Express.js |
| **Templating** | EJS (Embedded JavaScript) |
| **Database** | MySQL2 (with in-memory fallback for demo/offline mode) |
| **Payments** | Razorpay SDK |
| **Email** | Nodemailer (Gmail SMTP) |
| **SMS** | Twilio API |
| **PDF Generation** | PDFKit |
| **Spreadsheet Sync** | Google Sheets API v4 (Service Account) |
| **Excel Processing** | ExcelJS |
| **Scheduled Jobs** | node-cron |
| **Styling** | Vanilla CSS3 (Custom design system, Google Fonts — Outfit & Inter) |
| **Deployment** | Vercel (Serverless) |

---

## 📁 Project Structure

```
mmmdagdichawl/
├── server.js                    # Express app entry point
├── package.json                 # Dependencies & scripts
├── vercel.json                  # Vercel serverless deployment config
├── credentials.json             # Google Service Account key (gitignored)
├── .env                         # Environment variables (gitignored)
│
├── config/
│   ├── db.js                    # MySQL + in-memory fallback data store
│   ├── razorpay.js              # Razorpay SDK setup & order creation
│   ├── twilio.js                # Twilio SMS client
│   ├── googleSheets.js          # Google Sheets API client (3-tab sync)
│   ├── mailer.js                # Nodemailer Gmail SMTP transport
│   └── cron.js                  # Background scheduled jobs
│
├── controllers/
│   ├── yatraController.js       # Home, About, Schedule, Glimpses, Social Work, Committee
│   ├── donationController.js    # Donation CRUD + Razorpay + Sheets sync
│   ├── tshirtController.js      # T-Shirt booking + Razorpay + Sheets sync
│   ├── contactController.js     # Contact form + SMTP email + Sheets sync
│   ├── pdfController.js         # PDF receipt generation (Donation  + T-Shirt token)
│   ├── adminController.js       # Admin auth & dashboard
│   └── excelController.js       # Excel upload, parse, export (offline records)
│
├── routes/
│   ├── indexRoutes.js           # Public pages + T-Shirt + Contact routes
│   ├── donationRoutes.js        # Donation API routes
│   ├── adminRoutes.js           # Admin panel routes
│   └── excelRoutes.js           # Excel management routes
│
├── views/
│   ├── index.ejs                # Homepage
│   ├── about.ejs                # About mandal
│   ├── donate.ejs               # Donation portal
│   ├── tshirt.ejs               # T-Shirt booking
│   ├── contact.ejs              # Contact form + Google Maps
│   ├── schedule.ejs             # Festival schedule
│   ├── glimpses.ejs             # Photo gallery
│   ├── social-work.ejs          # Social work showcase
│   ├── committee.ejs            # Executive committee
│   ├── advertisement.ejs        # Advertisement info
│   ├── partials/
│   │   ├── header.ejs           # Shared navigation & head
│   │   └── footer.ejs           # Shared footer
│   └── admin/
│       ├── login.ejs            # Admin login
│       ├── dashboard.ejs        # Admin dashboard
│       └── excel.ejs            # Excel management panel
│
├── public/
│   ├── css/style.css            # Complete design system
│   ├── js/
│   │   ├── main.js              # Global JS (animations, i18n toggle)
│   │   ├── i18n.js              # Marathi/English language switcher
│   │   ├── donate.js            # Donation page logic
│   │   └── pass-form.js         # Pass registration logic
│   ├── images/                  # All website images (Ganpati, committee, glimpses, etc.)
│   └── docs/                    # Downloadable documents (brochure PDF)
│
├── receipts/                    # Generated PDF receipts (gitignored)
└── logs/                        # Application logs (gitignored)
```

---

## 🚀 Getting Started

### Prerequisites
- **Node.js** v18 or higher
- **npm** (comes with Node.js)
- **MySQL** (optional — app runs with in-memory data store if unavailable)

### 1. Clone & Install

```bash
git clone https://github.com/varadkadam26/mmmdagdichawl.git
cd mmmdagdichawl
npm install
```

### 2. Environment Setup

Create a `.env` file in the project root:

```env
# Google Sheets Sync
GOOGLE_SHEET_ID=your_google_sheet_id_here

# Gmail SMTP (Contact Form Emails)
SMTP_USER=mitramsolutions@gmail.com
SMTP_APP_PASSWORD=your_gmail_app_password_here

# Razorpay (Payment Gateway)
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret

# MySQL Database (Optional)
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=dagdichawl_db
DB_PORT=3306

# Twilio SMS (Optional)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
```

### 3. Google Sheets Setup

1. Place your Google Cloud **Service Account** `credentials.json` in the project root
2. Create a Google Spreadsheet and share it with the service account email as **Editor**
3. Set the `GOOGLE_SHEET_ID` in `.env` (extract from the spreadsheet URL)

### 4. Run the Server

```bash
# Development
npm run dev

# Production
npm start
```

Open **http://localhost:3000** in your browser.

---

## 🌐 Deployment (Vercel)

The project includes a `vercel.json` for one-click Vercel deployment:

```bash
npm i -g vercel
vercel --prod
```

Set the environment variables in the Vercel dashboard under **Settings → Environment Variables**.

---

## 📊 Google Sheets Integration

The app syncs data in real-time to a shared Google Spreadsheet with 3 tabs:

| Tab | Triggered When | Columns |
|-----|----------------|---------|
| **Donations** | New donation payment verified | Receipt No, Name, Phone, Email, Amount, Category, PAN, Payment ID, Order ID, Status, Date |
| **Contact Us** | Contact form submitted | Name, Contact, Message, Date |

---

## 📱 Pages & Routes

| Route | Page | Description |
|-------|------|-------------|
| `/` | Home | Hero carousel, highlights, live status |
| `/about` | About | Mandal history & mission |
| `/donate` | Donations | Razorpay payment +  receipt |
| `/contact` | Contact Us | SMTP email form + Google Maps |
| `/schedule` | Schedule | Festival day-by-day events |
| `/glimpses` | Gallery | Decade-wise photo archive |
| `/social-work` | Social Work | Community service showcase |
| `/committee` | Committee | Executive members directory |
| `/admin` | Admin Panel | Protected dashboard |
| `/admin/excel` | Excel Manager | Upload/export offline records |

---

## 🔗 Social & Contact

| Platform | Link |
|----------|------|
| 🌐 **Location** | Bapurao Jagtap Marg (BJ Marg), Byculla West, Mumbai, Maharashtra 400011 |
| 📧 **Email** | byculladagadichawlnavratri1973@gmail.com |
| 📧 **Marketing** | byculladagadichawlnavratri1973@gmail.com |
| 📞 **Helpline** | +91 95945 12999 |
| 📺 **YouTube** | [#dagdichawl](https://www.youtube.com/hashtag/dagdichawl) |
| 📸 **Instagram** | [@dagdichawlichiaaimauli](https://www.instagram.com/dagdichawlichiaaimauli/) |
| 📘 **Facebook** | [@dagdichawlichiaaimauli](https://www.facebook.com/dagdichawlichiaaimauli) |

---

## 📄 License

ISC License. Built for **Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal**, Dagdi Chawl, Mumbai.

****
