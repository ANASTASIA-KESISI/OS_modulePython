"""
File Organizer Project
----------------------
A Python script that organizes files in a directory based on their file extension using the 'os' module.
"""
import os

# Ορισμός φακέλου προέλευσης (όπου βρίσκονται τα αρχεία)
source_dir = "C:/Users/Admin/Desktop/Downloads" 

# Αντιστοίχιση τύπων αρχείων με φακέλους
file_types = {
    "Εικόνες": [".jpg", ".jpeg", ".png", ".gif"],
    "Έγγραφα": [".pdf", ".docx", ".txt", ".pptx"],
    "Βίντεο": [".mp4", ".mov", ".avi"],
    "Ήχος": [".mp3", ".wav"],
    "Συμπιεσμένα": [".zip", ".rar", ".tar"]
}

# Έλεγχος αν υπάρχει ο φάκελος προέλευσης=
if not os.path.exists(source_dir):
    print(f"Ο φάκελος '{source_dir}' δεν βρέθηκε.")
    exit()

# Επανάληψη για κάθε στοιχείο του φακέλου
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # Αν είναι φάκελος, τον παραλείπουμε
    if os.path.isdir(file_path):
        continue

    # Εξαγωγή επέκτασης αρχείου
    _, ext = os.path.splitext(filename)
    ext = ext.lower()  # για σιγουριά ότι είναι μικρά γράμματα (.JPG → .jpg)

    # Έλεγχος αν το αρχείο ανήκει σε κάποια κατηγορία
    moved = False
    for folder, extensions in file_types.items():
        if ext in extensions:
            target_folder = os.path.join(source_dir, folder)
            os.makedirs(target_folder, exist_ok=True)  # Δημιουργία φακέλου αν δεν υπάρχει

            # Νέα διαδρομή αρχείου
            new_path = os.path.join(target_folder, filename)

            # Μετακίνηση αρχείου (os.rename = "μετονομασία/μετακίνηση")
            try:
                os.rename(file_path, new_path)
                print(f"Μετακινήθηκε: {filename} → {folder}/")
                moved = True
            except PermissionError:
                print(f"Δεν επιτρέπεται η μετακίνηση του αρχείου: {filename}")
            break

    # Αν δεν βρέθηκε αντιστοίχιση επέκτασης
    if not moved:
        other_folder = os.path.join(source_dir, "Λοιπά")
        os.makedirs(other_folder, exist_ok=True)
        try:
            os.rename(file_path, os.path.join(other_folder, filename))
            print(f"Μετακινήθηκε: {filename} → Λοιπά/")
        except PermissionError:
            print(f"Δεν επιτρέπεται η μετακίνηση του αρχείου: {filename}")
