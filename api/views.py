from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from api.serializers import AdminOptionsModelSerializer, AdminQuestionsModelSerializer, CreateQuestionsSerializer, CustomUserSerializer, OptionsModelSerializer, QuestionsModelSerializer
from gameapp.models import QuestionsModel, OptionsModel, CustomUser
import random
    
class QuestionsListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_random_question(self, user_model):
        attempted_questions = user_model.attempted_questions.get('id', [])
        remaining_questions = QuestionsModel.objects.exclude(id__in=attempted_questions)
        if remaining_questions.exists():
            return random.choice(remaining_questions)
        return None
    
    def get(self, request, format=None):
        user_id = request.user.id
        user_model = CustomUser.objects.get(id=user_id)
        
        selected_question = self.get_random_question(user_model)
        if selected_question:
            serializer = QuestionsModelSerializer(selected_question)
            return Response(serializer.data)
        else:
            return Response({'message': 'No remaining questions'}, status=status.HTTP_404_NOT_FOUND)
    
        
    def post(self, request, format=None):
        selected_question_id = request.data.get('selected_question')
        selected_option_id = request.data.get('selected_option')
        selected_question = QuestionsModel.objects.get(pk=selected_question_id)
        
        selected_option = OptionsModel.objects.get(pk=selected_option_id)
        

        user_selected_option = selected_option.option.lower()
        answer = selected_question.answer_option.lower()
                
        user_id = request.user.id
        user_model = CustomUser.objects.get(id=user_id)
        
        if user_selected_option == answer:
            user_model.score = F('score') + 1
            
        if selected_question_id not in user_model.attempted_questions.get('id', []):
            user_model.attempted_questions['id'].append(selected_question_id)
        
        user_model.save()

        return Response({'message': 'Response recorded successfully'}, status=status.HTTP_200_OK)

class UserScoresAPIView(APIView):
    def get(self, request, format=None):
        scores = CustomUser.objects.all().order_by('-score')
        serializer = CustomUserSerializer(scores, many=True)
        return Response(serializer.data)
    
    
class CreateQuestionAPIView(APIView):    
    def get(self, request, format=None):
        questions = QuestionsModel.objects.all()
        serializer = AdminQuestionsModelSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CreateQuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Question created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class OptionCreateAPIView(APIView):
    def get(self, request, format=None):
        options = OptionsModel.objects.all()
        serializer = AdminOptionsModelSerializer(options, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AdminOptionsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)