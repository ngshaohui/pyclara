"""
Caesar Cipher

The Caesar Cipher is a rotational cipher to obfuscate a message

Write a program that generates the cipher text according to a given plaintext and number of rotations

The plaintext is a string containing 0 or many characters, and the number of rotations is an integer

We will preserve the case sensitivity of the plaintext and spaces within it

Examples

If the plaintext is "Hello world", positions is 6
The encrypted text is "Nkrru cuxrj"

If the plaintext is "zebra", positions is 2
The encrypted text is "bgdtc"
"""


def rotate_ch(ch: str, rotations: int) -> str:
    """
    rotates a character by its given displacement
    a, 1 -> b
    a, 2 -> c
    z, 1 -> a
    """
    # preserve spaces
    if ch.isspace():
        return ch

    ord_val = ord(ch)
    base_val = ord("A") if ch.isupper() else ord("a")

    return chr((ord_val + rotations - base_val) % 26 + base_val)


def encrypt_text(plaintext: str, rotations: int) -> str:
    "encrypts a plaintext with the caesar cipher"
    # Iterate through each character in the plaintext
    ls: list[str] = []
    for ch in plaintext:
        ls.append(rotate_ch(ch, rotations))
    return "".join(ls)


def main():
    print(encrypt_text("zebra", 2))


if __name__ == "__main__":
    main()
