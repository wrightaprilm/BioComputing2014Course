#Installing Linux (Ubuntu) on a Windows Machine using VirtualBox

Sorry Windows users, you need a whole new machine. Luckily, you can do this for free! This is a guide to making a “virtual computer” on a section of your hard drive on which you will then install a whole new operating system. Having a virtual Ubuntu machine will get you all the Linux/Unix capabilities that we will use in this class. 

There are other ways of getting these capabilities, but this is perhaps the best balance of convenience and performance, and, bottom line, it’s what I use and I don’t know much about other methods. It’s not super easy, but trust me, it’s well worth it.

There are two steps: installing VirtualBox (VB), and installing Ubuntu on your VB virtual machine. Give yourself some time to do all this. Depending on computer and internet speed, it could take an afternoon, but you don’t have to be there for most of it. I have provided instructions below, but you may want to look at some internet documentation first and compare and contrast; I can’t guarantee that my instruction are perfect, since it’s been a while since I’ve done it. Here are two such docs, in the order that your installation will follow:

A step-by-step guide to the Virtual Box part (with pictures!): http://www.psychocats.net/ubuntu/virtualbox

Instructions for making a folder that can be shared between your Windows and Ubuntu http://practicalcomputing.org/ubuntu

There are tons of other resources; just ask the mighty Google. You can also contact James Derry at SBS IT with questions: jderry@austin.utexas.edu. 

##My Instructions 

Adapted from “Practical Computing for Biologists” 

(Recommended reading from Haddock and Dunn)

Download Ubuntu disk image here: http://www.ubuntu.com/download.

- Download the 32-bit version – Virtual Box only allows 32-bit guest operating systems.
- Don’t do anything with it for now, but make sure you know where it. This will take a while to download.

(Downloads folder, probably).

Download VirtualBox here: (https://www.virtualbox.org/wiki/Downloads)

- Use default installer settings

Open VirtualBox and click “New” button to create a new virtual computer.

- Follow setup wizard instructions:

- Name it something. Mine’s called ‘Ubuntu.’

- Select Linux for the operating system,

- Select Ubuntu for the version, 

- And select at least 512 MB base memory (RAM). You can definitely go higher on this. A quarter of your RAM or less is a good rule of thumb – if you have less than 1GB of RAM, use 512 MB. Right click “Computer” on the start menu and hit “Properties” to see how much RAM you have.

- In the Virtual Hard Disk window, click “New” to make a new virtual hard disk

- You will now have to decide whether to let VB expand your virtual hard disk dynamically (as you fill it up) or whether to set a fixed cap. I will advocate a fixed cap at 8 GB (or whatever size the wizard recommends). This is because it’s faster to have all your hard memory in one place instead of strewn aroundyour real hard disk, which is what happens when VB expands dynamically. The downside is, if you reach the cap and want to expand, you have to wipe your virtual machine and make a new one (which isn’t a big deal – you just do these same steps again, after you’ve backed everything up, of course).

##Install Ubuntu on Virtual Box.

- Start you virtual computer in VB by double clicking the icon on the left panel.

- This will launch the First Run Wizard.

- Select CD/DVD-ROM Device for Media type, click the folder icon under Media Source, click the Add button at the top of the window that pops up, and then browse to where you saved the Ubuntu file that you downloaded and select that. (The step-by-step guide above does this a little differently – both should work).

- Your virtual computer should now start up and begin the Ubuntu installation process, which Ubuntu will guide you through.

## Install Guest Additions and make a shared folder.

- There are a few problems, like small screen size and weird mouse behavior, which come with running Ubuntu in the virtual environment. These can be solved by installing “Guest Additions.”

- Please follow the guide to setting up a shared folder in the Practical Computing link above. This should walk you through the process.

##Good Luck (hopefully you won’t need it)
