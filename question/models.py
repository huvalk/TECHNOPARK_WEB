from django.db import models
from django.contrib.auth.models import User, UserManager
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

# в классе нужен Meta class (verbous_name) и __str__


class Member(User):
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    avatar = models.ImageField(upload_to='question/media/avatars/', default='avatars/avatar.png',
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


# class TagsManager(models.Manager):


class Question(models.Model):
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    head = models.CharField(max_length=200, verbose_name='')
    body = models.TextField(verbose_name='Body')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    author = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Author')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.head

    def count_answers(self):
        res = Answer.objects.get_queryset().filter(que=self.id).count()
        return res

    def all_tags_for(self):
        res = Tag.objects.get_queryset().filter(question=self.id)
        return res


class Tag(models.Model):
    body = models.CharField(max_length=40, verbose_name='Body')
    question = models.ManyToManyField('Question')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.body


class Answer(models.Model):
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    body = models.TextField(verbose_name='Body')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    author = models.ForeignKey('Member', on_delete=models.CASCADE, verbose_name='Author')
    que = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Question')
    correct = models.BooleanField(default=False, verbose_name='Correct')

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return "%r" % self.correct


# class TagPivot(models.Model):
#     tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name='Tag')
#     question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Question')
#
#     class Meta:
#         verbose_name = 'TagPivot'
#         verbose_name_plural = 'TagPivots'
#
#     def __str__(self):
#         return 'TagPivot'


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


def Paginate_by(page, order, tag='Tag'):
    if tag == 'Tag':
        question_list = Question.objects.all().order_by(order)
    else:
        try:
            tag = Tag.objects.get(body=tag)
        except ObjectDoesNotExist:
            raise Http404
        question_list = tag.question.all().order_by('date')

    paginator = Paginator(question_list, 1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return questions