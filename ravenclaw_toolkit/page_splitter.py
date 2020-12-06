from PyPDF2 import PdfFileWriter, PdfFileReader
import os


TITLES = ('Harry Potter and the Sorcerer\'s Stone',
         'Harry Potter and the Chamber of Secrets',
         'Harry Potter and the Prisoner of Azkaban',
         'Harry Potter and the Goblet of Fire',
         'Harry Potter and the Order of the Phoenix',
         'Harry Potter and the Half-Blood Prince',
         'Harry Potter and the Deathly Hallows')

OFFSETS = (12, 12, 14, 16, 16, 14, 16)
TOTAL_PAGES = (309, 341, 435, 734, 870, 652, 759)
STATIC = 'static'

for idx in range(6, len(TITLES)):
    inputpdf = PdfFileReader(open(os.path.join(STATIC, TITLES[idx] + '.pdf'), 'rb'))

    for i in range(inputpdf.numPages):
        if i < OFFSETS[idx]:
            continue
        if i >= (TOTAL_PAGES[idx] + OFFSETS[idx]):
            break
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        output_dir = os.path.join(STATIC, f'HP{idx+1}')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        with open(os.path.join(output_dir, f'hp{(idx+1)}_{(i+1-OFFSETS[idx])}.pdf'), 'wb') as outputStream:
            output.write(outputStream)
        
