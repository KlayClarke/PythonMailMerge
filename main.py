with open('../PythonMailMerge/Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()

print(names_list)

with open('../PythonMailMerge/Input/Letters/starting_letter.txt', mode='r') as file:
    contents = file.read()
    for name in names_list:
        new_letter = contents.replace('[name]', name)
        print(new_letter)



# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
