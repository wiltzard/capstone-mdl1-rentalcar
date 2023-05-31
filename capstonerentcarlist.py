from tabulate import tabulate
import datetime

listMobil = [['TOYOTA ALL NEW AVANZA', 'Mini MPV', 4, 382500],
             ['DAIHATSU XENIA', 'Mini MPV', 5, 490000],
             ['SUZUKI ERTIGA', 'Mini MPV', 5, 539000],
             ['TOYOTA INNOVA REBORN', 'Compact MPV', 4, 735000],
             ['TOYOTA FORTUNER', 'SUV', 3, 1176000],
             ['TOYOTA ALPHARD', 'Minivan', 3, 1470000]]
#READ
def carlist() :
    print('RENT CAR LIST\n')
    print(tabulate(listMobil, headers=["Car","Car Type", "Unit", "Cost per Days"]))


def searchcarname() :
    car = input("Car Name : ")
    exist = False
    Mobil = []
            
    for Mobil in listMobil:
        if Mobil[0] == car:
            exist = True
            data = Mobil
        
    if exist:
        print(f"We Have That Car : {car}")
        print(f"Car: {data[0]}, Car Type: {data[1]}, Unit: {data[2]}, Cost Per Day: {data[3]}")
    else:
        print("We Don't Have That Car")

# UPDATE
# hanya mengubah unit dan cost per day karena jika ingin mengubah nama mobil serta tipe mobil lebih baik menambahkan data baru dan menghapus data yang tidak diperlukan
def editcarlist() :
    car = input("Car Name : ")
    exist = False
    index = 0
    i = 0
    for Mobil in listMobil:
        if Mobil[0] == car:
            exist = True
            index = i
            break
        i = i + 1
            
    if exist:
        data = listMobil[index]
        print(f"Car: {data[0]}, Car Type: {data[1]}, Unit: {data[2]}, Cost Per Day: {data[3]}")
        while(True):
            confirm = input("Input Y if you want to change the data or N to cancel (Y/N): ")
            if confirm == "Y":
                column = input("What data do you want to change: ")
                if column == "Unit":
                    newunit = input("Input Unit: ")
                    while(True):
                        confirm2 = input("Do you want to update? (Y/N): ")
                        if confirm2 == "Y":
                            listMobil[index][2] = newunit
                            print("Data has been updated")
                            carlist()
                            break
                        elif confirm2 == "N":
                            print("CANCELED")
                            break
                        else:
                            print("Only Input Y/N")
                            pass
                    break
                elif column == "Cost Per Day":
                    newcostperday = input("Input Cost Per Day: ")
                    while(True):
                        confirm2 = input("Do you want to update? (Y/N): ")
                        if confirm2 == "Y":
                            listMobil[index][3] = newcostperday
                            print("Data has been updated")
                            carlist()
                            break
                        elif confirm2 == "N":
                            print("CANCELED")
                            break
                        else:
                            print("Only Input Y/N")
                            pass
                    break
                else:
                    print("Only Input Unit Or Cost Per Day")
                    break
            if confirm == "N":
                print("CANCELED")
                break
            else:
                print("Only Input Y/N")
                pass
    else:
        print("The Data You Are Looking For Does Not Exist \n")
        menu()

# CREATE
def addnewcar() :
    carname = input("Input Car Name : ")
    exist = False

    for Mobil in listMobil:
        if Mobil[0] == carname:
            exist = True
            
    if exist:
        print("Data Already Exist")
    else:
        cartype = input("Input Car Type: ")
        unit = input("Input Unit: ")
        costperday = input("Input Cost Per Day: ")

        while(True):
            konfirmasi = input("Save Data? (Y/N) : ")

            if konfirmasi == "Y":
                Mobil = [carname, cartype, unit, costperday]
                listMobil.append(Mobil)
                print("Data Successfully Saved")
                carlist()
                break    
            if konfirmasi == "N":
                print("CANCELED")
                break
            else:
                print("Only Input Y/N")
                pass

# DELETE
def removecar():
    carname = input("Input Car Name: ")
    exist = False
    index = 0
    i = 0
    for Mobil in listMobil:
        if Mobil[0] == carname:
            exist = True
            index = i
            break
        i = i + 1
            
    if exist:
        while(True):
            confirm = input("Are you sure to delete this data? (Y/N): ")
            if confirm == "Y":
                listMobil.pop(index)
                print("Data Successfully Deleted")
                carlist()
                break
            if confirm == "N":
                print("CANCELED")
                break
            else:
                print("Only Input Y/N")
                pass
    else:
        print("The Data You Are Looking For Does Not Exist \n")
    
def menu():
    while True:
        menu = input('''
        RENT CAR BY WILT
        1. Car List
        2. Search Car
        3. Add New Car
        4. Edit Car List
        5. Remove Car
        6. Exit
        Masukkan nomor menu yang ingin di akses : ''')
        if (menu == '1'):
            carlist()
        elif (menu == '2'):
            searchcarname()
        elif (menu == '3'):
            addnewcar ()
        elif (menu == '4'):
            editcarlist()
        elif (menu == '5'):
            removecar()
        elif (menu == '6'):
            mainmenu()
        else:
            print("Input a right number!!!")


def login() :
    while True:
        print("LOGIN\n")
        print("Input Your Username and Password")
        username = "Wilt"
        password = "gta123"
        name = input("Input Username: ")
        mypass = input("Input password: ")
        if (name == username and mypass == password):
            print("Login Successful")
            menu()
        else:
            print("Wrong Username and Password")
            break
    

def mainmenu() :
    while True:
        time = datetime.datetime.now()
        print('=====================================')
        print('|      RENT CAR WILTZARD LIST       |')
        print('=====================================')
        print('|    {}     |'.format(time))
        print('|                                   |')
        print('|      1. Login | 2. Exit           |')
        print('|                                   |')
        print('=====================================')

        choice = input("Input mainmenu number you want to access = ")
        if (choice == '1'):
            login()
        elif (choice == '2'):
            print("GOODBYE")
            break
        else:
            print("Input a right number!!!")
            break

mainmenu()