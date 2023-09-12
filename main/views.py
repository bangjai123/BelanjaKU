from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Name',
        'amount': 'Amount',
        'price': 'Price/Item',
        'description' : 'Descriptions'
    }

    return render(request, "main.html", context)
