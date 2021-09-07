from django.shortcuts import render

def Index(request):
    return render(request, 'authenticationApp/index.html')

def Profile(request):
    return render(request, 'authenticationApp/profile.html' )
