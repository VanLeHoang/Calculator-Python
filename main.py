import tkinter as tk
from tkinter import ttk
def handle_button_click(clicked_button_text):
  current_text = result_var.get()
  if clicked_button_text == "=":
    try:
      expression = current_text.replace("÷","/").replace("x","*")
      result = eval(expression)
      if result.is_interger():
        result = int(result)
        result_var.set(result)
    except Exception as e:
      result_var.set("Error")
  elif clicked_button_text == "C":
    result_var.set("")
  elif clicked_button_text == "%":
    try:
      current_number = float(current_text)
      result_var.set(current_number / 100)
    except ValueError:
      result_var.set("Error")
