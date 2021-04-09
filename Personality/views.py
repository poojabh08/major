from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from Personality.models import registration_details,user_answers
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
# Create your views here.
def login(request):
    if request.method == "POST":
        # print("Inside login")
        request.session["username"] = request.POST.get('username')
        request.session["password"] = request.POST.get('password')
        uname = None
        passw = None
        try:
            uname = registration_details.objects.get(username= request.session["username"])
            passw = registration_details.objects.get(password= request.session["password"])
        except:
            uname = None
            passw = None
        if request.session["username"]==uname.username and request.session["password"]==passw.password:
            return redirect("/personality/question")
        else:
            messages.error(request,'Invalid Username or Password')
            return HttpResponseRedirect("/")
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        request.session["fullname"] = request.POST.get('fullname')
        request.session["username"] = request.POST.get('username')
        request.session["password"] = request.POST.get('password')
        request.session["mobileno"] = request.POST.get('mobileno')
        request.session["email"] = request.POST.get('email')
        check = None
        try:
            check = registration_details.objects.get(username=request.session["username"])
        except:
            check = None
        if check:
            messages.error(request,'Username already exists')
            return HttpResponseRedirect("/personality/register")
        else:
            userd = registration_details.objects.create(fullname=request.session["fullname"],username=request.session["username"],password=request.session["password"],mobileno=request.session["mobileno"],email=request.session["email"])
            userd.save()
            return redirect("/")
    else:
        return render(request,'register.html')

def question(request):
    if request.method=="POST":
        # print(request.session["username"])
        # request.session['name'] =  request.POST.get('name')  
        # print(request.session['name'])
        myname = None
        try:
            myname = registration_details.objects.get(username=request.session['username'])
        except:
            myname = None
        request.session['q1'] = float(request.POST.get('qu1'))
        request.session['q2'] = float(request.POST.get('qu2'))
        request.session['q3'] = float(request.POST.get('qu3'))
        request.session['q4'] = float(request.POST.get('qu4'))
        request.session['q5'] = float(request.POST.get('qu5'))
        request.session['q6'] = float(request.POST.get('qu6'))
        request.session['q7'] = float(request.POST.get('qu7'))
        request.session['q8'] = float(request.POST.get('qu8'))
        request.session['q9'] = float(request.POST.get('qu9'))
        request.session['q10'] = float(request.POST.get('qu10'))
        request.session['q11'] = float(request.POST.get('qu11'))
        request.session['q12'] = float(request.POST.get('qu12'))
        request.session['q13'] = float(request.POST.get('qu13'))
        request.session['q14'] = float(request.POST.get('qu14'))
        request.session['q15'] = float(request.POST.get('qu15'))
        request.session['q16'] = float(request.POST.get('qu16'))
        request.session['q17'] = float(request.POST.get('qu17'))
        request.session['q18'] = float(request.POST.get('qu18'))
        request.session['q19'] = float(request.POST.get('qu19'))
        request.session['q20'] = float(request.POST.get('qu20'))
        request.session['q21'] = float(request.POST.get('qu21'))
        request.session['q22'] = float(request.POST.get('qu22'))
        request.session['q23'] = float(request.POST.get('qu23'))
        request.session['q24'] = float(request.POST.get('qu24'))
        request.session['q25'] = float(request.POST.get('qu25'))
        request.session['q26'] = float(request.POST.get('qu26'))
        request.session['q27'] = float(request.POST.get('qu27'))
        request.session['q28'] = float(request.POST.get('qu28'))
        request.session['q29'] = float(request.POST.get('qu29'))
        request.session['q30'] = float(request.POST.get('qu30'))
        request.session['q31'] = float(request.POST.get('qu31'))
        request.session['q32'] = float(request.POST.get('qu32'))
        request.session['q33'] = float(request.POST.get('qu33'))
        request.session['q34'] = float(request.POST.get('qu34'))
        request.session['q35'] = float(request.POST.get('qu35'))
        request.session['q36'] = float(request.POST.get('qu36'))
        request.session['q37'] = float(request.POST.get('qu37'))
        request.session['q38'] = float(request.POST.get('qu38'))
        request.session['q39'] = float(request.POST.get('qu39'))
        request.session['q40'] = float(request.POST.get('qu40'))
        request.session['q41'] = float(request.POST.get('qu41'))
        request.session['q42'] = float(request.POST.get('qu42'))
        request.session['q43'] = float(request.POST.get('qu43'))
        request.session['q44'] = float(request.POST.get('qu44'))
        request.session['q45'] = float(request.POST.get('qu45'))
        request.session['q46'] = float(request.POST.get('qu46'))
        request.session['q47'] = float(request.POST.get('qu47'))
        request.session['q48'] = float(request.POST.get('qu48'))
        request.session['q49'] = float(request.POST.get('qu49'))
        request.session['q50'] = float(request.POST.get('qu50'))
        ans = user_answers.objects.create(username_id=myname.username,q1=request.session['q1'],q2=request.session['q2'],q3=request.session['q3'],q4=request.session['q4'],q5=request.session['q5'],q6=request.session['q6'],q7=request.session['q7'],q8=request.session['q8'],q9=request.session['q9'],q10=request.session['q10'],q11=request.session['q11'],q12=request.session['q12'],q13=request.session['q13'],q14=request.session['q14'],q15=request.session['q15'],q16=request.session['q16'],q17=request.session['q17'],q18=request.session['q18'],q19=request.session['q19'],q20=request.session['q20'],q21=request.session['q21'],q22=request.session['q22'],q23=request.session['q23'],q24=request.session['q24'],q25=request.session['q25'],q26=request.session['q26'],q27=request.session['q27'],q28=request.session['q28'],q29=request.session['q29'],q30=request.session['q30'],q31=request.session['q31'],q32=request.session['q32'],q33=request.session['q33'],q34=request.session['q34'],q35=request.session['q35'],q36=request.session['q36'],q37=request.session['q37'],q38=request.session['q38'],q39=request.session['q39'],q40=request.session['q40'],q41=request.session['q41'],q42=request.session['q42'],q43=request.session['q43'],q44=request.session['q44'],q45=request.session['q45'],q46=request.session['q46'],q47=request.session['q47'],q48=request.session['q48'],q49=request.session['q49'],q50=request.session['q50'])
        ans.save()
        print("Stored in Database")
        return redirect("/personality/result")
    else:  
        # name = request.session["username"]
        
        return render(request,'question.html')
        

