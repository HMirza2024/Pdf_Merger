PDF Merger Script
-
This Python script merges multiple PDF files into a single PDF file using the PyPDF2 library.

Requirements
-
1. Python 3.x
2. PyPDF2 library (pip install PyPDF2)

Usage
-
1. Run the script from the command line, providing the output file path and the paths to the input PDF files in the desired merge order.
2. python merge_pdfs.py output.pdf file1.pdf file2.pdf [file3.pdf ...]


output.pdf: The name/path of the merged PDF file.
file1.pdf, file2.pdf, etc.: Paths to the input PDF files to be merged.

Example
-
To merge doc1.pdf and doc2.pdf into merged_output.pdf:
python merge_pdfs.py merged_output.pdf doc1.pdf doc2.pdf

Script Details
-
1. The script uses the PyPDF2.PdfMerger class to append PDF files in the specified order.
2. It includes error handling to report issues with individual PDF files.
3. A success message is printed when the merged PDF is saved.

Notes
-
1. Ensure all input PDF files exist and are accessible.
2. The script requires at least two input PDF files (minimum of three arguments: script name, output file, and one input file).
3. If an error occurs while adding a PDF, the script will print the error and continue with the next file.

License
-
This script is free to use. It relies on PyPDF2, licensed under a modified BSD License (free to use). See PyPDF2 license for details.
