import subprocess
import os
from PIL import Image
import tempfile

class pytesseract(object):

    def __init__(self):
        self.tesseract_cmd = 'tesseract'
        # out_tmp
        out_tmp = tempfile.NamedTemporaryFile()
        out_tmp = out_tmp.name
        self.tmp = out_tmp
        self.outfile = self.tmp + '.txt'
        
        # load_tmp
        load_tmp = tempfile.NamedTemporaryFile(suffix = '.jpg')
        load_tmp = load_tmp.name
        self.loadfile = load_tmp

    def run_tesseract(self, load_img):
        load_img.save(self.loadfile)
        subprocess.run([self.tesseract_cmd, self.loadfile, self.tmp],stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)

        with open(self.outfile) as f:
            text = f.read()
            text = text.strip()

        return text
