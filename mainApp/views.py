from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/contacts.html', {'values': ['Вопросы по телефону',
    '8(42665)21331','admin@admin.com']})
