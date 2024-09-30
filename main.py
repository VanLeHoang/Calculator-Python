import tkinter as tk
from tkinter import ttk
def handle_button_click(clicked_button_text):
  current_text = result_var.get()
  if clicked_button_text == "=":
    expression = current_text.replace("÷","/").replace("x","*")
    result = eval(expression)
