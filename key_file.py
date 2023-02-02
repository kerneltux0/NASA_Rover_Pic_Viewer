import os

def get_api_key():
        api_key_file = os.path.join( os.getcwd(), 'api_key.txt' )
        file = open(api_key_file)
        api_key = file.readline()
        file.close()
        return api_key