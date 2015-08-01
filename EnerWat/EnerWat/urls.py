from django.conf.urls import include, url
from django.contrib import admin
from news.views import NewsDetailView, NewsListView
from user.views import UserDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'EnerWat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.main'),

    # User views
    url(r'^signup/?', 'user.views.signup'),
    url(r'^login/?', 'user.views.login'),
    url(r'^profile/(?P<pk>\d+)', UserDetailView.as_view(), name='user_detail'),

    # API views
    url(r'^api/get-news/(?P<id>\d+)', 'api.views.get_news'),

    # News views
    url(r'^news/(?P<pk>\d+)', NewsDetailView.as_view(), name='news_detail'),
    url(r'^news/?$', NewsListView.as_view(), name='news_list'),

    url(r'^contact/?', 'main.views.contact'),
    url(r'^submit-paper/?', 'user.views.paper'),
]
