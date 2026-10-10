const db = require('../config/db');

// Ganeshotsav Event Schedule Data for Dagdi Chawl Chi Aai Mauli
const SCHEDULE_LOCATION_EN = 'Bapurao Jagtap Marg, Byculla West, Mumbai-400011';
const SCHEDULE_LOCATION_MR = 'बापूराव जगताप मार्ग (बी.जे. मार्ग), भायखळा पश्चिम, मुंबई, महाराष्ट्र ४०००११';

const scheduleData = [
  { day:2, dateMr:'रविवार, ११-१०-२०२६', dateEn:'Sunday, 11-10-2026', titleMr:'घटस्थापना', titleEn:'Ghatasthapana', timeMr:'सकाळी ९:०० वा.', timeEn:'9:00 AM', bg: '#F47F24', color: '#FFFFFF' },
  { day:3, dateMr:'सोमवार, १२-१०-२०२६', dateEn:'Monday, 12-10-2026', titleMr:'आरती', titleEn:'Aarti', timeMr:'सकाळी ९:०० वा. / रात्री ८:०० वा.', timeEn:'9:00 AM / 8:00 PM', bg: '#FFFFFF', color: '#D32F2F' },
  { day:4, dateMr:'मंगळवार, १३-१०-२०२६', dateEn:'Tuesday, 13-10-2026', titleMr:'आरती / वेशभूषा स्पर्धा व रासगरबा', titleEn:'Aarti / Fancy Dress Competition & Rasgarba', timeMr:'सकाळी ९:०० वा. / रात्री ८:०० वा.', timeEn:'9:00 AM / 8:00 PM', bg: '#D32F2F', color: '#FFFFFF' },
  { day:5, dateMr:'बुधवार, १४-१०-२०२६', dateEn:'Wednesday, 14-10-2026', titleMr:'आरती / आरतीनंतर होम मिनिस्टर', titleEn:'Aarti / Home Minister (After Aarti)', timeMr:'सकाळी ९:०० वा. / रात्री ८:०० वा.', timeEn:'9:00 AM / 8:00 PM', bg: '#2B3B96', color: '#FFFFFF' },
  { day:6, dateMr:'गुरुवार, १५-१०-२०२६', dateEn:'Thursday, 15-10-2026', titleMr:'विभागातील देवीच्या ओटी भरण्याचा कार्यक्रम', titleEn:'Devi Oti Bharan Program for the Division', timeMr:'रात्री आरतीनंतर', timeEn:'After Night Aarti', bg: '#FDD835', color: '#D32F2F' },
  { day:7, dateMr:'शुक्रवार, १६-१०-२०२६', dateEn:'Friday, 16-10-2026', titleMr:'श्री. श्रावणबाळ प्रस्तुत "झाले तुझे दर्शन साई" साईलीला मंडळ', titleEn:'Shri Shravanbal Presents "Zale Tujhe Darshan Sai" (Saileela Mandal)', timeMr:'रात्री आरतीनंतर', timeEn:'After Night Aarti', bg: '#4CAF50', color: '#FFFFFF' },
  { day:8, dateMr:'शनिवार, १७-१०-२०२६', dateEn:'Saturday, 17-10-2026', titleMr:'आरती / स्त्री शक्तिनारी अवतार', titleEn:'Aarti / Stree Shakti Nari Avatar', timeMr:'सकाळी ९:०० वा. / सायं. ६:०० वा.', timeEn:'9:00 AM / 6:00 PM', bg: '#5E35B1', color: '#FFFFFF' },
  { day:9, dateMr:'रविवार, १८-१०-२०२६', dateEn:'Sunday, 18-10-2026', titleMr:'हळदीकुंकू समारंभ', titleEn:'Haldi Kumkum Ceremony', timeMr:'सायं. ६:०० वा. / रात्री ८:०० वा.', timeEn:'6:00 PM / 8:00 PM', bg: '#D81B60', color: '#FFFFFF' },
  { day:10, dateMr:'सोमवार, १९-१०-२०२६', dateEn:'Monday, 19-10-2026', titleMr:'होमहवन भंडारा / "गोंधळ जगदंबेचा" / "लोकनाद कला संस्कृती परंपरा"', titleEn:'Hom Havan Bhandara / "Gondhal Jagdambecha" / "Lokanad Kala Sanskruti Parampara"', timeMr:'सकाळी ९ नंतर / दुपारी १:०० वा. / रात्री आरतीनंतर', timeEn:'After 9:00 AM / 1:00 PM / After Night Aarti', bg: '#00ACC1', color: '#FFFFFF' }
];

