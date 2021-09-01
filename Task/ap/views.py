from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import *
from .suvey_check import auth_middleware
from rest_framework.permissions import IsAuthenticated
class SurveyView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    @method_decorator(auth_middleware)
    def list(self, request):
        queryset = Survey.objects.filter(is_active=True)
        serializer = SurveySerializerR(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        user=request.user
        serializer=SurveySerializer(data=request.data)
        if serializer.is_valid():
            survey_name=serializer.validated_data['survey_name']
            assign_users=serializer.validated_data['assign_user']
            survey=Survey.objects.create(survey_name=survey_name,created_by=user)
            for a in assign_users:
                survey.assign_user.add(a)
                survey.save()
        else:
            return Response(serializer.errors)

        m="Survey add Successfully"
        s=SurveySerializerR(survey)
        return Response({'message':m,'data':s.data})

    def retrieve(self, request, pk=None):
        queryset = Survey.objects.all()
        sur = get_object_or_404(queryset, pk=pk)
        serializer = SurveySerializerRet(sur)
        return Response(serializer.data)


class QuestionView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self, request):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            sur=serializer.validated_data['survey']
            question_name=serializer.validated_data['question_name']
            q=sur.question_set.all()
            if q.count() ==10 :
                print(q.count())
                m="Question limited excid"
                return Response({'message':m})
            else:
                qes=Question.objects.create(survey=sur,question_name=question_name)
        else:
            return Response(serializer.errors)

        m = "Survey add Successfully"
        q = QuestionSerializer(qes)
        return Response({'message': m, 'data': q.data})


class AnswersView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request):
        user=request.user
        serializer=AnswersSerializer(data=request.data)
        if serializer.is_valid():
            ans = serializer.validated_data['text']
            question = serializer.validated_data['question']
            answer=Answers.objects.create(text=ans, question=question,user=user)
            answer.save()
        else:
            return Response(serializer.errors)
        m = "Answer Submited Successfully"
        q = AnswersSerializerR(answer)
        return Response({'message': m, 'data': q.data})

class ReportView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request):
        user = request.user
        serializer=ReportSerializer(data=request.data)
        if serializer.is_valid():
            report = serializer.validated_data['text']
            survey = serializer.validated_data['survey']
            report=Report.objects.create(text=report, survey=survey,created_by=user)
            report.save()
        else:
            return Response(serializer.errors)
        m = "Report Submited Successfully"
        q = ReportSerializerR(report)
        return Response({'message': m, 'data': q.data})


