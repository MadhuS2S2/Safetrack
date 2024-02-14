from django.urls import path,include
from Guest import views

app_name='Guest'

urlpatterns=[
    path('user/',views.user,name='user'),
    path('wardmember/',views.wardmember,name='wardmember'),
    path('ashaworker/',views.ashaworker,name='ashaworker'),
    path('healthcenter/',views.healthcenter,name='healthcenter'),
    path('ajaxpan/',views.ajaxpan,name="ajaxpan"),
    path('ajaxward/',views.ajaxward,name="ajaxward"),
    path('login/',views.login,name='login'),
    
]
