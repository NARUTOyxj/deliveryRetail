import xlrd
import json

def is_json(str1):
    try:
        json.loads(str1)
    except ValueError:
        return False
    return True

def get_excel_data(excelDir,sheetName,caseName,*args,runCase = ['all']):
    resList = []  # 存放结果
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # workbook  是一个xx.xl文件对象
    workSheet = workBook.sheet_by_name(sheetName)
    colIdex = []  # 存放用户需要获取列名对应的列编号
    for i in args:  # 遍历元组
        colIdex.append(workSheet.row_values(0).index(i))  # 获取列表对应的下标
    # 5- 筛选用例

    runList = []  # 最后的运行列表
    if runCase[0] == 'all':  # 全部运行！
        runList = workSheet.col_values(0)  # 第一列所有的数据
    else:  # 如果不是all
        # 连续的 001-003
        # 不连续 001,005
        for one in runCase:  # ['001','004-008']
            if '-' in one:  # for 004 005 006 007 008
                start, end = one.split('-')  # 获取连续用例编号的头尾
                for i in range(int(start), int(end) + 1):
                    runList.append(caseName + f'{i:0>3}')
            else:
                runList.append(caseName + f'{one:0>3}')  # Login001

    idx = 0  # 行的初始值
    for one in workSheet.col_values(0):  # 对第一列数据进行遍历
        if caseName in one and one in runList:  # 说明这个用例是符合要求的
            getColData = []  # 这行代码必须要，每一次需要初始化
            # 读取对应的数据
            for num in colIdex:
                # workSheet.cell(行号，列号).value  前提是json
                # 如果是json字符串，就传话成字典，不是就不操作
                res = workSheet.cell(idx, num).value
                # if res[0] == '{' and res[-1] == '}':
                if is_json(res):  # 判断是不是json
                    res = json.loads(res)  # 获取单元格数据
                getColData.append(res)  # 把用户需要读取的列数据，append到一个列表
            resList.append(getColData)  # 获取所有符合要求的用例数据
        idx += 1  # 行编号变化
    return resList

if __name__ == '__main__':
    res = get_excel_data('../data/delivery.xls', '登录模块','Login','用例编号', 'URL')
    # print(res)
    for one in res:
        print(one)
