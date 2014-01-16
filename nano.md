#Install Instructions for Nano

Nano is a lightweight, programmatic text editor accessed from the command line. At some points during the semester, we will ask you to write to a text file using nano. Git Bash does not come with nano natively, so here are instructions for installing it

In your git bash window, copy and paste the following:

```UNIX
curl -L -O http://www.nano-editor.org/dist/v2.2/NT/nano-2.2.6.zip
```

This will download nano. Next, find the downloaded file in your downloads. In the git bash window, type:

```UNIX
unzip
```

Then, drag and drop the downloaded file into the window. Finally, follow the filename with the following command:

```UNIX
-d nano
```

The whole string should look like:

```UNIX
unzip 'path/to/nano' -d nano
```

This uncompresses the downloaded file.

Now that you have a copy of nano, move it to where git bash can find it:

```UNIX
mv nano ~/path/to/git/share
```

Except replace the path with the real path to where git bash is stored on your computer. Again, at this step, you can locate the folder of in which git bash is stored, and drag and drop the folder into your git bash window.

Then, we will type this script into the command line:

```UNIX
echo '
#!/bin/sh
exec /share/nano/nano.exe "$@"ut
' > nano
```

This creates a small text file containing the nano executeable. We'll move this into the built-in executables of your computer like so:

```UNIX
mv nano ~/bin
```

This should complete the installation. You can check this by creating a file with nano:

```UNIX
nano my_file
```

This should take you to the nano editor screen. Ctrl + x will allow you to exit.
