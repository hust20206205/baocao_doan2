from modules.Convert import Convert
import os
import shutil
import pyperclip
import re
# nhận văn bản
input = pyperclip.paste()
match = re.search(r'\{([^}]+)\}', input)
if match:
    input = match.group(1)
else:
    print("No match found.")
print(input)
input = input.replace("%", "")
input = input.replace("(", "")
input = input.replace(")", "")
input = input.replace("{", "")
input = input.replace("}", "")
input = input.replace("/", "")
input = input.replace("-", "")
input = input.replace("_", " ")
while "  " in input:
    input = input.replace("  ", " ")
# print(input)
output = Convert.VarSnakeCase(input)
#####################
# chapter="p0_"
# chapter="p001_"
# chapter="p1_hddt_"
# chapter="p2_msa_"
chapter="p3_ddd_"
#####################
# sao chép file
ten_file_nguon  = os.path.join("../../../baocao/contents", f"_a.tex")
ten_file_dich = os.path.join( "../../../baocao/contents", f"{chapter}{output}"+".tex")
shutil.copy(ten_file_nguon, ten_file_dich)
# dọn file
with open(ten_file_nguon, 'w') as file:
    file.write('')
# return văn bản
output = "\n\\input{contents/" +  f"{chapter}{output}" + "}\n\n\n\n\n\n\n\n\n\n\n\n" 
#####################
# output += "% \\chapter{xxxxxxx}\n\n\n\n" 
# output += "% \\section{xxxxxxx}\n\n\n\n" 
# output += "% \\subsection{xxxxxxx}\n\n\n\n" 
# output += "% \\subsubsection{xxxxxxx}\n\n\n\n" 
# output += "% \\paragraph{xxxxxxx}\n\n\n\n" 
# output += "% \\subparagraph{xxxxxxx}\n\n\n\n" 
#####################
# output += "% \\input{contents/_a}\n\n\n\n" 
pyperclip.copy(output)
import pyautogui
pyautogui.hotkey('alt', '2')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'j')