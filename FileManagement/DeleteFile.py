import os

#Αλλαγή τρέχοντος καταλόγου σε 'data' που δημιουργήθηκε προηγουμένως με το CreateFile.py
os.chdir("C:/Users/Admin/Desktop/Os module/OS_modulePython/data")
file_path = "example.txt"
# Έλεγχος αν το αρχείο υπάρχει
if not os.path.exists(file_path):
    print("Το αρχείο δημιουργήθηκε.")
else:
    print("Το αρχείο υπάρχει ήδη.")
# Μετονομασία αρχείου
os.rename("example.txt", "new_name.txt")
print("Το αρχείο example.txt μετονομάστηκε σε 'new_name.txt'.")

# Διαγραφή αρχείου
os.remove("mustdelete.txt")
print("Το αρχείο 'mustdelete.txt' διαγράφηκε επιτυχώς.")
