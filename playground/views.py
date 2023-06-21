from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def var_test(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        return render(request, 'result.html', {'user_input': user_input})
    
    return render(request, 'input.html')

