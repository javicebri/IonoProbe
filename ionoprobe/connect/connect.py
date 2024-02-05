from abc import ABC, abstractmethod 


class Connect(ABC): 
    
    def __init__(self, paths_dict, config):
        self.paths_dict = paths_dict
        self.config = config
  
    @abstractmethod
    def _get_url(self): 
        pass

    @abstractmethod
    def download(self):
        pass