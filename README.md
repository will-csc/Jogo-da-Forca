# Forca Game

Este é um simples jogo de Forca onde você pode escolher entre três opções de categorias de palavras: Aleatório, Programação e Cultura Pop. O objetivo do jogo é adivinhar a palavra correta antes de esgotar o número de tentativas.

Imagem Ilustrativa
![image](https://github.com/user-attachments/assets/04f84759-fed8-4173-b2f9-be398d031974)

## Como Jogar

1. **Escolha uma categoria**: No início do jogo, você será solicitado a escolher uma categoria para a palavra que deseja adivinhar:
    - **1** - Aleatório
    - **2** - Programação
    - **3** - Cultura POP
    - **4** - Sair (Encerra o jogo)

2. **Adivinhe as letras**: O jogo irá mostrar uma palavra com as letras ocultas e você precisará adivinhar uma letra por vez. Caso deseje, você pode usar dicas.

3. **Tentativas e Dicas**:
    - Você tem **6 tentativas** para adivinhar a palavra.
    - São oferecidas **3 dicas** no início do jogo.
    - Você pode usar a dica a qualquer momento digitando o asterisco `*`, que revelará uma letra da palavra.

4. **Figura de erro**: Cada erro que você comete vai adicionar um segmento a um boneco da forca, até que ele esteja completo após 6 tentativas.

Boneco no terminal:

![image](https://github.com/user-attachments/assets/23032ebe-e039-412c-8ee0-b1af01caf2e2)

5. **Vencer ou Perder**: O jogo termina quando você adivinha a palavra corretamente ou quando o boneco é completado (seus erros atingem 6 tentativas).

6. **Jogar Novamente**: Ao final de cada partida, você pode escolher se deseja jogar novamente.

## Funções

- `choose_option()`: Solicita ao jogador a escolha da categoria.
- `get_word(option)`: Retorna a palavra a ser adivinhada com base na categoria escolhida.
- `reveal_letter(word, guessed)`: Revela uma letra da palavra que ainda não foi adivinhada.
- `play(option)`: Controla a lógica principal do jogo, incluindo tentativas, dicas e erros.
- `play_again()`: Pergunta se o jogador deseja jogar novamente após o fim do jogo.
- `start()`: Inicializa o jogo e solicita ao jogador que escolha uma categoria.


