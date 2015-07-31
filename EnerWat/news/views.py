from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from .models import News


# Create your views here.
class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
