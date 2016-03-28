# from tasks import add
# add.delay(4, 4)

import sys
sys.path.append("..")

from proj import tasks
tasks.arch.delay(1,2)