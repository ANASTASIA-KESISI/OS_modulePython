import os

#Επιλέγω τον φάκελο που θέλω να ψάξω το αρχείο μου
os.chdir("C:/Users/Admin/Desktop/Os module/OS_modulePython/DirectoryManagement")
print("Changed directory:", os.getcwd())

# Επιλέγω το αρχείο που θέλω να ελέγξω στον φάκελο
file_path = "DeleteDirectory.py"
# Χρήση της συνάρτησης os.path.exists() για να ελέγξω αν το αρχείο υπάρχει
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File not found.")

