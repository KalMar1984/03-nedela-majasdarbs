#=====A daļa saraksti=====

print("-----saraksti----- ")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
my_list.append(11) #pievieno elementu saraksta beigās 
my_list.insert(0, 0) #pievieno elementu saraksta sākumā (divi argumenti: pozīcija, vērtība)
print(my_list) 

my_list.pop() #noņem pēdējo elementu (var atgriezt izdzēsto) dzēš pēc pozīcijas indeksa !!!skaitīšana sākas no 0!!!
my_list.pop(0) #noņem pirmo elementu
print(my_list) 


#---aprēķini---

summa = 0 #šeit glabāsim kopējo summu
count = 0 #šeit glabāsim elementu skaitu    

for num in my_list: #iterējam cauri sarakstam (paņemam katru elementu un saglabājam to mainīgajā num)
    summa += num #pievienojam katru elementu summai
    count += 1 #palielinām skaitītāju par 1 

    vidējais = summa / count #aprēķinām vidējo vērtību/elementu skaitu

print("Summa:", summa)
print("Elementu skaits:", count)
print("Vidējais:", vidējais)    

print(f"Summa: {summa}, Vidējais: {vidējais}") #īsāks kods f-formatēts teksts, summa-parasts teksts, {summa}-mainīgā vērtība vidējais-parasts teksts {vidējais}- mainīgā vērtība


#---filtrēšana - jauns saraksts ar pāra skaitļiem 

pāra_skaitļi = [] #tukšs saraksts kur glabāsim pāra skaitļus

for num in my_list:
    if num % 2 == 0: # % ir atlikuma operators ja num % 2 == 0 tad skaitlis dalās ar 2 bez atlikuma, tas ir pāra skaitlis 
        pāra_skaitļi.append(num) 
print(f"Pāra skaitļi: {pāra_skaitļi}") 


#---Šķēlumi (slice) 

print(f"pirmie 3: {my_list[:3]}") # [:3] nozīmē: no sākuma līdz 3. elementam (neieskaitot 3. indeksu)

print(f"pēdējie 2: {my_list[-2:]}") # [-2:] nozīmē: pēdējie 2 elementi 

print(f"katrs otrais elements: {my_list[::2]}") 


#=====B daļa vārdnīca===== 

