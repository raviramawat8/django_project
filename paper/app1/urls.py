from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login/signup/',views.signup,name='signup1'),
    path('sign/',views.sign,name='sign'),
]

