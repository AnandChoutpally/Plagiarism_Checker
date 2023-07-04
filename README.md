# Plagiarism_Checker
 The program is a plagiarism checker implemented in Python with a graphical user interface (GUI). It allows users to compare the similarity between two text documents using the cosine similarity metric.

 Upon launching the program, a GUI window appears, presenting two text entry fields labeled "Document 1" and "Document 2". Users can input the text they want to compare in these fields.

When the user clicks the "Check Plagiarism" button, the program retrieves the text from the text entry fields, preprocesses the documents by converting them to lowercase, removing punctuation marks, and splitting them into individual words. The program then calculates the cosine similarity between the two preprocessed documents.

The cosine similarity calculation involves computing the dot product of the word counts for each word and the magnitudes of each document's word vector. The cosine similarity value is a measure of how similar the documents are, with higher values indicating greater similarity.

After the calculation is complete, the program displays the cosine similarity value in a message box. If either of the text entry fields is empty, an error message is shown to prompt the user to enter both documents.

This program provides a simple and intuitive way to assess the similarity between two text documents, making it useful for identifying potential instances of plagiarism or finding similarities in content.
