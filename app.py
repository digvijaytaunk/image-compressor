import os
import wx
from PIL import Image

import form


class CompAppFrame(form.MyFrame1): 
    def __init__(self, parent):
        form.MyFrame1.__init__(self, parent)

    def OnCompressClick(self, event):
        source_path = self.txtSource.GetValue()
        dest_path = self.txtDestination.GetValue()
        quality = self.txtQuality.GetValue()
        target_size = self.txtSize.GetValue()

        for filename in os.listdir(source_path):
            fs = os.path.join(source_path, filename)
            fd = os.path.join(dest_path, filename)
            img = Image.open(fs)
            x, y = img.size
            target_x = int(target_size)
            scale = target_x/x
            img_compressed = img.resize((int(x*scale), int(y*scale)), Image.Resampling.LANCZOS)
            img_compressed.save(fd, quality=int(quality), optimize=True)


app = wx.App(False) 
frame = CompAppFrame(None) 
frame.Show(True)

# start the applications
app.MainLoop()
