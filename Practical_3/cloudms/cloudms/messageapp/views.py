from django.shortcuts import render
from datetime import datetime
from django.http import StreamingHttpResponse, HttpResponseBadRequest, HttpResponseNotModified, HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
#from django.template import Template, Context
import os
import stat

def msgproc(request):
    datalist =[]
    if request.method == 'POST':
       userA = request.POST.get( 'userA', None)
       userB = request.POST.get( 'userB', None)
       msg = request.POST.get('msg', None)
       time = datetime.now()
       with open('msgdata.txt', 'a+') as f:
           f.write('{}--{}--{}--{}--\n'.format(userB, userA, msg, time.strftime('%Y-%m-%d %H:%M:%S')))
    if request.method == 'GET':
        userC = request.GET.get('userC', None)
        if userC != None:
            with open('msgdata.txt','r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt+1
                        d = {'userA':linedata[1], 'msg':linedata[2], 'time':linedata[3]}
                        datalist.append(d)
                    if cnt >= 20:
                        break
    return render(request, 'messageweb.html', {'data':datalist})

def homeproc(request):
    response = HttpResponse()
    response.write("<h1> This is a page for test of HttpResponse.\
                   To see the message app, visit \
                   <a href='http://127.0.0.1:8000/msggate/'> here</a></h1>")
    return response
def homeproc1(request):
    response = HttpResponseRedirect('http://127.0.0.1:8000/msggate/')
    return response
def homeproc2(request):
    response = HttpResponsePermanentRedirect('http://127.0.0.1:8000/msggate/')
    return response
def homeproc3(request):
    return HttpResponseNotModified()
def homeproc4(request):
    return HttpResponseBadRequest('Bad request')
def homeproc5(request):
    return JsonResponse({'Oranges': '2'})
def homeproc6(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/messageapp/templates/logo.jpg", "rb"))
    response['Content-Type'] = 'application/octet=stream'
    response['Content-Disposition'] = 'attachment;filename="logo.jpg"'
    return response

    












   
    
   
    
# Create your views here.
