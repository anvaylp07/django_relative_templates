from django.conf.urls import url
from basic_app import views

#template tagging
app_name='basic_app' #should match in relative_url_templates.html

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'), #these will be extensions basic_app/relative
    url(r'^other/$',views.other,name='other'),          #basic_ap/others
]
