from django.urls import path,include
from User import views

app_name='User'

urlpatterns=[
    path('userprofile/',views.userprofile,name='userprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('Homepage/',views.home_page,name='homepage'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('usercomplaint/',views.sendcomplaint,name='usercomplaint'),
    path('userfeedback/',views.userfeedback,name='userfeedback'),
    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('deletecomplaint/<int:id>',views.deletecomplaint,name="deletecomplaint"),
    path('medicinelist/',views.medicinelist,name='medicinelist'),
    path('requestmedicine/<int:id>',views.requestmedicine,name='requestmedicine'),
    path('foodlist/',views.foodlist,name='foodlist'),
    path('requestfood/<int:id>',views.requestfood,name='requestfood'),

]
