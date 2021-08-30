from rest_framework import serializers
from .models import *
from .models import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')




class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model=Survey
        fields=('survey_name','assign_user')

class SurveySerializerR(serializers.ModelSerializer):
    assign_user=UserSerializer(many=True)
    created_by=UserSerializer()
    class Meta:
        model = Survey
        fields = '__all__'


class SurveySerializerRet(serializers.ModelSerializer):
    assign_user=UserSerializer(many=True)
    created_by=UserSerializer()
    class Meta:
        model = Survey
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        question=instance.question_set.all()
        response['questions'] = QuestionSerializer(question,many=True).data
        return response





class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('survey','text')

class ReportSerializerR(serializers.ModelSerializer):
    survey=SurveySerializerR()
    created_by=UserSerializer()
    class Meta:
        model = Report
        fields = '__all__'


