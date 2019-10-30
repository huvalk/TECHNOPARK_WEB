from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

# в классе нужен Meta class (verbous_name) и __str__


class Member(User):
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    avatar = models.ImageField(upload_to='question/static/avatars/', default='question/static/avatars/avatar.png',
                               blank=True, verbose_name='Аватар')

    objects = UserManager()

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return '%s - %d' % (self.username, self.rating)

    def create_user(name, password):
        user = Member.objects.create()
        user.username = name
        user.set_password(password)
        user.save()


class Tag(models.Model):
    body = models.CharField(max_length=40, verbose_name='Body')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.body


class Queion(models.Model):
    head = models.CharField(max_length=200, verbose_name='')
    body = models.TextField(verbose_name='Body')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    author = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Author')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.head


class Answer(models.Model):
    body = models.TextField(verbose_name='Body')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    author = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Author')
    que = models.ForeignKey('Queion', on_delete=models.CASCADE, verbose_name='Question')
    correct = models.BooleanField(default=False, verbose_name='Correct')

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return "%r" % self.correct


class TagPivot(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name='Tag')
    question = models.ForeignKey('Queion', on_delete=models.CASCADE, verbose_name='Question')

    class Meta:
        verbose_name = 'TagPivot'
        verbose_name_plural = 'TagPivots'

    def __str__(self):
        return 'TagPivot'


# class Like(models.Model):
#     value = models.IntegerField(
#         default=0,
#         validators=[MaxValueValidator(1), MinValueValidator(-1)]
#      )
#
#     member = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Member')
#
#     class Meta:
#         verbose_name = 'Like'
#         verbose_name_plural = 'Likes'
#
#     def __str__(self):
#         return '%d' % self.value