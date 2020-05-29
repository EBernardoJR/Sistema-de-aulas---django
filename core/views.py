from django.shortcuts import render
from django.http import HttpResponse #objeto a ser retornado

# Create your views here.
#os componentes são defifinidos por funções
def home(req):
   #return HttpResponse('hello world')
   #retornando html        / segundo parametro é o contexto
   #o template vai ser lido automaticamente dentro da pasta templates
   return render(req, 'home.html')

    
def teste(req):


    return render(req, 'teste.html', { 'protocol' : '233199e9288tcte3'})

def contacts (req):
    return render(req, 'contacts.html')