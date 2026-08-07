def _normalise(text: str) -> str:
    return "".join(character for character in text.casefold() if character.isalnum())

def is_anagram(first_text: str, second_text: str) -> bool:
    first_text = sorted(_normalise(first_text))
    second_text = sorted(_normalise(second_text))
    return first_text == second_text