from django.contrib import admin
from . models import Leaveinfo,admin_log,payroll_tbl,assign_tbl,lwa_payroll_tbl
# Register your models here.
admin.site.register(admin_log),
admin.site.register(Leaveinfo),
admin.site.register(payroll_tbl),
admin.site.register(assign_tbl),
admin.site.register(lwa_payroll_tbl),