const jagranData = [
  { day:1, dateMr:'रविवार, ११/१०/२०२६', dateEn:'Sunday, 11/10/2026', titleMr:'नवरात्रोत्सव मंडळ', titleEn:'Navratrotsav Mandal', bg: '#F47F24', color: '#FFFFFF' },
  { day:2, dateMr:'सोमवार, १२/१०/२०२६', dateEn:'Monday, 12/10/2026', titleMr:"'गिताई'", titleEn:"'Gitai'", bg: '#FFFFFF', color: '#D32F2F' },
  { day:3, dateMr:'मंगळवार, १३/१०/२०२६', dateEn:'Tuesday, 13/10/2026', titleMr:"'ई' चाळ", titleEn:"'E' Chawl", bg: '#D32F2F', color: '#FFFFFF' },
  { day:4, dateMr:'बुधवार, १४/१०/२०२६', dateEn:'Wednesday, 14/10/2026', titleMr:"'एफ' चाळ", titleEn:"'F' Chawl", bg: '#2B3B96', color: '#FFFFFF' },
  { day:5, dateMr:'गुरुवार, १५/१०/२०२६', dateEn:'Thursday, 15/10/2026', titleMr:"'जी' चाळ", titleEn:"'G' Chawl", bg: '#FDD835', color: '#D32F2F' },
  { day:6, dateMr:'शुक्रवार, १६/१०/२०२६', dateEn:'Friday, 16/10/2026', titleMr:'नवरात्रोत्सव मंडळ', titleEn:'Navratrotsav Mandal', bg: '#4CAF50', color: '#FFFFFF' },
  { day:7, dateMr:'शनिवार, १७/१०/२०२६', dateEn:'Saturday, 17/10/2026', titleMr:"'एच' चाळ", titleEn:"'H' Chawl", bg: '#5E35B1', color: '#FFFFFF' },
  { day:8, dateMr:'रविवार, १८/१०/२०२६', dateEn:'Sunday, 18/10/2026', titleMr:"'आय' चाळ", titleEn:"'I' Chawl", bg: '#D81B60', color: '#FFFFFF' },
  { day:9, dateMr:'सोमवार, १९/१०/२०२६', dateEn:'Monday, 19/10/2026', titleMr:"'जे' चाळ", titleEn:"'J' Chawl", bg: '#00ACC1', color: '#FFFFFF' }
];

