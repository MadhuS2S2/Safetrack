from django.urls import path,include
from Admin import views

app_name="Admin"

urlpatterns=[
        path('district/',views.district,name="district"),
        path('panchayat/',views.panchayat,name="panchayat"),
        path('ward/',views.ward,name="ward"),
        path('ajaxward/',views.ajaxward,name="ajaxward"),
        path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
        path('deletecomplaint/<int:id>',views.deletecomplaint,name="deletecomplaint"),
        path('reply/<int:id>',views.reply,name="reply"),
]