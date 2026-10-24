qiymet = float(input("Qiyməti daxil edin: "))
say = int(input("Sayını daxil edin: "))
verilen_pul = float(input("Verdiyiniz pulu daxil edin: "))

umumi_qiymet = qiymet * say
qaliq = verilen_pul - umumi_qiymet

print("Ümumi qiymət:", umumi_qiymet)
print("Qalan pul:", qaliq)
