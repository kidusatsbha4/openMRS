from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def members(request):
    
    template=loader.get_template('register.html')
    return HttpResponse(template.render())
@csrf_exempt
def register(request):
    if request.method=="POST":
      firstname=request.POST['firstname']
      lastname=request.POST['lastname']
      dateofbirth=request.POST['dateofbirth']
      gender=request.POST['gender']
      address=request.POST['address']
      phonenumber=request.POST['phonenumber']
      email=request.POST['email']
      nationality=request.POST['nationality']
      maritalstatus=request.POST['maritalstatus']
      occupation=request.POST['occupation']
      emergencycontact=request.POST['emergencycontact']
      insuranceinformation=request.POST['insuranceinformation']
      regi=Member(firstname=firstname,lastname=lastname,dateofbirth=dateofbirth,gender=gender,address=address,phonenumber=phonenumber,email=email,nationality=nationality,maritalstatus=maritalstatus,occupation=occupation,emergencycontact=emergencycontact,insuranceinformation=insuranceinformation)
      regi.save()
      return HttpResponse("data saved")
    else:
        template=loader.get_template('register.html')
        return HttpResponse(template.render())
def show(request):
       show=Member.objects.all().values()
       template=loader.get_template('show.html')
       context={'show':show,
       }
       return HttpResponse(template.render(context,request))
def delete(request,id):
       dele=Member.objects.get(id=id)
       dele.delete()
       template=loader.get_template('deleted.html')
       return HttpResponse(template.render())
def update(request,id):
       memb=Member.objects.get(id=id)
       template=loader.get_template('update.html')
       context={'memb':memb,
       }
       return HttpResponse(template.render(context,request))
@csrf_exempt
def up(request,id):
    memb = get_object_or_404(Member, id=id)
    if request.method=="POST":
      firstname = request.POST.get('firstname')
      lastname = request.POST.get('lastname')
      dateofbirth=request.POST.get('dateofbirth')
      gender=request.POST.get('gender')
      address=request.POST.get('address')
      phonenumber=request.POST.get('phonenumber')
      email=request.POST.get('email')
      nationality=request.POST.get('nationality')
      maritalstatus=request.POST.get('maritalstatus')
      occupation=request.POST.get('occupation')
      emergencycontact=request.POST.get('emergencycontact')
      insuranceinformation=request.POST.get('insuranceinformation')
      

      memb.firstname = firstname
      memb.lastname = lastname
      memb.dataofbirth=dateofbirth
      memb.gender=gender
      memb.address=address
      memb.phonenumber=phonenumber
      memb.email=email
      memb.nationality=nationality
      memb.maritalstatus=maritalstatus
      memb.occupation=occupation 
      memb.emergencycontact=emergencycontact
      memb.insuranceinformation=insuranceinformation
      memb.save()
      thismem=Member.objects.get(id=id)
      context={'thismem':thismem,
       }
      template=loader.get_template('updatedDetail.html')
      return HttpResponse(template.render(context,request))
    else:
        template=loader.get_template('update.html')
        return HttpResponse(template.render())
    