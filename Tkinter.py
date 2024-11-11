import tkinter as tk
from tkinter import messagebox

#Fungsi `hasil_prediksi()` memeriksa nilai input antara 0-100. 
# Jika semua nilai valid, menampilkan "Prediksi Prodi: Teknologi Informasi". 
# Jika ada kesalahan, menampilkan pesan kesalahan.
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0<= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
            messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")


#membuat jendela aplikasi dengan judul "Aplikasi Prediksi Prodi Pilihan", dan dapat mengatur ukuran dan warna latar belakang.
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

#membuat label dengan teks "Aplikasi Prediksi Prodi Pilihan", dapat mengatur font, latar belakang dan lalu menampilkan label dengan jarak.
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)

#membuat frame dengan latar belakang dan menambahkannya ke jendela dengan jarak 
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

#membuat 10 label dan 10 input untuk nilai mata pelajaran
# Semua input disimpan didalam list `entries`.
entries = []
for i in range(10):
     label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 10, "bold"), bg="#f0f0f0")
     label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
     entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
     entry.grid(row=i, column=1, padx=10, pady=5)
     entries.append(entry)

#membuat tombol "Hasil Prediksi" yang akan menjalankan fungsi hasil_prediksi saat diklik, dengan font Arial tebal dan latar belakang 
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#f0f0f0")
prediksi_button.pack(pady=30)

#membuat label kosong dengan teks berwarna hijau dan font Arial miring tebal.
hasil_label = tk.Label(root, text="", font=("Arial",14, "italic", "bold"), fg="Green",bg="#f0f0f0")
hasil_label.pack(pady=20)

#menjalakan Aplikasi
root.mainloop()





