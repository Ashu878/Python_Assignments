import logging
logging.basicConfig(filename = "tests.log", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")

class TupleU:
    logging.info("Class tuple")
    def __init__(self,tuple):
        """Function to accept a tuple in the class"""
        try:
            self.tuple = tuple
            if type(tuple) != tuple:
                raise Exception("Not a tuple")
        except Exception as e:
            logging.error("Error occured not a tuple: {}".format(e))

    def count(self,value):
        """Function to count number of occurences in the tuple"""
        try:
            count = 0
            for i in self.tuple:
                if i == value:
                    count += 1
            return count
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def index(self,value,*args):
        """Function to find index with start and stop"""
        try:
            for i,j in enumerate(self.tuple):
                if j == value:
                    return i
        except Exception as e:
            logging.error("Error occured {}".format(e))




