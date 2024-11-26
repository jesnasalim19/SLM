from django.urls import path
from . import views
urlpatterns = [
    path('',views.adminlog),
    path('dashboard',views.dashboard),
    path('leaveinfo',views.leave_info),
    path('staff_details',views.staff_details),
    path('staff_delete',views.staff_delete),
    path('leave-requests', views.leave_request_list),
    path('lwa-leave-requests', views.lwa_leave_request_list),
    path('lwa_approve_leave',views.lwa_approve_leave),
    path('approve-leave', views.approve_leave),
    path('approves',views.approves),
    path('lwa_approves',views.lwa_approves),
    path('payroll',views.payroll),
    path('lwa_payroll',views.lwa_payroll),
    path('salarycredit',views.salarycredit),
    path('lwa_salarycredit',views.lwa_salarycredit),
    path('staff_assign',views.staff_assign),
    path('newstaff',views.newstaff),
    path('newstaffl',views.newstaffl),
    path('assigned_staff',views.assigned_staff),
    path('assigned_staffl',views.assigned_staffl),
   
]