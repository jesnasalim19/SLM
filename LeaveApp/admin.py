from django.contrib import admin
from.models import reg_tbl,leave_req,leave_reg_lwa
# Register your models here.
admin.site.register(reg_tbl),
admin.site.register(leave_req),
admin.site.register(leave_reg_lwa)