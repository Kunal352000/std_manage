from django.urls import path
from student.views import home,std_add,delete_std,update_std,do_update_std
urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-std/",std_add),
    path("delete-std/<int:roll>",delete_std),
    path("update-std/<int:roll>",update_std),
    path("do-update-std/<int:roll>",do_update_std)
]