// Glimpses over a Decade (10+ Years Historical Retrospective Data)
const glimpsesData = [
  {year:'2026',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2026_new_1.jpg',descMr:'',descEn:''},
  {year:'2025',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2025_new_1.jpg',descMr:'',descEn:''},
  {year:'2025',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2025_new_2.jpg',descMr:'',descEn:''},
  {year:'2025',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2025_new_3.jpg',descMr:'',descEn:''},
  {year:'2025',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2025_new_4.jpg',descMr:'',descEn:''},
  {year:'2024',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2024_new_5.jpg',descMr:'',descEn:''},
  {year:'2024',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2024_new_2.jpg',descMr:'',descEn:''},
  {year:'2024',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2024_new_3.jpg',descMr:'',descEn:''},
  {year:'2024',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2024_new_4.jpg',descMr:'',descEn:''},
  {year:'2023',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2023_new_1.jpg',descMr:'',descEn:'', isHorizontal: true},
  {year:'2023',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2023_new_2.jpg',descMr:'',descEn:''},
  {year:'2023',category:'idols',titleMr:'',titleEn:'',themeMr:'',themeEn:'',height:'—',artistMr:'',artistEn:'',image:'/images/glimpses/2023_new_3.jpg',descMr:'',descEn:''}
];

// Social Work Data
const socialWorkData = [
  {
    id: 'tulsi-vatap',
    title: 'तुळशी वाटप - आषाढी एकादशी', titleMr: 'तुळशी वाटप - आषाढी एकादशी', titleEn: 'Tulsi Vatap - Ashadhi Ekadashi',
    category: 'Environment', categoryMr: 'पर्यावरण', categoryEn: 'Environment',
    image: '/images/tulsi_vatap.png',
    desc: 'आषाढी एकादशी निमित्त मंडळातर्फे तुळशी वाटप. प्रमुख पाहुणे श्री. अरुण भाई दुधवडकर यांच्या हस्ते भाविकांना तुळशी रोपांचे वाटप.', descMr: 'आषाढी एकादशी निमित्त मंडळातर्फे तुळशी वाटप. प्रमुख पाहुणे श्री. अरुण भाई दुधवडकर यांच्या हस्ते भाविकांना तुळशी रोपांचे वाटप.', descEn: 'Tulsi vatap from mandal on the occasion of Ashadhi Ekadashi. Special guest Mr. Arun Bhai Dudhwadkar distributed tulsi saplings to everyone.'
  },
  {
    id: 'school-kits',
    title: 'शालेय साहित्य वाटप', titleMr: 'शालेय साहित्य वाटप', titleEn: 'School Kits Distribution',
    category: 'Education', categoryMr: 'शैक्षणिक मदत', categoryEn: 'Education',
    image: '/images/school_kits.png',
    desc: 'परिसरातील सर्व विद्यार्थ्यांसाठी शालेय साहित्याचे वाटप.', descMr: 'परिसरातील सर्व विद्यार्थ्यांसाठी शालेय साहित्याचे वाटप.', descEn: 'School kits drive in our area for all the students.'
  },
  {
    id: '2017-rain-relief',
    title: '२०१७ अतिवृष्टी मदत - अन्न व निवारा', titleMr: '२०१७ अतिवृष्टी मदत - अन्न व निवारा', titleEn: '2017 Heavy Rain Relief - Food & Shelter',
    category: 'Disaster Relief', categoryMr: 'आपत्कालीन मदत', categoryEn: 'Disaster Relief',
    image: '/images/2017_rain_relief.png',
    desc: '२०१७ च्या मुसळधार पावसात गणेशोत्सवादरम्यान रेल्वे स्थानकावर अडकलेल्या नागरिकांसाठी अन्न आणि जवळच्या शाळेत निवाऱ्याची सोय.', descMr: '२०१७ च्या मुसळधार पावसात गणेशोत्सवादरम्यान रेल्वे स्थानकावर अडकलेल्या नागरिकांसाठी अन्न आणि जवळच्या शाळेत निवाऱ्याची सोय.', descEn: 'During the 2017 heavy rains in Mumbai amidst Ganeshotsav, provided meals and arranged shelter in a nearby school for people stranded at the railway station.'
  },
  {
    id: 'food-distribution-nov2025',
    title: 'भाजी गल्ली, गणेश चौक अन्नदान', titleMr: 'भाजी गल्ली, गणेश चौक अन्नदान', titleEn: 'Food Distribution at Bhajji Galli, Ganesh Chowk',
    category: 'Food Security', categoryMr: 'अन्नसुरक्षा', categoryEn: 'Food Security',
    date: 'Nov 2025', dateMr: 'नोव्हेंबर २०२५', dateEn: 'Nov 2025',
    image: '/images/food_distribution_nov2025.png',
    desc: 'भाजी गल्लीतील गणेश चौकात नागरिकांसाठी अन्न वाटपाचा उपक्रम.', descMr: 'भाजी गल्लीतील गणेश चौकात नागरिकांसाठी अन्न वाटपाचा उपक्रम.', descEn: 'Food distribution drive conducted at Bhajji Galli, near Ganesh Chowk for the local community.'
  },
  {
    id: 'escalator-request-dec2025',
    title: 'ग्रँट रोड स्टेशन एस्केलेटर मागणी', titleMr: 'ग्रँट रोड स्टेशन एस्केलेटर मागणी', titleEn: 'Grant Road Station Escalator Request',
    category: 'Civic Issue', categoryMr: 'नागरी सुविधा', categoryEn: 'Civic Issue',
    date: 'Dec 2025', dateMr: 'डिसेंबर २०२५', dateEn: 'Dec 2025',
    image: '/images/grant_road_escalator.png',
    desc: 'स्थानिक रहिवासी आणि प्रवाशांच्या सोयीसाठी ग्रँट रोड स्टेशनवर एस्केलेटर बसवण्याची मागणी करणारे पत्र रेल्वे स्टेशन मास्तर यांना देण्यात आले.', descMr: 'स्थानिक रहिवासी आणि प्रवाशांच्या सोयीसाठी ग्रँट रोड स्टेशनवर एस्केलेटर बसवण्याची मागणी करणारे पत्र रेल्वे स्टेशन मास्तर यांना देण्यात आले.', descEn: 'Submitted a formal request letter to the Railway Station Master on behalf of local residents and commuters to install an escalator at Grant Road Station.'
  },
  {
    id: 'food-distribution-jan2026',
    title: 'किंग जॉर्ज मेमोरियल स्कूल अन्नदान', titleMr: 'किंग जॉर्ज मेमोरियल स्कूल अन्नदान', titleEn: 'Food Distribution at King George Memorial School',
    category: 'Food Security', categoryMr: 'अन्नसुरक्षा', categoryEn: 'Food Security',
    date: 'Jan 2026', dateMr: 'जानेवारी २०२६', dateEn: 'Jan 2026',
    image: '/images/food_distribution_jan2026.png',
    desc: 'किंग जॉर्ज मेमोरियल स्कूल येथे विद्यार्थी आणि गरजू लोकांसाठी अन्न वाटपाचा उपक्रम राबविण्यात आला.', descMr: 'किंग जॉर्ज मेमोरियल स्कूल येथे विद्यार्थी आणि गरजू लोकांसाठी अन्न वाटपाचा उपक्रम राबविण्यात आला.', descEn: 'Conducted a food distribution drive at King George Memorial School for students and those in need.'
  },
  {
    id: 'khichadi-vatap-feb2026',
    title: 'महाशिवरात्री निमित्त खिचडी वाटप', titleMr: 'महाशिवरात्री निमित्त खिचडी वाटप', titleEn: 'Mahashivratri Khichadi Vatap',
    category: 'Food Security', categoryMr: 'अन्नसुरक्षा', categoryEn: 'Food Security',
    date: 'Feb 2026', dateMr: 'फेब्रुवारी २०२६', dateEn: 'Feb 2026',
    image: '/images/khichadi_vatap_feb2026.png',
    desc: 'महाशिवरात्रीच्या निमित्ताने विजयदत्त स्वामी समर्थ मठ, करी रोड येथे १००० लोकांसाठी उपवासाची खिचडी वाटप.', descMr: 'महाशिवरात्रीच्या निमित्ताने विजयदत्त स्वामी समर्थ मठ, करी रोड येथे १००० लोकांसाठी उपवासाची खिचडी वाटप.', descEn: 'Distributed Upwas Khichadi to 1000 people on the occasion of Mahashivratri at Vijaydatta Swami Samarth Math, Curry Road.'
  },
  {
    id: 'blind-school-donation-march2026',
    title: 'व्हिक्टोरिया मेमोरियल स्कूल अंधांसाठी मदत', titleMr: 'व्हिक्टोरिया मेमोरियल स्कूल अंधांसाठी मदत', titleEn: 'Donation at Victoria Memorial School for Blind',
    category: 'Education & Essentials', categoryMr: 'शिक्षण आणि आवश्यक वस्तू', categoryEn: 'Education & Essentials',
    date: 'March 2026', dateMr: 'मार्च २०२६', dateEn: 'March 2026',
    image: '/images/blind_school_march2026.png',
    desc: 'व्हिक्टोरिया मेमोरियल स्कूलमधील अंध विद्यार्थ्यांसाठी अन्नधान्य, जीवनावश्यक वस्तू आणि अभ्यास संचांचे वाटप.', descMr: 'व्हिक्टोरिया मेमोरियल स्कूलमधील अंध विद्यार्थ्यांसाठी अन्नधान्य, जीवनावश्यक वस्तू आणि अभ्यास संचांचे वाटप.', descEn: 'Provided food ingredients, various essential items, and study kits to blind students at the Victoria Memorial School for the Blind.'
  },
  {
    id: 'chappan-bhog-april2026',
    title: 'गणेश चौकात ५६ भोग प्रसाद', titleMr: 'गणेश चौकात ५६ भोग प्रसाद', titleEn: '56 Bhog Prasad at Ganesh Chowk',
    category: 'Religious Event', categoryMr: 'धार्मिक कार्यक्रम', categoryEn: 'Religious Event',
    date: 'April 2026', dateMr: 'एप्रिल २०२६', dateEn: 'April 2026',
    image: '/images/chappan_bhog_april2026.png',
    desc: 'गणेश चौक येथे गणपती बाप्पाला ५६ भोगाचा प्रसाद अर्पण करण्यात आला.', descMr: 'गणेश चौक येथे गणपती बाप्पाला ५६ भोगाचा प्रसाद अर्पण करण्यात आला.', descEn: 'Offered 56 Bhog Prasad to our Ganpati at Ganesh Chowk.'
  },
  {
    id: 'khichadi-vatap-july2026',
    title: 'आषाढी एकादशी निमित्त खिचडी वाटप', titleMr: 'आषाढी एकादशी निमित्त खिचडी वाटप', titleEn: 'Ashadhi Ekadashi Khichadi Vatap',
    category: 'Food Security', categoryMr: 'अन्नसुरक्षा', categoryEn: 'Food Security',
    date: 'July 2026', dateMr: 'जुलै २०२६', dateEn: 'July 2026',
    image: '/images/khichadi_vatap_july2026.png',
    desc: 'आषाढी एकादशीच्या निमित्ताने विजयदत्त स्वामी समर्थ मठ, करी रोड येथे स्वामी समर्थ आणि विठ्ठलाच्या १५०० भक्तांसाठी खिचडी वाटप.', descMr: 'आषाढी एकादशीच्या निमित्ताने विजयदत्त स्वामी समर्थ मठ, करी रोड येथे स्वामी समर्थ आणि विठ्ठलाच्या १५०० भक्तांसाठी खिचडी वाटप.', descEn: 'Distributed Khichadi to 1500 devotees of Swami Samarth and Vitthal on the occasion of Ashadhi Ekadashi at Vijaydatta Swami Samarth Math, Curry Road.'
  }
];

// Committee Members Data - 2025-26
const committeeData = [
  { number: 1, nameMr: 'श्री. केतन जमनादास पटेल', nameEn: 'Shri Ketan Jamnadas Patel', designationMr: 'कार्याध्यक्ष', designationEn: 'Working President', image: '/images/committee/ketan_patel.png' },
  { number: 2, nameMr: 'श्री. परेश रमेश परब', nameEn: 'Shri Paresh Ramesh Parab', designationMr: 'अध्यक्ष', designationEn: 'President', image: '/images/committee/paresh_parab.png' },
  { number: 3, nameMr: 'श्री. आदित्य पवार', nameEn: 'Shri Aditya Pawar', designationMr: 'उपाध्यक्ष', designationEn: 'Vice President', image: '/images/committee/aditya_pawar.png' },
  { number: 4, nameMr: 'श्री. अभिषेक उगले', nameEn: 'Shri Abhishek Ugale', designationMr: 'उपाध्यक्ष', designationEn: 'Vice President', image: '/images/committee/abhishek_ugale.png' },
  { number: 5, nameMr: 'श्री. चंद्रकांत सांगळे', nameEn: 'Shri Chandrakant Sangale', designationMr: 'उपाध्यक्ष', designationEn: 'Vice President', image: '/images/committee/chandrakant_sangle.png' },
  { number: 6, nameMr: 'सचिव', nameEn: 'Secretary', designationMr: 'सचिव', designationEn: 'Secretary', image: '/images/committee/secretary.jpg' },
  { number: 7, nameMr: 'श्री. निलेश पटेल', nameEn: 'Shri Nilesh Patel', designationMr: 'सचिव', designationEn: 'Secretary', image: '/images/committee/nilesh_patel.png' },
  { number: 8, nameMr: 'श्री. सर्वेश सांगळे', nameEn: 'Shri Sarvesh Sangle', designationMr: 'सचिव', designationEn: 'Secretary', image: '/images/committee/sarvesh_sangle.jpg' },
  { number: 9, nameMr: 'श्री. महेश यमकर', nameEn: 'Shri Mahesh Yamkar', designationMr: 'सहसचिव', designationEn: 'Joint Secretary', image: '/images/committee/mahesh_yamkar.png' },
  { number: 10, nameMr: 'श्री. भुपेंद्र पवार', nameEn: 'Shri Bhupendra Pawar', designationMr: 'सहसचिव', designationEn: 'Joint Secretary', image: '/images/committee/bhupendra_pawar.png' },
  { number: 11, nameMr: 'श्री. सुनिल घुगे', nameEn: 'Shri Sunil Ghuge', designationMr: 'सहसचिव', designationEn: 'Joint Secretary', image: '/images/committee/sunil_ghuge.png' },
  { number: 12, nameMr: 'श्री. भाविक पटेल', nameEn: 'Shri Bhavik Patel', designationMr: 'सोशल मीडिया प्रमुख', designationEn: 'Social Media Head', image: '/images/committee/bhavik_patel.jpg' },
  { number: 13, nameMr: 'श्री. शिवकुमार पांडे', nameEn: 'Shri Shivkumar Pande', designationMr: 'खजिनदार', designationEn: 'Treasurer', image: '/images/committee/shivkumar_pande.png' },
  { number: 14, nameMr: 'श्री. निखिल परब', nameEn: 'Shri Nikhil Parab', designationMr: 'खजिनदार', designationEn: 'Treasurer', image: '/images/committee/nikhil_parab_real.png' },
  { number: 15, nameMr: 'श्री. हर्ष पटेल', nameEn: 'Shri Harsh Patel', designationMr: 'खजिनदार', designationEn: 'Treasurer', image: '/images/committee/harsh_patel.png' },
  { number: 16, nameMr: 'श्री. क्षितीज सांगळे', nameEn: 'Shri Kshitij Sangale', designationMr: 'सह खजिनदार', designationEn: 'Joint Treasurer', image: '/images/committee/kshitij_sangale.png' },
  { number: 17, nameMr: 'श्री. अभिषेक पांडे', nameEn: 'Shri Abhishek Pande', designationMr: 'सह खजिनदार', designationEn: 'Joint Treasurer', image: '/images/committee/abhishek_pande.png' },
  { number: 18, nameMr: 'श्री. अमित उपाध्याय', nameEn: 'Shri Amit Upadhyay', designationMr: 'सह खजिनदार', designationEn: 'Joint Treasurer', image: '/images/committee/amit_upadhyay.png' },
  { number: 19, nameMr: 'श्री. राजेश पटेल', nameEn: 'Shri Rajesh Patel', designationMr: 'संयोजक', designationEn: 'Coordinator', image: '/images/committee/rajesh_patel.jpg' },
  { number: 20, nameMr: 'श्री. संतोष सांगळे', nameEn: 'Shri Santosh Sangale', designationMr: 'संयोजक', designationEn: 'Coordinator', image: '/images/committee/santosh_sangale.png' },
  { number: 21, nameMr: 'श्री. अंश जैन', nameEn: 'Shri Ansh Jain', designationMr: 'संयोजक', designationEn: 'Coordinator', image: '/images/committee/ansh_jain.png' },
  { number: 22, nameMr: 'श्री. किशोर शेट्टी कटील', nameEn: 'Shri Kishor Shetty Katil', designationMr: 'स्मरणिका प्रमुख', designationEn: 'Souvenir Head', image: '/images/committee/kishore_shetty_katil.png', objectPosition: 'left center' },
  { number: 23, nameMr: 'श्री. प्रथमेश वारंग', nameEn: 'Shri Prathamesh Warang', designationMr: 'स्मरणिका प्रमुख', designationEn: 'Souvenir Head', image: '/images/committee/prathamesh_warang.png' },
  { number: 25, nameMr: 'श्री. ओम बोले', nameEn: 'Shri Om Bole', designationMr: 'स्मरणिका प्रमुख', designationEn: 'Souvenir Head', image: '/images/committee/om_bole.png' },
  { number: 26, nameMr: 'श्री. प्रथमेश सांगळे', nameEn: 'Shri Prathamesh Sangale', designationMr: 'स्मरणिका प्रमुख', designationEn: 'Souvenir Head', image: '/images/committee/prathamesh_sangale.jpg' },
  { number: 27, nameMr: 'श्री. भौमिक शिर्के', nameEn: 'Shri Bhaumik Shirke', designationMr: 'संयोजक', designationEn: 'Coordinator', image: '/images/committee/bhaumik_shirke.png' }
];

module.exports = {
  // Render Home Page
  renderHomePage(req, res) {
    const status = db.getYatraStatus();
    res.render('index', {
      title: 'Dagdi Chawl Chi Aai Mauli | Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal, Mumbai',
      metaDescription: 'Official Portal of Dagdi Chawl Chi Aai Mauli (Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal, Est. 1973, Reg. ). Daily Ganeshotsav live darshan, schedule, historical gallery, social work &  tax exempt donations.',
      activeTab: 'home',
      yatraStatus: status,
      scheduleData: scheduleData.slice(0, 4),
      glimpsesData,
      socialWorkData
    });
  },

  // Render About Us Page
  renderAboutPage(req, res) {
    res.render('about', {
      title: 'About Us — History & Legacy | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'Explore the 50+ year legacy of Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal (Est. 1973) at Bapurao Jagtap Marg, Byculla West, Mumbai. Discover our history, vision, and 365-day social work.',
      activeTab: 'about'
    });
  },

  // Render Schedule Page
  renderSchedulePage(req, res) {
    const status = db.getYatraStatus();
    res.render('schedule', {
      title: 'Ganeshotsav 2026 Schedule & Maha Aarti Timings | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'Official 12-day Ganeshotsav 2026 festival schedule for Dagdi Chawl Chi Aai Mauli. Morning & Evening Maha Aarti timings, Annadan Mahaprasad, cultural events, Hom Havan & Visarjan procession.',
      activeTab: 'schedule',
      yatraStatus: status,
      scheduleData,
      jagranData
    });
  },

  // Render Glimpses Page
  renderGlimpsesPage(req, res) {
    res.render('glimpses', {
      title: 'Historical Photo Gallery & Idol Glimpses | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'Browse the 20+ year historical photo gallery and idol themes of Dagdi Chawl Chi Aai Mauli from 1990 to 2025 by Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal, Mumbai.',
      activeTab: 'glimpses',
      glimpsesData
    });
  },

  // Render Decade Gallery (Renamed from Photo Booth)
  renderPhotoBoothPage(req, res) {
    res.render('photo-booth', {
      title: 'Decade Glimpses Archive (2015-2025) | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'View historical retrospective photos and iconic themes of Dagdi Chawl Chi Aai Mauli over the past decade (2015-2025).',
      activeTab: 'photobooth',
      glimpsesData
    });
  },

  // Render Social Work Page
  renderSocialWorkPage(req, res) {
    res.render('social-work', {
      title: 'Social Initiatives & Community Service | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'Discover community welfare programs by Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal including Tulsi Vatap, student school kits, 2017 flood relief, and food security drives in Mumbai.',
      activeTab: 'socialwork',
      socialWorkData
    });
  },

  renderCommitteePage(req, res) {
    res.render('committee', {
      title: 'Executive Committee & Trustees | Dagdi Chawl Chi Aai Mauli',
      metaDescription: 'Meet the executive committee members, office bearers, advisory board, and karyakartas of Byculla Dagdi Chawl Sarvajanik Navratrotsav Mandal, Grant Road, Mumbai.',
      activeTab: 'committee',
      committeeData
    });
  },

  // Live Status API
  getLiveStatusApi(req, res) {
    const status = db.getYatraStatus();
    res.json({ success: true, status });
  }
};
