# Create your views here.
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html',{'douban_url':'www.douban.com','book_title':'test_book','book_author':'songzhibai'})