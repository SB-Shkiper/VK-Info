import webbrowser

def main():
    print('#Enter the id in format:"111111111" or "exit" to leave')
    print('#id you can get with services like "https://regvk.com/id/"')
    id = input('>>>')
    if id == 'exit':
        exit()
    else:
        webbrowser.open(f'https://onli-vk.ru/pivatfriends.php?id={id}')
        webbrowser.open_new_tab(f'https://topdb.ru/id{id}')
        webbrowser.open_new_tab(f'https://poiski.pro/vk/user/id{id}')
        webbrowser.open_new_tab(f'https://looka.one/vk_user/id{id}')
        webbrowser.open_new_tab(f'https://onli-vk.ru/id{id}')
        webbrowser.open_new_tab(f'https://vk.com/foaf.php?id={id}')

    menu()

def menu():
    print('1. Back' '\n2. Exit')
    i = input('>>>')
    if i == '1':
        return main()
    else:
        exit()

main()
