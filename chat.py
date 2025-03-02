import json
import random
import requests
import os

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

def classify_questions(questions):
    """Classify questions by difficulty using categories from quiz content"""
    physics_questions = []
    chemistry_questions = []
    astronomy_questions = []
    general_science_questions = []
    
    for q in questions:
        # Simple classification based on keywords
        question_text = q["question"].lower()
        
        if any(keyword in question_text for keyword in ["बल", "वेग", "न्यूटन", "गती", "विद्युत", "घर्षण"]):
            physics_questions.append(q)
        elif any(keyword in question_text for keyword in ["पाणी", "उत्कलनांक", "विद्रावक", "उष्णता"]):
            chemistry_questions.append(q)
        elif any(keyword in question_text for keyword in ["ग्रह", "black hole"]):
            astronomy_questions.append(q)
        else:
            general_science_questions.append(q)
    
    return {
        "physics": physics_questions,
        "chemistry": chemistry_questions,
        "astronomy": astronomy_questions,
        "general_science": general_science_questions
    }

def gemini_evaluate_aptitude(quiz_results, api_key):
    """
    Use Google Gemini API to evaluate the user's science aptitude
    
    Parameters:
    quiz_results (dict): Dictionary with quiz statistics and user's answers
    api_key (str): Google Gemini API key
    
    Returns:
    dict: Aptitude evaluation from Gemini
    """
    # API endpoint for Gemini
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    
    # Prepare the API request
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    }
    
    # Create prompt with quiz results
    categories = quiz_results["categories"]
    category_scores = []
    for category, stats in categories.items():
        if stats["total"] > 0:
            percentage = (stats["correct"] / stats["total"]) * 100
            category_scores.append(f"{category}: {stats['correct']}/{stats['total']} ({percentage:.1f}%)")
    
    category_performance = "\n".join(category_scores)
    
    prompt = f"""Analyze the following science quiz results and provide:
1. A comprehensive science aptitude score (out of 100)
2. A descriptive evaluation of the student's science knowledge level in both English and Marathi
3. Detailed strengths and weaknesses based on the performance
4. Personalized recommendations for improvement
5. Career paths in science that might suit this student

Quiz Results:
- Overall Score: {quiz_results["score"]}/{quiz_results["total"]} ({quiz_results["percentage"]:.1f}%)
- Performance by category:
{category_performance}

Make the feedback constructive, encouraging, and educational. Include specific tips for improving in each science category.
"""

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 1024
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        result = response.json()
        if "candidates" in result and len(result["candidates"]) > 0:
            text_result = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"success": True, "evaluation": text_result}
        else:
            return {"success": False, "error": "No evaluation generated"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

def run_quiz():
    """Run the quiz application"""
    print("\n===== विज्ञान क्विझ सेटअप =====")
    api_key = "AIzaSyCJWYIyjEmKIq0U9ft2IOfsjCRyfzw5AU0"
    
    if not api_key:
        print("API key आवश्यक आहे. कृपया API key सह पुन्हा प्रयत्न करा.")
        return
    
    questions = load_questions()
    
    # Classify questions by topic
    classified_questions = classify_questions(questions)
    
    # Select 10 random questions with at least 1 from each category if possible
    selected_questions = []
    
    # Try to get at least one question from each non-empty category
    for category, category_questions in classified_questions.items():
        if category_questions:
            selected_questions.append(random.choice(category_questions))
    
    # Fill the rest with random questions
    remaining_count = min(10 - len(selected_questions), len(questions) - len(selected_questions))
    remaining_pool = [q for q in questions if q not in selected_questions]
    selected_questions.extend(random.sample(remaining_pool, remaining_count))
    
    # Shuffle the final selection
    random.shuffle(selected_questions)
    
    # Initialize score and tracking dictionaries
    score = 0
    user_answers = []
    category_performance = {
        "physics": {"correct": 0, "total": 0},
        "chemistry": {"correct": 0, "total": 0},
        "astronomy": {"correct": 0, "total": 0},
        "general_science": {"correct": 0, "total": 0}
    }
    
    # Display welcome message
    print("\n===== मराठी विज्ञान क्विझ =====")
    print("10 प्रश्नांच्या या क्विझ मध्ये आपले स्वागत आहे!")
    print("प्रत्येक प्रश्नासाठी, योग्य पर्याय निवडण्यासाठी a, b, c, किंवा d टाईप करा.")
    print("क्विझ संपल्यानंतर Google Gemini तुमचा विज्ञान कौशल्य स्कोर आणि विश्लेषण देईल.")
    print("चला सुरू करूया!\n")
    
    # Ask each question
    for i, q in enumerate(selected_questions, 1):
        print(f"प्रश्न {i}: {q['question']}")
        
        # Find which category this question belongs to
        question_category = None
        for category, questions_list in classified_questions.items():
            if q in questions_list:
                question_category = category
                break
        
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
        is_correct = user_option and user_option == q['answer']
        if is_correct:
            print("बरोबर! ✓")
            score += 1
            if question_category:
                category_performance[question_category]["correct"] += 1
        else:
            correct_letter = next(key for key, value in answer_map.items() if value == q['answer'])
            correct_option = q.get(q['answer'], "")
            print(f"चूक! ✗ बरोबर उत्तर: {correct_letter}) {correct_option}")
        
        # Track category performance
        if question_category:
            category_performance[question_category]["total"] += 1
            
        # Track user answer for later analysis
        user_answers.append({
            "question": q["question"],
            "user_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct,
            "category": question_category
        })
        
        # Show current score
        print(f"वर्तमान गुण: {score}/{i}")
        print("\n" + "-" * 40 + "\n")
    
    # Prepare results for Gemini evaluation
    quiz_results = {
        "score": score,
        "total": len(selected_questions),
        "percentage": (score / len(selected_questions)) * 100,
        "categories": category_performance,
        "answers": user_answers
    }
    
    # Show interim results
    print("\n===== क्विझ संपला =====")
    print(f"आपला अंतिम गुण: {score}/{len(selected_questions)}")
    print("Google Gemini API वापरून आपला विज्ञान कौशल्य स्कोर आणि विश्लेषण तयार करत आहे...")
    
    # Get aptitude evaluation from Gemini
    evaluation_result = gemini_evaluate_aptitude(quiz_results, api_key)
    
    if evaluation_result["success"]:
        print("\n===== Google Gemini विज्ञान कौशल्य मूल्यांकन =====")
        print(evaluation_result["evaluation"])
    else:
        print("\n===== त्रुटी =====")
        print(f"Gemini API वापरताना त्रुटी आली: {evaluation_result.get('error', 'अज्ञात त्रुटी')}")
        
        # Provide basic feedback if API fails
        if score == len(selected_questions):
            print("उत्कृष्ट! आपण सर्व प्रश्न बरोबर सोडवले!")
        elif score >= len(selected_questions) * 0.7:
            print("छान! आपण बर्‍याच प्रश्नांची उत्तरे बरोबर दिली!")
        elif score >= len(selected_questions) * 0.5:
            print("चांगले प्रयत्न! आपण निम्म्यापेक्षा जास्त प्रश्न बरोबर सोडवले.")
        else:
            print("पुढच्या वेळी अधिक अभ्यास करून पुन्हा प्रयत्न करा.")

if __name__ == "__main__":
    run_quiz()