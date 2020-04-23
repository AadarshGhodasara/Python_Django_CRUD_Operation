# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from mysite.forms import StudentForm
from mysite.models import students


def index(request):
    return render(request, 'index.html')


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         re_password = request.POST["password2"]

#         if password == re_password:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'User name taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Id is exists !!!')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(
#                     username=username, password=password, email=email)
#                 user.save()
#                 print('user created')
#         else:
#             print("Password is not match !!!")
#         return redirect('/')
#     else:
#         return render(request, 'register.html')


def register(request):
    if request.method == "POST":
        Roll_Number = request.POST["Roll_Number"]
        form = StudentForm(request.POST)
        if form.is_valid():
            # print(students.objects.filter(Roll_Number=Roll_Number).exists())
            try:
                if students.objects.filter(Roll_Number=Roll_Number).exists():
                    messages.success(request, 'User name taken')
                    print("king")

                print("-----")
                print("+++++")
                form.save()
                print("create user")
                return redirect('/index')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})


def view(request):
    st = students.objects.all()
    return render(request, 'view.html', {'students': st})


def delete(request, id):
    st = students.objects.get(id=id)
    st.delete()
    return redirect("/view")


def edit(request, id):
    st = students.objects.get(id=id)
    print("IN EDIT")
    print(st)
    return render(request, 'edit.html', {'students': st})


def update(request, id):
    print("--------------------------------------UPDATE")
    st = students.objects.get(id=id)
    print(st)
    form = StudentForm(request.POST, instance=st)
    print("--------------------------------------DONE")
    print(form)
    # print(form.is_valid())
    print("----------------------------------------CHECK")
    # if form.is_valid():
    try:
        form.save()
        return redirect("/view")
    except:
        pass
