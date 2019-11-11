from django.shortcuts import render
from django.http import HttpResponse
from .models import Athletes, Results


def view_certificate(request):
    return render(request, 'index.html')


def bib_no_submission(request):
    bibno = request.POST['bibno']
    mobileno = request.POST['mobileno']
    db_bibno = Athletes.objects.filter(bibno=bibno).values_list('bibno', flat=True).first()
    db_mobileno = Athletes.objects.filter(bibno=bibno).values_list('mobilenumber', flat=True).first()
    db_name = Athletes.objects.filter(bibno=bibno).values_list('name', flat=True).first()
    context = {
        'db_name': db_name,
        'db_bibno': db_bibno,
        'db_mobileno': db_mobileno,
    }
    if bibno == db_bibno and db_mobileno == mobileno:
        return render(request, 'result.html', {'context': context})
    else:
        return render(request, 'error.html', {'db_bibno': db_bibno,
                                              'bibno': bibno})

