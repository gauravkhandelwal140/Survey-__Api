from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
router=DefaultRouter()
router.register('survey',SurveyView,basename='survey')
router.register('question',QuestionView,basename='question')
router.register('answers',AnswersView,basename='answers')
router.register('report',ReportView,basename='report')
urlpatterns = [
     path('',include(router.urls))

]
