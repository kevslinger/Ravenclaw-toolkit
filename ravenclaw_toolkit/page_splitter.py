from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import constants



OFFSETS = (12, 12, 14, 16, 16, 14, 16)

STATIC = 'static'

for idx in range(6, len(constants.TITLES)):
    inputpdf = PdfFileReader(open(os.path.join(STATIC, constants.TITLES[idx] + '.pdf'), 'rb'))

    for i in range(inputpdf.numPages):
        if i < OFFSETS[idx]:
            continue
        if i >= (constants.TOTAL_PAGES[idx] + OFFSETS[idx]):
            break
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        output_dir = os.path.join(constants.STATIC, f'HP{idx+1}')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        with open(os.path.join(output_dir, f'hp{(idx+1)}_{(i+1-OFFSETS[idx])}.pdf'), 'wb') as outputStream:
            output.write(outputStream)
        
