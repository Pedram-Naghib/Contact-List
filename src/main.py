def read():
    with open('contacts.txt', 'r') as f:
        data = f.readline()
        if not data:
            print('Your contact list is clear!')
        while data:
            print(data, end='')
            data = f.readline()


def find():
    name = input("Enter your contact's name here: ")
    with open('contacts.txt', 'r') as f:
        data = f.readline()
        contacts = {}
        while data:
            name_, number = data.split(':')
            if name_ == name:
                contacts[name] = number.strip()
            data = f.readline()
        if not contacts:
            print('No saved information about this contact')
            return
        for i in contacts:
            print(f'{i}: {contacts[i]}')
        

def add():
    data = []
    ans = None
    while not ans:
        data.append([input('name: '), input('number: ')])
        ans = input("Type 'y' if you are done or nothing if you want to add more: ")
    with open('contacts.txt', 'a') as f:
        for i in data:
            name, number = i
            f.write(f'{name}: {number}\n')
            
def delete():
    name = input('Enter the contact name you want to delete: ')
    lines = []
    with open('contacts.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            name_, _ = line.split(':')
            if name_.strip() != name:
                lines.append(line)
    with open('contacts.txt', 'w') as f:
        for line in lines:
            f.write(line)
    print(f"'{name}' got deleted from your contacts!")

            
def clear():
    with open('contacts.txt', 'w'):
        pass
    

def file_verify():
    try:
        open('contacts.txt', 'r')
    except FileNotFoundError:
        open('contacts.txt', 'w')


if __name__ == '__main__':
    file_verify()
    comm = input('read/find/add/del/clear: ')
    comms = {'read': read, 'add': add, 'find': find, 'clear': clear, 'del': delete}
    while True:
        comms[comm]()
        comm = input('\nread/add/del/clear: ')
