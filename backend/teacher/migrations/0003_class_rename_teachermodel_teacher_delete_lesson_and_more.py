# Generated by Django 4.1.2 on 2022-10-13 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='TeacherModel',
            new_name='Teacher',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='teacher.teacher'),
        ),
    ]
