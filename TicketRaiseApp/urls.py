from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    path('credentialCheck/', views.credentialCheck, name="credentialCheck"),

    path('home/',views.home,name='home'),
    path('newTicket/',views.newTicket,name='newTicket'),

    path('addQuery/',views.addQuery,name='addQuery'),
    path('studentSignup/',views.studentSignup,name='studentSignup'),
    path('addStudent/',views.addStudent,name='addStudent'),

    path('removeInQuery/<int:queryId>/', views.removeInQuery, name='removeInQuery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
