from django.contrib import admin
from django.urls import path
from app.views import employeelistview,userlistview,employeedetailview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',employeelistview ),
    path('user',userlistview),
    path('<int:pk>',employeedetailview),
]
