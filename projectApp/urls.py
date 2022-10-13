from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_view),
    path('',views.list_view),
    path('<id>',views.detail_view),
    path('<id>/update',views.update_view)
]
