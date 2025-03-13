import random as r

words = ["Analise","Java","VS Code","Git hub","Skywalker"]

tips = {"Analise":"Quando você quer ver algo mais afundo, saber mais detalhes",
        "Java":"Uma linguagem de programação",
        "VS Code":"Uma IDE, usada em desenvolvimento web",
        "Git hub":"Uma rede social para programadores",
        "Skywalker":"Sobrenome famoso na trilogia star wars"}

global_score = 0

cartoons = {1:" O \n",
            
            2:" O \n"+
              " | \n",

            3:" O \n"+
              "/| \n",
            
            4:" O \n"+
              "/|\ \n",
            
            5:" O \n"+
              "/|\ \n"+
              "/ \n",
            
            6:" O \n"+
              "/|\ \n"+
              "/ \ \n",}

def choose_option():
    print("Vamos Jogar!\nEscolha um dos tópicos: ")
    option = int(
    input("1 - Aleatorio\n"+
        "2 - Programação\n"+
        "3 - Cultura POP\n"+
        "4 - Sair:\n"))
    
    while option not in range(1,4):
        print("Escolha uma opção de 1 a 3:")
        option = int(
    input("1 - Aleatorio\n"+
        "2 - Programação\n"+
        "3 - Cultura POP\n"+
        "4 - Sair:\n"))
    
    if option == 4:
        return option
    else:
        return option

def get_word(option):
    if option == 1:
        return r.choice(words)
    elif option == 2:
        return r.choice(words[:4])
    else:
        return words[4]
    
def play_again():
    opção = input("Deseja jogar novamente?\nY- Sim\n\nSua opção -> ")
    if opção.upper() == "Y":
        start()

def reveal_letter(word, guessed):
    hidden_letters = [char for idx, char in enumerate(word) if guessed[idx] == "_"]
    if hidden_letters:
        return r.choice(hidden_letters).upper()
    return None

def play(option):
    global cartoons

    word = get_word(option)
    guessed = ["_" if char != " " else " " for char in word]
    attempts = 0
    hints = 3
    used_letters = set()

    print("\nVocê tem 3 dicas e 6 chances!\n")
    
    while attempts < 6 and "_" in guessed:
        print("\nPalavra:", " ".join(guessed))
        print("Letras usadas:", ", ".join(used_letters))

        print(f"Tentativas disponíveis: {6-attempts}")
        print("\nDica:", tips[word])
        print(f"Dicas disponíveis: {hints}")

        auto_reveal = reveal_letter(word, guessed)
        if auto_reveal:
            print(f"\nDica automática! Revelando a letra: {auto_reveal}")
            for idx, char in enumerate(word.upper()):
                if char == auto_reveal:
                    guessed[idx] = word[idx]

        letter = input("\nEscolha uma letra ou digite '*' para usar uma dica -> ").strip().upper()

        if letter == "*":
            if hints > 0:
                hint_letter = reveal_letter(word, guessed)
                if hint_letter:
                    print(f"\nUsando uma dica! Revelando a letra: {hint_letter}")
                    for idx, char in enumerate(word.upper()):
                        if char == hint_letter:
                            guessed[idx] = word[idx]
                    hints -= 1
                else:
                    print("Não há mais letras para revelar!")
            else:
                print("Você não tem mais dicas disponíveis!")
            continue
        
        if not letter.isalpha() or len(letter) != 1:
            print("Digite apenas uma letra válida!")

            attempts += 1
            continue
        
        if letter in used_letters:
            print("Você já tentou essa letra!")
            attempts += 1
            print(cartoons[attempts])
            continue
        
        used_letters.add(letter)
        
        if letter in word.upper():
            for idx, char in enumerate(word.upper()):
                if char == letter:
                    guessed[idx] = word[idx] 
        else:
            attempts += 1
            print("\nErro! Tentativas restantes:", 6 - attempts)
            print(cartoons[attempts])
            continue

        if hints > 0:
            hints -= 1

    if "_" not in guessed:
        print("\nParabéns! Você acertou a palavra:", word)
    else:
        print("\nGame Over! A palavra era:", word)
    
    play_again()

def start():
    print("\nSeja bem-vindo ao jogo da forca!\n")
    while True:
        option = choose_option()
        if option == 4:
            print("Obrigado por jogar! Até mais.")
            break
        play(option)

start()


