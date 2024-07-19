import streamlit as st

# Sample quizzes dictionary
quizzes = {
    "Quiz 1": {
        "questions": [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris"],
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5"],
                "answer": "4"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
        ]
    },
    "Quiz 2": {
        "questions": [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "O2", "CO2"],
                "answer": "H2O"
            },
            {
                "question": "Which element has the atomic number 1?",
                "options": ["Helium", "Hydrogen", "Oxygen"],
                "answer": "Hydrogen"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["Nucleus", "Ribosome", "Mitochondria"],
                "answer": "Mitochondria"
            },
            {
                "question": "What is the speed of light?",
                "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s"],
                "answer": "300,000 km/s"
            },
        ]
    }
}

def display_quiz(quiz_name):
    quiz = quizzes[quiz_name]
    
    user_answers = []
    
    for i, question in enumerate(quiz['questions']):
        st.subheader(f"Q{i + 1}: {question['question']}")
        options = question['options']
        selected_option = st.radio(f"Select your answer:", options, key=f"q{i}")
        user_answers.append(selected_option)
    
    if st.button("Submit"):
        score = 0
        results = []
        for i, question in enumerate(quiz['questions']):
            correct_answer = question['answer']
            user_answer = user_answers[i]
            if user_answer == correct_answer:
                results.append((question['question'], user_answer, 'correct', 'green'))
                score += 1
            elif user_answer == "":
                results.append((question['question'], user_answer, 'missed', 'yellow'))
            else:
                results.append((question['question'], user_answer, 'wrong', 'red'))
                
        st.subheader("Results:")
        for question, answer, status, color in results:
            st.markdown(f"<span style='color: {color};'>{question} - Your Answer: {answer} - Status: {status}</span>", unsafe_allow_html=True)

        st.write(f"Your score: {score}/{len(quiz['questions'])}")

# Streamlit app structure
st.title("Quiz App")
st.sidebar.title("Select a Quiz Topic")
quiz_topic = st.sidebar.selectbox("Choose your quiz:", list(quizzes.keys()))

display_quiz(quiz_topic)