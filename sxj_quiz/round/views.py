from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponse
from .models import Que_ans, MixedBag, Round, Au_Vis, Multiple 

# Create your views here.
class Main(View):
    def get(self, request):
        val = request.session
        ctxt = {}
        for i in range(1,9):
            ctxt[f"round{i}"]= val.get(f"round{i}",1)
        ctxt["subject"] = val.get("subject", "None")
        return render(request, "rounds.html", context=ctxt)

def common(request, round, iter):
    
    q_na = Que_ans.objects.filter(round__name__iexact = round.replace("_"," "))
    if len(q_na) < 1:
        return HttpResponse("<h1>No Questions</h1>")
    ctxt = {
        "question":q_na[iter - 1].question,
        "answer":q_na[iter - 1].answer,
        "iter":iter,
        "limit": len(q_na),
        "round":request.session.get(f"{round}",0)
    }
    request.session[f"{round}"] = iter
    return render(request, f'Rounds/{round}.html', context=ctxt)

def mix_bag(request, subject, iter):
    request.session[subject] = True
    request.session["subject"] = subject
    request.session["round2"] = iter
    mi = MixedBag.objects.get(subject = str(subject))
    di = mi.q_ans
    try:
        ctxt = {
            "question":list(di.keys())[iter - 1],
            "answer":list(di.values())[iter - 1],
            "iter":iter,
            "limit": len(di)
        }
    except IndexError:
        return Http404()
    return render(request, 'Rounds/mixed_bag.html', ctxt)

def visual_a(request, pk):
    db = Au_Vis.objects.get(pk = pk)
    ctxt = {
        "question":db.ques,
        "answer":db.answr,
        "image_url":db.image.url,
        "limit":len(Au_Vis.objects.all())
    }
    return render(request, 'audio_visual.html',context=ctxt)

def m_choice(request, pk):
    zeek = Multiple.objects.get(pk = pk)
    print(zeek.ques)
    ctxt = {
        "question":zeek.ques,
        "answer":zeek.answer,
        "choices":zeek.choi,
        "limit":len(Multiple.objects.all())
    }
    return render(request, 'Rounds/multiple_choice.html',context=ctxt)

def mix_main(request):
    return render(request, 'Rounds/mixed_bag.html')