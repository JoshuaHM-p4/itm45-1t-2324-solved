'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your "inter"mediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    4 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if not letter.isalpha():
        return letter if letter == " " else None

    # Using ASCII values to shift amount
    ascii_offset = 65
    shifted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)

    if not 65 <= ord(shifted_letter) <= 90:  # If the shifted value exceeds the uppercase range
        shifted_letter = chr((ord(shifted_letter) - 65) % 26 + 65)  # Wrap back to uppercase range

    return shifted_letter


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    6 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    shifted_message = ""
    ascii_offset = 65

    for ch in message:
        if ch.isupper():
            ascii_offset = 65
            shifted_ch = chr((ord(ch) - ascii_offset + shift) % 26 + ascii_offset)

            if not 65 <= ord(shifted_ch) <= 90:  # If the shifted value exceeds the uppercase range
                shifed_ch = chr((ord(shifted_ch) - 65) % 26 + ascii_offset)  # Wrap back to uppercase range

            shifted_message += shifted_ch

        elif ch == " ":
            shifted_message += ch

        else:
            pass

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    4 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    if not letter.isalpha():
        return letter if letter == " " else None

    # Translate the letter shit from A to Z to 0 to 25
    shift = ord(letter_shift) - 65

    # Using ASCII values to shift amount
    ascii_offset = 65
    shifted_letter = chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)

    if not 65 <= ord(shifted_letter) <= 90:  # If the shifted value exceeds the uppercase range
        shifted_letter = chr((ord(shifted_letter) - 65) % 26 + 65)  # Wrap back to uppercase range

    return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    6 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    shifted_message = ""
    ascii_offset = 65

    for index, ch in enumerate(message):
        shift = ord(key[index]) - 65

        if ch.isupper():
            ascii_offset = 65
            shifted_ch = chr((ord(ch) - ascii_offset + shift) % 26 + ascii_offset)

            if not 65 <= ord(shifted_ch) <= 90:  # If the shifted value exceeds the uppercase range
                shifed_ch = chr((ord(shifted_ch) - 65) % 26 + ascii_offset)  # Wrap back to uppercase range

            shifted_message += shifted_ch

        elif ch == " ":
            shifted_message += ch

        else:
            pass

    return shifted_message