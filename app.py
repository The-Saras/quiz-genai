import json
import random

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