def install_requirements():
    import subprocess

    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])


def configure_data():
    print("Before running setup.py please enter the text to be sent into text.txt and save it\n")

    print("Your API ID : ")
    api_id = input()

    print("Your API HASH : ")
    api_hash = input()

    print("Your Phone Number : ")
    phone_number = input()

    print("Proxy. Write 'n' if you don't want to use proxy, 'y' otherwise:")
    proxy = input()

    scheme = None
    hostname = None
    port = None
    username = None
    proxy_password = None

    if proxy == 'y':
        print('Proxy scheme ("socks4", "socks5" and "http" are supported):')
        scheme = input()

        print('Proxy hostname:')
        hostname = input()

        print('Proxy port:')
        port = input()

        print('Proxy username:')
        username = input()

        print('Proxy password:')
        proxy_password = input()

    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '\delpop')

    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(f"api_id = '{api_id}'\n")
        f.write(f"api_hash = '{api_hash}'\n")
        f.write(f"phone_number = '{phone_number}'\n")
        f.write(f"text = '{text}'\n")
        f.write(f"proxy = '{proxy}'\n")
        f.write(f"scheme = '{scheme}'\n")
        f.write(f"hostname = '{hostname}'\n")
        f.write(f"port = '{port}'\n")
        f.write(f"username = '{username}'\n")
        f.write(f"proxy_password = '{proxy_password}'\n")


if __name__ == '__main__':
    install_requirements()
    configure_data()
