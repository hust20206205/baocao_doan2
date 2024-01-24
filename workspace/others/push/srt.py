import os
import glob


folder = r"C:\Users\vvn20206205\Documents\_1DDD\vn"


sub_files = glob.glob(os.path.join(folder, f'**/*.srt'), recursive=True)
contents = ""
for i in sub_files:
    with open(i, mode="r",  encoding='utf-8') as f:
        contents += f"<!--@ {os.path.basename(i)} -->\n\n"
        contents += f.read()
    with open("_output.md", mode="w",  encoding='utf-8') as output:
        output.write(contents)
