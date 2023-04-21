#Kütüphane yüklümü degilmi sorgulayan kod
import importlib.util
libary = input("Kütüphane adını giriniz: ")
lib = importlib.util.find_spec(libary)
if lib is None:
    print("Kütüphane bulunamadı")
else:
    print("Kütüphane var")    


