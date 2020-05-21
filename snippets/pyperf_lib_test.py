# https://pyperf.readthedocs.io/en/latest/examples.html#examples
# pip install pyperf

import pyperf
import time


def func():
    time.sleep(0.001)


runner = pyperf.Runner()
runner.bench_func('sleep', func)
