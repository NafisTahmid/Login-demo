from django.shortcuts import render

# Create your views here.
def home_page(request):
    diction = {}
    return render(request, 'Login_App/index.html', context=diction)