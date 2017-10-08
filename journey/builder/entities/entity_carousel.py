class Column(object):
    
    def __init__(self, url, title, text):
        self.url = url
        self.title = title
        self.text = text
    
    @property
    def column_url(self):
        pass
    
    @column_url.setter
    def column_url(self, url):
        self.url = url
    
    @property
    def column_title(self):
        pass
    
    @column_title.setter
    def column_title(self, title):
        self.title = title
        
    @property
    def column_text(self):
        pass
    
    @column_text.setter
    def column_text(self, text):
        self.text = text
    
class Action(object):
    
    def __init__(self, type, label, text):
        self.type = type
        self.label = label
        self.text = text
        
    @property
    def action_type(self):
        pass
        
    @action_type.setter
    def action_type(self, type):
        self.type = type
    
    @property
    def action_label(self):
        pass
    
    @action_label.setter
    def action_label(self, label):
        self.label = label
      
    @property
    def action_text(self):
        pass
    
    @action_text.setter
    def action_text(self, text):
        self.text = text

class Carousel(object):
    
    def __init__(self):
        self.column = {}
        self.actions = []
    
    @property
    def carousel_column(self):
        pass
    
    @carousel_column.setter
    def carousel_column(self, column):
        self.column = column
    
    @property
    def carousel_actions(self):
        pass
    
    @carousel_actions.setter
    def carousel_actions(self, actions):
        self.actions = actions