from PyPDF2 import PdfFileWriter, PdfFileReader
import os


PATHS = ('J.K._Rowling_HP_1_Harry_Potter_and_the_S.pdf', '2-harry-potter-and-the-chamber-of-secrets.pdf', 'J.K. Rowling - HP 3 - Harry Potter and the Prisoner of Azkaban.pdf', 'J.K.-Rowling-HP-4-Harry-Potter-and-the-Goblet-of-Fire.pdf', '5_-_harry_potter_and_the_order_of_the_phoenix_chapter_37.pdf', 'J.K.-Rowling-HP-6-Harry-Potter-and-the-Half-Blood-Prince.pdf', 'J.K. Rowling - HP 7 - Harry Potter and the Deathly Hallows.pdf')

OFFSETS = (12, 12, 14, 16, 16, 14, 17, )
TOTAL_PAGES = (309, 341, 435, 734, 870, 652, 758)


for idx in range(0, len(OFFSETS)):
    inputpdf = PdfFileReader(open(os.path.join('/Users/kevin/Downloads', PATHS[idx]), 'rb'))

    for i in range(inputpdf.numPages):
        if i < OFFSETS[idx]:
            continue
        if i >= (TOTAL_PAGES[idx] + OFFSETS[idx]):
            break
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        output_dir = os.path.join('HP', f'HP{idx+1}')
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        with open(os.path.join(output_dir, f'hp{(idx+1)}_{(i+1-OFFSETS[idx])}.pdf'), 'wb') as outputStream:
            output.write(outputStream)
        
