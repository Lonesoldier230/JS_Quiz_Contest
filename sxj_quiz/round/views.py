from django.shortcuts import render
from django.views import View
import random
from .models import Que_ans, MixedBag, Multiple, Memory


# Create your views here.
class Main(View):
    def get(self, request):
        
        val = request.session
        ctxt = {}
        li = ["general_round","mixed_bag","rapid_fire","buzzer","audio_visual","multiple_choice","recall","mental_maths"]
        
        for i in range(1,9):
            ctxt[f"round{i}"]= val.get(f"{li[i-1]}",1)
        ctxt["subject"] = val.get("subject", "None")
        
        return render(request, "rounds.html", context=ctxt)


# round/<str:round>/<int:iter>
def common(request, round, iter):
    q_na = Que_ans.objects.filter(round__name__iexact = round.replace("_"," "))
    if len(q_na) < 1:
        return render(request, '404.html')
    
    ctxt = {
        "question":q_na[iter - 1].question,
        "answer":q_na[iter - 1].answer,
        "iter":iter,
        "limit": len(q_na),
        "file":q_na[iter - 1].file,
        "round":request.session.get(f"{round.lower()}",0)
    }
    
    request.session[f"{round.lower()}"] = int(iter)
    return render(request, f'Rounds/{round.lower()}.html', context=ctxt)
    #return render(request, f'Rounds/general_round.html', context=ctxt)

# MixedBag/<str:subject>/<int:iter>
def mix_bag(request, subject, iter):
    request.session[subject] = True
    request.session["subject"] = str(subject)
    request.session["mixed_bag"] = int(iter)
    mi = MixedBag.objects.get(subject = str(subject))
    di = mi.q_ans
    
    ctxt = {
            "subject":subject,
            "question":list(di.keys())[iter - 1],
            "answer":list(di.values())[iter - 1],
            "iter":iter,
            "limit": len(di)
        }
    
    return render(request, 'Rounds/mixed_bag.html', ctxt)

# Multiple/<int:pk>
def m_choice(request, pk):
    try:
        zeek = Multiple.objects.get(pk = pk)
    except:
        return render(request, '404.html')
    
    ctxt = {
        "question":zeek.ques,
        "answer":zeek.answer,
        "choices":random.shuffle(zeek.choi),
        "limit":len(Multiple.objects.all())
    }
    
    request.session["multiple_choice"] = int(pk)
    return render(request, 'Rounds/multiple_choice.html',context=ctxt)


# MixedBag/
def mix_main(request):
    db = MixedBag.objects.all()
    
    ctxt = {
        "subjects":[i.subject for i in db]
    }
    
    return render(request, 'Rounds/mixed_bag_main.html', context=ctxt)

# Recall/<int:pk>
def recall(request, pk):
    try:
        db = Memory.objects.get(pk = 1)
    except:
        return render(request, '404.html')
    
    ctxt = {
        "words":db
    }
    
    request.session["recall"] = int(pk)
    return render(request,"Rounds/recall.html",context=ctxt)