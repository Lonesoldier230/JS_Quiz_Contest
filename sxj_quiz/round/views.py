from django.shortcuts import render
from django.views import View
import json
from .models import Que_ans, MixedBag, Multiple, Memory
from django.contrib.staticfiles import finders

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
    q_na = Que_ans.objects.filter(round__name__iexact = round.replace("_"," ")).order_by("id")
    if len(q_na) < 1 or iter > len(q_na) :
        return render(request, 'Rounds/questions_finished.html')
    request.session[f"{round.lower()}"] = int(iter) + 1 
    
    with open (finders.find("json/file_type.json"), "r") as js:
        types = json.load(js)
        
    file_type = None
    try:
        file = q_na[iter - 1].file.url
        for key, val in types.items():
            if file.split(".")[-1].lower() in val:
                file_type = key
    except:
        file = None
    
    ctxt = {
        "question":q_na[iter - 1].question,
        "answer":q_na[iter - 1].answer,
        "iter":iter,
        "limit": len(q_na),
        "file":file,
        "file_type":file_type,
        "round":request.session.get(f"{round.lower()}",0)
    }
    
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
        "choices":zeek.choi,
        "iter":pk,
        "limit":len(Multiple.objects.all())
    }
    
    request.session["multiple_choice"] = int(pk)
    return render(request, 'Rounds/multiple_choice.html',context=ctxt)


# MixedBag/
def mix_main(request):
    db = MixedBag.objects.all()
    
    ctxt = {
        "numbers":[i for i in range(1,len(db) + 1)],
        "subjects":[i.subject for i in db]
    }
    
    return render(request, 'Rounds/mixed_bag_main.html', context=ctxt)

# Recall/<int:pk>
def recall(request, pk):
    try:
        db = Memory.objects.get(pk = pk)
    except:
        print()
        return render(request, 'Rounds/questions_finished.html')
    
    ctxt = {
        "words":db.words,
        "iter":pk
    }
    
    request.session["recall"] = int(pk)
    return render(request,"Rounds/recall.html",context=ctxt)