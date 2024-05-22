class Dates:
    def __init__(self,date):
        self.date = date
    
    def get_date(self):
        return self.date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")
