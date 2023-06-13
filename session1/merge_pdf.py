import os

#pip install PyPDF2

from PyPDF2 import PdfMerger


os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

print(os.getcwd())

merger = PdfMerger()

for irgend_eine_datei in os.listdir():
    if "Kapitel" in irgend_eine_datei:
        merger.append(irgend_eine_datei)
        os.remove(irgend_eine_datei)

merger.write(os.getcwd() + "/meine_neu_beste_pdf.pdf")
merger.close()
