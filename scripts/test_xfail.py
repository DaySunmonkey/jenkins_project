import pytest


class TestLogin:

    # 预期成功 结果成功
    # 预期成功 结果失败
    # 预期失败 结果成功
    # 预期失败 结果失败

    # 报告为红色的提示，预期和实际结果不符
    # 预期和实际结果相符的情况下，如果是通过，那么是绿色，如果是失败，那么是橙色
    # 预期失败前面会有 X，如果通过了，那么就是Xpass
    # 预期失败前面会有 X，如果失败了，那么就是Xfail
    # 预期成功前面不会有 X，如果通过了，那么就是pass
    # 预期成功前面不会有 X，如果失败了，那么就是fail

    # 预期成功 结果成功
    @pytest.mark.xfail(condition=False, reason="xx")
    def test_login1(self):
        assert 1

    # 预期成功 结果失败
    @pytest.mark.xfail(condition=False, reason="xx")
    def test_login2(self):
        assert 0

    # 预期失败 结果成功
    @pytest.mark.xfail(condition=True, reason="xx")
    def test_login3(self):
        assert 1

    # 预期失败 结果失败
    @pytest.mark.xfail(condition=True, reason="xx")
    def test_login4(self):
        assert 0
