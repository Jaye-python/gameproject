from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout 
from gameapp.forms import LoginForm, QuestionForm, SignupForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, QuestionsModel, OptionsModel
from django.urls import reverse_lazy
from django.db.models import F

def home(request):
    scores = CustomUser.objects.all()
    return render(request, 'gameapp/home.html', {'scores':scores})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'gameapp/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'gameapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class QuestionsListView(LoginRequiredMixin, ListView):
    model = QuestionsModel
    context_object_name = 'questions'
    template_name = 'gameapp/questions.html'
    paginate_by = 1
    
    def get_queryset(self, *args, **kwargs):
        user_id = self.request.user.id
        user_model = CustomUser.objects.get(id=user_id)
        attempted_questions = user_model.attempted_questions["id"]
                
        queryset = QuestionsModel.objects.exclude(id__in = attempted_questions)                
        
        return queryset 

        
    def post(self, *args, **kwargs):
        selected_option_id = self.request.POST.get('selected_option')
        selected_option = OptionsModel.objects.get(pk=selected_option_id)
        question_id = selected_option.question_id
        
        user_selected_option = selected_option.option.lower()
        answer = QuestionsModel.objects.get(id = question_id).answer_option.lower()
                
        user_id = self.request.user.id
        user_model = CustomUser.objects.get(id=user_id)       
               
        
        if user_selected_option == answer:
            user_model.score = F('score') + 1
            
        if selected_option.question.id not in user_model.attempted_questions["id"]:
            user_model.attempted_questions["id"].append(selected_option.question.id)
        
        user_model.save()

        return redirect('home')  
    
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = QuestionsModel
    context_object_name = 'question'
    template_name = 'gameapp/question_detail.html'
    
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = QuestionsModel
    template_name = 'gameapp/create_question.html' 
    fields = ["question_text", "answer_text", "answer_option"]
    success_url = reverse_lazy('questions')
    
    
class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = QuestionsModel
    fields = ["question_text", "answer_option"]
    template_name = 'gameapp/update_question.html'
    
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = QuestionsModel
    success_url = reverse_lazy("questions")
    
class OptionCreateView(LoginRequiredMixin, CreateView):
    model = OptionsModel
    template_name = 'gameapp/create_option.html' 
    fields = ["question", "option", "options_text"]
        
class OptionDetailView(LoginRequiredMixin, DetailView):
    model = OptionsModel
    context_object_name = 'option'
    template_name = 'gameapp/option_detail.html'

class OptionsListView(LoginRequiredMixin, ListView):
    model = OptionsModel
    context_object_name = 'options'
    template_name = 'gameapp/options.html'
    paginate_by = 1
    
class OptionUpdateView(LoginRequiredMixin, UpdateView):
    model = OptionsModel
    fields = ["options_text", "option"]
    template_name = 'gameapp/update_option.html'
    


    