from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post, Category


class Home(ListView):
    queryset = Post.objects.filter(draft=False)
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        result = super(Home, self).get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            result = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_queryset(self):
        result = super(PostDetail, self).get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            result = Post.objects.all()

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CatgoryDetail(ListView):
    model = Post
    template_name = 'category.html'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Post.objects.filter(category=self.category)
        else:
            return Post.objects.filter(category=self.category, draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['category_list'] = Category.objects.all()
        return context
