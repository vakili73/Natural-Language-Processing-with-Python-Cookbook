import pdf

pdfFile = 'Chapter02/sample-one-line.pdf'
pdfFileEncrypted = 'Chapter02/sample-one-line.protected.pdf'

print('PDF 1: \n', pdf.getTextPDF(pdfFile))
print('PDF 2: \n', pdf.getTextPDF(pdfFileEncrypted, 'tuffy'))
