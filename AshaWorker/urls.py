from django.urls import path,include
from AshaWorker import views

app_name='Ashaworker'

urlpatterns=[
    path('workerprofile/',views.workerprofile,name='workerprofile'),
    path('workeredit/',views.workeredit,name='workeredit'),
    path('changepassword/',views.change_password,name='changepassword'),

]