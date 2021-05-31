program undo_redo.py merupakan program implementasi undo redo sederhana dimana user dapat input text (string), lalu user dapat menghapus text menggunakan tombol redo, dan juga bisa memulihkan text menggunakan redo

cara running program :  
pastikan telah menginstall library tkinter python. cara install nya yaitu : buka command prompt, lalu ketik pip install tk, lalu tekan enter. maka library tkinter telah terinstall di laptop anda.

cara menggunakan program :
1. masukkan text kedalam entri form
2. pencet tombol "add to file", maka text yang telah ditulis akan ditambahkan ke file.txt
3. jika ingin memasukkan banyak data, ulangi langkah 1
4. jika ingin melihat data, pencet tombol show, maka data akan ditampilkan lewat window baru
5. jika ingin menghapus data sebelumnya, pencet tombol undo
6. jika setelah di undo ingin memulihkan data, pencet tombol redo
7. jika ingin melihat history undo redo, pencet tombol history, maka akan muncul window baru.

fitur : 
1. menambahkan teks ke file.txt
2. menunjukkan history undo redo add_text
3. menunjukkan berapa kali kita melakukan undo, redo, dan add_text
4. menunjukkan isi file.txt di window baru
5. menunjukkan file readme.txt (file ini)
6. ketika program dijalankan, meskipun didalam file.txt ada file, kita gabisa undo.
7. redo akan bisa dijalankan jika dan hanya jika undo dijalankan terlebih dahulu.
8. pesan error akan muncul di terminal
9. 
