import re

class DataClass():
    def __init__(self, datastr):
        dataday, datamonth, datayear = self.intdata(datastr)
        if DataClass.checkdata(dataday, datamonth, datayear):
            self.dataday = dataday
            self.datamonth = datamonth
            self.datayear = datayear


    def __str__( self ):
        return "Дата(%02d-%02d-%04d)" % (self.dataday, self.datamonth, self.datayear)


    @classmethod
    def intdata( cls, datestr ):
        match = re.match( r'(\d{2})-(\d{2})-(\d{4})', datestr )
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            raise ValueError( "Формат даты: " + datestr + " не подходит" )

    @staticmethod
    def checkdata(dataday, datamonth, datayear):
        if not(datayear >= 1 and datayear <= 2500):
            raise ValueError( "Год заполнен некорректно" )
        if not(datamonth >= 1 and datamonth <= 12):
            raise ValueError( "Месяц заполнен некорректно" )
        if not(dataday >= 1 and dataday <= 31):
            raise ValueError( "День заполнен некорректно" )
        return True


try:
    d = DataClass('ДД-ММ-ГГГГ')
    print(d)
except Exception as e:
    print( e )

try:
    d = DataClass('09-02-3000')
    print(d)
except Exception as e:
    print( e )

try:
    d = DataClass('09-13-2021')
    print(d)
except Exception as e:
    print( e )

try:
    d = DataClass('32-02-2021')
    print(d)
except Exception as e:
    print( e )

try:
    d = DataClass('09-02-2021')
    print(d)
except Exception as e:
    print( e )