def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    lowercase = value.lower()
    word = lowercase.replace(' ', '')
    if word[::-1] == word:
        return True
    else:
        return False

