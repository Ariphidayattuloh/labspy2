LATIHAN TUGAS 7
----------------


Nama : Arip Hidayattuloh

Nim  : 312010244

Kelas : TI.20.B.1

Dosen : Agung Nugroho S.Kom., M.Kom.

Tugas : Pertemuan ke 7

Pernyataan if
Pada python dikenal penggunaan struktur kondisi menggunakan statement if, dimana
format/syntax penggunaan statement if adalah:


syntax:
if kondisi:

statement_true

Contoh program penggunaan statement if
----------------------------------------------

num = input("Masukkan angka: ")

if (int(num) > 0):

     print(num, "adalah bilangan positif")

print("ini diluar pernyataan if")

----------------------------------------------

Pernyataan if … else

syntax:

if kondisi:

     statement_true

else:

     statement_false

Contoh program penggunaan statement if … else
----------------------------------------------

num = input("Masukkan angka: ")

if (int(num) >= 0):

    print(num, "adalah bilangan positif")

else:

     print(num, "adalah bilangan negatif")
     print("ini diluar pernyataan if")
------------------------------------------------

Pernyataan if … elif
syntax:

if kondisi:

    statement_true

elif kondisi2:

    statement_true

else:
 
   statement_false

Contoh program penggunaan statement if … elif
-----------------------------------------------

num = input("Masukkan angka: ")

if int(num) > 0:

     print(num, "adalah bilangan positif")

elif int(num) == 0:

     print(num, "adalah angka nol")

else:

     print(num, "adalah bilangan negatif")

--------------------------------------------------

Operator Ternary

syntax:
-------
condition_true if condition else condition_false

contoh:

nilai = input("Masukkan nilai: ")

keterangan = "LULUS" if nilai > 60 else "TIDAK LULUS"

print(keterangan)

------------------------------------------------------

syntax:
-------
(condition_false, condition_true)[condition]

contoh:

nilai = input("Masukkan nilai: ")

keterangan = ("TIDAK LULUS", "LULUS")[nilai > 60]

print(keterangan)

-----------------------------------------------------

Latihan 1: Latihan 1: Membuat program menentukan nilai akhir
--------------------------------------------------------------------

![latihan 1](https://user-images.githubusercontent.com/72840534/98449594-54069e00-2167-11eb-8ad0-c8b00e47b2a2.png)

![hasil latihan 1](https://user-images.githubusercontent.com/72840534/98449605-6ed91280-2167-11eb-8ccc-a8ed06fa3463.png)


Latihan 2: Membuat program menampilkan status gaji karyawan.
---------------------------------------------------------------

![latihan 2](https://user-images.githubusercontent.com/72840534/98449619-89ab8700-2167-11eb-8828-c0641aba3668.png)


![hasil latihan 2](https://user-images.githubusercontent.com/72840534/98449628-9af49380-2167-11eb-9138-5f87fb86f3bf.png)


Latihan 3: penggunaan kondisi OR
program membandingkan 3 input bilangan, apabila penjumlahan 2 bilangan hasilnya
sama dengan bilangan lainnya, maka cetak pernyataan “BENAR”
-----------------------------------------------------------------------------------


![latihan 3](https://user-images.githubusercontent.com/72840534/98449639-ac3da000-2167-11eb-95be-077cb3bb2199.png)


![latihan 3 1](https://user-images.githubusercontent.com/72840534/98449651-bfe90680-2167-11eb-8379-a0010544fe93.png)

latihan 4 input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya
-------------------------------------------------------------------------------------------


![Latihan 4](https://user-images.githubusercontent.com/72840534/98449659-d68f5d80-2167-11eb-8846-dab184bda919.png)


![hasil Latihan 4](https://user-images.githubusercontent.com/72840534/98449668-e27b1f80-2167-11eb-9349-192f886f58f9.png)



Sekian dari saya 

--arip hidayattuloh--
