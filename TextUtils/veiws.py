from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return  HttpResponse('''<h1>hello</h1> <a href="https://www.youtube.com/watch?v=ER9SspLe4Hg&list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR&ab_channel=CodeWithHarry"> Javascript</a> ''')

# def about(request):
#     return  HttpResponse('about') 


def index(request):
    return render(request,'index.html')

def analyze(request):
    #POST the text
    djtext = request.POST.get('text','default')
    # analyzed = djtext
    #analyze the text
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    # print(removepunc)
    newlineremover = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*~'''
    analyzed= ""
    # if( removepunc == "on"and fullcaps=="on"):
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char.upper()
    #     params = {'purpose':'Remove Punctuations and Changed to Uppercase','analyzed_text': analyzed}
    #     return render(request,'analyze.html', params)

    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text': analyzed}  
        # return render(request,'analyze.html', params)
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text': analyzed}  
        # return render(request,'analyze.html', params)
        djtext = analyzed
    if(extraspaceremover=="on"):
        analyze = ""
        for index ,char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyze = analyze + char
        
        params = {'purpose':'New Line Remover','analyzed_text': analyze}  
        # return render(request,'analyze.html', params)
        djtext = analyze
    if(charcount=="on"):
        analyze = 0
        for index ,char in enumerate(djtext):
            if djtext[index] ==" ":
                pass
            else:
                analyze = analyze + 1 
        params = {'purpose':'Character count','analyzed_text': analyze}  
    
    return render(request,'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlinermove(request):
#     return HttpResponse("new line and remove space")

# def spacermove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("char count")