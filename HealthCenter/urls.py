from django.urls import path,include
from HealthCenter import views

app_name='Healthcenter'

urlpatterns=[
    path('Homepage/',views.home_page,name='homepage'),
    path('centreprofile/',views.centreprofile,name='centreprofile'),
    path('centreedit/',views.centreedit,name='centreedit'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('viewpatient/',views.viewpatient,name='viewpatient'),
    path('medicinerequest/<int:id>',views.medicinerequest,name='medicinerequest'),
    path('deletepatient/<int:id>',views.deletepatient,name="deletepatient"),
    path('ajaxward/',views.ajaxward,name="ajaxward"),
    path('ajaxpan/',views.ajaxpan,name="ajaxpan"),
    path('district/',views.district,name="district"),
    path('foodrequest/<int:fid>',views.foodrequest,name="foodrequest"),
]
