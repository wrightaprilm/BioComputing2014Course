#Homework One

For this exercise, you have downloaded a small, but realistic directory structure. You'll find a manuscript folder and an analysis folder, each of which has a back up. The analysis files are phylogenetic trees of a sodium channel we're studying and writing a paper on. We want you to do some exercises, fill in your answers on the instructions.md file (using the text editor your downloaded for this class) and then copy the results into the manuscript folder.

**Answers are in bold**

1. Change directories into the homework directory. Type:

```UNIX
ls -R
```

How does the -R flag modify the function of 'ls'?

**R stands for recursive and lists the contents of all the subdirectories of your working directory.**

Try:

```UNIX
ls -F
```

How has the -F flag modified the behavior of ls?

**I don't know what F _actually_ stands for, but this prints a backslash after the names of directories.**

2. Change into the analysis_files folder, and then into one of the subfolders. How many lines are in the tree file in the subfolder?

**4, obtained with wc -l.**

How many words are in the tree file? Is anything surprising about this? How do you think wc is deciding where a word ends?

**228. Words are delimited on white space.**

3. Change back into the analysis_files folder. Let's say we wanted to run some advanced statistics on these trees, but our analytical software can only accept trees from one file at a time. Concatenate the trees into one text file programmatically. Paste the command you used below.

```UNIX
cat tree*/tree*.txt >> all_trees
```

4. Change directories into the hw_1 directory. Is the analysis_files directory identical to the analysis_backup anymore?

**No. Now we have a new file called "all_trees" that is not backed up.**

Copy files to the backup as necessary to make them identical.

5. Copy this homework file into the directory manuscript_files. Also copy your concatenated tree file into that directory. 

6. Create a file called 'works_cited.txt'. In a text editor, or nano, write in it "Ben and April, pers. comm."

```UNIX
touch works_cited.txt
nano works_cited.txt
```

**or**

```UNIX
nano works_cited.txt
```

**or**

```UNIX
touch works_cited.txt
```

**followed by opening the document in a text editor.**

7. Copy all three of these files simultaneously into manuscript_backup.


```UNIX
cp * ../manuscript_backup
```

8. One last thing. Type:

```UNIX
history
```

And paste the results into this document. Update your backup as needed.

**Answers will vary, depending on how long you bashed around for. There no wrong answer.**

Submitting the homework:

Email to bliebeskind@austin.utexas.edu and wright.aprilm@utexas.edu. In the email: include the whole hw_1 directory so we can see all your answers and the output files of your work. We'll post a key and the best student responses to the Wiki and GitHub.



