from django.urls import path,include
from HealthCenter import views

app_name='Healthcenter'

urlpatterns=[
    path('Homepage/',views.home_page,name='homepage'),
    path('profilepage/',views.profilepage,name='profilepage'),
    path('centreprofile/',views.centreprofile,name='centreprofile'),
    path('centreedit/',views.centreedit,name='centreedit'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('viewpatient/',views.viewpatient,name='viewpatient'),
    path('addmedicines/',views.addmedicines,name='addmedicines'),
    path('deletepatient/<int:id>',views.deletepatient,name="deletepatient"),
    path('patientdischarge/<int:id>',views.patientdischarge,name="patientdischarge"),
    path('ajaxward/',views.ajaxward,name="ajaxward"),
    path('ajaxpan/',views.ajaxpan,name="ajaxpan"),
    path('district/',views.district,name="district"),
    path('requestlist/',views.requestlist,name="requestlist"),
    path('assigntask/<int:id>',views.assigntask,name='assigntask'),
    path('PatientReport/',views.PatientReport,name='PatientReport'),
    path('PatientcountReport/',views.PatientcountReport,name='PatientcountReport'),
]
