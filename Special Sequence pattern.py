import re

def demonstrate_special_sequence():
    sample_text = """
    The quick fox jumps over the lazy dog.
    foxes are wild animal.the dog quickly ran away.
    my email is meghajaiswal1437@gtmail.com.
    my phone number is - 9770500749
    visit us at meghajaiswal1437.www.
    """


# \d Matches any digit (0-9)

    digit_pattern = r'\d+'
    print(f"Digits (\\d) pattern '{{digit_pattern}}':", re.findall(digit_pattern, sample_text))
    print("*****************************::::::::*************************")
 
    #\D -- for non digit character
    non_digit_pattern = r'\D+'
    print(f"Non digit (\\D) pattern: '{non_digit_pattern}':", re.findall(non_digit_pattern, sample_text))
    print("*********************...............******************")

    # \w - match word character (alphanumeric + underscore)
    word_char_ptrn  = r'\w+'
    print(F"word char (\\w) pattern,{word_char_ptrn}:-", re.findall(word_char_ptrn,sample_text))
    print("*********************...............******************")

    #\W non word character
    nonWord_char_ptrn = r'\W+'
    print(F"Non word char (\\W) pattern {nonWord_char_ptrn}:",re.findall(nonWord_char_ptrn, sample_text))

    #\s- matches whitespace char (space, tabs, newline)
    whitespace_pattern = r'\s+'
    print(f"whitespace character (\\s) pattern-- {whitespace_pattern}:",re.findall(whitespace_pattern,sample_text))


    #\S - match Non whitespace char
    non_whiteSpace_pattern = r'\S+'
    print(F"Non whitespace (\\d)-- {non_whiteSpace_pattern}:", re.findall(non_whiteSpace_pattern, sample_text))

    #\b - match word boundary
    word_boundary_pattern = r'\bwild animal\b'
    print(F"word boundary (\\b) pattern-- {word_boundary_pattern}:", re.findall(word_boundary_pattern, sample_text))











def main():
    demonstrate_special_sequence()

if __name__ == '__main__':
    main()