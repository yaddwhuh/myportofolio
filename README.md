Nama : Muhammad Fayadh Azzahran

NPM : 2506586961

Kelas : PBP C

Jurusan : S1 Ilmu Komputer

### Tugas 1

1. Saya menggunakan (section) pada tugas pertama ini. (section) membantu saya untuk memisahkan bagian-bagian penting pada website saya, seperti membagi bagian hero dengan art portofolio.

2. Tantangan yang ada yaitu container art saya menempel di kiri website dan gambar saat dimasukkan memenuhi satu section. Saya mengevaluasi bagian-bagian yang penting menggunakan grouping Figma, sehingga saya mengerti kapan saya bisa menggunakan (div) pada code saya.

3. Jika saya menambahkan lebih banyak elemen--atau pada tugas saya, karya seni--maka website akan terus menjalar ke bawah. Ini bisa menjadi sebuah limitasi pada website static murni, sehingga saya mungkin membutuhkan fungsionalitas yang lebih dinamis untuk mengatasi problem tersebut.

Pada pengerjaan Tugas 1, saya menggunakan AI saat mencari beberapa sintaks html + css di Google (AI overview). Namun saya memastikan bahwa semua snippet code yang diberikan oleh AI overview telah diubah sehingga saya mengerti fungsi setiap bagian kode.

### Tugas 2

1. Ketika pengguna mengunjungi website, urls.py akan mengatur apa yang harus ditunjukkan melalui views.py. views.py akan memanggil: html yang akan ditampilkan dan model yang diperlukan. models.py ini akan menyimpan class-class yang telah dibuat dan diperlukan sehingga template bisa langsung mengambil data dari model. Template hanya bertugas untuk mengatur bagaimana website terlihat bersama dengan style.css.

2. Ketika data harus terus diperbarui, mengubah kode html akan membuat kode template terlalu panjang. Hal ini akan buruk dalam pengembangan lebih jauh.

3. makemigrations akan membuat berkas migrasi yang belum diaplikasikan ke dalam database, lalu migrate akan mengaplikasikan berkas yang dibuat makemigrations ke dalam database. Kedua hal tersebut dilakukan ketika kita membuat perubahan pada struktur model (mengubah nama variabel, menambahkan model baru)

### Tugas 3

1. ModelForm pada Django akan secara otomatis membaca model yang sudah terdefinisi dan membentuk template berdasarkan hal tersebut. Oleh karena itu, penggunaan ModelForm akan mengurangi pengulangan kode saat membuat form dengan HTML manual. Selain itu, csrf_token berfungsi sebagai validasi dan verifikasi ketika user mengisi form atau melakukan aksi.

2. JSON lebih disukai karena bentuknya yang ringkas, lebih cepat untuk diambil datanya, dan 'natural' terhadap bahasa-bahasa pemrograman lainnya.

3. Pertama, fungsi views akan mengambil data dengan bentuk Object Python. Dari sini, browser API tidak bisa mengenali data yang diambil, karena bentuknya masih dalam Object Python, sehingga serialization (Object -> JSON/XML) diperlukan. Kita menggunakan serializer dari Django framework. Fungsi get_projects_json pada views.py adalah fungsi yang kita buat untuk proses serialisasi tersebut.

AI Digunakan pada tugas ini, precisely ketika mengimplementasikan Edit pada website. 

Prompt: `Lets say I have a model called Project, and a form called ProjectForm, and a template for creating form for it. Do I need to make new template for updating form?`

Jawaban: `No — you can (and generally should) reuse the same template for both creating and updating a Project. The template just renders whatever form object it's given; it doesn't care whether that form is bound to a new instance or an existing one. The difference between "create" and "update" lives in the view, not the template...` dan diberikan contoh kode. Kode dibaca sendiri dan diimplementasikan sendiri untuk memastikan dua hal: Sintaks yang digunakan konsisten dan Saya mengerti proses dari fungsi tersebut.