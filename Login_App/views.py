from django.shortcuts import render
from Login_App.forms import UserForm, UserInfoForm

# Create your views here.
def home_page(request):
    diction = {}
    return render(request, 'Login_App/index.html', context=diction)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit = False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            
            user_info.save()
            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    dict = {'user_form':user_form, 'user_info_form':user_info_form, 'registered':registered}
    return render(request, 'Login_App/register.html', context = dict)