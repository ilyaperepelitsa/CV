"""django_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from jobs.views import Index
from django.urls import include

admin.autodiscover()

urlpatterns = [
    url(r'^$', Index.as_view()),
    path('api/', include('jobs.urls')),
    # path('admin/', admin.site.urls),

]

# curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"display_job_title": "NIAH Recruiting"}'  http://127.0.0.1:8000/api/display_title/
# {"display_job_title": "Data Scientist"}

# from tweets.views import Index, Profile, PostTweet, HashTagCloud, Search



# urlpatterns = [
#     url(r'^user/(\w+)/$', Profile.as_view()),
#     url(r'^admin/', admin.site.urls),
#     url(r'^user/(\w+)/post/$', PostTweet.as_view()),
#     url(r'^hashtag/(\w+)/$', HashTagCloud.as_view()),
#     url(r'^search/$', Search.as_view())
# ]
