from PdfSim.util.readPdf import readPdf 
from PdfSim.util.similarity import Similarity
from PdfSim.util.findPdf import find_pdfs

class Pdf_Similarity:
    """Find similarity ratio between pdfs"""

    def __init__(self):
        """Initiate class"""
        self.path = "."
        self.pdfs = []
        self.sim = Similarity()
        self.skipped_files = 0
        self.ratio_matrix = []
    
    def directory(self, path):
        """Define directory for pdfs"""
        self.path = path

    def find_pdf(self):
        """Find pdfs in given directory"""
        pdfs = find_pdfs(self.path)
        for pdf in pdfs:
            self.pdfs.append(pdf)


    def process_text(self):
        """Extract text from pdf"""
        for pdf in self.pdfs:
            pdf_text = readPdf(pdf["path"])
            sim.add_strings(pdf_text)

    def generate_ratios(self):
        """Generate similarity ratios for pdfs"""
        """Very small pdf are skipped"""
        try:
            self.sim.generate()
        except:
            self.skipped_files += 1

        print(f"{self.skipped_files} file skipped")

    def print_ratio_matrix(self):
        """Print pdf similarity ratios obtained"""
        print("PDFs found:")
        print(self.pdfs)
        print("Ratio Matrix: ")
        for row in self.ratio_matrix:
            print(row)

    def generate(self):
        """Combine all the steps in one
        ./ directory is taken as default to search for pdfs"""
        self.find_pdf()
        self.process_text()
        self.generate_ratios()
        self.print_ratio_matrix()
