import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f" Text Editor - {filepath}")


window = tk.Tk()

window.title("Text Editor")

window.configure( width=300, height=300)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


txt_edit = tk.Text(window)


frame_buttons = tk.Frame(window, relief = tk.RAISED, bd = 2)

open_button = tk.Button(frame_buttons, text="OPEN", command=open_file)
save_button = tk.Button(frame_buttons, text="SAVE AS", command=save_file)

open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)

frame_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")



window.mainloop()

