# Bible-ar-random-verse
Getting Holy Bible ( New Testament ) random verse within a notification in i3wm

Verses full text is got by **Bible database** from [WordofGOD](https://wordofgod.in/wog/2022/01/09/download-arabic-bible-database-and-software-modules-for-android-iphone-and-laptop/)

It downloaded with a huge database, choose `AVD` arabic Van Dyke edition.

Then the downloaded `.json` file is formatted into `.txt` file with 3 columns: 
`the verse`, `book name`, `chapter` & `verse number` 

After that, the process of coding python file to read a random line from `23145` ( 1st verse in Matthew book in new testament ) to line `31103` ( obviously the last ) , however you can edit it to `1 ~ 31103` to read both old & new testaments.

Also the python script when  called, it writes the verse number into `CSV` file, and then being ordered in `verseord.csv` file so you can trace most randomly viewed verses.

I used `notify-send` package in `pacman package manager` to parse the verse in it, calculated timeout of the notification based on length of the verse, you can freely adjust it.

Finally I editied my [i3blocks config file](https://github.com/MateBerg/my_i3wm_i3blocks_configs/blob/main/i3blocks/config) to make the notification pops out when I press on i3blocks desired label by adding:
 ```
 [separator]
[name]
command=echo "Random Verse"; i3-msg exec python3 [YOUR_PATH]/main.py
interval=once
 ```
 Notification example: \
![image](https://user-images.githubusercontent.com/69548206/226843020-cf3c20cf-0e4c-4f7e-9f6d-d5ade0feb18a.png)

 
 
