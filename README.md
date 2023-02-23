# Bible-ar-random-verse
Getting Holy Bible ( New Testament ) random verse within a notification in i3wm

At First, I downloaded the **Bible database** from [WordofGOD](https://wordofgod.in/wog/2022/01/09/download-arabic-bible-database-and-software-modules-for-android-iphone-and-laptop/)

It downloaded with a huge database, choose `AVD` arabic Van Dyke edition.

Then I formatted the `.json` file of whole book verses, turned it into `.txt` file with 3 columns: 
`the verse`, `book name`, `chapter` & `verse number` 

After that, the process of coding python file to read a random line from `23145` ( 1st verse in Matthew book in new testament ) to line `31103` ( obviously the last ) , however you can edit it to `1 ~ 31103` to read both old & new testaments.\
When executing the `main.py` file, output example : 
`"وَلَمَّا قَالَ هَذَا تَقَدَّمَ صَاعِدًا إِلَى أُورُشَلِيمَ. ( لُوقَا ١٩ : ٢٨ ) "
`

I used `notify-send` package in `pacman package manager` to parse the verse in it.

Finally I editied my [i3blocks config file](https://github.com/MateBerg/my_i3wm_i3blocks_configs/blob/main/i3blocks/config) to make the notification pops out when I press on i3blocks desired label
