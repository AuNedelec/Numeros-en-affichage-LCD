lcd_digits_dictionary = {
   0: (" _ ", "| |", "|_|"),
   1: (" ", "  |", "  |"),
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
   for i in range(3):
       row_display = ""
       for d in input_digits:
           integer_digit = int(d)
           lcd_representation = lcd_digits_dictionary[integer_digit][i]
           row_display += lcd_representation + " "
       print(row_display)

value = input("Entrez un numéro pour l'afficher au format display LCD. Pour sortir, entrez \"exit\" : ")

while value.lower() != "exit":
    if not value.isdigit():
        print("Désolé, je ne comprends que les nombres et le mot \"exit\". Veuillez réessayer.")
    else:
        display_lcd(value)
    value = input("Entrez un numéro pour l'afficher au format display LCD. Pour sortir, entrez \"exit\" : ")
       
print("Merci et au-revoir !")
