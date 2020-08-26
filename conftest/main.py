import pytest


if __name__ == "__main__":
    for i in range(10):
        pytest.main(
                        [
                        '-s',
                        '-v',
                        'test_003_wx_index.py::Test_integral_shop_commodity'
                        ]
                )
        pytest.main(
                        [
                        '-s',
                        '-v',
                        'test_003_wx_index.py::Test_integral_shop_order'
                        ]
                )
        pytest.main(
                        [
                        '-s',
                        '-v',
                        'test_004_wx_my.py::test_get_order_page'
                        ]
                )
        pytest.main(
                        [
                        '-s',
                        '-v',
                        'test_005_check_system.py::Test_check::test_order_check'
                        ]
                )
