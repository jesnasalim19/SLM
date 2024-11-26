from django.shortcuts import render,redirect
from . models import reg_tbl,leave_req,leave_reg_lwa
from AdminApp.models import payroll_tbl,assign_tbl,lwa_payroll_tbl
# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        fn = request.POST.get('fn')
        mb = request.POST.get('mb')
        gn = request.POST.get('gn')
        st = request.POST.get('st')
        em = request.POST.get('em')
        ps = request.POST.get('ps')
        cps = request.POST.get('cps')
        obj = reg_tbl.objects.create(fn=fn,mb=mb,gn=gn,st=st,em=em,ps=ps,cps=cps)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render(request,"reg.html")
    else:
        return render(request,"reg.html")
def log(request):
    if request.method=='POST':
        em = request.POST.get('em')
        ps = request.POST.get('ps')
        obj = reg_tbl.objects.filter(em=em,ps=ps)
        if obj:
            for ls in obj:
                idno = ls.id
            request.session['idl']=idno
            obb = reg_tbl.objects.filter(id=idno)
            return render(request,"home.html",{"user":obb})
        else:
            msg = 'Invalid credentials..'
            return render(request,"log.html",{"error":msg})
    else:
        return render(request,"log.html")
def home(request):
    return render(request,"common.html")

def leave_request(request):
    idno = request.session.get('idl')  
    obj = reg_tbl.objects.get(id=idno)  
    sn = obj.fn
    st = obj.st
    if request.method == 'POST':
        sn = request.POST.get('sn')
        st = request.POST.get('st')
        lt = request.POST.get('lt')
        start = request.POST.get('start')
        end = request.POST.get('end')
        al = request.POST.get('al')
        rs = request.POST.get('rs')
        rd = int(request.POST.get('rd'))
        md = request.FILES.get('md')
        rm = request.POST.get('rm')
        if lt=='LWA':
            lop = rd
            obc = leave_reg_lwa.objects.create(sn=sn, st=st, start=start, lt=lt,end=end, rs=rs,rd=rd, md=md, lop=lop)
            obc.save()
            if obc:
                msg = "Request Accepted, Wait for Approval"
                return render(request, "leave_request.html", {"success": msg})
        else:
            obc = leave_req.objects.create(sn=sn, st=st, start=start, lt=lt,al=al,end=end, rs=rs, rm=rm,rd=rd, md=md, lop=0)
            obc.save()
            if obc:
                msg = "Request Accepted, Wait for Approval"
                return render(request, "leave_request.html", {"success": msg})

    return render(request, "leave_request.html", {"sn": sn, "st": st})


def remaining(request):
    idno = request.session['idl']
    user_data = reg_tbl.objects.get(id=idno)
    staff_category = user_data.st  # Assuming 'st' is the field representing the staff category

    # Initialize variables to store leave information
    leave_info = {
        'Casual Leave': {'total': 15 if staff_category == 'Teaching' else 20, 'taken': 0},
        'Commuted Leave': {'total': 10, 'taken': 0},
        'Maternity Leave': {'total': 180, 'taken': 0},
        'Paternity Leave': {'total': 10, 'taken': 0},
        'Vacation' : {'total': 60 if staff_category == 'Teaching' else 0, 'taken' : 0}
    }

    # Retrieve leave requests for the logged-in user
    user_leave_requests = leave_req.objects.filter(sn=user_data.fn, approved=True)

    # Calculate taken leaves for each leave type
    for leave_request in user_leave_requests:
        leave_type = leave_request.lt
        days_requested = leave_request.rd

        if leave_type in leave_info:
            leave_info[leave_type]['taken'] += days_requested

    # Calculate remaining leaves for each leave type
    for leave_type, info in leave_info.items():
        info['remaining'] = info['total'] - info['taken']

    return render(request, "myleaves.html", {"leave_info": leave_info})


def leave_cancel(request):
    idno = request.GET.get('idn')
    obj = leave_req.objects.filter(id=idno)
    obj.delete()
    msg = 'Leave Cancelled'
    return render(request,"notif.html",{"error":msg})

def leave_history(request):
    idno = request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fnm = ls.fn
    obb = leave_req.objects.filter(sn=fnm)
    return render(request,"history.html",{"not":obb})

def notif(request):
    idno = request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    
    # Assuming fn is the field representing the first name
    fnm = obj.first().fn  # Retrieve the first name from the queryset

    # Filter leave requests by user's first name and approved status
    obb = leave_req.objects.filter(sn=fnm, approved=True)
    obc = leave_reg_lwa.objects.filter(sn=fnm, approved=True)
    
    return render(request, "notif.html", {"not": obb,"lnot":obc})

def salary(request):
    idno = request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fnm = ls.fn
        obb = payroll_tbl.objects.filter(sn=fnm)
        return render(request,"salaryview.html",{"payroll":obb})
    
def lwasalary(request):
    idno = request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fnm = ls.fn
        obb = lwa_payroll_tbl.objects.filter(sn=fnm)
        return render(request,"lwasalaryview.html",{"payroll":obb})

def view_assign(request):
    idno = request.session['idl']
    obj = reg_tbl.objects.filter(id=idno)
    for ls in obj:
        fnm = ls.fn
        obb = assign_tbl.objects.filter(fn=fnm)
        return render(request, "assign_notif.html", {"ass": obb})
    