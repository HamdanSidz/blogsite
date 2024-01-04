from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, Loginform, Post_form, Comments_form
from django.contrib.auth import authenticate, logout, login
from .models import Post


# Create your views here.

def home(request):
    post_inst = Post.objects.filter(parent_post = None)
    return render(request, "blogapp/home.html", {"post": post_inst})


def about(request):
    return render(request, "blogapp/about.html")


def contact(request):
    return render(request, "blogapp/contact.html")


def signupuser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("SAVED............")
            return render(request, 'blogapp/login.html', {"message": "Your account is successfully created, please login to continue to use our services "})
    else:
        form = SignUpForm()
        return render(request, "blogapp/signup.html", {"form": form})
        
    return render(request,"blogapp/signup.html",{"form":form})        


def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Loginform(request=request, data=request.POST)
            if form.is_valid():
                nm = form.cleaned_data["username"]
                ps = form.cleaned_data["password"]
                user = authenticate(username=nm, password=ps)
                if user is not None:
                    # print(user.get_username())
                    login(request, user)
                    post = Post.objects.filter(user_id=request.user.id)
                    return render(request, "blogapp/dashboard.html", {"user": user, "posts": post})
                else:
                    return render(request, "blogapp/login.html")
            else:
                form = Loginform()
                return render(request, "blogapp/login.html", {"form": form, "message": "Please enter valid username or password"})
        else:
            form = Loginform()
            return render(request, "blogapp/login.html", {"form": form})
    else:
        return HttpResponseRedirect("/dashboard/")


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")


def dashboard(request):
    if request.user.is_authenticated:
        only_specific_post = Post.objects.filter(user_id=request.user.id)
        return render(request, "blogapp/dashboard.html", {"posts": only_specific_post})
    else:
        return HttpResponseRedirect("/login/")


def update(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post_user = Post.objects.get(pk=id)
            form = Post_form(request.POST, instance=post_user)
            if form.is_valid():
                form.save()
                return render(request, "blogapp/update.html", {"message": "Successfully Upadated"})
            else:
                return render(request, "blogapp/update.html", {"message": "please fill the form in right manner"})
        else:
            post = Post.objects.get(pk=id)
            form = Post_form(instance=post)
            return render(request, "blogapp/update.html", {"form": form})
    else:
        return HttpResponseRedirect("/login/")



def delete(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(pk=id)
            post.delete()
            return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")


def addpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Post_form(request.POST)
            if form.is_valid():
                form.instance.user_id = request.user.id
                form.instance.post_username = request.user.username
                form.instance.parent_post = None
                form.save()
                return render(request, 'blogapp/addpost.html', {"form": form, "message": "Your post is successfully added"})
            else:
                return render(request, 'blogapp/addpost.html', {"form": form, "message2": "Information enter is not valid"})
        else:
            form = Post_form()
            return render(request, "blogapp/addpost.html", {"form": form})
    else:
        return HttpResponseRedirect("/login/")



def comment_fun(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_comm = Comments_form(request.POST)
            if form_comm.is_valid():
                form_comm.instance.parent_post = id
                form_comm.instance.post_username = request.user.username
                form_comm.instance.user_id = None
                form_comm.save()
                return render(request, 'blogapp/home.html', { "message": "Your comment is successfully added"})
        else:
            selected_form_to_comm = Post.objects.get(pk=id)
            selected_post_comm_count = Post.objects.filter(parent_post=id).count()
            selected_post_comm = Post.objects.filter(parent_post=id)
            form_comm = Comments_form()
            return render(request,"blogapp/comments.html",{"form_comm":form_comm,"selected_form_to_comm":selected_form_to_comm,"selected_post_comm_count":selected_post_comm_count,"selected_post_comm":selected_post_comm})    
    else:
        return HttpResponseRedirect("/login/")        
