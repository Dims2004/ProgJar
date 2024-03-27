#1.Membuat program untuk menghitung jumlah huruf dalam sebuah kata yang dimasukkan pengguna.

#kata = input("katanya apa? : ")

#jumlah = len(kata)

#print("jumlah huruf dalam kata {} tersebut adalah {}".format(kata, jumlah))

#2.Membuat program untuk menghitung luas dan keliling lingkaran dengan input jari-jari dari pengguna.

#jari_jari = float(input("masukan jari jari lingkaran :"))

#luas = 3.14 * (jari_jari ** 2)

#keliling = 2 * 3.14 * jari_jari

#print("luas lingkaran jari-jari {} adalah {:.2f}". format(jari_jari, luas))
#print("keliling lingkaran dengan jari-jari {} adalah {:.2f}". format(jari_jari,keliling))


#3.Membuat program untuk mengubah suhu dari Fahrenheit ke Celsius atau sebaliknya.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    print("Program Konversi Suhu Fahrenheit - Celsius")
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Fahrenheit ke Celsius")
    print("2. Celsius ke Fahrenheit")

    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")
    elif choice == '2':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    main()

     
