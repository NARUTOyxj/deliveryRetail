import pytest
from tools.controlExcel import get_excel_data
from libs.login import Login
import os
class TestLogin:
    @pytest.mark.parametrize('inBody,expData',get_excel_data('../data/delivery.xls','登录模块','Login','请求参数','响应预期结果'))
    def test_login(self,inBody,expData):
        res = Login().login(inBody)
        print('用例执行')
        assert res['code'] == expData['code']


if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    os.system('allure serve ../report/tmp')



