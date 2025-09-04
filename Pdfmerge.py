
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(output_path, *input_paths):
    """
    Merge multiple PDF files into a single PDF.

    Parameters:
        output_path (str): Path to the merged output PDF file.
        *input_paths (str): Paths to input PDF files in desired order.
    """
    merger = PdfMerger()
    
    for pdf in input_paths:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")
    
    merger.write(output_path)
    merger.close()
    print(f"\n Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_pdfs.py output.pdf file1.pdf file2.pdf [file3.pdf ...]")
    else:
        output_file = sys.argv[1]
        input_files = sys.argv[2:]
        merge_pdfs(output_file, *input_files)
