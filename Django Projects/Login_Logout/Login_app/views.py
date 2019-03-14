from django.shortcuts import render, redirect
from Login_app.forms import MyUserForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# view to show the index page
def index(request):
    return render(request, 'HomePage/index.html', {})


# User-Creation Form
def register(request):

    form = UserRegisterForm()

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
         
        if form.is_valid():

            form.save()
            uname = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! Yor are now able to log in')
            return redirect('Login_app:login')

    return render(request, 'Login_app/register.html', {'form':form})


# view for user profile
@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('Login_app:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Login_app/profile_1.html', context)

# view to show the register page and store the form values into Database
# def signin(request):

#     form = MyUserForm()

#     if request.method == 'POST':
#         form = MyUserForm(request.POST)

#         if form.is_valid():
#             uname = form.cleaned_data.get('first_name')
#             form.save(commit=True)
#             return render(request, 'Login_app/profile.html', {'form':uname})
#         else:
#             print("Some Error Occurred!!!")

#     return render(request, 'Login_app/signin.html', {'form':form})


# view to retrieve the info form the database and pass it to the webpage 
@login_required
def show_database(request):

    usr = Register_User.objects.order_by('id')
    data_dict = {'user':usr}

    return render(request, 'Login_app/db.html', data_dict)


