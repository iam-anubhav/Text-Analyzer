# This file is created by Anubhav.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    receivedText = request.GET.get('textarea', 'default')
    removepunc = request.GET.get('cbRemovepunc','off')
    fullcaps = request.GET.get('cbFullcaps','off')
    extraspaceremover = request.GET.get('cbExtraspacerem','off')
    newlineremover = request.GET.get('cbNewlinerem','off')
    charcount = request.GET.get('cbCharcount','off')

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analysed = ""

    if removepunc == "on":
        for i in receivedText:
            if i not in punctuations:
                analysed += i
                print(analysed)
        params = {'purpose': "Removed Punctuations", 'analyzed_text': analysed}

        return render(request, 'removepunc.html', params)


    elif fullcaps == "on":
        analysed = receivedText.upper()
        params = {'purpose': "UPPERCASE", 'analyzed_text': analysed}

        return render(request, 'fullcaps.html', params)

    elif extraspaceremover == 'on':
        for i in range(0,len(receivedText)):
            if (receivedText[i]==" ") and (receivedText[i+1]==" "):
                pass
            else:
                analysed += receivedText[i]
        params = {'purpose': "Removed Extra Space", 'analyzed_text': analysed}

        return render(request, 'extraspace.html', params)

    elif newlineremover == 'on':
        for i in receivedText:
            if i != '\n':
                analysed += i
        params = {'purpose': "Removed New Lines", 'analyzed_text': analysed}

        return render(request, 'newlineremover.html', params)

    elif charcount == 'on':
        total_char = len(receivedText)
        params = {'purpose': "Character Count", 'analyzed_text': total_char}
        return render(request, 'charcount.html', params)

    else:
        return HttpResponse('Error')


