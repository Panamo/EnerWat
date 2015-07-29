from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'EnerWat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.main'),
    url(r'^signup/', 'user.views.signup'),
    url(r'^login/', 'user.views.login'),
    url(r'^api/get-news/(?P<id>\d+)', 'api.views.get_news')
]
