 #1.Da se napravi programa vo koja korisnikot ke moze da vnese 10 broevi, da se dodadat vo list i da se soberat site broevi vo listata
lista = list ()
for i in range (10):
    br=int (input ("Vnesete broj: "))
    lista.append (br)
print ("Broevi sto gi imate vneseno vo listata se slednive:", lista)
zbir=sum(lista)
print("Zbir na broevite od listata iznesuva {}".format (zbir))



#2.Da se napravi programa vo koja korisntikot ke moze da vnese proizvolen broj na broevi, da se dodadt vo lista i da se najde najgolemiot broj
lista = []
da ="da"
while da == "da":
    print ("Ve molime vnesete nekoj broj.")
    broj= int(input())
    lista.append (broj)
    da=input ("da prodolzime? 'da' ili 'ne'")
print ("Vie gi imate Vneseno slednive broevi: ",lista)

maxbr=max(lista)
print ("Najgolem broj vo listata e {}".format (maxbr))

#3. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na elementi, da se ispecati listata i korisnikot da moze da izbere kolku elementi 
#i koi elementi ke gi izbrise

lista = []
da ="da"
while da == "da":
    print ("Ve molime vnesete nekolku iminja na ovosje:")
    ovosje = str (input())
    lista.append (ovosje)
    da=input ("da prodolzime? 'da' ili 'ne'")
print ("Vie gi imate Vneseno slednive iminja na ovosje: ",lista)
print ("Od vkupno vneseni {} iminja na ovosje, izberete kolku podatoci sakate da gi izbrisete od Vasata lista".format(len(lista)))
izbrisi = int (input())
for i in range (izbrisi):   
    print("Ve molime napisete koj od slednive podatoci bi sakale da go izbrisete")
    brisenje = str (input (lista))
    lista.remove (brisenje)
print ("Novata lista izgleda vaka:",lista)


#4. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na iminja, da se dodadat vo lista, i da se najde najdolgoto ime

lista =[]
dolzina = []
dane="da"
while dane =="da":
    print ("Vnesete ime")
    ime=str (input ())
    lista.append (ime)
    dolzina.append (len (ime))
    #print(lista)
    #print (dolzina)
    dane=str(input ("Napisete 'da' dokolku sakate da vnesete novo ime: "))
treba=max(dolzina)
#print (treba)
brisi=dolzina.index (treba)
#print (brisi)

print ("Vasata lista izgleda vaka" , lista)
print ("Najdolgo ime e {}".format (lista[dolzina.index (treba)]))

#5. Da se napravi programa vo koja korisnikot ke vnese proizvolen broj na broevi, da se dodadat vo lista i da se najde vtoriot najgolem broj

lista = []
da ="da"
while da == "da":
    print ("Ve molime vnesete nekoj broj.")
    broj= int(input())
    lista.append (broj)
    da=input ("da prodolzime? 'da' ili 'ne'")
print ("Broevi sto gi vnesovte se slednive: ",lista)
bri= (max (lista))
#print (bri)
brisi=lista.remove (bri)
#print (brisi)
najdi=(max (lista))
print("Vtoriot najgolem broj od listata e {}".format(najdi))

#6. Da se napravi programa koja ke bide upotrebuvana vo nekoja prodavnica za prodazba. Korisnikot da moze da vnesuva produkti se dodeka 
#ne izbere deka saka da plati. Produktitte da se dodavaat vo edna lista, cenite vo druga lista. 
#Koga ke izbere deka saka da plati da mu se ispecatat produktite i cenite vo nalik na "fiskalna smetka". Da ima moznost korisnikot da plati 
# i da se presmeta dali i kolku treba da mu se vrati kusur"""
produkt =[]
cena =[]
dane="da"
while dane=="da":
    print ("Vnesete go imeto na produktot:")
    ime=str (input ())
    produkt.append(ime)
    print ("Vnesete ja cena na {}:".format(ime))
    den=int(input ())
    cena.append(den)
    dane=input ("Odgovorite so 'da' dokolku sakate da vnesete nov produkt: ")
[print(x,y) for x,y in zip(produkt, cena)]
print ("Vkupno za naplata {} mkd".format (sum(cena)))
print ("Izberete nacin na plakanje: 'kes' ili 'karticka'")
pay=str (input ())
if pay == "kes":
    dep=int(input("So kolku MKD ke platite: "))
    kusur=dep-sum(cena)
    print ("Za vrakanje ima {} mkd".format (kusur))
elif pay =="karticka":
    pin=int (input ("Vnesete go Vasiot pin: "))
    print ("Transakcijata e uspesna. Imajte ubav den")