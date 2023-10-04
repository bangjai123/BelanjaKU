1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat     untuk menggunakannya.

Selectors digunakan agar kita dapat menerapkan style atau rule pada komponen tertentu.

Selesctors dapat dikategorikan dalam lima kategori:
a. Simple (elemen, id, class):
  - Elemen. Selector ini dapat digunakan untuk memilih berdasarkan nama elemen Misalnya p (tag HTML) maka akan memilih semua tag <p>. Tepat digunakan untuk memengaruhi elemen dengan tag yang sama
  - id. Kita dapat memberi "tanda" pada element di HTML menggunakan suatu id. Dengan demikian, semua yg kita lakukan terhadap id tersebut berlaku untuk element dengan id tersebut. Tepat digunakan jika kita ingin memilih elemen tertentu dan memberinya id, serta menerapkan rule untuk item tertentu itu saja
  - class. Mengelompokkan element dengan karakteristik yang sama. Diterapkan untuk memilih untuk menerapkan style pada element di class yang sama.

b. Pseudo-class selectors. Untuk memilih elemen pada keadaan tertentu.
c. Pseudo-elements selectors untuk memilih dan mengubah elemen yang ada dalam elemen lain
d. Attribute selectors. Untuk memilih berdasarkan attribute

2.  Jelaskan HTML5 Tag yang kamu ketahui
   - <body> mengandung konten dari tampilan web
   - <h1>,<h2>,...<h6> Elemen header dengan h1 paling tinggi dan h6 paling       rendah
   - <p>paragraf
   - <title> Membuat judul dari tampilan web
   - <a> memuat hyperlink ke tampilan atau resource lainnya
 
3. Jelaskan perbedaan antara margin dan padding
   Margin mengosongkan area di sekitar border (transparan), sedangkan padding mengosongkan area di sekitar konten (transparan)

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Dari segi design, tailwind memberikan fleksibilitas yang lebih besar dalam desain tampilan. Hal tersebut dapat menjadi pretimbangan bahwa bootstrap sudah menyediakan tema dan desain yang sudah jadi. Dengan demikian, user tinggal membuat perubahan sedikit. Dari ukuan file, tailwind lebih ringan. Bootstrap lebih mudah digunakan untuk orang yang baru belajar

Dengan demikian, menentukan mana yang digunakan mungkin dapat didasarkan dari pengalaman pengembang. Bootstrap lebih memudahkan untuk orang yang masih kurang pengalaman.Tailwind dapat digunakan jika butuh fleksibilitas dalam kustomisasi.

5. 1. Kustomisasi template HTML
      - Pada base.html menambahkan <meta name="viewport"> agar tampilannya lebih fleksibel.
      - menambahkan bootstrap css dan bootstrap js
      - kustom tampilan sesuai yang diinginkan dengan template dari bootstrap
