ilkin_qiymet = float(input("ilkin qiymet daxil edin: "))
endirim_faiz = float(input("endirim qiymeti daxil edin: "))

endirim_mebleg = ilkin_qiymet*endirim_faiz/100
son_qiymet = ilkin_qiymet - endirim_mebleg

print("endirim meblegi:", endirim_mebleg )
print("son qiymet:", son_qiymet)