Superpy

Introduction

The following code is based on a supermarket inventory system to basically buy and sell products and also keeping track with the expiration dates.
At the end you can always use the statistics command to generate a pdf file so you can see the statistics over time.

The modules that are used are:
- Argparse
- CSV
- Pandas
- Matplotlib
- Os
- Datetime


Highlights in the code

The first thing I think that stands out the most are my buy, sell and profit commands.
The reason why is because when a product gets bought it goes into the df_bought.csv file and df_inventory.csv file.
This is because you can later generate a pdf file that compares the sold and bought file.
From here I can easily get the records from a specific date and later on delete some of the files I want to be deleted with the reset_files command to start over.

Another thing about my code is that it adds up the quantity.
If you buy something on 2023-01-01 and the same item on 2023-01-05 the item gets his own row in the df_bought.csv but it adds up in the df_inventory.csv file.
This way you can calculate the profits better. When I buy 10 apples with an expiration date: 2026-02-02 en also buy 10 apples with an expiration date: 2026-09-09 you will see the rows getting made.
The moment you want to sell some of these apples on 2026-05-05 the first 10 apples will be expired but the other apples aren't. It will sell the apples that are within the expiration date.

If a item is expired or you want to sell it after the expiration date the code tells you.
If you use the export code it will also make a csv file for all things that are expired. Further or less it does nothing more with it.

You can also jump into dates with the advance_time command or set an entirley new date. if you want to reset the date to today's date you can simply say setdate --setdate today.

I also want to talk about the last highlight in the code: “reset_files” I made this py file because once you’re done with a file or want to delete a specific csv file you can reset files.
You can also reset all files by the command line: “reset_files all” before you delete something you can make a pdf out of it by using the plot command line.
This way it makes a pdf file you can save somewhere wherever you like.
