from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LoanConsultation,Blog
from django.utils.timezone import localtime

# ---------- LOGIN ----------
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('admin_login')

    return render(request, 'adminapp/login.html')

#-------login-redirect------------

def redirect_to_login(request):
    return redirect('admin_login')


# ---------- DASHBOARD ----------
@login_required(login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'adminapp/dashboard.html')

@login_required(login_url='admin_login')
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'adminapp/blogs.html',{'blogs':blogs})


# ---------- LOGOUT ----------
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


from django.contrib import messages
from .models import Blog

@login_required(login_url='admin_login')
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('blog_title')
        subtitle = request.POST.get('blog_subtitle')
        description = request.POST.get('blog_description')
        author = request.POST.get('author_name')
        image = request.FILES.get('blog_image')

        if not title or not description or not author:
            messages.error(request, 'Title, description and author are required!')
            return redirect('create_blog')

        blog = Blog(
            title=title,
            subtitle=subtitle,
            description=description,
            author=author,
            image=image
        )
        blog.save()
        messages.success(request, 'Blog created successfully!')
        return redirect('blogs') 

    return render(request, 'adminapp/add_blog.html')


@login_required(login_url='admin_login')
def message_list(request):
    # Fetch all loans, newest first
    loans = LoanConsultation.objects.all().order_by('-created_at')
    return render(request, 'adminapp/message_list.html', {'loans': loans})


@login_required(login_url='admin_login')
def message_detail(request, pk):
    loan = get_object_or_404(LoanConsultation, pk=pk)
    return render(request, 'adminapp/message_detail.html', {'loan': loan})


@login_required(login_url='admin_login')
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()  # image auto delete ho jayegi
    messages.success(request, f'Blog "{blog.title}" deleted successfully.')
    return redirect('blogs')