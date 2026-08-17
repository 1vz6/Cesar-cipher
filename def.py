from logo import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print(logo)

while True:

    direction = input(
        "Digite 'encode' se quiser criptografar, "
        "digite 'decode' para descriptografar\n"
    ).lower()

    text = input("Digite sua mensagem:\n").lower()
    shift = int(input("Digite o numero de deslocamento:\n"))

    def cesar(text_original, shift_amount):

        og = ""

        if direction == "decode":
            shift_amount *= -1

        for letter in text_original:
            if letter == " ":
                og += " "
            else:
                position = alphabet.index(letter)
                new_position = (position + shift_amount) % len(alphabet)
                og += alphabet[new_position]

        print(
            f"Decodificada: {og}"
            if direction == "decode"
            else f"Codificada: {og}"
        )

    cesar(text, shift)

    continuar = input("Deseja continuar? Digite 'sim' ou 'nao': ").lower()

    if continuar != "sim":
        print("Programa encerrado.")
        break 