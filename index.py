import json
import random

from google import genai

client  = genai.Client(api_key="AIzaSyCJWYIyjEmKIq0U9ft2IOfsjCRyfzw5AU0")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)

def load_questions():
    """Load questions from the data structure"""
    questions = [
        {
            "question": "कोणते बल गतीच्या विरोधात काम करते ",
            "option_a": " गुरुत्व बल ",
            "option_b": "घर्षण बल ",
            "option_c": " चुंबकीय बल ",
            "option_d": "स्नायू बल ",
            "answer": "option_b"
        },
        {
            "question": "न्यूटनचे प्रसिद्ध 3 नियम काशविषयी आहेत  ",
            "option_a": " गुरुत्वाकर्षण ",
            "option_b": " चुंबक ",
            "option_c": "गती ",
            "option_d": " विद्युत ",
            "answer": "option_c"
        },
        {
            "question": "विद्युतधार कोणत्या एककात मोजतात ",
            "option_a": "व्होल्ट ",
            "option_b": " कुलोम ",
            "option_c": "ओहोम ",
            "option_d": "अॅमपियर  ",
            "answer": "option_d"
        },
        {
            "question": "कोणता ग्रह लाल रंगाचा दिसतो ",
            "option_a": " मंगळ ",
            "option_b": " गुरु ",
            "option_c": "बुध ",
            "option_d": "शुक्र ",
            "answer": "option_a"
        },

        {
    "question": "पुढीलपैकी संवगाचे SI एकक आहे ",
    "option_a": "   kg /ms ",
    "option_b": " kg m/s ",
    "option_c": "  gm cm/s ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "वादळामुळे झाडं तुटून पडतात हे गतीच्या कितव्या नियमाचे उदाहरण आहे  ",
    "option_a": " पहिला ",
    "option_b": " दूसरा ",
    "option_c": " तिसरा ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "चुंबकीय क्षेत्राचे एकक काय आहे ",
    "option_a": " टेस्ला  ",
    "option_b": "  कुलोम ",
    "option_c": " नोहा ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "प्रकाशाचा वेग काय आहे ",
    "option_a": "    3.0 x 10^2 m /s ",
    "option_b": "    3.0 x  10^8 m /h ",
    "option_c": " 3.0 x 10^8 m/s ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "पाणी का सार्वत्रिक विद्रावक आहे ",
    "option_a": "पाणी द्रवरूप असते ",
    "option_b": "पाणी अपसामान्यता दर्शवत  ",
    "option_c": "पाणी भरपूर गोष्टींना विरघळून घेते  ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "पाण्याचा उत्कलनांक काय आहे  (फॅरनहाइट मध्ये ) F-32/2 = C/5     - सूत्र ",
    "option_a": "   212 F",
    "option_b": "   100 F",
    "option_c": "   32 F",
    "option_d": "  200 F",
    "answer": "option_a"
  },
  {
    "question": "कोणत्या प्रक्रियेत उष्णता शोषली जाते  ",
    "option_a": "उष्मा दायी ",
    "option_b": "रेडॉक्स ",
    "option_c": "उष्मा ग्राही ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "जेंव्हा तांब्याच्या तारेच्या कुंतलाभोवती  जोरात चुंबक फिरवल्यास काय होते  ",
    "option_a": "चुंबकात विद्युतउर्जा आली ",
    "option_b": "कुंतलात चुंबकत्व आले  ",
    "option_c": "कुंतलात विद्युतधार प्रवर्तित झाली  ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "वितळतार कोणत्या पदार्था पासून बनलेली असते ",
    "option_a": " टीन ",
    "option_b": " लोह + जस्त  ",
    "option_c": "  टंगस्टन ",
    "option_d": " अॅलुमीनियम ",
    "answer": "option_a"
  },
  {
    "question": "दूरद्रुष्टीता आजारात कुठल्या वस्तु आपल्याला दिसत नाही  ",
    "option_a": "शेजारच्या ",
    "option_b": " लांबच्या ",
    "option_c": "जवळच्या ",
    "option_d": "रात्रीच्या ",
    "answer": "option_c"
  },
  {
    "question": "black hole  मध्ये वस्तु का खेचल्या जातात ",
    "option_a": "अत्यंत शक्तीशील चुंबकत्व ",
    "option_b": "अत्यंत शक्तिशील गुरुत्वाकर्षण  ",
    "option_c": "रेडियो धर्मी विकिरणामुळे ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "मुक्तपतन होत असताना दोन वस्तूंचे वस्तुमान भिन्न असून सुद्धा त्या सोबत का जमिनीवर पडतात ",
    "option_a": "त्वरण वास्तुमानवर अवलंबून नसते",
    "option_b": "न्यूटनच्या  गतीविषयी 2 रा नियम ",
    "option_c": "गुरुत्वीय त्वरण सगळ्या वस्तूंवर समान कार्य करते ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "एखाद्या चुंबकीय पदार्थाला कायमचे चुंबकत्व देण्यासाठी काय करतात    ",
    "option_a": "पदार्थ तापवून चुंबकीय क्षेत्रात ठेवणे ",
    "option_b": "पदार्थ थंड करून चुंबकीय क्षेत्रात ठेवणे  ",
    "option_c": "पदार्थ दाबाखाली ठेवून चुंबकीय क्षेत्रात ठेवणे  ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "उन्हाळ्यात दिसणारे मृगजळ कोणत्या कारणामुळे दिसते",
    "option_a": "वातावरणातील दबामुळे ",
    "option_b": "हवेतील आर्द्रते मुळे ",
    "option_c": " जमीन चमकते म्हणून ",
    "option_d": "प्रकाशाचे अपवर्तन ",
    "answer": "option_d"
  },
  {
    "question": "पृथ्वीच्या गुरुत्वाकर्षणावर मात करून बाहेर पडण्यास लागणारा  मुक्तिवेग किती ",
    "option_a": "   11.2 km /s ",
    "option_b": "    1100   m /h ",
    "option_c": "      100  km /h ",
    "option_d": "    11.2  cm/h  ",
    "answer": "option_a"
  },
  {
    "question": "जर आपण पृथ्वीच्या केंद्रात गेलो तर गुरुत्वीय बलावर काय परिणाम होईल ",
    "option_a": " ते धन होईल ",
    "option_b": "ते ऋण होईल ",
    "option_c": "ते 0.1 होईल ",
    "option_d": "ते शून्य होईल ",
    "answer": "option_d"
  },
  {
    "question": "अवटू व परावटू ग्रंथिनचे कार्य काय ",
    "option_a": " पंचनावर नियंत्रण ",
    "option_b": "शरीरातील फॉस्फरसचे नियंत्रण ",
    "option_c": "चेताचे नियंत्रण ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "वनस्पति व प्राणी पेशी यांतील ठळक फरक काय ",
    "option_a": " हरित लवक   आहे / नाही ",
    "option_b": "  केंद्रक  मोठे /छोटे ",
    "option_c": "तंतुकणीक    आहे / नाही ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": " वनस्पति उतीं मध्ये  दृढ उती  कुठे आढळतात ",
    "option_a": "फळांचा मगस ",
    "option_b": "   बी व फळांचे कठीण आवरण ",
    "option_c": " पानांच्या शिरा ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "मानवाच्या उत्सर्जक पदार्थात मुख्य घटक काय  ",
    "option_a": " अमोनिया ",
    "option_b": "मिथेन ",
    "option_c": "ईथेन ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "पेशित  परासरणीय दाब कोण नियंत्रित करते ",
    "option_a": "  केंद्रक ",
    "option_b": "  तंतुकणीक ",
    "option_c": "  रिक्तिका ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "पेशित ऊर्जा निर्मिती कोण करते ",
    "option_a": " तंतुकणीक ",
    "option_b": " केंद्रक ",
    "option_c": " पेशिपटल ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "पुढील कोणता RNA चा प्रकार नाही ",
    "option_a": " t-RNA ",
    "option_b": "  m-RNA",
    "option_c": "  c-RNA",
    "option_d": "  r-RNA ",
    "answer": "option_c"
  },
  
  {
    "question": "पुढील कोणत्या पेशित केंद्रक नसते ",
    "option_a": "  RBC",
    "option_b": " WBC",
    "option_c": " वनस्पति पेशी ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "जलवनस्पतींमध्ये तरंगण्यासाठी काय अनुकूलन घडले आहे ",
    "option_a": " लवचिक खोड ",
    "option_b": "पाणी विरोधक द्रव ",
    "option_c": "  अंतरपेशीय पोकळ्या ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "वनस्पतींची हालचाल कोणत्या स्वरूपात होते ",
    "option_a": " अन्न निर्मिती ",
    "option_b": "उद्दीपनाला प्रतिसाद",
    "option_c": " श्वसन ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "मानवी मेंदूचा कोणता भाग शरीराचा तोल सांभाळतो ",
    "option_a": "  प्रमस्तीष्क ",
    "option_b": " अनूमस्तीष्क ",
    "option_c": "  मस्तीष्क पुच्छ ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "मानवी पचनसंस्था तंतुमय पदार्थ का पचवू शकत नाही ",
    "option_a": "आपण रवंथ करू शकत नाही ",
    "option_b": "आपल्यात ते संप्रेरक नसते ",
    "option_c": " आपल्या जठरातील अम्ल विरल असते ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "जेंव्हा आपल्याला जखम होते तेंव्हा त्यातून निघणारे रक्त कोणामुळे थांबते ",
    "option_a": "लसीका गोठतात ",
    "option_b": " रक्तपट्टीकांमुळे ",
    "option_c": " प्लाजमा मुळे ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणता पेशितील घटक सगळ्या पेशित असतो ",
    "option_a": "पेशीभित्तिक ",
    "option_b": "पटल बद्ध केंद्रक ",
    "option_c": " DNA",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "कोणते संप्रेरक ग्लुकोज च्या पातळीवर नियंत्रण ठेवते ",
    "option_a": "इंसुलिन ",
    "option_b": " अॅड्रेनॅलीन ",
    "option_c": "  ग्लायकोजेन ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "प्लास्मोडियम या परोपजीवी प्राण्यामुळे कोणता आजार होतो ",
    "option_a": "डेंग्यू ",
    "option_b": "हत्ती रोग ",
    "option_c": "मलेरिया ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "मानवाच्या शरीरात अंतर्गत अवयवांपैकी सर्वात मोठा अवयव कोणता ",
    "option_a": " हृदय ",
    "option_b": "यकृत ",
    "option_c": "फुफुस ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणता घटक शरीरातील हाडांना मजबूत करण्यास मदत करतो ",
    "option_a": "   मॅग्नेशियम ",
    "option_b": " फॉस्फरस ",
    "option_c": "     क्लोरिन ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "व्हीनेगरचे रासायनिक सूत्र काय ",
    "option_a": "  CH3 COOH",
    "option_b": " CHCOOH",
    "option_c": "  CH2COOH",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "समुद्रात तेल गळती झाली तर ती स्वच्छ करण्यासाठी कोणते किण्व वापरतात ",
    "option_a": "सॅकरोमायसीस सेरेवीसी ",
    "option_b": " कॅन्डीडा ",
    "option_c": "हेन्सेन्यूला ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "प्राणी वर्गीकरणात खेकडा कोणत्या संघात मोडला जातो ",
    "option_a": "वलयी ",
    "option_b": " शुंडक ",
    "option_c": " संधीपाद ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "सॅकरोमायसीस  सेरेवीसी हे किण्व कशासाठी वापरतात  ",
    "option_a": " वाईन निर्मिती ",
    "option_b": " कॉफी निर्मिती ",
    "option_c": "  चीज निर्मिती ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "एखाद्या वस्तूचे वयमापन करण्याची पद्धत कोणती व त्यासाठी कोणते मूलद्रव्य वापरतात  ",
    "option_a": "कार्बन डेटींग , C-12",
    "option_b": " कार्बन डेटींग , CO3 ",
    "option_c": " फॉस्फरस डेटींग , P-14",
    "option_d": "कार्बन डेटींग , C-14",
    "answer": "option_c"
  },
  {
    "question": "रेशीम उद्योगात वापरले जाणारे रेशीम कीड्यांचे नाव काय ",
    "option_a": "बॉम्बीक्स्  मोरी  ",
    "option_b": "एपिस मेलीफेरा ",
    "option_c": "मेंडुका",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "पक्षी कोणत्या कारणांमुळे हवेत उडू शकतात ",
    "option_a": " लवचिक शरीर रचना व पोकळ हाडे ",
    "option_b": "मजबूत शरीर व हाडे ",
    "option_c": "पसरट पंख व भरीव हाडे ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "कशामुळे जैविक उत्क्रांती वेगवान होते ",
    "option_a": " स्थिर पर्यावरणीय स्थिति ",
    "option_b": " कमी उत्पत्ति दर ",
    "option_c": " निसर्ग निवडिच सिद्धांत ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "मूलद्रव्यांचे नाव व त्याची संज्ञा यानुसार वेगळा घटक ओळखा ",
    "option_a": " Ag ",
    "option_b": "  Au",
    "option_c": " Cl",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "HCl चा सामू किती आहे ",
    "option_a": 2,
    "option_b": 0,
    "option_c": 1,
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणत्या संयुगाला अम्ल राज म्हणतात ",
    "option_a": "  HCl + H2SO4",
    "option_b": "HCl + HNO3",
    "option_c": "H2SO4",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "खालील कोणता वायु निष्क्रिय आहे ",
    "option_a": " N",
    "option_b": " H",
    "option_c": "  Ar",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "कोणत्या संयुगात आयनिक बंध आढळतो ",
    "option_a": " H2O",
    "option_b": "NaCl",
    "option_c": "CH4",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणते आम्ल व कोणते आम्लारी मिसळल्यास मीठ तयार होते ",
    "option_a": " HCl + Ca(OH)2",
    "option_b": " HCl + NaOH ",
    "option_c": "  H2SO4 + NaOH",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "बेंझिन चे रासायनिक सूत्र काय ",
    "option_a": " C2H6",
    "option_b": "C6H12O6",
    "option_c": "  C6H6",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "कोणता वायु  'Laughing gas' आहे ",
    "option_a": "  CO2",
    "option_b": " N2O ",
    "option_c": "SO2",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "रेडॉक्स अभिक्रियेत ऑक्सिडायझिंग एजंट म्हणजे काय ",
    "option_a": "जो अभिक्रियेत  O2 वापरतो ",
    "option_b": "जो अभिक्रियेत ऑक्सिडेशन करतो ",
    "option_c": "जो अभिक्रियेत क्षपण करतो ",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणता रेडियोअॅक्टीव संस्थानिक वैद्यकीय उपचारत वापरतात  ",
    "option_a": "C- 14",
    "option_b": " U-235",
    "option_c": " I - 131",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "कोणत्या धातूचा गंज थर निळा असतो ",
    "option_a": " तांब ",
    "option_b": " जस्त ",
    "option_c": "लोह ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "खालील कोणते मूलद्रव्य सर्वात जास्त विद्युत ऋणता असलेले आहे ",
    "option_a": " N",
    "option_b": "O",
    "option_c": " F",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "कोणते संयुग चांदीचा काळपट रंग होण्यास कारणीभूत आहे ",
    "option_a": " H2S",
    "option_b": " SO2",
    "option_c": "  H2N2",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "रेडॉक्स अभिक्रियेत कोणत्या प्रक्रिया घडते ",
    "option_a": "क्षपण+अपघटन ",
    "option_b": " ऑक्सिडिकरण + अपघटन ",
    "option_c": "क्षपण+   ऑक्सिडिकरण ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "खालील कोणते मूलद्रव्य ट्रान्सयुरेनियम घटक आहे ",
    "option_a": " U",
    "option_b": "PU",
    "option_c": " Li",
    "option_d": "",
    "answer": "option_b"
  },
  {
    "question": "कोणते कार्बनि संयुगाचे गंधकाच्या उपस्थितीत ज्वलन केल्यास आम्लवर्षाव होतो ",
    "option_a": "SO2",
    "option_b": "NO2",
    "option_c": "SO4",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "कोणत्या धातूचा वापर अणूभट्टीत न्यूट्रॉन मंदक म्हणून केला जातो ",
    "option_a": "ग्रॅफाईट ",
    "option_b": "जस्त ",
    "option_c": " लेड ",
    "option_d": "",
    "answer": "option_a"
  },
  {
    "question": "हायड्रोजन आणि कलोरीन वायूच्या संयोगातून  HCl   तयार होते ही कोणत्या प्रकारची  अभिक्रिया आहे ",
    "option_a": " अपघटन अभिक्रिया ",
    "option_b": "विस्थापन अभिक्रिया ",
    "option_c": "  संयोग  अभिक्रिया ",
    "option_d": "",
    "answer": "option_c"
  },
  {
    "question": "वातावरणातील कोणत्या वायूचे द्रव स्थितीत सर्वात कमी तापमान असते ",
    "option_a": "  नायट्रोजन ",
    "option_b": "हीलियम ",
    "option_c": "  ऑक्सीजन ",
    "option_d": "",
    "answer": "option_a"
  }
        # ... And many more questions from the dataset
        # The full list is truncated here but all questions from the data would be included
    ]
    
    # Return the full list of questions
    return questions

