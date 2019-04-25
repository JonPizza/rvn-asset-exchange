# rvn-asset-exchange
Made for donations to Notre Dame

       ----    ----
     /      \/      \
    |                |
     \              /
      \            /
        \        /
          \    /
           \ /
           
           
________

VERY IMPORTANT:

THIS SCRIPT CURRENTLY CONTAINS A HUGE BUG! IT WILL SEND OUT TOKENS BASED ON THE ENTIRE INPUT, SO IF YOUR FINE WITH THE SCRIPT SENDING MORE ASSETS THEN NECCICARY IT IS FINE, BUT OTHERWISE DO NOT USE THIS SCRIPT... maybe


HOW TO (Linux):

You must have Python installed (Duh)

Download this file

Put exchange.py in the folder that raven-qt lives in (for me it was ~/Downloads/raven-2.2.2.0/bin)

Open up exchange.py with your favorite text editor

Set the variables

Save + Close the file

Open up 2 terminals in the same dir as where exchange.py lives (Again, for me it was ~/Downloads/raven-2.2.2.0/bin)

In the first terminal:

_./ravend_

In the second:

_python exchange.py_

As transactions come in, as long as there is a sufficent amount of the asset left, the sender should recive the tokens. How long this takes is up to you, by setting the min # of confirms (I recomend 5.) 

IF THIS BREAKS ITS NOT ON ME

-JonPizza has struck (For the 2nd time with a kinda decent script)
