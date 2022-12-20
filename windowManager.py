
#class for managing windows
class Windows:
    def __init__(self):
        #array of all available windows
        self.windows = {}
        self.current = None
        
    #opens window by label
    def open_window(self,label):
        w = self.windows.get(label)
        if w:
            self.current = w.openWindow() 
        
        return self.current
    
    #gets currently opened window
    def get_window(self):
        cu = self.current
        if cu == None:
            cu = list(self.windows.values())[0]
        return cu
    
    
    #adds window to the array
    def add(self, label : str, window):
        self.windows[label]  = window
