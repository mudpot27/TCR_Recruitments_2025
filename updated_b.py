from c import random_noise

def star(String):
    return "--*--" + String + "--*--"

def wowify(String):
    return "✨" + String.upper() + "✨"

def invert_case(String):
    return ''.join(character.lower() if character.isupper() else character.upper() for character in String)

def add_noise(String):
    noise = random_noise() #Change was made in this line check description for details
    return noise + String + noise

def echo(String):
    return (String + " ") * 5 

def wrap_in_brackets(String):
    return "[[" + String + "]]"
