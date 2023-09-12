Link app: https://belanjaku-apps.adaptable.app/main/
Jawaban:
1. Pertama-tama, saya membuat sebuah direktori baru bernama BelanjaKu yang akan menampung proyek dan aplikasinya. Direktori ini berada di github dan pc saya dan keduanya terhubung (setelah melalui berbagai konfigurasi).

   Lalu, saya menjalankan perintah (python -m venv env) untuk membuat virtual environment pada direktori yang sudah saya buat. Perintah tersebut dilakukan di command prompt. Setelah itu, saya mengaktifkan virtual environment dengan perintah (env\Scripts\activate.bat). Lalu, saya menginstall berbagai dependencies yang dibutuhkan, salah satunya Django. Lalu, dengan perintah (django-admin startproject BelanjaKu .), saya membuat proyek Django baru bernama BelanjaKu sekaligus membuat direktori baru di dalam BelanjaKu yang bernama BelanjaKu. Langkah ini merupakan langkah untuk melakukan checklist pertama.

   Setelah membuat berkas gitignore dan mensetting host, saya melakukan checklist kedua dengan menjalankan perintah python (manage.py startapp main). Perintah ini akan membuat aplikasi main sekaligus direktori baru bernama main yang menjadi direktori aplikasi.

   Untuk melakukan checklist ketiga (routing pada proyek), yang saya lakukan adalah membuka urls.py pada direktori proyek dan memasukkan kode:

   from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]

  Yang dilakukan kode itu adalah mengatur path url untuk menyesuaikan halaman yang akan dipanggil sesuai dengan url yang dimasukkan.

  Selanjutnya, membuat model pada aplikasi main (sesuai yang ditentukan soal) dilakukan dengan memasukkan kode berikut ini ke dalam models.py pada direktori main.

  from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()

  Kode tersebut akan mengimport models dan memasukkan item yang diingikan untuk attributes dari Item.

  checklist selanjutnya saya lakukan dengan memasukkan kode berikut ini ke dalam views.py yang ada dalam direktori main.

  from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Name',
        'amount': 'Amount',
        'price': 'Price/Item',
        'description' : 'Descriptions'
    }

    return render(request, "main.html", context)
kode tersebut adalah fungsi yang akan mengisi html sekaligus merender tampilannya.

 Untuk melakukan checklist ketiga (routing pada aplikasi), yang saya lakukan adalah membuka urls.py pada direktori main dan memasukkan kode:

   from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

  Yang dilakukan kode itu adalah mengatur rute url yang terkait aplikasi main. Hal ini dapat dilihat dari dipanggilnnya show_main dari views.py yang berada di direktori main.

  Melakukan deployment ke adaptable saya lakukan dengan signup menggunakan akun github saya dan memilih repositori yang akan saya deploy (dalam hal ini, BelanjaKu). Setelah itu, saya hanya perlu mengikuti langkah yang ditunjukkan oleh adaptablenya serta mengisi beberapa konfigurasi. Setelah menunggu beberapa saat, aplikasi saya telah terdeploy dan dapat diakses melalui  (https://belanjaku-apps.adaptable.app/main/).

2. 
3.  Virtual environment dibutuhkan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang telah ada di komputer. Kita bisa saja membuatnya tanpa menggunakan virtual environment. Akan tetapi, akan terdapat kekurangan apabila dibandingkan dengan menggunakan virtual environment. Kekurangannya adalah dependensi antar proyek dapat salah mempengaruhi dan menyulitkan kita untuk melakukan manajemen proyek.
4.  
