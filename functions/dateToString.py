import datetime

class dateToString(object):

    def get_strTotime(self,str,format="%Y-%m-%d %H:%M:%S"):
        """
        :param str: '2017-06-13 16:00:00'
        :param format:  "%Y-%m-%d %H:%M:%S"
        :return:
        """
        return datetime.datetime.strptime(str,format ).date()


    def get_adddate(self,data):
        """
        :param data:
        :return:
        """
        return  data+datetime.timedelta(days=1)






if __name__ == '__main__':
    a=dateToString()
    time1='2017-06-13 16:00:00'
    b=a.get_strTotime(time1)
    c=a.get_adddata(b)
    print  c


