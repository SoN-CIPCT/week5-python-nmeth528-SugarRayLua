languages = ["R","python","lua","Mumps","Javascript","BASIC"]
print(languages)
print("The  first two items in the  list are: ",languages[0:2])
print("The middle two items in the list are: ",languages[2:4])
print("The  first and last items in the list are ",languages[0:6:5])
menu = ("tuna","peanut butter","steak","bread","pistachio")
print()
print("Original foods on the menu:")
for food in menu:
    print(food)
revised_menu = list(menu)
revised_menu[2] = "sherbert"
revised_menu[3] = "puffer fish"
print()
print("Revised foods on the menu:")
menu = tuple(revised_menu)
for food in menu:
    print(food)
print()
print("Bon Appetit!")