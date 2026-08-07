from anagram import is_anagram

def main() -> None:
    print("Welcome to an Anagram Detector")

    first_text = input("Please input your first text: ")
    second_text = input("Please input your second text: ")

    if(is_anagram(first_text, second_text) == True):
        print(f"{first_text} and {second_text} are anagrams")
    else:
        print(f"{first_text} and {second_text} are not anagrams")

if __name__ == "__main__":
    main()