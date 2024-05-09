from django.urls import path
from gameapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
    # ANCHOR QUESTIONS
    path('questions/', views.QuestionsListView.as_view(), name="questions"),
    path("question-detail/<pk>/", views.QuestionDetailView.as_view(), name="question-detail"),    
    path("create-questions/", views.QuestionCreateView.as_view(), name="create-questions"),   
    path("update-question/<pk>/", views.QuestionUpdateView.as_view(), name="update-question"), 
    path("delete-question/<pk>/", views.QuestionDeleteView.as_view(), name="delete-question"), 
    
    # ANCHOR QUESTIONS    
    path("create-options/", views.OptionCreateView.as_view(), name="create-options"),
    path("option-detail/<pk>/", views.OptionDetailView.as_view(), name="option-detail"), 
    path('options/', views.OptionsListView.as_view(), name="options"), 
    path("update-option/<pk>/", views.OptionUpdateView.as_view(), name="update-option"), 
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)