# Generated by Django 3.2.8 on 2022-01-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
            ],
        ),
    ]
