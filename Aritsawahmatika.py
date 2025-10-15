print ('Selamat Datang Di Aritmatika Python by maspip:v')
print ('Silahkan masukan angka')

nilai_a = input('berapa nilai a:')
nilai_n = input('berapa nilai n:')
nilai_b = input('berapa nilai b:')

print()
print('Diketahui')
print('nilai a adalah :' + nilai_a)
print('nilai n adalah :' + nilai_n)
print('nilai b adalah :' + nilai_b)
print()
print('maka jawabannya adalah:')

print('Un= a (n-1)×b')
print('Un=' + nilai_a + '+' + '(' + nilai_n + '-1' + ')' + '×' + nilai_b  ) 

hasil_n = int(nilai_n) -1

print('Un=' + nilai_a + '+' + str(hasil_n) + '×' + nilai_b  ) 

hasil_beda = (hasil_n) * int(nilai_b)

print('Un=' + nilai_a + '+' + str(hasil_beda))

hasil_Un = int(nilai_a) + int(hasil_beda)

print('Un=' + str(hasil_Un))
print('maka hasilnya adalah :' + str(hasil_Un))