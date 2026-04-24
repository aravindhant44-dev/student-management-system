from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(student_id__icontains=query) |
            Q(department__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students})


# ADD STUDENT
@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


# UPDATE STUDENT
@login_required
def update_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})


# DELETE STUDENT
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})


# SEARCH PAGE
@login_required
def search_student(request):
    return render(request, "search_student.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')