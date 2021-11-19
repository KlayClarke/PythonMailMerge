with open('../PythonMailMerge/Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()

with open('../PythonMailMerge/Input/Letters/starting_letter.txt', mode='r') as file:
    contents = file.read()
    for name in names_list:
        name_strip = name.strip()
        new_text_content = contents.replace('[name]', name_strip)
        with open(f'/Users/klayclarke/Desktop/python/PythonMailMerge/Output/ReadyToSend/{name}.txt', mode='w') \
                as new_letter:
            new_letter.write(new_text_content)
