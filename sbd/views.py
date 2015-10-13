from django.shortcuts import get_object_or_404, render

from sbd.models import Tvr
import re


def search(request, srq):
    p = re.compile(srq)
    for i in range(5):
        q = get_object_or_404(Tvr, art=i)
        if p.search(q.name):
            sout = q.name
    return render(request, 'search.html', {'sout': sout})


def gart(request, rq):
    art = get_object_or_404(Tvr, pk=rq)
    return render(request, 'gart.html', {'art': art})
