import csv
import os
import random
import json

students_path = '../data/students.json'
profesori_path = '../data/profesori.csv'


listStudents = []
listTeachers = []
listSubjects = []

def get_all_students():
    with open(students_path,'r', encoding='UTF-8') as file_json:
        listStudentsInput = json.load(file_json)
        for student in listStudentsInput:
            listStudents.append(student)
    
def get_all_teachers():
    with open(profesori_path, 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0 
        for row in csv_reader:
            if line_count > 0:
                listTeachers.append(row)
                line_count += 1
            line_count += 1
def get_all_subjects():
    with open('C:\\Users\\Hp\\Desktop\\Faks\\Osnove programiranja\\op_projekat_Vanja_Petric_2019270603\\data\\predmeti.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                listSubjects.append(row)
                line_count += 1
            line_count += 1

def save_students(listStudents):
    with open('../data/students.json', 'w', encoding='UTF-8') as json_file:
        json.dump(listStudents, json_file, indent=2)
 

def new_table(lista):
    with open(profesori_path, 'w', newline='', encoding='UTF-8') as f :
        writer = csv.writer(f)
        rowHeader=["Sifra", "Lozinka", "Ime", "Prezime", "Mail", "Termin konsultacija", "Sifra profesora"]
        writer.writerow(rowHeader)
        writer.writerows(lista)

def konsultacije(profesor):

    
    for t in listTeachers:
        if t[5] == str(profesor[5]):
            print(t[4])
            novi_termin = input("Unesite novi termin u formatu 'Dan : sat': ")
            t[4] = str(novi_termin)
            
    new_table(listTeachers)
    glavni_meni_profesora(profesor)
def app():

    get_all_students()
    get_all_subjects()
    get_all_teachers()
    glavni_meni()
    

def glavni_meni():
    print("*******************************************")
    print("1.Prijava na sistem.")
    print("2.Registracija.")
    print("3.Izlazak iz aplikacije.")
    choice = input("Unesite redni br. zeljene opcije: ")
    if choice == str(1):
        prijava_na_sistem()
    elif choice == str(2):
        registracija()
    elif choice == str(3):
        izlazak_iz_app()   
    else:
        print("Opcija nije ponudjena")
        glavni_meni()
    
    

def prijava_na_sistem():
    try:
        print("*******************************************")
        kIme = input("Unesite korisnicko ime: ")
        lozinka = input("Unesite lozinku: ")
        if kIme != "" and  lozinka != "":
            for student in listStudents:
                if str(student["broj_indeksa"]) == kIme and str(student["lozinka"]) == lozinka:
                    glavni_meni_studenta(student)
            
            for row in listTeachers:
                if str(row[0]) == kIme and str(row[1]) == lozinka:
                    glavni_meni_profesora(row)

            print("Pogresno uneti podaci")
            glavni_meni()    
        print("Morate uneti podatke!!!")
        glavni_meni()
    except IndexError:
        print("Unesite tacno podatke!")
        glavni_meni()

def registracija():
    try:
        print("*******************************************")
        print("1.Profesor.")
        print("2.Student.")
        print("3.Povratak u glavni meni.")
        reg_num =  int(input("Unesite redni br. zeljene opcije: "))
        if reg_num ==1:
            sifra_profesora= random.randint(204,300)
            lozinka = input("Unesite Vasu lozinku: ")
            ime = input("Unesite Vase ime: ")
            prezime = input("Unesite Vase prezime: ")
            email = input("Unesite Vas email: ")
            konsultacije = str(input("Unesite novi termin u formatu 'Dan : sat': ")) 
            ind = False
            while ind == False:
                for i in range(len(listTeachers)):
                    if sifra_profesora == listTeachers[i][0]:
                        sifra_profesora= random.randint(204,300)
                else:
                    ind = True
            new_professor= [lozinka,ime,prezime, email,konsultacije,sifra_profesora]
            listTeachers.append(new_professor)
            new_table(listTeachers)
            glavni_meni()

        elif reg_num ==2:

            broj_indeksa = input("Unesite Vas broj indeksa: ")
            lozinka = input("Unesite Vasu lozinku: ")
            ime = input("Unesite Vase ime: ")
            prezime = input("Unesite Vase prezime: ")
            email = input("Unesite Vas email: ")
            ocene = []
           #for i in range(len(listStudents))
            #    if broj_indeksa == listStudents"""
            new_student = {"broj_indeksa":broj_indeksa ,"lozinka":lozinka,"ime":ime, "prezime":prezime,"email":email,"ocene":ocene}
            listStudents.append(new_student)
            save_students(listStudents)
            glavni_meni()
        else: 
            print("Morate uneti jednu od ponudjenih opcija.")
            glavni_meni()
    except (KeyError, TypeError,ValueError):
        print("Unesite jednu od ponudjenih opcija.") 
        registracija()




def izlazak_iz_app():
    print("Turning off..")
    quit()

def glavni_meni_studenta(keys):
    print("*********************************")
    print("Dobrodosli na sistem "+ keys["ime"] )
    print("1.Globalna prosecna ocena.")
    print("2.Polozeni predmeti.")
    print("3.Nepolozeni predmeti.")
    print("4.Podaci profesora.")
    print("5.Povratak na glavni meni.")
    try:

        choice_s = int(input("Unesite redni br. zeljene opcije: "))
        if choice_s == 1:
            globalna_ocena(keys)
        elif choice_s == 2:
            polozeni_predmeti(keys)
        elif choice_s == 3:
            nepolozeni_predmeti(keys)
        elif choice_s == 4:
            podaci_o_profesoru(keys)
        elif choice_s == 5:
            glavni_meni()
        else:
            print("------------------")
            print("Morate uneti jednu od ponudjenih opcija.")
            glavni_meni_studenta(keys)
    except ValueError:
        print("------------------")
        print("Neispravan unos!")
        glavni_meni_studenta(keys)

def glavni_meni_profesora(profesor):
    try:
        print("***************PROFESOR***************")
        print("Dobrodosli na sistem profesore " + profesor[3] )
        print("1.Dodavanje ocene studentu.")
        print("2.Brisanje ocene studentu.")
        print("3.Prosecna ocena za predmet.")
        print("4.Promena termina konsultacija.")
        print("5.Povratak na glavni meni.")
        try:
            choice_p = int(input("Unesite redni br. zeljene opcije: "))
            if choice_p == 1:
                unos_ocene(profesor)
            elif choice_p == 2:
                brisanje_ocene(profesor)
            elif choice_p == 3:
                prosek(profesor)
            elif choice_p == 4:
                konsultacije(profesor)
            elif choice_p == 5:
                to_glavni_meni()
            else:
                print("------------------")
                print("Morate uneti jednu od ponudjenih opcija.")
                glavni_meni_profesora(profesor)
        except TypeError:
            print("------------------")
            print("Morate uneti jednu od datih opcija.")
            glavni_meni_profesora(profesor)
    except (KeyError,TypeError,ValueError):
        print("------------------")
        print("Morate uneti jednu od datih opcija.")
        glavni_meni_profesora(profesor)
def to_glavni_meni():
    glavni_meni()

def username():
     ime = input("Korisnicko ime: ")
     return ime

def password():
     lozinka = input("Lozinka: ")
     return lozinka

def globalna_ocena (student):#student je ulogovan student
    try:
        ukupna_ocena = 0
        ukupan_broj_ocena = 0 
        for keys in student["ocene"]:
            ukupna_ocena += keys["ocena"]
            ukupan_broj_ocena +=1
        print("-------------------")
        print( "Globalna prosecna ocena studenta je: " + str(ukupna_ocena/ukupan_broj_ocena))
        print("-------------------")  
    except ZeroDivisionError:
        print("Nema polozenih ispita")
    glavni_meni_studenta(student)

def polozeni_predmeti(student):
    print("-------------------")
    for keys in student["ocene"]:
        predmet = predmeti_by_id(keys["sifra_predmeta"])
        print(str(predmet[1]) +": "+ str(keys["ocena"]))
    print("-------------------")
    glavni_meni_studenta(student)

def nepolozeni_predmeti(student):
    nepolozeni_predmeti = []

    
    for row in listSubjects:
        if provera_predmeta(row[0],student["ocene"]) == False:
            nepolozeni_predmeti.append(row)
    print("-------------------")
    print("SIFRA|PREDMET")
    for nepolozen_predmet in nepolozeni_predmeti:
        print(nepolozen_predmet[0] + "  |" + nepolozen_predmet[1])
    glavni_meni_studenta(student)


def provera_predmeta(id_predmeta, lista_polozenih_predmeta): #Vraca nepolezene predmete
        for polozen_predmet in lista_polozenih_predmeta:
            if str(polozen_predmet["sifra_predmeta"]) == str(id_predmeta):
                return True
        return False

def print_predmeti_base():
    for row in listSubjects:
        print(row[0] + "  |" + row[1]) 
            

def podaci_o_profesoru(student_prosledjeni):

  
    detalji_predmeti = {}
    
    try:
        print("====================")
        for row in listSubjects:

            print(row[0] + "  |" + row[1]) 
            detalji_predmeti[row[0]] =  row[1]

        print("\n")
        print("====================")
        izbor = input("Unesite sifru predmeta: ")
        print("\n")
        for student in listStudents:
            for ocene in student["ocene"]:
                if izbor == str(ocene["sifra_predmeta"]):

                    profesor = get_profesor_by_id(str(ocene["sifra_profesora"]))

                    for sifra, naziv in detalji_predmeti.items():
                        if str(sifra) == str(ocene["sifra_predmeta"]):
                            print(naziv + " predaje " + profesor[2] + " " + profesor[3] )   
                        
    except (ValueError,TypeError):
        print("Error")
    glavni_meni_studenta(student_prosledjeni) 

 

def get_profesor_by_id(id):
    for row in listTeachers:
        if str(row[0]) == str(id):
            return row

def predmeti_by_id(id):
    for row in listSubjects:
        if str(row[0]) == str(id):
            return row
    
def unos_ocene(profesor):
    try:
        izbor = str(input("Unesite ime studenta: "))
        izabrani_studenti = get_students_by_name(izbor)
        brojac = 0
        if izabrani_studenti != None:
            for student in izabrani_studenti:
                brojac += 1
                print(str(brojac) + ". " + str(student["broj_indeksa"]) + " " + str(student["ime"]) + " "+ str(student["prezime"]))
            try:
                izabrani_student = {}
                izbor_indeksa =int(input("Unesite broj indeksa: "))
                for student in izabrani_studenti:
                    if izbor_indeksa == int(student["broj_indeksa"]):
                        print(str(student["ime"]) + " " + str(student["prezime"]))
                        izabrani_student = student
                brojac = 0
                for predmet in listSubjects:
                    brojac +=1
                    print(str(brojac) + ". "+  str(predmet[0]) +" " + str(predmet[1]))
                try:
                    izbor_predmeta = int(input("Unesite sifru predmeta: "))
                    predmet = predmeti_by_id(izbor_predmeta)
                    for ocene in izabrani_student["ocene"]:
                        if int(ocene["sifra_predmeta"]) == int(izbor_predmeta):
                            print("Predmet je polozen.")
                            glavni_meni_profesora(profesor)
                    
                    try:
                        ocena = int(input("Unesite ocenu: "))
                        if ocena >= 6 and ocena <=10:
                            nova_ocena = dodavanjeOcene(ocena, predmet, profesor)
                            izabrani_student["ocene"].append(nova_ocena)
                            save_students(listStudents)
                            print("-----------------------------")
                            print("Uspesno ste dodali ocenu.")
                            print(izabrani_student["ime"] + " je polozio sa ocenom " + str(ocena))
                            print("-----------------------------")
                            glavni_meni_profesora(profesor)
                        else:
                            print("Ocena nije u opsegu")
                    except (ValueError,TypeError):
                        print("Pogresno ste uneli ocenu!!!")
                except (ValueError,TypeError):
                    print("Ne postoji dati predmet")
            except (ValueError,TypeError):
                print("Ne postoji student sa datim indeksom")
    except(KeyError):
        print("Ne postoji student sa datim imenom")
    
    else:
        print("Ne postoji student sa tim imenom")
    glavni_meni_profesora(profesor)

def brisanje_ocene(profesor):
    try:
        izbor = str(input("Unesite ime studenta: "))
        izabrani_studenti = get_students_by_name(izbor)
        brojac = 0
        if izabrani_studenti != None:
            for student in izabrani_studenti:
                brojac += 1
                print(str(brojac) + ". " + str(student["broj_indeksa"]) + " " + str(student["ime"]) + " "+ str(student["prezime"]))
            try:
                izabrani_student = {}
                izbor_indeksa =int(input("Unesite broj indeksa: "))
                for student in izabrani_studenti:
                    if izbor_indeksa == int(student["broj_indeksa"]):
                        print(str(student["ime"]) + " " + str(student["prezime"]))
                        izabrani_student = student
                brojac = 0
                for ocene in izabrani_student["ocene"]:
                
                    brojac+=1
                    if int(ocene["sifra_profesora"]) == int(profesor[6]):
                        predmet = predmeti_by_id(ocene["sifra_predmeta"])
                        print(str(brojac) + ". "+  str(predmet[0]) +" " + str(predmet[1]))
                try:
                    izbor_predmeta = int(input("Unesite sifru predmeta: "))
                    predmet = predmeti_by_id(izbor_predmeta)

                    for i in range(len(izabrani_student["ocene"])):
                        if izabrani_student["ocene"][i]["sifra_predmeta"] == izbor_predmeta:
                            izabrani_student["ocene"].pop(i)
                            break
                
                    save_students(listStudents)
                    glavni_meni_profesora(profesor)
                
                except (ValueError,TypeError,KeyError):
                    print("Ne postoji dati predmet")
            except (ValueError,KeyError):
                print("Ne postoji student sa datim indeksom")
    except(KeyError):
        print("Ne postoji student sa datim imenom")

    else:
        print("Niste izabrali ponudjeni predmet")
        glavni_meni_profesora(profesor)


def dodavanjeOcene(ocena, predmet, profesor):
    nova_ocena = {"sifra_predmeta": None,
                "sifra_profesora": None,
                "ocena": None}
    nova_ocena["sifra_predmeta"] = int(predmet[0])
    nova_ocena["sifra_profesora"] = int(profesor[0])
    nova_ocena["ocena"] = int(ocena)
    return nova_ocena

def get_students_by_name(name):
    izabrani = []
    for student in listStudents:
        if name.lower() == student["ime"].lower():
            izabrani.append(student)
    return izabrani

def prosek(profesor):
    try:
        brojac= 1
        for predmeti in listSubjects:
            print(str(brojac) + ". " + str(predmeti[0]) + "; " + str(predmeti[1]) + "\n")
            brojac+=1
        izbor = int(input("Unesite redni broj predmeta: "))
        predmet = listSubjects[izbor-1]
        br_ocena = 0
        ukupna = 0
        prosecna = 0
        nepolozen = True
        for student in listStudents:
            for ocene in student["ocene"]:
                if int(ocene["sifra_predmeta"]) == int(predmet[0]):
                    br_ocena +=1
                    ukupna += int(ocene["ocena"])
                    nepolozen = False
        
        if nepolozen == True:
            print("Predmet nije polozen")
        else:
            prosecna = ukupna/br_ocena
            print("Prosecna ocena je: " + str(prosecna) )
        glavni_meni_profesora(profesor)
    except(IndexError,ValueError,TypeError):
        print("Unesite jednu oda datih ocena")
        glavni_meni_profesora(profesor)
app()




