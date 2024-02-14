from django.urls import path,include
from Panchayat import views

app_name='panchayat'

urlpatterns=[
    # path('editprofile/',views.editprofile,name='editprofile'),
     path('Homepage/',views.home_page,name='homepage'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.change_password,name='changepassword'),
]
