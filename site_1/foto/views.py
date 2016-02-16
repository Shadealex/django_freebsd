from django.shortcuts import render, render_to_response
from django.template.loader import get_template
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('page1.html', {'current_date': now})


def photo_index(request):
	return render_to_response('photoart/index.html', locals())


def duty(request):
        return render_to_response('index.html', locals())

def album_1(request):
	return render_to_response('photoart/portfolio_one.html', locals())

def album_2(request):
	return render_to_response('photoart/portfolio_two.html', locals())

def test_page(request):
	return render_to_response('photoart/base.html')