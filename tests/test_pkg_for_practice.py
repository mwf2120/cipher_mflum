from pkg_for_practice import pkg_for_practice

def test_cipher_negative_shift():
    example = 'message'
    expected = 'jbppXdb'
    actual = pkg_for_practice.cipher(example, -3)
    assert actual == expected, 'Negative shift not functioning'

test_cipher_negative_shift() 