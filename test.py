with open('/Users/rahul/Downloads/log.txt') as file:
    data = file.readlines()
    for line in reversed(data):
        if 'POST /addUser/' in line:
            links = line.split('/')[2]
            adduser_link = links.split(' ')[0]
            print(f'http://192.168.1.100:3000/{adduser_link}')
            break