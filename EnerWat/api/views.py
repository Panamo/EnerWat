import json

from django.http import HttpResponse

from news.models import News
from .encoders import NewsEncoder


# Create your views here.
def get_news(request, id):
    news = News.objects.filter(id__gt=id).order_by("date")
    response = HttpResponse(content_type='application/json')
    result = []
    for new in news:
        result.append(NewsEncoder.encode(new))
    response.write(json.dumps(result))
    return response
