import pytest


if __name__ == "__main__":
        for i in range(5):
                pytest.main(
                        [
                        '-s',
                        '-v',
                        'test_002_manage_shop.py::Test_remove_putaway_commodity'
                        ]
                )
                
        # 自助积分
        # for i in range(5):
        #         #会员注册
        #         # pytest.main(
        #         #         [
        #         #         '-s',
        #         #         '-v',
        #         #         'test_001_manage_member.py::test_member_register'
        #         #         ]
        #         # )
        #         #查询会员
        #         pytest.main(
        #                 [
        #                 '-s',
        #                 '-v',
        #                 'test_001_manage_member.py::Test_select_vipdata'
        #                 ]
        #         )
        #         #查询会员卡
        #         pytest.main(
        #                 [
        #                 '-s',
        #                 '-v',
        #                 'test_001_manage_member.py::Test_get_vipcard'
        #                 ]
        #         )
        #         #积分规则
        #         pytest.main(
        #                 [
        #                 '-s',
        #                 '-v',
        #                 'test_004_manage_integral.py'
        #                 ]
        #         )
        #         #小票上传积分
        #         pytest.main(
        #                 [
        #                 '-s',
        #                 '-v',
        #                 'test_005_wx_index.py::Test_upload_receipt'
        #                 ]
        #         )
        #         #获取积分明细
        #         pytest.main(
        #                 [
        #                 '-s',
        #                 '-v',
        #                 'test_006_wx_my.py::Test_wx_my::test_get_integral_statistics'
        #                 ]
        #         )