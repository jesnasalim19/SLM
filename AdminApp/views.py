from django.shortcuts import render,redirect
from. models import Leaveinfo,admin_log,payroll_tbl,assign_tbl,lwa_payroll_tbl
from LeaveApp.models import reg_tbl,leave_req,leave_reg_lwa
from django.contrib import messages
from django.db.models import F
# Create your views here.

def leave_info(request):
   idno = request.session['idl']
   objs = reg_tbl.objects.filter(id=idno)

# Check if leave information already exists for each user and create if not
   for obj in objs:
      if not Leaveinfo.objects.filter(sn=obj.fn, st=obj.st).exists():
         if obj.st == 'Teaching':
            obb = Leaveinfo.objects.create(sn=obj.fn, st=obj.st, cs=15, sl=3, cl=10, ml=180, pl=10, vc=60)
            obb.save()
         else:
            obb = Leaveinfo.objects.create(sn=obj.fn, st=obj.st, cs=20, sl=3, cl=10, ml=180, pl=10, vc=0)
            obb.save()

# Retrieve leave information for the user
   obc = Leaveinfo.objects.filter(sn=objs[0].fn, st=objs[0].st)
   return render(request, 'leave_info.html', {"leave_data": obc})


def adminlog(request):
   if request.method=='POST':
      usr = request.POST.get('usr')
      psw = request.POST.get('psw')
      obj = admin_log.objects.filter(usr=usr,psw=psw)
      if obj:
         return render(request,"dashboard.html")
      else:
         msg = 'Invalid Credentials'
         return render(request,"adminlog.html",{"error":msg})
   else:
      return render(request,"adminlog.html")

def dashboard(request):
   return render(request,"dashboard.html")
      
def staff_details(request):
   obj = reg_tbl.objects.all()
   return render(request,"staffs.html",{"staff":obj})

def staff_delete(request):
   idno = request.GET.get('idn')
   obj = reg_tbl.objects.filter(id=idno)
   obj.delete()
   return redirect("/AdminApp/staff_details")

def leave_request_list(request):
   leave_requests = leave_req.objects.filter(approved=False)
   return render(request, 'leave_request_list.html', {'leave_requests': leave_requests})

def lwa_leave_request_list(request):
   leave_requests = leave_reg_lwa.objects.filter(approved=False)
   return render(request, 'lwa.html', {'leave_requests': leave_requests})

def approve_leave(request):
   leave_id = request.GET.get('idn')
   leave_request = leave_req.objects.get(id=leave_id)
   leave_request.approved = True
   leave_request.save()
   messages.success(request, 'Leave request approved.')
   return redirect('/AdminApp/dashboard')

def lwa_approve_leave(request):
   leave_id = request.GET.get('idn')
   leave_request = leave_reg_lwa.objects.get(id=leave_id)
   leave_request.approved = True
   leave_request.save()
   messages.success(request, 'Leave request approved.')
   return redirect('/AdminApp/dashboard')

def approves(request):
   app = leave_req.objects.filter(approved=True)
   return render(request, 'approves.html', {'approved': app})

def lwa_approves(request):
   app = leave_reg_lwa.objects.filter(approved=True)
   return render(request, 'lwa_approves.html', {'approved': app})

def payroll(request):
   idno = request.GET.get('idn')
   obj = leave_req.objects.filter(id=idno)
   return render(request, 'payroll.html',{'payroll':obj})


def lwa_payroll(request):
   idno = request.GET.get('idn')
   obj = leave_reg_lwa.objects.filter(id=idno)
   return render(request, 'lwa_payroll.html',{'payroll':obj})

def lwa_salarycredit(request):
   sn = request.POST.get('sn')
   lt = request.POST.get('lt')
   st = request.POST.get('st')
   start = request.POST.get('start')
   end = request.POST.get('end')
   basic = request.POST.get('basic')
   lop = request.POST.get('lop')
   net = request.POST.get('net')
   obb = lwa_payroll_tbl.objects.filter(start=start) and lwa_payroll_tbl.objects.filter(sn=sn)
   if not(obb):
      obj = lwa_payroll_tbl.objects.create(sn=sn,lt=lt,st=st,start=start,end=end,basic=basic,lop=lop,net=net)
      obj.save()
   return redirect("/AdminApp/dashboard")

def salarycredit(request):
   sn = request.POST.get('sn')
   lt = request.POST.get('lt')
   st = request.POST.get('st')
   start = request.POST.get('start')
   end = request.POST.get('end')
   al = request.POST.get('al')
   nl = request.POST.get('nl')
   rm = request.POST.get('rm')
   basic = request.POST.get('basic')
   lop = request.POST.get('lop')
   net = request.POST.get('net')
   obb = payroll_tbl.objects.filter(start=start) and payroll_tbl.objects.filter(sn=sn)
   if not(obb):
      obj = payroll_tbl.objects.create(sn=sn,lt=lt,st=st,rm=rm,al=al,start=start,end=end,nl=nl,basic=basic,lop=lop,net=net)
      obj.save()
   return redirect("/AdminApp/dashboard")

def staff_assign(request):
   # Fetch approved leave requests from leave_req table
    leave_req_data = leave_req.objects.filter(approved=True)

    # Fetch approved leave requests from leave_reg_lwa table
    leave_reg_lwa_data = leave_reg_lwa.objects.filter(approved=True)

    # Combine the data into one dictionary
    combined_data = {
        'leave_req_data': leave_req_data,
        'leave_reg_lwa_data': leave_reg_lwa_data
    }

    # Render the template with the combined data
    return render(request, 'sassign.html', {"combined_data":combined_data})
def newstaff(request):
   idno = request.GET.get('idn')
   obj = leave_req.objects.filter(id=idno)
   obb = reg_tbl.objects.filter(st='Teaching')
   return render(request,"newstaff.html",{"lev":obj,"st":obb})

def newstaffl(request):
   idno = request.GET.get('idn')
   obj = leave_reg_lwa.objects.filter(id=idno)
   obb = reg_tbl.objects.filter(st='Teaching')
   return render(request,"newstaffl.html",{"lev":obj,"st":obb})

def assigned_staff(request):
   if request.method=='POST':
      sn = request.POST.get('sn')
      start = request.POST.get('start')
      end = request.POST.get('end')
      nl = request.POST.get('nl')
      fn = request.POST.get('fn')
      obj = assign_tbl.objects.create(sn=sn,start=start,end=end,nl=nl,fn=fn)
      obj.save()
      if obj:
         msg = "Assigned Successfully,"
         msg1 = "will get notification..."
      return render(request,"assign.html",{"staff":fn,"sn":sn,"start":start,"end":end,"nl":nl,"msg":msg,"msg1":msg1})
   return render(request,"newstaff.html")

def assigned_staffl(request):
   if request.method=='POST':
      sn = request.POST.get('sn')
      start = request.POST.get('start')
      end = request.POST.get('end')
      nl = request.POST.get('nl')
      fn = request.POST.get('fn')
      obj = assign_tbl.objects.create(sn=sn,start=start,end=end,nl=nl,fn=fn)
      obj.save()
      if obj:
         msg = "Assigned Successfully,"
         msg1 = "will get notification..."
      return render(request,"assignl.html",{"staff":fn,"sn":sn,"start":start,"end":end,"nl":nl,"msg":msg,"msg1":msg1})
   return render(request,"newstaffl.html")


   





