from django_cron import CronJobBase, Schedule
import datetime 
from django.utils import timezone
from .models import Quiz

utc=timezone.utc
now = datetime.datetime.now().replace(tzinfo=utc)

class UpdateStatus(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'base.update_status'    # a unique code

    def do(self):
        quizzes = Quiz.objects.all()
        for quiz in quizzes:
            if quiz.start_date.replace(tzinfo=utc) <= now <= quiz.end_date.replace(tzinfo=utc):
                quiz.status = 'active'
            elif quiz.start_date.replace(tzinfo=utc) > now:
                quiz.status = 'inactive'
            else:
                quiz.status = 'finished'
            quiz.save()
