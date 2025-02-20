from alphabet import alphabets

def decrypt(original_text, shift_number):
    decoded_text = ""
    for letter in original_text:
        if letter in alphabets:
            shift_amount  = alphabets.index(letter) + (shift_number *-1)
            shift_amount %= len(alphabets)
            decoded_text += alphabets[shift_amount]
        else:
            decoded_text += letter
    return f"Here is the decoded result: {decoded_text}"