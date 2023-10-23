from django.urls import path
from student.views import home,std_add
urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-std/",std_add),
]