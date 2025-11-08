import os

folder = "data"
filename = "example.txt"
filenamenew = "mustdelete.txt"

# Δημιουργία φακέλου αν δεν υπάρχει
os.makedirs(folder, exist_ok=True)

# Πλήρης διαδρομή αρχείου
file_path = os.path.join(folder, filename)
file_path_new = os.path.join(folder, filenamenew)

# Δημιουργία νέου αρχείου και εγγραφή περιεχομένου
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Αυτό είναι ένα νέο αρχείο που δημιουργήθηκε μέσω Python.\n")
    f.write("Η Python καθιστά εύκολη τη διαχείριση αρχείων.\n")

print(f"Το αρχείο '{filename}' δημιουργήθηκε επιτυχώς στον φάκελο '{folder}'.")

with open(file_path_new, "w", encoding="utf-8") as f:
    f.write("Αυτό είναι ένα νέο αρχείο που δημιουργήθηκε μέσω Python.\n")
    f.write("Το αρχείο αυτό θα το διαγράψουμε.\n")


# Προσθήκη νέας γραμμής στο τέλος του αρχείου
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Προστέθηκε νέα γραμμή στο τέλος του αρχείου.\n")


#Χρήση με os.path για μεγαλύτερη ευελιξία
print("Όνομα αρχείου:", os.path.basename(file_path))
print("Φάκελος αρχείου:", os.path.dirname(file_path))
print("Μέγεθος:", os.path.getsize(file_path), "bytes")

