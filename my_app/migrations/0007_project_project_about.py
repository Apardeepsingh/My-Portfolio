# Generated by Django 4.2.4 on 2023-08-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_remove_skill_my_skills_project_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_about',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]