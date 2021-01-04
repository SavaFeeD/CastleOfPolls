from django.contrib import admin

from .models import Choice, Question, Voted


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Description', {'fields': ['question_short_description', 'question_full_description']}),
        ('Date information', {'fields': ['pub_date', 'term_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'question_short_description', 'question_full_description', 'pub_date',
                    'was_published_recently', 'will_be_removed')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class VotedAdmin(admin.ModelAdmin):
    list_display = ('question', 'user')
    list_filter = ['question']
    search_fields = ['question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Voted, VotedAdmin)
