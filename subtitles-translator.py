# simple application for translate all Disney subtitles (JS filter "seg") 
# from DEutsch to RUssian
# 
# 
import sys
import subprocess

def clear_binary_line(b_line):
    return b_line.decode('utf-8').rstrip()


buffer = ""

for line in sys.stdin:
    prepared_line = line.strip()
    if len(prepared_line)==0:
        continue
    
    remove_marker = prepared_line.find("-->")    
    if remove_marker > 0:
        translation = subprocess.check_output(["trans", "--no-warn", "-source", "de","-target","ru", "-brief", buffer])
        print(buffer, "   ")
        print("```",clear_binary_line(translation),"```")
        print(line[0:remove_marker]+"  \n---")
        buffer = ""
    else:        
        buffer = buffer + " " + prepared_line