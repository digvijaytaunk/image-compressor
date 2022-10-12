import wx 
  
#import the newly created GUI file 
import form  
class CalcFrame(form.MyFrame1): 
    def __init__(self,parent): 
        form.MyFrame1.__init__(self,parent)  
		
    def OnCompressClick1(self,event): 
        num = int(self.txtSource.GetValue()) 
        self.txtDestination.SetValue (str(num*num)) 

    def OnCompressClick(self,event): 
        source_path = self.txtSource.GetValue()
        dest_path = self.txtDestination.GetValue()
        quality = self.txtQuality.GetValue()
        target_size = self.txtSize.GetValue()

        for filename in os.listdir(source_path):
            fs = os.path.join(source_path, filename)
            fd = os.path.join(dest_path, filename)
            img = Image.open(fs)
            x, y = img.size
            target_x = 1024
            scale = target_x/x
            img_compressed = img.resize((int(x*scale), int(y*scale)), Image.Resampling.LANCZOS)
            img_compressed.save(fd, quality=90, optimize=True)

app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 