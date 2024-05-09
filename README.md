# Game Application
This is an API-based Django app built using Django Rest Framework. You can create questions, options, answer questions and get scores.

Commands below uses `Linux OS`.

### Implementations:

1. Questions previously attempted by a user are excluded from new question pool for the user
2. The excluded question IDs are stored on a JSON field on the user model
3. Questions are randomized
4. Questions are created on the QuestionsModel
5. While options are created on the OptionsModel with a Foreign key relationship to each created question
6. The correct answer option (a, b or c) is stored on the QuestionModel and the OptionModel
7. To answer question, user sends the question ID and Option ID
8. The user-submitted answer is checked against the answer stored on the QuestionModel by getting the Option ID and checking its option with the option stored as answer on the QuestionModel (using the question ID)
9. All user scores are also available on the user model; as each correct question answered by the user increments the user's score
10. You can manage the app from the Django admin interface and click on `View On Site` buttons on the admin page


### To launch this app on your system:

1. Navigate to your desktop (or any folder of your choice)
```
cd Desktop
```
2. Create a new folder/directory called `game`
```
mkdir game
```
3. Navigate into this new folder
```
cd game
```
4. Create a new Python Virtual environment in the `game` folder.
```
python3 -m venv ./gamevenv
```
5. Activate this new virtual environment
```
source gamevenv/bin/activate
```
6. Clone this git repo
```
git clone https://github.com/Jaye-python/gameproject.git
```
7. Move into the `gameproject` folder 
```
cd gameproject
```
8. Install dependencies
```
pip install -r requirements.txt
```
9. Create `superuser` account
```
python manage.py createsuperuser
```
10. Launch application
```
python manage.py runserver
```
11. To create ticket, send below sample payload to `http://127.0.0.1:8000/api/create-question/` via POSTMAN using `raw/json` format and using `BASIC AUTHENTICATION` (email and password of user):
```
{
    "question_text": "Who is the US President?" ,
    "answer_option": "b",
    "answer_text": "John"
}
```
12. To create option, send below sample payload to `http://127.0.0.1:8000/api/create-option/` via POSTMAN using `raw/json` format and using `BASIC AUTHENTICATION` (email and password of user):
```
{
    "question": 1,
    "option": "c",
    "options_text": "I don't know"
}
```
13. To view questions and their options as an enduser, send GET request to `http://127.0.0.1:8000/api/questions/` via POSTMAN using `BASIC AUTHENTICATION` (email and password of user)

14. To view questions as an ADMIN user, send GET request to `http://127.0.0.1:8000/api/create-question/` via POSTMAN using `BASIC AUTHENTICATION` (email and password of user)
15. To view all options created, send GET request to `http://127.0.0.1:8000/api/create-option/` via POSTMAN using `BASIC AUTHENTICATION` (email and password of user)
16. To answer a question, send `question id` and `option id` as POST request to `http://127.0.0.1:8000/api/questions/` using `BASIC AUTHENTICATION` (email and password of user)
```
{
  "selected_question": 2,
  "selected_option": 1  
}
```
    
17. To get scores, send GET request to `http://127.0.0.1:8000/api/user-scores/` via POSTMAN using `BASIC AUTHENTICATION` (email and password of user)
18. Login in to `http://127.0.0.1:8000/admin/` to manage the app
19. To check the short API documentation, visit either of these:
```
http://127.0.0.1:8000/api/schema/swagger-ui/#/
http://127.0.0.1:8000/api/schema/redoc/
```
