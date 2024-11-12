def luaspersegipanjang(panjang, lebar):
    return panjang*lebar

def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)

panjang = int(input("masukan nilai panjang :"))
lebar = int(input("masukan nilai lebar :"))


hasil_luas = luaspersegipanjang(panjang,lebar)
hasil_keliling = kelilingpersegipanjang(panjang,lebar)

print("luas =", hasil_luas) 
print("keliling=", hasil_keliling)
