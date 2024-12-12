# Django Quiz App

This is a simple Django-based Quiz App that allows a user to:

1. Start a new quiz session.
2. Get random multiple-choice questions from a database.
3. Submit answers for a question.
4. View quiz statistics, including total questions answered and correct/incorrect submissions.

## Features

- **Session-based Quiz Management**: User progress is tracked using Django sessions.
- **Random Question Retrieval**: Each question is fetched randomly from the database.
- **RESTful API**: API endpoints are built using Django REST Framework (DRF).

---

## API Endpoints

### 1. **Start a Quiz Session**
   **Endpoint**: `/quiz/start/`  
   **Method**: `GET`  
   **Description**: Initializes a new quiz session by resetting the total questions, correct answers, and incorrect answers for the user session.  

   **Response**:
   ```json
   {
       "message": "Quiz session started"
   }
2. Get a Random Question
Endpoint: /quiz/get-question/
Method: GET
Description: Retrieves a random multiple-choice question from the database. The response includes the question text and four answer options.

Response:

json
{
    "id": 1,
    "question": "What is the capital of France?",
    "options": [
        "Berlin",
        "Madrid",
        "Paris",
        "Rome"
    ]
}
3. Submit an Answer
Endpoint: /quiz/submit-answer/
Method: POST
Description: Accepts a user’s answer for a specific question and updates the session with the result (correct/incorrect).

Request Body (JSON):

json
{
    "question_id": 1,
    "selected_option": 3
}
Response:

For a correct answer:
json
{
    "result": "correct"
}
For an incorrect answer:
json
{
    "result": "incorrect"
}
4. View Quiz Statistics
Endpoint: /quiz/stats/
Method: GET
Description: Retrieves the current quiz statistics for the session, including total questions answered, correct answers, and incorrect answers.

Response:

json
{
    "total_questions": 5,
    "correct_answers": 3,
    "incorrect_answers": 2
}
