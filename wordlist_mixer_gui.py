import tkinter as tk
from tkinter import filedialog, messagebox, font, ttk
import itertools
import random
import os

def save_wordlist():
    file_name = entry_filename.get().strip()
    file_path = entry_filepath.get().strip()
    words_raw = text_words.get("1.0", tk.END).strip()
    
    if not file_name or not file_path or not words_raw:
        messagebox.showwarning("Input Error", "All fields are required.", parent=root)
        return
    
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    words = [w.strip() for w in words_raw.splitlines() if w.strip()]
    if len(words) < 2:
        messagebox.showwarning("Input Error", "Enter at least two words!", parent=root)
        return

    combos = set()
    for l in range(2, len(words)+1):
        for p in itertools.permutations(words, l):
            combos.add(''.join(p))
    combos = list(combos)
    random.shuffle(combos)

    if not os.path.exists(file_path):
        try:
            os.makedirs(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directory:\n{e}", parent=root)
            return

    full_path = os.path.join(file_path, file_name)
    try:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(combos))
        messagebox.showinfo("Success", f"Wordlist saved to:\n{full_path}", parent=root)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}", parent=root)

def browse_path():
    path = filedialog.askdirectory(parent=root)
    if path:
        entry_filepath.delete(0, tk.END)
        entry_filepath.insert(0, path)

root = tk.Tk()
root.title(" Wordlist Mixer & Creator")
root.geometry("480x420")
root.resizable(False, False)

# Style/Decoration
s = ttk.Style()
s.theme_use('clam')
s.configure('TButton', font=('Segoe UI', 10, 'bold'), foreground='#222', background='#fff')
s.configure('TLabel', font=('Segoe UI', 11, 'bold'))

font_title = font.Font(family='Segoe UI', size=16, weight='bold')
label_title = tk.Label(root, text="Wordlist Mixer & Creator", font=font_title, fg="#1e88e5")
label_title.pack(pady=12)

frame = ttk.Frame(root)
frame.pack(padx=24, pady=6, fill='both', expand=True)

# File Name
ttk.Label(frame, text="File Name:").grid(row=0, column=0, sticky='e', padx=4, pady=5)
entry_filename = ttk.Entry(frame, width=34)
entry_filename.grid(row=0, column=1, padx=4, pady=5)

# File Path
ttk.Label(frame, text="File Path:").grid(row=1, column=0, sticky='e', padx=4, pady=5)
entry_filepath = ttk.Entry(frame, width=34)
entry_filepath.grid(row=1, column=1, padx=4, pady=5)
ttk.Button(frame, text="Browse", command=browse_path).grid(row=1, column=2, padx=4, pady=5)

# Words Area
ttk.Label(frame, text="Words (one per line):").grid(row=2, column=0, sticky='ne', padx=4, pady=5)
text_words = tk.Text(frame, width=34, height=8, font=('Consolas', 11))
text_words.grid(row=2, column=1, padx=4, pady=5, columnspan=2)

# Save Button
ttk.Button(root, text="Save", command=save_wordlist).pack(pady=16)

# Tips
tip = tk.Label(root, text="from https://github.com/moscow36/wordlist_mixer_gui", fg="#666", font=('Segoe UI', 9))
tip.pack()

root.mainloop()
