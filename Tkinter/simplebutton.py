# https://www.geeksforgeeks.org/python-gui-tkinter/
# pip install tk
import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()