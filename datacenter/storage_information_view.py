from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': visit.is_visit_long(minutes=60)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


