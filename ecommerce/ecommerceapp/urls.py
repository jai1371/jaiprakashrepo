from django.contrib import admin
from django.urls import path
from .views import studentlistview,studentcreateview,studentdetailview,studentupdateview,studentdeleteview,profiletemplateview,\
    exception_signal,school
# from .views import contact,loginformview,userchange,home,verify
'''registerform'''
urlpatterns = [
    # path('register',contact),
    # # path('',registerform.as_view()),
    # path('login/',loginformview.as_view()),
    # path('change/',userchange),
    # path('',home),
    # path('verify/<str:token>/',verify,name='verify'),
    path('student/',studentlistview.as_view(),name='studentlist'),
    path('studentdetail/<int:pk>',studentdetailview.as_view(),name='studentdetailview'),
    path('studentcreate/',studentcreateview.as_view(),name='studentcreate'),
    path('studentupdate/<int:pk>',studentupdateview.as_view(),name='studentupdate'),
    path('studentdelete/<int:pk>',studentdeleteview.as_view(),name='studentdelete'),


#accounts
    path('/profile/',profiletemplateview.as_view(),name='profiletemplateview'),
    # path("profile/", LogouttemplateView.as_view(), name="logout"),
    # path("profile/", PasswordChangetemplateView.as_view(), name="password_change" ),
    # # path("profile/",PasswordResettemplateView.as_view(), name="password_reset"),
    # # path("profile/done/",PasswordResetDonetemplateView.as_view(),name="password_reset_done",),
    # # path("profile/<uidb64>/<token>/",PasswordResetConfirmtemplateView.as_view(),name="password_reset_confirm",),
    # # path("profile/done/",PasswordResetCompletetemplateView.as_view(),name="password_reset_complete",),


    path('exception/',exception_signal),
    path("school/",school)

]
