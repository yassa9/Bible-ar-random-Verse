import random 
import subprocess
import time 
import csv
import arabic_reshaper
from bidi.algorithm import get_display


# The verses.text contains the both old & new testaments
# However, I read from the 1st verse in the new New testament
# So we choose any random number assigned to one verse
verse_rand = random.randint(23145 , 31103)
##################### verse(00000 , 07958)
verse = verse_rand-23145

# Define the path to the CSV file
# If it gave a error, use the full path in your machine
csv_path = "verse_stats.csv"

with open("verses.txt") as file :
    content = tuple(file)[verse_rand]

# We modify the line to make it parsable
content = content.split("\t")[1:-1]
shahed = "✝️  " + content[0]+" "+content[1] + " : " +  content[2]
v = " "+ content[4] + "\n" + shahed   

text = f"\"{v}\""
shahed_num = f"\"{shahed}\""

# Write verse number to CSV file
with open(csv_path, mode='a', newline='') as csv_file:
	
    writer = csv.writer(csv_file)
    writer.writerow([verse])

input_file = '/home/yassa/.scripts/bible/verse_stats.csv'
output_file = '/home/yassa/.scripts/bible/verses_order.csv'

# read input CSV file into a list
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    input_list = list(reader)

# create a dictionary to count the occurrences of each number
counts = {}
for row in input_list:
    num = int(row[0])
    counts[num] = counts.get(num, 0) + 1

# write the results to the output CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for num, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        writer.writerow([f'{num} ({count})'])    

# Define a mapping of English digits to Arabic (Indian) digits
digits_map = {
    '0': '٠',
    '1': '١',
    '2': '٢',
    '3': '٣',
    '4': '٤',
    '5': '٥',
    '6': '٦',
    '7': '٧',
    '8': '٨',
    '9': '٩'
}

# Convert the number to a string and replace English digits with Arabic digits
arabic_num = ''.join(digits_map.get(d, d) for d in str(verse))

# Reshape the Arabic string
reshaped_num = arabic_reshaper.reshape(arabic_num)

# Display the reshaped Arabic string with proper formatting
display_num = get_display(reshaped_num)
print(display_num)

# Calculate the timeout for the notification, based on lenth of the verse
timeout = int(len(content[4]) / 18)
print(timeout)

command = f"notify-send {text} {display_num} -t {timeout*1000}"
subprocess.call(command,  shell=True)

##################################



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
#   if c in nums : 
#       v = v.replace(c , nums[c])
