from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from .models import Feedback
from django.utils.http import is_safe_url

from .forms import FeedbackForm
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def profile_view(request, *args, **kwargs):
    return render(request, "pages/profile.html", context={}, status=200)


def feedback_create_view(request, *args, **kwargs):
    form = FeedbackForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = FeedbackForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
        
    return render(request, "components/form.html", context={"form": form})


def feedback_detail_view(request, feedback_id, *args, **kwargs):
    data = {
        "id": feedback_id,
        # "image_path": obj.image.path
    }
    status = 200
    try:
        a_feedback = Feedback.objects.get(id=feedback_id)
        data['content'] = a_feedback.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)


def feedback_list_view(request, *args, **kwargs):
    qs = Feedback.objects.all()
    feedbacks_list = [each_feedback.serialize() for each_feedback in qs]
    data = {"response": feedbacks_list}
    return JsonResponse(data)
