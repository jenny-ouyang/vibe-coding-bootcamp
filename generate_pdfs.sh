#!/bin/bash

cd /Users/bouyang/Documents/Zxperiment/media/newsletter_position/publication_content_collection/my_products/vibe-coding-zero-to-ship

echo "Generating Chapter 1..."
md-to-pdf 01-introduction.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 01-introduction.pdf individual_pdfs/Chapter-01-introduction.pdf

echo "Generating Chapter 2..."
md-to-pdf 02-understanding-apps.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 02-understanding-apps.pdf individual_pdfs/Chapter-02-understanding-apps.pdf

echo "Generating Chapter 3..."
md-to-pdf 03-choosing-stack.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 03-choosing-stack.pdf individual_pdfs/Chapter-03-choosing-stack.pdf

echo "Generating Chapter 4..."
md-to-pdf 04-tutorial.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 04-tutorial.pdf individual_pdfs/Chapter-04-tutorial.pdf

echo "Generating Chapter 5..."
md-to-pdf 05-building-blocks.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 05-building-blocks.pdf individual_pdfs/Chapter-05-building-blocks.pdf

echo "Generating Chapter 6..."
md-to-pdf 06-debugging.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 06-debugging.pdf individual_pdfs/Chapter-06-debugging.pdf

echo "Generating Chapter 7..."
md-to-pdf 07-testing.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 07-testing.pdf individual_pdfs/Chapter-07-testing.pdf

echo "Generating Chapter 8..."
md-to-pdf 08-whats-next.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv 08-whats-next.pdf individual_pdfs/Chapter-08-whats-next.pdf

echo "Generating README..."
md-to-pdf README.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv README.pdf individual_pdfs/README.pdf

echo "Generating GLOSSARY..."
md-to-pdf GLOSSARY.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv GLOSSARY.pdf individual_pdfs/GLOSSARY.pdf

echo "Generating QUICK-START..."
md-to-pdf QUICK-START.md --pdf-options '{"format": "Letter", "margin": {"top": "1in", "bottom": "1in", "left": "1in", "right": "1in"}, "printBackground": true}'
mv QUICK-START.pdf individual_pdfs/QUICK-START.pdf

echo "All PDFs generated successfully!"
