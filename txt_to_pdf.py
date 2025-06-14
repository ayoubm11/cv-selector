import os
from fpdf import FPDF

input_folder = "cvs"
output_folder = "cvs"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        txt_path = os.path.join(input_folder, filename)
        pdf_filename = filename.replace(".txt", ".pdf")
        pdf_path = os.path.join(output_folder, pdf_filename)

        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        
        # Ajouter le texte en page, ligne par ligne
        for line in text.split("\n"):
            pdf.cell(0, 10, line, ln=True)
        
        pdf.output(pdf_path)
        print(f"Converti {txt_path} en {pdf_path}")
