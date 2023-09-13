Nama: Zaidan Naufal Ilmi
NPM: 2206081761
Kelas: PBP F

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
![gambar bagan - Copy](https://github.com/bangjai123/BelanjaKu/assets/120235144/bb85b21a-d9d3-4251-beda-9ae2712c2c90)

Request yang diberikan user akan diproses melalui urls.py untuk dihubungkan pada aplikasi main melalui views.py. Main akan menghubungi mode untuk mengatur data dan memintanya ke database apabila diperlukan. Selain itu, views.py akan memilih template html yang akan digunakan. view tersebut akan ditampilkan kepada user.

3.  Virtual environment dibutuhkan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang telah ada di komputer. Kita bisa saja membuatnya tanpa menggunakan virtual environment. Akan tetapi, akan terdapat kekurangan apabila dibandingkan dengan menggunakan virtual environment. Kekurangannya adalah dependensi antar proyek dapat salah mempengaruhi dan menyulitkan kita untuk melakukan manajemen proyek.
   
4.
a. MVC (Model-View-Controller) adalah salah satu pola desain arsitektur software yang umum digunakan. Pola desain arsitektur ini membagi pengembangan software menjadi tiga komponen, yaitu model, view, dan controller. Model berfungsi untuk mengelola data dan logika bisnis aplikasi. View berfungsi untuk menampilkan data dari model kepada pengguna. Controller berfungsi untuk menjadi perantara antara model dan view.

b. MVVM (Model-View-ViewModel) adalah salah satu pola desain arsitektur software berbasis GUI. Pola dasar arsitektur ini memisahkan pengembangan menjadi tiga komponen utama, yaitu model, view, dan viewmodel. model berfungsi untuk mengelola data dan logika bisnis aplikasi. View berfungsi sebagai UI yang menampilkan informasi kepada pengguna serta menerima input yang dimasukkan pengguna. Viewmodel berfungsi sebagai perantara antara model dan view dengan mengambil data dari model dan mempersiapkannya untuk ditampilkan di view.

c. MVT (Model-View-Template) juga merupakan salah satu pola desain arsitektur. MVT membagi pengembangan menjadi tiga komponen yaitu model, view, dan template. Model berfungsi untuk mengelola data da logika bisnis dari aplikasi. View berfungsi untuk menangani tampilan data dan interaksi dengan pengguna. Template memisahkan tampilan dari logika dalam aplikasi.

Ketiga pola pengembangan aplikasi di atas sebenarnya memiliki tujuan yang sama, yaitu membagi pengembangan ke dalam beberapa komponen sehingga dapat memudahkan proses pengembangan aplikasi, terutama dalam pembagian tugas. Akan tetapi, ketiganya memiliki perbedaan, di antaranya adalah sebagai berikut.

1. View: pada MVC, view berfungsi untuk menangani tampilan data dan interaksi pengguna. View menggambarkan informasi kepada pengguna dan menerima input. Dalam MVT, view juga berfungsi untuk tampilan data dan interkasi pengguna, sedangkan MVVM view lebih berfokus pada tampilan visual dan kurang dalam logika aplikasi.
2. Interaksi antar komponennya. Pada MVC, controller berfungsi untuk mengatur interaksi antara model dan view. Dalam MVT, template dan view bersama dalam mengontrol tampilan dan interaksi pengguna. Dalam MVT, model akan berfungsi dalam mengolah data. Dalam MVVM, ViewMode berfungsi untuk menatur interaksi antara model dan view serta memungkinkan pengikatan data untuk sinkronisasi tampilan dengan model secara otomatis.
3. Perbedaan ketiganya paling utama terletak pada bagaimana diaturnya tampilan dan logika aplikasi serta interaksi antar komponennya. Penggunaannya akan bergantung pada kebutuhan. MVT lebih banyak digunakan dalam pengembangan web menggunakan teknologi seperti Django, sedangkan MVVM lebih banyak digunakan dalam pengembangan aplikasi berbasis platform seperti WPF.
