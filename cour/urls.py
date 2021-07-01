from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="my_index"),
    path('new/', views.new, name="my_new"),
    path('view/<int:course_id>/', views.view, name="my_view"),
    path('comment/<int:course_id>/', views.comment, name="my_comment"),
    path('delete/', views.delete, name="my_delete"),
]