def run_quiz():
    """Run the quiz application"""
    questions = load_questions()
    
    # Select 10 random questions
    if len(questions) > 10:
        selected_questions = random.sample(questions, 10)
    else:
        selected_questions = questions
    
    # Initialize score
    score = 0
    
    # Display welcome message
    print("\n===== मराठी क्विझ =====")
    print("10 प्रश्नांच्या या क्विझ मध्ये आपले स्वागत आहे!")
    print("प्रत्येक प्रश्नासाठी, योग्य पर्याय निवडण्यासाठी a, b, c, किंवा d टाईप करा.")
    print("चला सुरू करूया!\n")
    
    # Ask each question
    for i, q in enumerate(selected_questions, 1):
        print(f"प्रश्न {i}: {q['question']}")
        
        # Display options
        if q.get("option_a"):
            print(f"a) {q['option_a']}")
        if q.get("option_b"):
            print(f"b) {q['option_b']}")
        if q.get("option_c"):
            print(f"c) {q['option_c']}")
        if q.get("option_d") and q['option_d']:
            print(f"d) {q['option_d']}")
        
        # Get user's answer
        user_answer = input("\nआपले उत्तर (a/b/c/d): ").lower().strip()
        
        # Map user input to option format
        answer_map = {'a': 'option_a', 'b': 'option_b', 'c': 'option_c', 'd': 'option_d'}
        user_option = answer_map.get(user_answer)
        
        # Check answer
        if user_option and user_option == q['answer']:
            print("बरोबर! ✓")
            score += 1
        else:
            correct_letter = next(key for key, value in answer_map.items() if value == q['answer'])
            correct_option = q.get(q['answer'], "")
            print(f"चूक! ✗ बरोबर उत्तर: {correct_letter}) {correct_option}")
        
        # Show current score
        print(f"वर्तमान गुण: {score}/{i}")
        print("\n" + "-" * 40 + "\n")
    
    # Show final results
    print("\n===== क्विझ संपला =====")
    print(f"आपला अंतिम गुण: {score}/10")
    
    # Provide feedback based on score
    if score == 10:
        print("उत्कृष्ट! आपण सर्व प्रश्न बरोबर सोडवले!")
    elif score >= 7:
        print("छान! आपण बर्‍याच प्रश्नांची उत्तरे बरोबर दिली!")
    elif score >= 5:
        print("चांगले प्रयत्न! आपण निम्म्यापेक्षा जास्त प्रश्न बरोबर सोडवले.")
    else:
        print("पुढच्या वेळी अधिक अभ्यास करून पुन्हा प्रयत्न करा.")

if __name__ == "__main__":
    run_quiz()