def is_anagram(first_text: str, second_text: str) -> bool:
    first_text = sorted(first_text)
    second_text = sorted(second_text)
    return first_text == second_text