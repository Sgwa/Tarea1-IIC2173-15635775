from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Comment
from ipware import get_client_ip


def index(request):
    comment_list = Comment.objects.order_by('-date')
    context = {'comment_list': comment_list}
    return render(request, 'comments/index.html', context)


def new(request):
    ip, is_routable = get_client_ip(request)
    content = request.POST['content']
    comment = Comment(content=content, ip=ip)
    comment.save()
    return HttpResponseRedirect(reverse('comments:index'))
