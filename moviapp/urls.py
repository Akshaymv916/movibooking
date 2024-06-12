from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('cinema/<int:id>',views.details,name='cinema'),
    path('seat/<int:id>', views.seating, name='seat'),
    path('bookings', views.bookings, name='bookings'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('movibook',views.movibook,name='movibook'),
    path('ticket/<int:id>', views.moviticket, name='ticket'),
    path('dashoboard', views.dashboard, name='dashboard'),
    path('showadd',views.showadd,name='showadd'),
    path('add/<int:id>', views.addshow, name='addshow'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('search',views.search,name='search')

    # path('seat/<int:id>',views.seat,name='seat'),
    # path('booked',views.booked,name='booked'),
    # path('ticket/<int:id>',views.ticket,name='ticket'),

]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
