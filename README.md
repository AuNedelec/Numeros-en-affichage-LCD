# Une brève explication de ma solution

La consigne pour la réalisation de ce test technique était la suivante : 


>Écrivez un petit programme qui prend des numéros en entrée et qui les imprime sous format display LCD (la console ou formulaire web). Vous pouvez voir un exemple en dessous.
Vous pouvez le faire dans le langage de programmation de votre choix, de la manière qui vous convient le mieux.
```
   _  _     _  _  _  _  _  
 | _| _||_||_ |_   ||_||_|  
 ||_  _|  | _||_|  ||_| _|
```
J'ai choisi d'utiliser Python, de stocker chaque chiffre et leur représentation LCD dans un dictionnaire et de créer une fonction afin d'afficher la représentation LCD des chiffres en input. J'ai également ajouté une boucle `while`.

## Pourquoi utiliser un dictionnaire ?

Après quelques essais et réflexions, j'ai pensé à utiliser :

* un array 

```python
lcd_digits_list = [
    (" _ ", "| |", "|_|"),  # 0
    (" ", "  |", "  |"),  # 1
    # ... reste des chiffres
]
```

* un dictionnaire avec des chaînes de caractères multilignes
```python
lcd_digits_dictionary = {
    0: " _ \n| |\n|_|",
    1: " \n  |\n  |",
    # ... reste des chiffres
}
```

J'ai choisi d'utiliser un dictionnaire basique pour plus de clarté et de flexibilité.

```python
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
```

## Pourquoi ajouter une boucle `while` ?
```python
while value.lower() != "exit":
    if not value.isdigit():
        print("Désolé, je ne comprends que les nombres et le mot \"exit\". Veuillez réessayer.")
    else:
        display_lcd(value) 
    value = input("Entrez un numéro pour l'afficher au format display LCD. Pour sortir, entrez \"exit\" : ")    
print("Merci et au-revoir !")
```
* Cette dernière permet une interraction continue avec l'utilisateur qui n'a pas besoin de relancer le programme pour entrer un nouvel input. Pour sortir de la boucle, il suffit de taper `exit` dans la console.
De plus, la méthode `.lower()` permet d'éviter les erreurs de format.
```pyhton
while value.lower() != "exit":
```

* Pour éviter un cas d'erreur fréquent, la boucle permet de vérifier que l'input est valide. Dans le cas où l'on entrerait des caractères autres que des chiffres ou le mot `exit`, le programme propose à l'utilisateur d'entrer un nouvel input valide.

```python
if not value.isdigit(): 
        print("Désolé, je ne comprends que les nombres et le mot \"exit\". Veuillez réessayer.")
```
* J'aurais également pu utiliser des expressions régulières à l'intérieur de la boucle, mais j'ai préféré utiliser la méthode `.isdigit()` pour des raisons de simplicité et de lisibilité.

```python
import re

while value.lower() != "exit":
    if not re.match("^\d+$", value):
        print("Désolé, je ne comprends que les nombres et le mot \"exit\". Veuillez réessayer.")
    else:
        display_lcd(value)
```




Je vous remercie pour votre attention, ainsi que pour votre temps ! 
