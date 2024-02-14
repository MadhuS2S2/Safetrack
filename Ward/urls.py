from django.urls import path,include
from Ward import views

app_name='Ward'

urlpatterns = [
    path('memberprofile/',views.memberprofile,name="memberprofile"),
    path('Homepage/',views.home_page,name='homepage'),
    path('memberedit/',views.memberedit,name='memberedit'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('kitchenReg/',views.kitchenreg,name='kitchenreg'),
    path('viewpatient/',views.viewpatient,name='viewpatient'),
    path('medicinerequest/',views.medicinerequest,name='medicinerequest'),
    path('deletepatient/<int:id>',views.deletepatient,name="deletepatient"),
    path('deletekitchen/<int:id>',views.deletekitchen,name="deletekitchen"),
    path('viewkitchen/',views.viewkitchen,name='viewkitchen'),

]
