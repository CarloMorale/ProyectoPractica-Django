from django.shortcuts import render
from Blog.models import post, categoria

# Create your views here.
def blog(request):
	posts = post.objects.all()
	return render(request, 'Blog/blog.html', {"posts":posts})

def filtro_categoria(request, categoria_id):
	cat = categoria.objects.get(id=categoria_id)
	posts = post.objects.filter(categorias=cat)
	return render(request, "blog/categorias.html", {'categoria':categoria, 'posts':posts})