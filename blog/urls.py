from django.conf.urls import patterns
import  blog.views

urlpatterns = patterns('blog.views',
                       (r'^$',blog.views.archive),
                       (r'^create/',blog.views.create_blogpost),)