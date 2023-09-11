from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Sebuah baran',
        'jumlah': '7 buah',
        'harga': 'Rp30.000,00',
        'total' : 'Rp210.000,00'
    }

    return render(request, "main.html", context)
