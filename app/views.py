from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from My_Website.settings import EMAIL_HOST_USER
from app.models import SkillModel, PersonalModel, PortfolioModel, BlogModel



def myindex(request):
    skill=SkillModel.objects.all()
    portfolio=PortfolioModel.objects.all()
    blog=BlogModel.objects.all()
    return render(request,"index.html",{"skill":skill,"personal":PersonalModel.objects.all(),"portfolio":portfolio,"blog":blog})


def sending_mail(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        message1 = f'{name}\n{email}\n{message}'
        send_mail(subject,message1, EMAIL_HOST_USER,["rajeshbhagure99@gmail.com"])
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect('index')
    else:
        messages.success(request, "Error in sending Email.Thank you!")
        return redirect('index')

