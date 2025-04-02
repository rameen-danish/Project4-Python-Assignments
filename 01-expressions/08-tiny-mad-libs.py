#Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
sentence_start : str = "Panaversity is fun. I learned to program and used Python to make my "
adjective : str = input("Enter an adjective: ")
noun : str = input("Enter a noun: ")
verb : str = input("Enter a verb: ")
print(sentence_start + adjective + " " + noun + " "+ verb + "!")