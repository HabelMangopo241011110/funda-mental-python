data_pemain = [
    {"nama" : "lamine yamal", "umur" : 18},
    {"nama" : "messi", "umur" : 39},
    {"nama" : "neymar", "umur" : 34},
    {"nama" : "luis suarez", "umur" : 38}
]

umur_ideal = 27
analisis_umur =[]

for umur in data_pemain:
    if umur["umur"] <= umur_ideal:
        kategori = "masih muda"
    else:
        kategori = "pemain sudah tua"
    analisis_umur.append(f"{umur['nama']} {kategori}")

for i in analisis_umur:
    print(i)