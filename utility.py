import pandas as pd 

class Crypto():

    def __init__(self, parameters):

        self.parameters = parameters
        self.base = 'https://api.x.immutable.com/v1/'
        self.cursor = ""
    
        while True:
            data = self.get_main_request()
            if data['remaining'] == 1 : # means there are more results to query 
                self.get_main_request()
                self.json_elements(data)
                self.cursor = self.cursor_helper(data)

            else:
                break 
        
        # return results and store as a dataframe 

        self.df = pd.DataFrame(self.json_elements(data)) 
        self.df.columns = self.df.columns.str.upper() 
    
    def cursor_helper(self, data):
        return data['cursor']
