# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from ivotecoz.web.models import Reel

def index(request):
    if request.POST:
        reel1 = Reel.objects.filter(order=1).order_by('?')[0]
        reel2 = Reel.objects.filter(order=2).order_by('?')[0]
        reel3 = Reel.objects.filter(order=3).order_by('?')[0]
        reel4 = Reel.objects.filter(order=4).order_by('?')[0]
        
        url = "/%s-%s-%s-%s" % (reel1.id, reel2.id, reel3.id, reel4.id)
        return redirect(url)
        
    return render_to_response("index.html",{}, context_instance=RequestContext(request))

def reason(request, reels):
    reel = reels.split('-')
    
    reel1 = Reel.objects.get(id=reel[0])
    reel2 = Reel.objects.get(id=reel[1])
    reel3 = Reel.objects.get(id=reel[2])
    reel4 = Reel.objects.get(id=reel[3])
    
    context = {
        'reel1': reel1,
        'reel2': reel2,
        'reel3': reel3,
        'reel4': reel4
    }
    return render_to_response("reason.html", context, context_instance=RequestContext(request))