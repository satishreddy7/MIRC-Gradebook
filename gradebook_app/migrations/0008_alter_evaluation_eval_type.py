# Generated by Django 4.1.2 on 2022-12-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook_app', '0007_remove_course_max_score_remove_course_mean_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='eval_type',
            field=models.CharField(choices=[('Assignment', 'Assignment'), ('Quiz', 'Quiz'), ('MidExam', 'MidExam'), ('FinalExam', 'FinalExam'), ('Miscellaneous', 'Miscellaneous')], max_length=20),
        ),
    ]