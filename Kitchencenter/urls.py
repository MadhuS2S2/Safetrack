from django.urls import path,include
from Kitchencenter import views

app_name='kitchencenter'

urlpatterns=[
    path('Homepage/',views.home_page,name='homepage'),
    path('kitchenprofile/',views.kitchenprofile,name='kitchenprofile'),
    path('kitchenedit/',views.kitchenedit,name='kitchenedit'),
    path('viewrequest/',views.viewrequest,name='viewrequest'),
    path('addfood/',views.addfood,name='addfood'),
    path('assigntask/<int:id>',views.assigntask,name='assigntask'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('addfood/',views.addfood,name='addfood'),
    
]
