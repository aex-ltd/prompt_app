# Generated by Django 5.1.1 on 2024-09-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_prompt', '0002_remove_textprompt_file_textprompt_response_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textprompt',
            name='response',
            field=models.TextField(),
        ),
    ]