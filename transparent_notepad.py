import tkinter as tk

def save_file():
    text = text_area.get("1.0", tk.END)
    with open(input_file_path, "w") as file:
        file.write(text)

def on_text_change(event):
    save_file()

root = tk.Tk()

# Set window transparency
root.attributes("-alpha", 0.7)

# Window title
root.title("Transparent Notepad")

# Text area
text_area = tk.Text(root, bg="white")
text_area.pack(fill=tk.BOTH, expand=1)

# Set input file path
input_file_path = "Transparent_notepad\input.txt"

# Read content from input.txt and insert into text area
try:
    with open(input_file_path, "r") as file:
        content = file.read()
        text_area.insert(tk.END, content)
except FileNotFoundError:
    print("File not found!")


text_area.bind("<<Modified>>", on_text_change)

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()

