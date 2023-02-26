from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
    id = int(all_data[-1][0])
    return all_data



def show_all():
    result = read_records()
    if not all_data:
        print("Empty data")
    else:
        print(*result, sep="\n")

def add_new_contact():
    global id
    array = ['surname','name','surname_2','phone_number']
    string = ''
    for i in array:
       string += input(f"enter {i} ") + " "
    id+=1
    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')
    
        

def search_record():
    search_data = exist_contact(0, input("Введите искомую информацию: " ))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Информация не найдена.")

def change_record(data_tuple):
    global all_data
    symbol = "\n"

    rec_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v == rec_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")

def data_collection(num):
    
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name surname_2":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer




def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i]
    else:
        candidates = [i for i in all_data if data in i]

    return candidates

def edit_menu():
    
    add_dict = {"1": "surname", "2": "name", "3": "surname_2", "4": "phone number"}

    show_all()
    rec_id = input("Enter the record id: ")

    if exist_contact(rec_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. surname_2\n"
                           "4. phone number\n"
                           "5. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return rec_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")

def del_contact():

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")
   
def main_menu():
    play = True
    while play:
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete\n"
                       "6. Exit\n")
        match answer:
            case "1":
               show_all()
            case "2":
               add_new_contact()
            case "3":
               search_record()
            case "4":
               work = edit_menu()
               if work:
                    change_record(work)
            case "5":
               del_contact()
            case "6":
               play = False
            case _:
               print("Try again!\n")


main_menu()