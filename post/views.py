from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from properties.models import Advertising, Contacts, Logo
from slider.models import Slider
from .models import Post, Category, Tag


class IndexView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['sliders'] = Slider.objects.all().filter(published=True)[:3]
        context['post_views'] = Post.objects.filter(view__gt=100).order_by('-view')[:5]
        context['advertising'] = Advertising.objects.all()[:2]
        context['contacts'] = Contacts.objects.all()
        context['logos'] = Logo.objects.all()[:1]
        return context

    def get_queryset(self):
        return Post.objects.filter(published=True)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    post.view = post.view + 1
    post.save()
    contacts = Contacts.objects.all()
    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'contacts': contacts
    }
    return render(request, 'post/detail.html', context=context)


def slider_detail(request, slider_pk):
    slider = Slider.objects.get(pk=slider_pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    slider.view = slider.view + 1
    slider.save()
    contacts = Contacts.objects.all()
    context = {
        'slider': slider,
        'categories': categories,
        'tags': tags,
        'contacts': contacts
    }
    return render(request, 'post/slider_detail.html', context=context)


class GetCategory(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/category.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_views'] = Post.objects.filter(view__gt=100).order_by('-view')[:5]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['contacts'] = Contacts.objects.all()
        context['advertising'] = Advertising.objects.all()[:2]
        return context

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['category_pk'])


class GetTag(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/tag.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_views'] = Post.objects.filter(view__gt=100).order_by('-view')[:5]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['contacts'] = Contacts.objects.all()
        context['advertising'] = Advertising.objects.all()[:2]
        return context

    def get_queryset(self):
        return Post.objects.filter(tag=self.kwargs['tag_pk'])


class Search(ListView):
    template_name = 'post/search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Contact(ListView):
    model = Contacts
    template_name = 'post/contact.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['logos'] = Logo.objects.all()[:1]
        return context


