from django.shortcuts import render
from .models import Blog
from django.shortcuts import render, get_object_or_404
from .forms import BlogForm
from django.shortcuts import redirect

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()#order_by('-published_date')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('blog_list')


def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_edit.html', {'form': form, "type": 1})


def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_edit.html', {'form': form, "type": 2})
