from django.contrib import admin
from .models import Member, Tag, Question, Answer


admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
