from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User_Info
from first_app.forms import SignForm
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Now I am Coming from First_app/index.html !"}
    return render(request, 'HomePage/index.html', context = my_dict)

def first(request):
    ## Retrieving the Data of Websites,toics,AccessRecords from Database
    # webpages_list = AccessRecord.objects.order_by('date')
    # user_list = Webpage.objects.order_by('url')
    # data_dict = {'access_records': zip(user_list, webpages_list)}

    ## Retrieving the Data of User_info from the Database
    user_info = User_Info.objects.order_by('first_name')
    data_dict = {'usr_info':user_info}
    return render(request, 'first_app/index.html', context = data_dict)

def signin(request):
    form = SignForm()

    if request.method == 'POST':
        form = SignForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("SOME ERROR OCCURRED")

    return render(request, 'HomePage/signin.html', context = {'form':form})