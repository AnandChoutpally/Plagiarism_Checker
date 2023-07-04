import string
from collections import Counter
from math import sqrt
import tkinter as tk
from tkinter import messagebox

def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation marks
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the text into individual words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    return word_counts

def calculate_cosine_similarity(doc1, doc2):
    # Preprocess the text documents
    word_counts1 = preprocess_text(doc1)
    word_counts2 = preprocess_text(doc2)

    # Create a set of unique words from both documents
    all_words = set(word_counts1).union(set(word_counts2))

    # Calculate the dot product
    dot_product = sum(word_counts1.get(word, 0) * word_counts2.get(word, 0) for word in all_words)

    # Calculate the magnitude of each document's word vector
    magnitude1 = sqrt(sum(word_counts1.get(word, 0) ** 2 for word in all_words))
    magnitude2 = sqrt(sum(word_counts2.get(word, 0) ** 2 for word in all_words))

    # Calculate the cosine similarity
    cosine_similarity = dot_product / (magnitude1 * magnitude2)

    return cosine_similarity

def check_plagiarism():
    document1 = entry_doc1.get("1.0", "end-1c")
    document2 = entry_doc2.get("1.0", "end-1c")

    if document1.strip() == "" or document2.strip() == "":
        messagebox.showerror("Error", "Please enter both documents.")
        return

    similarity = calculate_cosine_similarity(document1, document2)
    messagebox.showinfo("Plagiarism Checker", f"Cosine similarity: {similarity}")

# GUI Setup
window = tk.Tk()
window.title("Plagiarism Checker")

# Document 1 Label and Text Entry
label_doc1 = tk.Label(window, text="Document 1:")
label_doc1.pack()
entry_doc1 = tk.Text(window, height=10, width=50)
entry_doc1.pack()

# Document 2 Label and Text Entry
label_doc2 = tk.Label(window, text="Document 2:")
label_doc2.pack()
entry_doc2 = tk.Text(window, height=10, width=50)
entry_doc2.pack()

# Check Plagiarism Button
button_check = tk.Button(window, text="Check Plagiarism", command=check_plagiarism)
button_check.pack()

window.mainloop()

