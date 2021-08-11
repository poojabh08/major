from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from Personality.models import registration_details,user_answers,clusterNum
# from django.views.decorators.csrf import csrf_protect
import pandas as pd

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
            uname = registration_details.objects.get(username= request.session["username"],password= request.session["password"])
            # passw = registration_details.objects.get()
        except:
            uname = None
            passw = None
        if uname:
            if request.session["username"]==uname.username and request.session["password"]==uname.password:
                ch=None
                try:
                    ch=clusterNum.objects.get(username=request.session["username"])
                except:
                    ch=None
                if ch:
                    return render(request,'result.html',{'name':request.session["username"],'a1':ch.extroversion,'a2':ch.neurotic,'a3':ch.agreeable,'a4':ch.conscientious,'a5':ch.openness})
                else:
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
        results,a1,a2,a3,a4,a5 = getPredictions(check)
        username = request.session["username"]
        ans = clusterNum.objects.create(username_id=request.session["username"],clusNo = results[0],extroversion=a1,neurotic=a2,agreeable=a3,conscientious=a4,openness=a5)
        ans.save()
    # results = getPredictions()
    return render(request,'result.html',{'result':results,'name':username,'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5})

def getPredictions(check):
    import pickle
    model = pickle.load(open("/home/poojahegde/Desktop/MajorProject/Personality_Prediction/Personality_Prediction/Big.sav", "rb"))
    final_lists=[[check.q1,check.q2,check.q3,check.q4,check.q5,check.q6,check.q7,check.q8,check.q9,check.q10,check.q11,check.q12,check.q13,check.q14,check.q15,check.q16,check.q17,check.q18,check.q19,check.q20,check.q21,check.q22,check.q23,check.q24,check.q25,check.q26,check.q27,check.q28,check.q29,check.q30,check.q31,check.q32,check.q33,check.q34,check.q35,check.q36,check.q37,check.q38,check.q39,check.q40,check.q41,check.q42,check.q43,check.q44,check.q45,check.q46,check.q47,check.q48,check.q49,check.q50]]
    prediction = model.predict(final_lists)
    # prediction = model.predict([[2.0,3.0,4.0,5.0,4.0,4.0,3.0,4.0,4.0,4.0,3.0,4.0,4.0,4.0,5.0,3.0,3.0,5.0,5.0,2.0,4.0,5.0,5.0,5.0,4.0,5.0,4.0,5.0,4.0,4.0,4.0,5.0,4.0,5.0,5.0,4.0,5.0,5.0,5.0,4.0,4.0,4.0,3.0,3.0,4.0,5.0,4.0,3.0,4.0,4.0]])
    print(prediction)
    # return prediction #uncomment this line and comment next lines
    data_raw = pd.read_csv('/home/poojahegde/Desktop/MajorProject/IPIP-FFM-data-8Nov2018/data-final.csv', sep='\t')
    data = data_raw.copy()
    data.drop(data.columns[50:107], axis=1, inplace=True)
    data.drop(data.columns[51:], axis=1, inplace=True)
    result = data.head(10000)
    result.dropna(inplace=True)
    df_model = result.drop('country', axis=1)
    df2 = {'EXT1': 5.0,'EXT2': 5.0,'EXT3': 5.0,'EXT4': 5.0,'EXT5': 5.0,'EXT6': 5.0,'EXT7': 5.0,'EXT8': 5.0,'EXT9': 5.0,'EXT10': 5.0, 'EST1': 5.0,'EST2': 5.0,'EST3': 5.0,'EST4': 5.0,'EST5': 5.0,'EST6': 5.0,'EST7': 5.0,'EST8': 5.0,'EST9': 5.0,'EST10': 5.0, 'AGR1': 5.0,'AGR2': 5.0,'AGR3': 5.0,'AGR4': 5.0,'AGR5': 5.0,'AGR6': 5.0,'AGR7': 5.0,'AGR8': 5.0,'AGR9': 5.0,'AGR10': 5.0, 'CSN1': 5.0, 'CSN2': 5.0,'CSN3': 5.0,'CSN4': 5.0,'CSN5': 5.0,'CSN6': 5.0,'CSN7': 5.0,'CSN8': 5.0,'CSN9': 5.0,'CSN10': 5.0, 'OPN1':5.0,'OPN2':5.0,'OPN3':5.0,'OPN4':5.0,'OPN5':5.0,'OPN6':5.0,'OPN7':5.0,'OPN8':5.0,'OPN9':5.0,'OPN10':5.0}
    df_model = df_model.append(df2, ignore_index = True)
    a = model.labels_
    df_model['clusters'] = a
    # print("After")
    col_list = list(df_model)
    ext = col_list[0:10]
    est = col_list[10:20]
    agr = col_list[20:30]
    csn = col_list[30:40]
    opn = col_list[40:50]

    data_sums = pd.DataFrame()
    data_sums['extroversion'] = df_model[ext].sum(axis=1)/10
    data_sums['neurotic'] = df_model[est].sum(axis=1)/10
    data_sums['agreeable'] = df_model[agr].sum(axis=1)/10
    data_sums['conscientious'] = df_model[csn].sum(axis=1)/10
    data_sums['open'] = df_model[opn].sum(axis=1)/10
    # print("Clusters before")
    data_sums['clusters'] = a
    val = data_sums.groupby('clusters').mean()
    # print(val)
    # print(type(val))
    a1 = round((val.at[prediction[0],"extroversion"]/5)*100,2)
    a2 = round((val.at[prediction[0],"neurotic"]/5)*100,2)
    a3 = round((val.at[prediction[0],"agreeable"]/5)*100,2)
    a4 = round((val.at[prediction[0],"conscientious"]/5)*100,2)
    a5 = round((val.at[prediction[0],"open"]/5)*100,2)
    # res = val.head(prediction[0]+1).tail(1)
    # a1 = (res.extroversion/5)*100
    # a2 = (res.neurotic/5)*100
    # a3 = (res.agreeable/5)*100
    # a4 = (res.conscientious/5)*100
    # a5 = (res.open/5)*100
    print(a1,a2,a3,a4,a5)
    return(prediction,a1,a2,a3,a4,a5)
