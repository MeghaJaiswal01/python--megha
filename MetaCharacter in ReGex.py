import re

def demontrate_metacharacters():

    sample_text = """the quick fox jumps over the lazy dog.
    foxes are wild animal. the dog quickly ran away.
    my email is meghajaiswal1437@gtmail.com.
    my phone n umber is - 9770500749
    """

    
    # (.)
    dot_pattern = r'the.quick'
    print(f"dot (.) pattern '{{dot_pattern}}':",re.findall(dot_pattern, sample_text))


    #caret (^) and dollar($)
    caret_pattern = r'^the'
    dollar_pattern = r'dog.$'
    print(F"start of string (^) pattern {{caret_pattern}}:" , re.match(caret_pattern,sample_text))
    print(F"end of string ($) pattern {{caret_pattern}}:" , re.match(sample_text,dollar_pattern))

    #ASterisk (*) and (+):--
    Asterisk_pattern = r'foxes*'
    print("Asterisk (*) {{Asterisk_pattern}}:", re.findall(Asterisk_pattern,sample_text))

    plus_pattern = r'fox+'
    print(F"plus(+) pattern {{plus_pattrn}} :", re.findall(plus_pattern, sample_text))

    #@Question mark(?)
    question_pattern = r'fox?'
    print(F"Question Mark (?) pattern {{question_pattern}}:",re.findall(question_pattern,sample_text) )

    #braces({})
    braces_pattern = r'97{2}'
    print(f"braces  ({{}}) pattern {{braces_pattern}}:", re.findall(braces_pattern,sample_text))

    #square brackets([])
    square_brackets_pattern = r'[Ff]ox'
    print(F"Square brackets ([]) pattern {{square_brackets_pattern}}:", re.findall(square_brackets_pattern, sample_text))

    pipe_pattern = r'fox|dog'
    print(F"pipe (|) pattern '{{pipe_pattern}}:", re.findall(pipe_pattern,sample_text))



    #Escaped character and special sequences

    emial_pattern = r'\b\w+\.\w+\b'
    print(F"Email pattern {{email_pattern}}:", re.findall(emial_pattern, sample_text))

    phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
    print(f"phone pattern  {{phone_pattern}}:", re.findall(phone_pattern,sample_text))



def main():
    demontrate_metacharacters()

if __name__ == "__main__":
     main()