from django.urls import path 
from . import views
app_name="core"

urlpatterns = [
    path('', views.index, name="index"),
    path('submit-todo', views.add_todo, name="submit-todo"),
    path('update-todo/<int:pk>', views.update_todo, name="update-todo"),
    path('delete-todo/<int:pk>', views.delete_todo, name="delete-todo"),
]

