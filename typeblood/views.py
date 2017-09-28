from django.shortcuts import render

def cad_list(request):
    return render(request, 'typeblood/cad_list.html', {})
