from django.utils.timezone import utc
from rest_framework import serializers
from .models import *
import datetime
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
    expire_time = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Survey
        fields = '__all__'

    def get_expire_time(self, obj):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        hours_added = obj.created_at + datetime.timedelta(hours=24)
        timediff = hours_added - now
        seconds = timediff.seconds
        d=str(datetime.timedelta(seconds=seconds))
        return d


class SurveySerializerRet(serializers.ModelSerializer):
    assign_user=UserSerializer(many=True)
    created_by=UserSerializer()
    expire_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'

    import datetime
    def to_representation(self, instance):
        response = super().to_representation(instance)
        question=instance.question_set.all()
        response['questions'] = QuestionSerializer(question,many=True).data
        return response

    def get_expire_time(self, obj):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        hours_added = obj.created_at + datetime.timedelta(hours=24)
        timediff = hours_added - now
        seconds = timediff.seconds
        d=str(datetime.timedelta(seconds=seconds))
        return d


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['text','question']

class AnswersSerializerR(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
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





