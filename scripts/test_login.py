import pytest
class Testlogin():

    @pytest.mark.xfail(1==1,reason = '相等')
    @pytest.mark.run(order=2)
    def test_login_001(self):
        print('test002')
        assert 1

    # @pytest.mark.skipif(1==1,reason = '相等')
    @pytest.mark.skipif(True, reason='...')
    @pytest.mark.run(order=1)
    def test_login_002(self):
        print('test001')
        assert 1


    def test_login_003(self):
        print('test001')
        assert 1
        

    def test_login_004(self):
        print('test001')
        assert 1

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])