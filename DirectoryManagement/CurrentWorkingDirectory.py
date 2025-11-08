import os

#1 Εμφανίζει τον τρέχοντα κατάλογο εργασίας
current_dir = os.getcwd()
print("Current directory:", current_dir)
#Εάν θέλουμε να αλλάξουμε τον κατάλογο εργασίας, χρησιμοποιούμε τη συνάρτηση os.chdir(path):
# Αλλάζουμε στον φάκελο "CapstoneProject2"
os.chdir("C:/Users/Admin/Desktop/CapstoneProject2")
print("Changed directory:", os.getcwd())

#2 Λίστα όλων των στοιχείων μέσα στο τρέχον directory
entries = os.listdir(".")
print("Contents:", entries)

# Εμφάνιση μόνο των φακέλων
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
print("Directories:", dirs)

# Εμφάνιση μόνο των αρχείων
files = [f for f in os.listdir(".") if os.path.isfile(f)]
print("Files:", files)
