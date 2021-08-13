from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [

    url('^$', views.dashboard, name='home'),
    url('login/', views.loginPage, name='login'),
    url('logout/', views.logoutPage, name='logout'),
    url('signup/', views.registerPage, name= 'signup'),
    url('students/', views.studentsPage, name='students'),
    path('supervisor/<int:my_id>/', views.supervisor, name='supervisors'),
    path('rating/<int:my_id>/', views.rating, name='rating'),
    path('codRating/<int:my_id>/', views.codRating, name='codRating'),
    path('contact/<int:my_id>', views.contact, name='contact'),
    # path('secondForm/', views.secondForm, name='secondForm'),
    path('coordinator/<int:my_id>/', views.coordinatorRating, name='coordinators'),
]