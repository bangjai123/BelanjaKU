Nama: Zaidan Naufal Ilmi
NPM: 2206081761
Kelas: PBP F

1. Django UserCreationForm adalah form bawaan Django yang digunakan untuk membuat form otentikasi pengguna. Kelebihan Django UserCreationForm adalah memudahkan pengguna untuk membuat form otentikasi, sudah menyediakan validasi otomatis, sudah terintegrasi dengan sistem kemanan Django, form ini masih dapat dikostumisasi. Meskipun demikian, form ini masih meliki kekurangan, diantaranya adalah terbatasnya fitur, kurang fleksibel (mungkin tidak sesuai dengan kebutuhan), tampilan bawaan mungkin tidak sesuai dengan konsep UI/UX yang diinginkan

2. Autentikasi adalah proses untuk memastikan entitas yang hendak masuk, sederhananya terkait dengan pertanyaan (who?) misalnya dengan mengecek kesesuiaan username dan passwordnya. Di sisi lain, otorisasi adalah proses untuk memastikan suatu entitas mengakses atau melakukan hal yang bisa entitas tersebut lakukan sesuai hak nya (what it can do?). Kedua proses ini penting untuk memastikan keamanan, kepatuhan hukum, kontrol akses, dan personalisasi. Keduanya merupakan dua hal yang sama-sama penting. Setelah web mengetahui siapa entitas yang login, web juga harus memastikan entitas tersebut hanya mengakses atau melakukan hal-hal yang diizinkan untuk entitas tersebut.

3. cookies adalah salah satu mekanisme penyimpanan data yang digunakan pada web seperti informasi login, referensi, dan identifikasi pengguna pada perangkat pengguna. Dalam Django, cookies digunakan untuk mengelola data sesi pengguna. Penggunaannya adalah sebagai berikut:
   a. Session Identifier
   b. Penyimpanan Data Sesi
   c. Menggunakan Session Middleware
   d. Akses Data Sesi
   e. Durasi sesi

4. Penggunaan cookies masih memimiliki beberapa risiko potensial yang perlu diwaspadai. Di antaranya adalah risiko keamanan privasi, cross-site scripting, cross-site request forgery, session hijacking, dan cookie theft.

5. Langkah yang saya lakukan untuk mengimplementasikan checklist adalah sebagai berikut.
   1. Mengimplementasikan fungsi registrasi:
      pada views.py di main:
      - import redirect, UserCreationForm, dan messages
      - buat fungsi register
      - buat html baru bernama register.html sebagai tampilan register
      pada urls.py:
      - import register
      - tambahkan url ke register pada urlpatterns
   2. Mengimplementasikan fungsi login:
      pada views.py di main:
      - import authenticate dan login
      - buat fungsi login_user
      - buat html baru bernama login.html
      pada urls.py:
      - import login_user
      - tambahkan url ke login_user pada urlpatterns
   3. Mengimplementasikan fungsi logout:
      pada views.py:
      - import logout
      - buat fungsi logout_user
      - tambahkan tombol logout di main.html yang menghubungkan kembali ke          halaman login
      pada urls.py:
      - import logout_user
      - tambahkan url ke logout_user pada urlpatterns
        
   4. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal:
      Cara mengisi form registrasi lalu login dan membuat item baru
      
   5. Menghubungkan model Item dengan User
      1. pada models.py di main:
         - import user
         - pada Item yang telah dibuat masukkan kode:
           user = models.ForeignKey(User, on_delete=models.CASCADE)
      2. pada views.py:
         - ubah fungsi create_item menjadi:
           def create_item(request):
            form = ItemForm(request.POST or None)

           if form.is_valid() and request.method == "POST":
               product = form.save(commit=False)
               product.user = request.user
               product.save()
               return HttpResponseRedirect(reverse('main:show_main'))
         - ubah kode pada fungsi show_main line pertama menjadi
          items = Item.objects.filter(user=request.user)
       3. Simpan semua perubaha dengan makemigrations dan migrate

   6. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi:
         1. pada views.py:
            -  import HttpResponseRedirect, reverse, dan datetime
            -  menambahkan cookie dengan menambahkan last_login pada fungsi                login_user
            -  menambahkan variable last_login padan show_main
            -  mengubah fungsi logout_user untuk menghapus last_login
         2. Pada main.html:
            agar informasi dapat ditampilkan, masukkan teks untuk                       menampilkannya pada main.html
