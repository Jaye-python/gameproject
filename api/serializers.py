from rest_framework import serializers
from gameapp.models import CustomUser, QuestionsModel, OptionsModel

class OptionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsModel
        fields = ('id', 'option', 'options_text')

class QuestionsModelSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField() 

    class Meta:
        model = QuestionsModel
        fields = ('id', 'question_text', 'options', 'date_created')
        
    def get_options(self, obj):
        options = OptionsModel.objects.filter(question=obj.id)
        serializer = OptionsModelSerializer(options, many=True)
        return serializer.data
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'score')
        
class CreateQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsModel
        fields = ('question_text', 'answer_option', 'answer_text' )
        
class AdminQuestionsModelSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField() 

    class Meta:
        model = QuestionsModel
        fields = ('id', 'question_text', 'answer_option', 'answer_text', 'options', 'date_created')
        
    def get_options(self, obj):
        options = OptionsModel.objects.filter(question=obj.id)
        serializer = OptionsModelSerializer(options, many=True)
        return serializer.data
    
class AdminOptionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsModel
        fields = ('id', 'question', 'option', 'options_text')
