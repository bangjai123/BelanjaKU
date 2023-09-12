from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Name',
        'amount': 'Amount',
        'price': 'Price/Item',
        'descripstion' : 'Descriptions'
    }

    return render(request, "main.html", context)
