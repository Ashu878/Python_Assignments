import logging
import copy
logging.basicConfig(filename = "test1.log", level = logging.DEBUG, format= "%(asctime)s %(levelname)s %(message)s")

class Ulist:
    """Class for list"""
    def __init__(self,list):
        try:
            self.list = list
            if type(self.list) != list:
                raise Exception("User input not a list")
        except Exception as e:
            logging.error("User input wrong {}".format(e))

    def append(self,to_add):
        """Class method to add objects inside list"""
        logging.info("Append function called to add {} to {}".format(to_add,self.list))
        try:
            adder = []
            for i in to_add:
                adder.append(i)
            self.list + adder
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def clear(self):
        """Class method to clear a list"""
        try:
            self.list.clear()

        except Exception as e:
            logging.error("Error occured {}".format(e))

    def insert(self,pos,val):
        """Class method to insert value at a position"""
        try:
            self.list.index(pos,val)
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def indexer(self,value):
        """Class method to find index"""
        try:
            for i,j in enumerate(self.list):
                if j == value:
                    return i
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def sort(self,**kwargs):
        """Class method to sort"""
        try:
            key = kwargs.get('key')
            reverse = kwargs.get('reverse')
            self.list.sort(key = key, reverse = reverse)
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def copy(self):
        """Class method to copy"""
        try:
            copy.deepcopy(self.list)
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def count(self,value):
        """Class method to count"""
        try:
            total = 0
            for i in self.list:
                if i == value:
                    total += 1
            return total
        except Exception as e:
            logging.error("error occured at {}".format(e))

    def extend(self,*value):
        """Function add extened the original list"""
        try:
            for i in value:
                self.list.append(i)
        except Exception as e:
            logging.error("Error occured {}".format(e))

    def pop(self,pos):
        """Function to pop a function"""
        try:
            for i,j in enumerate(self.list):
                if i == pos:
                    self.list.pop(i)

        except Exception as e:
            logging.error("Error occured {}".format(e))

    def remove(self,value):
        """Function to remove a val"""
        try:
            self.list.remove(value)
        except Exception as e:
            logging.error("Error occured".format(e))


test =  Ulist([11,2])
test.list.append(69)
print(test.list)