from django.shortcuts import get_object_or_404, render

from sbd.models import Tvr
import re


def search(request, srq):
    p = re.compile(srq)
    # sout = p.search('tempo')
    for q in Tvr._meta.get_all_field_names():
        sout = q
    # if p.search(q):
    #        sout = p.search(q)
    return render(request, 'search.html', {'sout': sout})


def gart(request, rq):
    art = get_object_or_404(Tvr, pk=rq)
    return render(request, 'gart.html', {'art': art})
