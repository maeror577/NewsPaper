from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView)

from .models import Post
from .filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-posted']
    paginate_by = 10


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = NewsForm
    success_url = '/news'


class PostEditView(UpdateView):
    template_name = 'post_create.html'
    form_class = NewsForm
    success_url = '/news'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(
            self.request.GET,
            queryset=self.get_queryset()
        )
        return context
