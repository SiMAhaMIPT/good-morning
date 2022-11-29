
class Windows:
    def __init__(self):
        self.windows = {}
        self.current = None
        
    def open_window(self,label):
        w = self.windows.get(label)
        if w:
            self.current = w   
        
        return self.current
    
    def get_window(self):
        cu = self.current
        if cu == None:
            cu = list(self.windows.values())[0]
        return cu
    
    def add(self, label : str, window):
        self.windows[label]  = window
