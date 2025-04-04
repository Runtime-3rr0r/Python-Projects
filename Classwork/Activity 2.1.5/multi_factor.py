# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What was your first car?"
answer = "1966 Mustang"

username = "admin"
password = "2378527358"

my_auth.set_authentication(question, answer)
my_auth.set_authorization(username, password)

# start the GUI
my_auth.mainloop()