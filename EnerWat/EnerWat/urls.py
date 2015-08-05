from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from news.views import NewsDetailView, NewsListView
from user.views import UserDetailView, UserSignup, UserLogin, StaffListView
from main.views import ContactView, MainView
from api.views import GetNews

urlpatterns = [
    # Examples:
    # url(r'^$', 'EnerWat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name='home'),
    url(r'contact/?', ContactView.as_view(), name='contact'),

    # User views
    url(r'^signup/?', staff_member_required(UserSignup.as_view(), login_url='user_login'), name='user_signup'),
    url(r'^login/?', UserLogin.as_view(), name='user_login'),
    url(r'^staff/?', StaffListView.as_view(), name='user_staff'),
    url(r'^profile/?', login_required(UserDetailView.as_view()), name='user_detail'),

    # API views
    url(r'^api/get-news/(?P<id>\d+)', GetNews.as_view(), name='api_get_news'),

    # News views
    url(r'^news/(?P<pk>\d+)', NewsDetailView.as_view(), name='news_detail'),
    url(r'^news/?$', NewsListView.as_view(), name='news_list'),
]
