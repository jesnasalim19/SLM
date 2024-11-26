from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('reg',views.reg),
    path('log',views.log),
    path('home',views.home),
    path('leave_request',views.leave_request),
    path('remaining',views.remaining),
    path('leave_cancel',views.leave_cancel),
    path('leave_history',views.leave_history),
    path('notif',views.notif),
    path('salary',views.salary),
    path('lwasalary',views.lwasalary),
    path('view_assign',views.view_assign),

]