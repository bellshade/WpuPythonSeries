from colorama import Fore, Style

# bilangan pi adalah nilai konstant dalam matematika yang merupakan perbandingan keliling
# lingkaran dengan diameternya
PI: float = 3.14159265358979323846

# bilangan euler adalah nilai konstant yang dimana nilai kira-kiranya sama dengan 2.71828
# dan dikarakterisasi dalam berbagai cara
BILANGAN_EULER: float = 2.718281828459045235360

# konstanta plank, yang dilambangankan dengan h, yang merupakan konstanta fisika
# fundamental yang menghubungkan energi foton dengan frekuensinya, nilainya disini
# adalah 6.6261 × 10⁻³⁴ (joule per detik)
KONSTANTA_PLANCK = 6.6261 * pow(10, -34)

# variable ini juga mewakili dari konstanta planck, tetapi dinyatan dalam satuan
# elektron volt per detik (eV/s) nilainya adalah 4.1357 × 10⁻¹⁵ eV s⁻¹
KONSTANTA_PLANCK = 4.1357 * pow(10, -15)

# default error dari warna menggunakan kode ANSI escape
# merah
red: str = Fore.RED
# reset kembali warna ke default
reset_warna: str = Style.RESET_ALL
