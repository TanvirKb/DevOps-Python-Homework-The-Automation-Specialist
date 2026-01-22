import os
import shutil

original_file = "app.log"

if os.path.exists(original_file):
    for i in range(1, 6):
        new_file = f"app_{i}.log"
        shutil.copyfile(original_file, new_file)
        print(f"Created {new_file}")
else:
    print(f"{original_file} not found.")
