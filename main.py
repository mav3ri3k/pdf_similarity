from readPdf import readPdf 
from similarity import Similarity
from findPdf import find_pdfs

print("Hello")
sim = Similarity()

pdfs = find_pdfs(".")
print(pdfs)

for pdf in pdfs:
    pdf_text = readPdf(pdf["path"])
    sim.add_strings(pdf_text)

print("text read")
print("generating ratios")
skippedFils = 0 
try:
    sim.generate()
except:
    skippedFils += 1

print(f"{skippedFils} file skipped")
print("add done")
print(sim.ratios)
