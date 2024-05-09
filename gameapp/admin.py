from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, QuestionsModel, OptionsModel

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'score', 'attempted_questions')
    search_fields = ('email', 'first_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('score', 'attempted_questions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )


class OptionsModelInline(admin.TabularInline):
    model = OptionsModel
    extra = 1

@admin.register(QuestionsModel)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_option', 'answer_text', 'date_created')
    search_fields = ('question_text',)
    ordering = ('-id',)
    inlines = [OptionsModelInline]


@admin.register(OptionsModel)
class OptionsModelAdmin(admin.ModelAdmin):
    list_display = ('option', 'options_text', 'question')
    search_fields = ('option', 'options_text')
    ordering = ('-id',)
    
