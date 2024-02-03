from django.shortcuts import get_object_or_404, redirect, render
from . import models
import openai

API_KEY = "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"
openai.api_key= API_KEY
# Create your views here.
def index(request):
    return render(request, "main/index.html")

def ordinary(request):
    return render(request, 'main/ordinary.html')

def bac(request):
    return render(request, "main/bac.html")

def advanced(request):
    return render(request, 'main/advanced.html')

def scienceA(request):
    subject = models.Subject.objects.all()
    return render(request, 'main/science/scienceA.html', {"subject":subject})

def artA(request):
    subject = models.Subject.objects.all()
    return render(request, 'main/art/artA.html', {"subject":subject})

def scienceO(request):
    subject = models.Subject.objects.all()
    return render(request, 'main/science/scienceO.html', {"subject":subject})

def about(request):
    return render(request, 'main/about.html')

def artO(request):
    subject = models.Subject.objects.all()
    return render(request, 'main/art/artO.html', {"subject":subject})

def year(request, subject_id):
    subject = models.Subject.objects.get(pk = subject_id)
    years = models.Year.objects.filter(subject = subject)
    return render(request, "main/science/years.html",{"years": years})

def success(request):
    return render(request, "main/success.html")

def paper(request, year_id):
    year = models.Year.objects.get(pk = year_id )
    return render(request, 'main/science/paper.html', {'year':year})


def paper1(request, year_id):
    subject = models.Year.objects.get(pk= year_id)
    question = models.Question.objects.filter(subject = subject)
    points = 0   
    correct = [] 
    print(correct)
    if request.method == 'POST':
        for questions in question:
            answer = request.POST.get(f"{questions.pk}", 0)
            print(answer)
            correct.append(answer)
            print(f'{correct} this answer')
            for answered in questions.answer_set.filter(correct = True): # type: ignore
                print(answered.id)
                if int(answer) == answered.id:
                    points+=1                    
        return render(request, 'main/success.html',{"points":points, "id":subject.pk})
        #return render(request, 'main/science/paper1.html',{'subject': subject, 'question':question, 'best':correct})
    return render(request, 'main/science/paper1.html',{'subject': subject, 'question':question})

def ans(request, year_id):
    year = models.Year.objects.get(pk = year_id)
    cle = request.GET.get('cle')
    question = models.Question.objects.filter(subject = year)
    if request.method == 'POST':
        return redirect ('index')
    return render(request, "main/science/ans1.html", {'question':question,"year": year, 'points':cle})


def paper2(request, year_id):
    subject = models.Year.objects.get(pk= year_id)
    question = models.Question.objects.filter(subject = subject)
    if request.method == 'POST':
        print(request.POST.get('answer'))
        question_asked= models.Question.objects.filter(question = request.POST.get('answer'))
        asked = models.Question.objects.get()      
        response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages =[
            {'role':'user', 'content': str(question_asked)}
        ]
        )
        good_reponse = response['choices'][0]['message']['content'] # type: ignore
        return render(request, 'main/science/answer.html',{'response':good_reponse})
    return render(request, 'main/science/paper2.html',{'subject': subject, 'question':question})

def get_answer(request):
    return render(request, 'main/science/answer.html')


def paper3(request, year_id):
    subject = models.Year.objects.get(pk= year_id)
    question = models.Question.objects.filter(subject = subject)
    points = 0   
    if request.method == 'POST':
        for questions in question:
            answer = request.POST.get(f"{questions.pk}", 0)
            print(answer)
            for answered in questions.answer_set.filter(correct = True): # type: ignore
                print(answered.id)
                if int(answer) == answered.id:
                    points+=1
        return render(request, "main/success.html",{'points':points})
    return render(request, 'main/science/paper3.html',{'subject': subject, 'question':question})







