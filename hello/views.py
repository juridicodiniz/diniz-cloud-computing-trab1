from django.http import HttpResponse

def home(request):
    return HttpResponse("<b>Nome:</b> Fernando Mendes Diniz<br><b>Disciplina:</b> Cloud Computing & Site Reliability Engineering")