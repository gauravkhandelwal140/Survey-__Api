# Generated by Django 3.2.6 on 2021-08-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0003_remove_question_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ap.survey'),
            preserve_default=False,
        ),
    ]