def result(request):
    check = None
    try:
        check = user_answers.objects.get(username=request.session["username"])
    except:
        check = None
    if check:
        results = getPredictions(check)
    # results = getPredictions()
    return render(request,'result.html',{'result':results})

def getPredictions(check):
    import pickle
    model = pickle.load(open("/home/poojahegde/Desktop/MajorProject/Personality_Prediction/Personality_Prediction/Big_five_Personality.sav", "rb"))
    final_lists=[[check.q1,check.q2,check.q3,check.q4,check.q5,check.q6,check.q7,check.q8,check.q9,check.q10,check.q11,check.q12,check.q13,check.q14,check.q15,check.q16,check.q17,check.q18,check.q19,check.q20,check.q21,check.q22,check.q23,check.q24,check.q25,check.q26,check.q27,check.q28,check.q29,check.q30,check.q31,check.q32,check.q33,check.q34,check.q35,check.q36,check.q37,check.q38,check.q39,check.q40,check.q41,check.q42,check.q43,check.q44,check.q45,check.q46,check.q47,check.q48,check.q49,check.q50]]
    prediction = model.predict(final_lists)
    # prediction = model.predict([[2.0,3.0,4.0,5.0,4.0,4.0,3.0,4.0,4.0,4.0,3.0,4.0,4.0,4.0,5.0,3.0,3.0,5.0,5.0,2.0,4.0,5.0,5.0,5.0,4.0,5.0,4.0,5.0,4.0,4.0,4.0,5.0,4.0,5.0,5.0,4.0,5.0,5.0,5.0,4.0,4.0,4.0,3.0,3.0,4.0,5.0,4.0,3.0,4.0,4.0]])
    print(prediction)
    return prediction