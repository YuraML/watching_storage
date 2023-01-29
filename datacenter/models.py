import django
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        visitor_leaved_at = self.leaved_at
        return django.utils.timezone.localtime(visitor_leaved_at) - self.entered_at

    def is_visit_long(self, minutes=60):
        time_limit = django.utils.timezone.timedelta(minutes=minutes)
        return self.get_duration() > time_limit


def format_duration(duration):
    seconds = duration.total_seconds()
    minutes = int((seconds % 3600) // 60)
    hours = int(seconds // 3600)
    if hours == 0:
        return f'{minutes} мин'
    return f'{hours} ч {minutes} мин'   