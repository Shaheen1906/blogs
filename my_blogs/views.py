from django.shortcuts import redirect, render

from my_blogs.forms import BlogForm

from .models import Blog

# Create your views here.

def home(request):
    return render(request, 'base.html')

#all blogs
def blog_list(request):
    # blogs = Blog.objects.all().order_by('-created_at').filter(created_at__gte='2025-05-15') # Fetch all blog posts from the database
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})

# Create a new blog post
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def blog_detail(request, pk): #pk is the primary key of the blog post
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'blog': blog})