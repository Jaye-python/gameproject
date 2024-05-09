from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser, OptionsModel, QuestionsModel
from django.forms import inlineformset_factory


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ['question_text', 'answer_option']
    
    
class OptionsForm(forms.ModelForm):
    class Meta:
        model = OptionsModel
        fields = ['option', 'options_text']
        # labels = {
        #     'option': 'Option',
        #     'options_text': 'Option Text',
        # }
        # widgets = {
        #     'options_text': forms.Textarea(attrs={'rows': 4}),  # Adjust rows as needed
        # }