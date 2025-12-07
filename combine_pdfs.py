from pypdf import PdfWriter
import os

# Change to the directory containing the script
os.chdir("/Users/bouyang/Documents/Zxperiment/media/newsletter_position/publication_content_collection/my_products/vibe-coding-zero-to-ship")

merger = PdfWriter()

# List of PDFs to combine in order
pdfs = [
    "individual_pdfs/README.pdf",
    "individual_pdfs/PATHWAYS.pdf",
    "individual_pdfs/QUICK-START.pdf",
    "individual_pdfs/Chapter-01-introduction.pdf",
    "individual_pdfs/Chapter-02-understanding-apps.pdf",
    "individual_pdfs/Chapter-03-choosing-stack.pdf",
    "individual_pdfs/Chapter-04-tutorial.pdf",
    "individual_pdfs/Chapter-05-building-blocks.pdf",
    "individual_pdfs/Chapter-06-debugging.pdf",
    "individual_pdfs/Chapter-07-testing.pdf",
    "individual_pdfs/Chapter-08-whats-next.pdf",
    "individual_pdfs/GLOSSARY.pdf"
]

print("Combining PDFs...")
for pdf in pdfs:
    print(f"  Adding {pdf}")
    merger.append(pdf)

output_file = "Vibe-Coding-Bootcamp-Complete.pdf"
print(f"\nWriting combined PDF to {output_file}")
with open(output_file, "wb") as output:
    merger.write(output)

print(f"✓ Combined PDF created: {output_file}")
print(f"  Total pages: {len(merger.pages)}")
