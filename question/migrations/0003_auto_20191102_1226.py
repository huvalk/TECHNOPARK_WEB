# Generated by Django 2.2.6 on 2019-11-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_answer_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatar.png', upload_to='question/media/avatars/', verbose_name='Аватар'),
        ),
    ]