from alphabet import alphabets

def encrypt(original_text, shift_number):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:
            shift_amount  = alphabets.index(letter) + shift_number
            shift_amount %= len(alphabets)
            cipher_text += alphabets[shift_amount]
        else:
            cipher_text += letter
    return f"Here is the encoded result: {cipher_text}"