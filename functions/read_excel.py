#coding:utf-8
import xlrd

class ReadExcel:

    def __init__(self,file_path):
        self.file_path=file_path
        print self.file_path

    def get_info(self):
        EL_data=xlrd.open_workbook(self.file_path)
        table=EL_data.sheet_by_name(u'Sheet1')
        #确定表格一共多少行数据
        user_info={}
        for i in xrange(table.nrows):
            rows_info=table.row_values(i)
            user_info[rows_info[0]]={'phone':str(rows_info[1]).split('.')[0],
                                     'pwd':str(rows_info[2]),'amount':str(rows_info[3]).split('.')[0]}
        return user_info


    def get_buy_product_info(self):
        EL_data=xlrd.open_workbook(self.file_path)
        table=EL_data.sheet_by_name(u'Sheet1')

        buyProduct_info={}
        for i in xrange(table.nrows):
            rows_info=table.row_values(i)
            buyProduct_info[rows_info[0]]={'phone':str(rows_info[1]).split('.')[0],
                                     'pwd':str(rows_info[2]),
                                     'amount':str(rows_info[3]).split('.')[0],
                                     'load_create':str(rows_info[4]),
                                     'times':str(rows_info[5]).split(".")[0],
                                     'exec':str(rows_info[6])}
        return buyProduct_info



if __name__=="__main__":
    readExcel=ReadExcel('D:\\quarkscript\\UFO_appium\\config\\buy_product_info.xls')
    buyProduct_info=readExcel.get_buy_product_info()
    if buyProduct_info['beauti']['phone']=='':
        print 111
    # print user_info['quarkZX']