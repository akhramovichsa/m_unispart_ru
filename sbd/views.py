from django.shortcuts import get_object_or_404, render
from sbd.models import Tvr

def search(request):
    return render(request, 'search.html')


def gart(request):
    qq = request.GET['q']
    code = get_object_or_404(Tvr, product_code=qq)
    return render(request, 'gart.html', {'g': code})
