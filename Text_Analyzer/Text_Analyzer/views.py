# This file is created by Anubhav.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    receivedText = request.GET.get('textarea', 'default')
    cbremovepunc = request.GET.get('cbRemovepunc','off')
    cbfullcaps = request.GET.get('cbFullcaps','off')
    cbextraspaceremover = request.GET.get('cbExtraspacerem','off')
    cbnewlineremover = request.GET.get('cbNewlinerem','off')
    cbcharcount = request.GET.get('cbCharcount','off')

    def removepunc(str1):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        updated_str = ''
        for i in str1:
            if i not in punctuations:
                updated_str += i
        return updated_str

    def fullcaps(str1):
        updated_str = ''
        updated_str = str1.upper()
        return updated_str

    def extraspaceremover(str1):
        updated_str = ""
        for i in range(0,len(str1)):
            if (str1[i]==" ") and (str1[i+1]==" "):
                pass
            else:
                updated_str += str1[i]
        return updated_str

    def newlineremover(str1):
        updated_str = ""
        for i in str1:
            if i != "\n":
                updated_str = updated_str + i
        return updated_str

    def charcount(str1):
        total_char = len(str1)
        return total_char

    analysed = receivedText
    total_char = 0

    options = [cbcharcount,cbremovepunc,cbfullcaps,cbextraspaceremover,cbnewlineremover]
    if options[0] == 'on':
        total_char = charcount(analysed)
    if options[1] == 'on':
        analysed = removepunc(analysed)
    if options[2] == 'on':
        analysed = fullcaps(analysed)
    if options[3] == 'on':
        analysed = extraspaceremover(analysed)
    if options[4] == 'on':
        analysed = newlineremover(analysed)

    print(analysed)
    params = {'analyzed_text' : analysed}
    return render(request, 'results.html', params)




