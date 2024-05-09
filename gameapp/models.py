from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, ):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None,):
        if not email:
            raise ValueError('Email is Required')
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

def default_id():
    return {
        "id" : []
    }
    
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20)
    email = models.EmailField(db_index=True, unique=True)
    score = models.IntegerField(default=0)
    attempted_questions = models.JSONField(default=default_id)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    
    
    class Meta:
        ordering = ['-date_joined']
        
    def __str__(self):
        return self.email
    
class QuestionsModel(models.Model):    
    question_text = models.CharField(max_length=500, db_index=True)
    answer_option = models.CharField(max_length=20)
    answer_text = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
        
    def get_absolute_url(self):
        return reverse('question-detail', kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.question_text
    
class OptionsModel(models.Model):
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE, db_index=True)
    option = models.CharField(max_length=20)
    options_text = models.CharField(max_length=500)
    
    class Meta:
        ordering = ['-id']
        
    def get_absolute_url(self):
        return reverse('option-detail', kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.options_text 