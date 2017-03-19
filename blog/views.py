from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import  datetime
from  blog import  models

# Create your views here.
def archive(request):
    posts = models.BlogPost.objects.all()[:10]
    return  render_to_response('archive.html',
                               {'posts':posts,'form':models.BlogPostForm()},
                               RequestContext(request))
def create_blogpost(request):
    if request.method == 'POST':
        #models.BlogPost(
            #title=request.POST.get('title'),
            #body = request.POST.get('body'),
            #timestamp = datetime.now(),
        #).save()
        form = models.BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')