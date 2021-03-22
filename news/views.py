from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_news'] = Post.objects.all()
        context['is_not_author'] = \
            not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDetailView(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    template_name = 'news/post_create.html'
    form_class = NewsForm
    success_url = '/'


class PostEditView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news/post_create.html'
    form_class = NewsForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'


class Search(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(
            self.request.GET,
            queryset=self.get_queryset()
        )
        return context
