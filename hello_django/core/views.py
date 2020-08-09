from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

def soma(request, v1, v2):
    total = v1 + v2
    return HttpResponse('Soma dos valores {}'.format(total))

def subtracao(request, v1, v2):
    total = v1 - v2
    return HttpResponse('Subtração dos valores {}'.format(total))

def multiplicacao(request, v1, v2):
    total = v1 * v2
    return HttpResponse('Multiplicação dos valores {}'.format(total))

def divisao(request, v1, v2):
    total = v1 / v2
    return HttpResponse('Divisão dos valores {}'.format(total))