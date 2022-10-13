from django.urls import path
from . import views
from .views import GeeksDeleteView


urlpatterns = [
    path('create/', views.create_view),
    path('', views.list_view),
    path('<id>', views.detail_view),
    path('<id>/update', views.update_view),
    path('<pk>/delete/',GeeksDeleteView.as_view())
]
