import math
lcd_digits_dictionary = {
    0: (" _ ", "| |", "|_|"),
    1: ("   ", " | ", " | "),  
    2: (" _ ", " _|", "|_ "),
    3: (" _ ", " _|", " _|"),
    4: ("   ", "|_|", "  |"),
    5: (" _ ", "|_ ", " _|"),
    6: (" _ ", "|_ ", "|_|"),
    7: (" _ ", "  |", "  |"),
    8: (" _ ", "|_|", "|_|"),
    9: (" _ ", "|_|", "  |")
}
def display_lcd(input_digits):
    digits_per_page = 10
    num_digits = len(input_digits)
    num_pages = math.ceil(num_digits / digits_per_page)

    for page in range(num_pages):
        start_index = page * digits_per_page
        end_index = start_index + digits_per_page
        if end_index > num_digits:
            end_index = num_digits
        page_digits = input_digits[start_index:end_index]

        for i in range(3):
            row_display = ""
            for d in page_digits:
                integer_digit = int(d)
                lcd_representation = lcd_digits_dictionary[integer_digit][i]
                row_display += lcd_representation + " "
            print(row_display)

value = input("Entrez un numéro pour l'afficher au format display LCD. Pour sortir, entrez \"exit\" : ")

while value.lower() != "exit":
    if not value.isdigit():
        print("Désolé, je ne comprends que les nombres et le mot \"exit\". Veuillez réessayer.")
    else:
        display_lcd(value)  # Pass the input_digits variable as an argument
    value = input("Entrez un numéro pour l'afficher au format display LCD. Pour sortir, entrez \"exit\" : ")
       
print("Merci et au-revoir !")