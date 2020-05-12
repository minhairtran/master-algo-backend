

from django.urls import path
from .views import feedback_detail_view, feedback_list_view, feedback_create_view, profile_view, feedback_delete_view

urlpatterns = [
    path('', feedback_list_view),
    path('create/', feedback_create_view),
    path('<int:feedback_id>/', feedback_detail_view),
    path('<int:feedback_id>/delete/', feedback_delete_view),
]