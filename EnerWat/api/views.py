from django.http import HttpResponse
from django.core import serializers

from news.models import News


# Create your views here.
def get_news(request, id):
    news = News.objects.filter(id__gt=id).order_by("date")
    response = HttpResponse(content_type='application/json')
    response.write(serializers.serialize('json', news))
    return response
