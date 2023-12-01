import os
import shutil

for day in range(1, 26):
    new_path = f"{os.getcwd()}\\Day {day}"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        shutil.copy("input.txt", f"Day {day}/")
        shutil.copy("second_part.py", f"Day {day}/")
        shutil.copy("first_part.py", f"Day {day}/")
        shutil.copy("small_input.txt", f"Day {day}/")