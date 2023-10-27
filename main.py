import itertools

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def line():
    print(Colors.ENDC + "+--------------------------------------------------------------------------------------------------+")

def logo():
    print(Colors.HEADER + " __        __               _   ____                ____  _      ___ ")
    print(" \ \      / /___   _ __  __| | / ___|  ___  _ __   / ___|| |    |_ _|")
    print("  \ \ /\ / // _ \ | '__|/ _` || |  _  / _ \| '_ \ | |    | |     | | ")
    print("   \ V  V /| (_) || |  | (_| || |_| ||  __/| | | || |___ | |___  | | ")
    print("    \_/\_/  \___/ |_|   \__,_| \____| \___||_| |_| \____||_____||___| \n" + Colors.ENDC)
    print(Colors.FAIL + "                                       WordGenCLI v1.0 - by Renan D. " + Colors.ENDC)
                                                                  
def generate_wordlist(characters, min_length, max_length, output_file):
    try:
        with open(f"{output_file}.txt", 'w') as file:
            for length in range(min_length, max_length + 1):
                for word_tuple in itertools.product(characters, repeat=length):
                    word = ''.join(word_tuple)
                    file.write(word + '\n')
    except:
        print(Colors.FAIL + "+ Erro ao gerar wordlist" + Colors.ENDC)

if __name__ == '__main__':
    logo()
    resp = "Y"
    while resp == "Y":
        try:
            line()
            characters = input("+ Digite os caracteres a serem usados na geração da wordlist: " + Colors.WARNING)
            min_length = int(input(Colors.ENDC + "+ Comprimento mínimo da palavra: " + Colors.WARNING))
            max_length = int(input(Colors.ENDC + "+ Comprimento máximo da palavra: " + Colors.WARNING))
            output_file = input(Colors.ENDC + "+ Nome do arquivo de saída: " + Colors.WARNING)
            line()
            print("+ Gerando wordlist...")

            generate_wordlist(characters, min_length, max_length, output_file)
            line()
            print("+ " + Colors.GREEN + f"Wordlist gerada com sucesso e salva em '{output_file}'.txt" + Colors.ENDC)
            
            line()
            resp = input("+ Deseja continuar? [Y/N]: " + Colors.WARNING).upper()
        except ValueError:
            print(Colors.ENDC + "+ " + Colors.FAIL + "Valor inválido" + Colors.ENDC)
