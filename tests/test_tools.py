import pytest
import json
import datetime

from ..project.utils.tools import json_serial


def test_serial():
    t = {'l': datetime.datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')}
    res = json.dumps(t, default=json_serial)
    class A:
        pass

    a = A()
    t = {'a': a}

    with pytest.raises(TypeError):
        json.dumps(t, default=json_serial)
