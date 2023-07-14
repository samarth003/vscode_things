from region_common import region

class kanto(region):
    '''
    kanto specific starter pokemon to be added 
    trainers registering from kanto to be added 
    database to be added for storage (later)
    '''
    def __init__(self, fname, lname, township, myRegion):
        super().__init__(fname, lname, township)
        self.trainer_region = myRegion