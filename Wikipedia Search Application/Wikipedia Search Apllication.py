import tkinter as tk
from tkinter import messagebox, scrolledtext
import wikipedia

def search_wikipedia():
    query = entry.get().strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter a topic to search.")
        return

    # Show loading message
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "🔎 Searching Wikipedia...")
    text_area.config(state=tk.DISABLED)
    root.update_idletasks()  # Refresh UI while searching

    try:
        result = wikipedia.summary(query, sentences=3)
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, result)
        text_area.config(state=tk.DISABLED)
    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showerror("Error", f"Multiple results found: {', '.join(e.options[:5])}...")
    except wikipedia.exceptions.PageError:
        messagebox.showerror("Error", "No Wikipedia page found for your query.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def clear_text():
    """Clear both the input field and the output area."""
    entry.delete(0, tk.END)
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("Wikipedia Search App")
root.geometry("600x500")
root.configure(bg="#f5f5dc")  # Light Beige Background

# Heading Label
title_label = tk.Label(root, text="🔍 Wikipedia Search", font=("Arial", 18, "bold"), bg="#f5f5dc", fg="#333333")
title_label.pack(pady=10)

# Entry field for user input
entry = tk.Entry(root, font=("Arial", 14), width=40, bd=2, relief="solid", bg="#ffffff", fg="#333333", insertbackground="black")
entry.pack(pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#f5f5dc")
button_frame.pack(pady=5)

# Search Button
search_button = tk.Button(button_frame, text="Search", font=("Arial", 15), bg="#28a745", fg="white", width=10, relief="flat", command=search_wikipedia)
search_button.grid(row=0, column=0, padx=5)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 15), bg="#ff5733", fg="white", width=10, relief="flat", command=clear_text)
clear_button.grid(row=0, column=1, padx=5)

# Text area to display results
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=60, state=tk.DISABLED, bd=2, relief="solid", bg="#ffffff", fg="#333333", insertbackground="black")
text_area.pack(pady=10, padx=10)

# Run the Tkinter event loop
root.mainloop()
