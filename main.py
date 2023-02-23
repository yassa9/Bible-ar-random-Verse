
import random 
import subprocess

# The verses.text contains the both old & new testaments
# However, I read from the 1st verse in the new New testament
# So we choose any random number assigned to one verse
verse = random.randint(23145 , 31103)

with open("verses.txt") as file :
	content = tuple(file)[verse]

# We modify the line to make it parsable
content = content.split("\t")[1:-1]
v = content[4] + " ( " + content[0]+" "+content[1] + " : " +  content[2]+ " ) " 

timeout = len(content[4]) // 10
print(timeout)
# width   = 400
# height  = 400
# posx    = 800
# posy    = 100
text    = f"\"{v}\""

command =f"notify-send {text} " 
subprocess.call(command,  shell=True)

# command1 = rf""" yad --timeout {timeout} --skip-taskbar \
# --no-buttons  --width={width} \
# --text-align=center  --text={text} \
# --no-buttons --posx={posx} --posy={posy} \
# >/dev/null  """

# 23145 - 31103
# nums = {"0" : "٠", 	
# "1" : "١" ,	
# "2" : "٢" ,	
# "3" : "٣" ,	
# "4" : "٤" ,	
# "5" : "٥" ,	
# "6" : "٦" ,	
# "7" : "٧" ,	
# "8" : "٨" ,	
# "9" : "٩" }

# for c in v :
# 	if c in nums : 
# 		v = v.replace(c , nums[c])