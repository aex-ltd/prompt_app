# Generated by Django 5.1.1 on 2024-10-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_prompt', '0008_hint_rename_response_textprompt_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='audience',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='context',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='examples',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='format_result',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='goal',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='keywords',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='restrictions',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='role',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='tone',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='hint',
            name='writing_style',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
