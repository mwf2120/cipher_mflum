def cipher(text, shift, encrypt=True):


    """
    Function that replaces a given letter by a given number of positions forward or backward in the alphabet.
    Parameters:
    ----------
    text: str
        A string of text for encryption or decryption. 
    shift: int
        An integer indicating the digit(s) and directionality (- or +) of encryption/decryption.  
    encrypt: boolean
        A boolean value indicating either True (encrypt) or False (decrypt).
    Returns:
    -------
    new_text: str
    The encrypted or decrypted string. 
    
    Example:
    --------
    >>> from cipher_mwf2120 import cipher_mwf2120
    >>> a = 'c' 
    >>> b = -1
    >>> cipher_mwf2120.cipher(a, b)
    b  
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
