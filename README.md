# Quiz-API
API Endpoints:
- POST /quizzes - to create a new quiz
### http://127.0.0.1:8000/quizzes/
#### example: (body) {
    "question" : "What is the capital of India?",
    "option" : ["New Delhi", "Rajasthan", "Uttarakhand", "Goa"],
    "right_answer" : 0,
    "start_date" : "29/5/2023 18:56:33",
    "end_date" : "30/5/2023 00:40:33"
}

- GET /quizzes/active - to retrieve the active quiz (the quiz that is currently within its start and end time) 
### http://127.0.0.1:8000/quizzes/active/

- GET /quizzes/:id/result - to retrieve the result of a quiz by its ID 
### http://127.0.0.1:8000/quizzes/14/result/

- GET /quizzes/all - to retrieve the all quizes
### http://127.0.0.1:8000/quizzes/all

Functionalities:
## * status is changed using cron job every minute
## * rate-limiting to prevent abuse of the API is done using throttling (2 or 3 erequest per minute)
## * filesystem caching is done (every 5 minutes) to reduce the response time of frequently accessed data 

Create a Quiz: Users is able to create a quiz by sending a POST request to the API with the following fields:
- question: the text of the question
- options: an array of the answer options for the question
- rightAnswer: the index of the correct answer in the options array
- startDate: the date and time when the quiz should start
- endDate: the date and time when the quiz should end
### Get Active Quiz: Users is able to retrieve the active quiz (the quiz that is currently within its start and end time).
### Get Quiz Result: After the 5 minute of end time of a quiz, users is able to retrieve the result of the quiz. The result is basically the right answer 

