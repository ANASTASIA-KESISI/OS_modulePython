import os 

# Δημιουργεί έναν νέο φάκελο
os.mkdir("new_folder")

# Δημιουργεί μια ιεραρχία φακέλων (εάν δεν υπάρχουν)
os.makedirs("project/data/raw", exist_ok=True)
