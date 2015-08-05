from django.http import HttpResponse
from django.core import serializers
from django.views.generic.base import View

from news.models import News


# Create your views here.
class GetNews(View):
    def get(self, request, news_id):
        news = News.objects.filter(id__gt=news_id).order_by("date")
        response = HttpResponse(content_type='application/json')
        response.write(serializers.serialize('json', news))
        return response
