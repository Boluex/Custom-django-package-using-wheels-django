from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# Create your views here.
# login user using phone_number


# def sign_in(request):
#     if request.method == 'POST':
#         get_email=request.POST.get('email')
#         get_password=request.POST.get('password')
#         user=authenticate(request,username=get_email,password=get_password)
#         if user.is_valid(raise_exception=True):
#             login(request,user)
#             return HttpResponse('Logged in')
#         else:
#             return HttpResponse('Error')


def report(request):
    return HttpResponse('Try using django test to login using email and password,if the login is successful it will return True else it will return False')