from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        (None,               {'fields': ['question_text']}),
    ]

#admin.site.register(Question)
admin.site.register(Question,QuestionAdmin) #customised
