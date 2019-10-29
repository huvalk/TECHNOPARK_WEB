from django.contrib import admin
from .models import Member, Tag, Queion, Answer, TagPivot


admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(Queion)
admin.site.register(Answer)
admin.site.register(TagPivot)
