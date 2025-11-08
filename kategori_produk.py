jumlah = int(input("Masukkan jumlah produk yang ingin dikategorikan: "))

for i in range(jumlah):
    print(f"\nProduk ke-{i+1}")
    jenis = input("Masukkan jenis produk (Laptop/Smartphone/Tablet): ").lower()
    harga = float(input("Masukkan harga produk (dalam juta): "))

    if jenis == "laptop":
        if harga < 5:
            kategori = "Budget"
        elif harga <= 10:
            kategori = "Mid"
        else:
            kategori = "Premium"

    elif jenis == "smartphone":
        if harga < 2:
            kategori = "Low-end"
        elif harga <= 5:
            kategori = "Mid-range"
        else:
            kategori = "Flagship"

    elif jenis == "tablet":
        if harga < 3:
            kategori = "Entry"
        elif harga <= 7:
            kategori = "Standard"
        else:
            kategori = "Pro"

    else:
        kategori = "Jenis produk tidak dikenali"

    print(f"Kategori produk: {kategori}")

print("\n=== Selesai Mengkategorikan Semua Produk ===")