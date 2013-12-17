Gspread-helper
==============

Want to connect to a spreadsheet on your Google Drive quickly and easily? This makes it relatively painless. 


Installation
------------

Clone the repo, or download the zip into a folder and unzip it.

Open a terminal and `cd` into that folder. 

Type the following to install the tools you need.

    $ ./install-gspread

If it asks for your password, provide it.


Configure
---------

Open the `settings` file.

Put your username and password in there.


Use
---

Open the python interpreter in the Terminal by typing:

    $ python

Then import the spreadsheet tool by typing this:

    $ from spreadsheet import Spreadsheet

Next, load the spreadsheet you want (in this example, I'm loading a spreadsheet on my Google Drive called `test`).

    $ sheet = Spreadsheet.load('test')

Now you can programmatically manipulate it to your heart's content using the gspread library. See here for some tips: https://github.com/burnash/gspread

