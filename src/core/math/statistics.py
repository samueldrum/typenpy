from typenpy.Vector import Vector
from core.errors import NotAVectorError
from collections import Counter


class Stats(Vector):

    
    @staticmethod
    def mean(object: Vector):
        if isinstance(object, Vector):
            sum_ = object.sum()
            lenght = object.__len__()

            return sum_ / lenght
        
        else:
            raise NotAVectorError
        
    @staticmethod
    def median(object: Vector):
        lenght = object.__len__()
        middle = lenght >> 1 #Shift to right

        if not lenght % 2 == 0:
            return object.data[middle]
        else:
            result = (object.data[middle] + object.data[middle - 1]) / 2
            return result
    


    @staticmethod
    def mode(object: Vector):
        result = Counter(object.data).most_common(1)[0][0]
        return result
    
    
    @staticmethod
    def variance(object: Vector):
        ...


    @staticmethod
    def stdev(object: Vector):
        ...




    

