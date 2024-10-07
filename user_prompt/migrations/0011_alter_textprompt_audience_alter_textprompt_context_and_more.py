# Generated by Django 5.1.1 on 2024-10-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_prompt', '0010_alter_hint_audience_alter_hint_context_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textprompt',
            name='audience',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='context',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='examples',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='format_result',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='goal',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='keywords',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='restrictions',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='role',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='tone',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='textprompt',
            name='writing_style',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
