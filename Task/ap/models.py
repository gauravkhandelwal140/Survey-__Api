from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Survey(models.Model):
    survey_name = models.CharField(max_length=50,)
    assign_user = models.ManyToManyField(User, related_name='assign_user')
    is_active = models.BooleanField(default=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)



class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_name = models.CharField('question', max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)


class Answers(models.Model):
    text = models.CharField('answers', max_length=45)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Report(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text=models.CharField('Report',max_length=20)

