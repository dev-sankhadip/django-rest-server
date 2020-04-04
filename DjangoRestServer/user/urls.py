from django.urls import path, include

from .views import AddRetrieveUserView, UpdateDeleteUserView

urlpatterns = [
    path('add/', AddRetrieveUserView.as_view()),
    path('list/', AddRetrieveUserView.as_view()),
    path('update/', UpdateDeleteUserView.as_view()),
    path('delete/', UpdateDeleteUserView.as_view())
]
