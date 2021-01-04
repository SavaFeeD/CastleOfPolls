from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    term_date = models.DateTimeField('date term')
    question_short_description = models.CharField(max_length=200)
    question_full_description = models.CharField(max_length=200)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def will_be_removed(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.term_date <= now

    will_be_removed.admin_order_field = 'term_date'
    will_be_removed.boolean = True
    will_be_removed.short_description = 'Remove soon?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Voted(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.question_text
