from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Algorithm

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def algorithm_detail_view(request, algorithm_id, *args, **kwargs):
    data = {
        "id": algorithm_id,
        # "image_path": obj.image.path
    }
    status = 200
    try:
        an_algorithm = Algorithm.objects.get(id=algorithm_id)
        data['title'] = an_algorithm.title
        data['subtitle'] = an_algorithm.subtitle
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)


def algorithm_list_view(request, *args, **kwargs):
    qs = Algorithm.objects.all()
    algorithms_list = [{"id": each_algorithm.id, "title": each_algorithm.title,
            "subtitle": each_algorithm.subtitle} for each_algorithm in qs]
    data = {"response": algorithms_list}
    return JsonResponse(data)
