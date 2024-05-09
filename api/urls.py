from django.urls import path
from api.views import CreateQuestionAPIView, OptionCreateAPIView, QuestionsListAPIView, UserScoresAPIView


urlpatterns = [
    path('api/questions/', QuestionsListAPIView.as_view(), name='questions-list'),
    path('api/user-scores/', UserScoresAPIView.as_view(), name='user-scores'),
    path('api/create-question/', CreateQuestionAPIView.as_view(), name='create-question'),
    path('api/create-option/', OptionCreateAPIView.as_view(), name='create-option'),
    
]