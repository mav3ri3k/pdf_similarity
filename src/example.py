from src.pdf_similarity import Pdf_Similarity 
ps = Pdf_Similarity()

# Automatically find pdfs in currenly directory and print ratios
ps.generate()


# For more control complete the process one by one
ps.directory(".")
ps.find_pdf()
ps.process_text()
ps.generate_ratios()
ps.print_ratio_matrix()
