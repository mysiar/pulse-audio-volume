import unittest
import pulsectl
from var_dump import var_dump

class MyTestCase(unittest.TestCase):
    def test_something(self):

        with pulsectl.Pulse('volume-increaser') as pulse:
            for sink in pulse.sink_list():
                # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
                # pulse.volume_change_all_chans(sink, 0.1)
                var_dump(sink.name)
                var_dump(sink.description)


if __name__ == '__main__':
    unittest.main()
