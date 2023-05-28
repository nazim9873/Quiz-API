# Generated by Django 4.2.1 on 2023-05-26 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2048)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('inactive', 'inactive'), ('active', 'active'), ('finished', 'finished')], default='inactive', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048, verbose_name='option text')),
                ('correct', models.BooleanField(default=False)),
                ('from_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.quiz')),
            ],
        ),
    ]
