# Generated by Django 4.2.4 on 2023-08-17 08:50

from django.db import migrations, models
import django.db.models.deletion
import my_app.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('resume', models.FileField(blank=True, default='', null=True, upload_to=my_app.models.get_my_doc_upload_path)),
                ('readme', models.TextField()),
                ('currentStatus', models.CharField(max_length=255)),
                ('codingAchievement', models.CharField(max_length=255)),
                ('myImage', models.ImageField(default='', upload_to=my_app.models.get_my_doc_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=255)),
                ('skill_level', models.IntegerField()),
                ('skill_description', models.TextField()),
                ('skill_icon', models.CharField(max_length=255)),
                ('my_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='my_app.aboutme')),
            ],
        ),
    ]
