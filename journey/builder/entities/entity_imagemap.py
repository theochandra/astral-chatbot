class Action(object):
    
    def __init__(self, type):
        self.type       = type
        # self.link_uri   = ""
        self.text       = ""
        self.area       = {}
        
    @property
    def action_type(self):
        pass
        
    @action_type.setter
    def action_type(self, type):
        self.type = type
      
    # @property
    # def action_link_uri(self):
    #     pass
    
    # @action_link_uri.setter
    # def action_link_uri(self, link_uri):
    #     self.link_uri = link_uri 
    
    @property
    def action_text(self):
        pass
    
    @action_text.setter
    def action_text(self, text):
        self.text = text
        
    @property
    def action_area(self):
        pass

    @action_area.setter
    def action_area(self, area):
        self.area = area


class Area(object):
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @property 
    def image_x(self):
        pass
    
    @image_x.setter
    def image_x(self, x):
        self.x = x
        
    @property 
    def image_y(self):
        pass
    
    @image_y.setter
    def image_y(self, y):
        self.y = y
        
    @property 
    def image_width(self):
        pass
    
    @image_width.setter
    def image_width(self, width):
        self.width = width
        
    @property 
    def image_height(self):
        pass
    
    @image_height.setter
    def image_height(self, height):
        self.height = height