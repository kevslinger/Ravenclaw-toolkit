# File to add line number annotations to the book page PNGs
# This will be a WIP for I imagine a long time...

from PIL import Image
import glob
import os
import constants



ss_to_gof = ('ss_cos_poa_gof_overlay.png', 'ss_cos_poa_gof_chapter_overlay.png')
ootp = ('ootp_overlay.png', 'ootp_chapter_overlay.png')
hbp_to_dh = ('hbp_dh_overlay.png', 'hbp_dh_chapter_overlay.png')
OVERLAY_PATHS = {
    1: ss_to_gof,
    2: ss_to_gof,
    3: ss_to_gof,
    4: ss_to_gof,
    5: ootp,
    6: hbp_to_dh,
    7: hbp_to_dh
}



for book in range(1, 8):
    # BLAGH THIS FIRST LINE IS SO GROSS LMAO
    file_list = list(filter(lambda x: 'lines' not in x, glob.glob(os.path.join(constants.STATIC, f'HP{book}/*.png'))))

    for idx in range(1, len(file_list)+1):
        # It's kinda awkward to use another string instead of make some var
        bg = Image.open(os.path.join(constants.STATIC, f'HP{book}/hp{book}_{idx}.png'))

        # Check if we're on a chapter page or not
        if idx in constants.CHAPTER_PAGE[book]:
            overlay_idx = 1
        else:
            overlay_idx = 0
            
        overlay = Image.open(os.path.join(constants.STATIC, OVERLAY_PATHS[book][overlay_idx]))

        bg.paste(overlay, box=None, mask=overlay)
        # Okay now it's REALLY awkward that I didn't just define a string earlier xD
        bg.save(os.path.join(constants.STATIC, f'HP{book}/hp{book}_{idx}_lines.png'))
        

#book = '7'
#file_list = glob.glob('static/HP' + book + '/*.png')

#idx = 0
#for i in sorted(file_list)[:100]:
#    bg = Image.open(i)

#    bg.paste(overlay, box=None, mask=overlay)

#    bg.save(f'/Users/kevin/Desktop/test/HP' + book + f'/page_{idx}.png')
#    idx += 1



#line_numbers_2 seems to be fine for books 1-4. We can drop line number 30, I don't think any book uses it.
# for book 5, it's terribly off the mark
# for books 6 and 7, It seems to be slightly downshifted.
# Weird, I wonder what happened....
# 


## OFFICIAL LIST OF LINE NUMBER OVERLAYS
# HP1: line_numbers_gof.png, line_numbers_chapters_gof.png
# HP2: line_numbers_gof.png, line_numbers_chapters_gof.png
# HP3: line_numbers_gof.png, line_numbers_chapters_gof.png
# HP4: line_numbers_gof.png, line_numbers_chapters_gof.png
# HP5: line_numbers_ootp.png, line_numbers_chapters_ootp.png
# HP6: line_numbers_hbp.png, line_numbers_chapters_hbp.png
# HP7: line_numbers_hbp.png, line_numbers_chapters_hbp.png 
