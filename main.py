import pytest
import datetime


if __name__ == "__main__":
        now_time='%s' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        pytest.main(
                        [
                        'conftest/',
                        '-v',
                        '--html=./report/NEWCRM__%s.html' % now_time,
                        '--self-contained-html'
                        ]
                )


