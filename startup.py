from encryption.controller import PlayFairController
cl = PlayFairController()
cl.create_key_table()
while True:
    switch = {
        '1': cl.encrypt,
        '2': cl.decrypt,
        '3': cl.create_key_table
    }
    print('*'*30)
    print('Choose your option:')
    print('1 - Encrypt')
    print('2 - Decrypt')
    print('3 - Change key table')
    print('Any other character - exit')
    option = input()
    option = switch.get(option, None)
    if option is not None:
        option()
    else:
        break
