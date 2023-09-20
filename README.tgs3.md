Nama: Zaidan Naufal Ilmi
NPM: 2206081761
Kelas: PBP F

1. Sebenarnya, keduanya berfungsi untuk mengirimkan data dari klien ke server. Yang membedakan keduanya adalah cara masing-   masing untuk mengirimkannya. form GET mengirimkan data sebagai parameter URL, sedangkan form POST mengirimkan data sebagai  badan permintaan. Dengan demikian, perbedaan keduanya dapat dilihat pada tabel di bawah ini.

   ![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/2776b65a-6865-4d2c-bb8f-76e2e8b95f55)

2. Ketiganya memiliki perbedaan karakteristik, di antaranya adalah sebagai berikut.
   ![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/419c8fad-778d-44d5-b5c0-bba67ae4687d)

   Jika ditinjau dari penggunaannya, JSON lebih banyak digunakan untuk pengirimiman data, XML lebih banyak digunakan untuk mengirimkan data yang kompleks, sedangkan HTML lebih banyak digunakan untuk menampilkan data secara visual.

3. JSON lebih sering digunakan dalam pertukaran data antar aplikasi web modern karena JSON dapat dibaca dengan mudah oleh manusia dan mesin. Selain itu, JSON memiliki ukuran file yang cenderung lebih kecil cocok digunakan untuk API.
   
4. a.  Membuat input form untuk menambahkan objek model pada app sebelumnya:
       Dimulai dengan membuat file forms.py di direktori main aplikasi. File tersebut diisi dengan kode untuk menunjukkan model yang digunakan untuk form. Ketika form diisi, objek tersebut akan disimpan sebagai objek yang telah ditentukan. Dalam aplikasi ini, objeknya adalah Item. Selain itu, forms.py akan berisi fields yang diinginkan untuk diisi. Maka kodenya akan menjadi:

from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "price","description"]

   b. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. :

   Pertama, saya melakukan import yang dibutuhkan untuk menampilkan viewsnya. Setelah melakukan semua import yang dibutuhkan, views.py akan memiliki bagian kode:

from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

Untuk menampilkan data dalam format html, saya menggunakan fungsi

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

yang akan mengupdate main.html untuk menampung data yang baru saja dimasukkan

Untuk menampilkan data dalam XML, fungsi yang digunakan adalah
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

Untuk menampilkan data dalam JSON, fungsi yang digunakan adalah
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

Untuk menampilkan data dalam XML by ID, digunakan fungsi
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

Untuk menampilkan data dalam JSON by ID, digunakan fungsi
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

Selain itu, urls.py perlu ditambahi path ke urlpatterns agar data dapat dibaca. Sehingga urlpatterns akan berisi:

    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/', show_json, name='show_json'), 
selain itu, perlu dilakukan import fungsi-fungsi tadi di url.py:
from main.views import show_main, create_item, show_json, show_xml, show_json_by_id,show_xml_by_id

5. Berikut ini adalah screenshot dari akses kelima url di atas menggunakan postman. Secara berurutan: html, json, xml, xml by id (1), json by id (1):

![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/ad556b6a-29f9-4fe7-bf27-29e8fb000231)
![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/24cb3397-dbbb-4c94-ba8e-fa9174210ab6)
![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/e9a796ed-a068-4d9e-bb7e-c84cf98b32ca)
![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/4db56b87-2fec-4fbb-981b-e7967c8fb652)
![image](https://github.com/bangjai123/BelanjaKu/assets/120235144/5c74831a-1b8a-4eea-8c90-2cd85c35ed41)




   
