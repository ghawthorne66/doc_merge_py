# import docx
#
# # Grabs the text list txt file
# with open("Input/Names/invited_names.txt") as guest_list:
#     new_guest_list = guest_list.read()
#
# # Grabs the sample letter
# letter = docx.Document("./Input/Letters/starting_letter.docx")
#
# # Splits the text docs of names into a list containing those names
# list_names = new_guest_list.split("\n")
#
# # Takes the pre-made letter and converts to a string
# new_text = []
#
# for para in letter.paragraphs:
#     new_text.append(para.text)
#
# new_string = '\n'.join(new_text)
#
# for names in list_names:
#     # stripped_name = name.strip()
#     new_letter = new_string.replace("[name]", names)
#     list_of_para = new_letter.split("\n")
#
#     finished_letter = docx.Document()
#
#     for para in list_of_para:
#         finished_letter.add_paragraph(para)
#
#     finished_letter.save(f"./Output/ReadyToSend/{names}_letter.docx")

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
