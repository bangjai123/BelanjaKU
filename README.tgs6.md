1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
   pada sychronous, suatu task harus menunggu task lain selesai untuk dikerjakan, sedangkan pada asynchronous tidak. Masing-masing task bisa berjalan berdampingan. Hal ini berarti pada sychronous tasknya harus berurutan, sedangkan asynchronous dapat dilakukan bersamaan.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

   event driven programming artinya suatu task dilakukan ketika suatu perstiwa terjadi. Sebagai contoh, tombol yang diklik yaitu pada tombol tambah produk.
3. Jelaskan penerapan asynchronous programming pada AJAX.
   pertama-tama, menggunakan Fetch API untuk menginisiasi request ke server. Setelah itu, menentapkan function untuk menangani event, lalu mengirim request ke server, respons akan dihandle dari server.
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan. Ukuran file Fetch API lebih kecil dari library jQuery, selain itu Fecth API lebih mudah digunakan.
5. Bagaimana menerapkan checklist?
   - Pertama, dengan membuat Fungsi untuk Mereturn Data JSON
   - Lalu, membuat Fungsi untuk menambah produk dengan AJAX
   - Lalu, membuat routing Untuk Fungsi get_product_json dan add_product_ajax
   - Setelah itu, membuat tampilan data produk dengan Fetch API
   - Membuat modal
   - Membuat fungsi untuk menambahkan data product dengan AJAX
