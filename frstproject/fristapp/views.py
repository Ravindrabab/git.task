# from django.shortcuts import render
# from django.http import HttpResponse
# # from .models import Employee
# from .models import Movie
# # Create your views here.
# # def display(request):
# #     return render(request,'index.html')


######### Employee
# def display(request):
#     if request.method=='POST':
#         ename=request.POST['name']
#         edomain=request.POST['domain']
#         ecompany=request.POST['company']
#         emp=Employee(name=ename,domain=edomain,company=ecompany)
#         emp.save()
    #  return render(request,'index.html')      
#     #changes
#     employees=Employee.objects.all()      
#     return render(request,'index.html',{'data':employees})    

# def display(request):
#     return render(request,'index.html')

######## movie
# def display(request):
#     if request.method=='post':
#         emoviename=request.POST['moviename']
#         ebudget=request.POST['budget']
#         edirector=request.POST['director']
#         eheroname=request.POST['heroname']
#         mov=Movie(moviename=emoviename,budget=ebudget,director=edirector,heroname=eheroname)
#         mov.save()
#     # return render(request,'index.html')    
#     # changes 
#     movies=Movie.objects.all()
#     return render(request,'index.html',{'data':movies}) 

  
#########gmail,login,logout
from django.shortcuts import render,HttpResponse, redirect
from .models import facebook
def user_sigin(request):
    if request.method == "POST":
       user_name =request.POST["username"]
       user_gmail = request.POST["gmail"]
       user_password = request.POST["password"]
       user_confrmpassword = request.POST["confrmpassword"]
       if user_password != user_confrmpassword:
        return HttpResponse("password does not match")
       else:
        user = facebook(username=user_name,gmail=user_gmail,password=user_password,confrmpassword=user_confrmpassword)
        user.save()
        return redirect(user_login)
    return render(request,"regist.html")

def user_login(request):
    if request.method == "POST":
       username =request.POST["username"]
       password = request.POST["password"]
       user_details = facebook.objects.all()
       user = None
       for user in user_details:
        if(user.username,user.password)==(username,password):
            user = user.username
            request.method = " "
            break
       if user is not None:
          return redirect (home_page)
       else:
          return HttpResponse("invalid details")
    return render(request,"login.html")

def home_page(request):
   if request.method == "POST":
    return redirect(user_login)
   return render(request,"home.html")
    

                    

   