import os

#Αλλαγή τρέχοντος καταλόγου σε 'data' που δημιουργήθηκε προηγουμένως με το CreateFile.py
os.chdir("C:/Users/Admin/Desktop/Os module/OS_modulePython/data")


filename = "example.txt"
# Διαχωρισμός ονόματος αρχείου και επέκτασης
name, ext = os.path.splitext(filename)
print("Name:", name)
print("Extension:", ext)
