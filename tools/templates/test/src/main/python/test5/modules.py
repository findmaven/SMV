from smv import *

from integration.test.test5 import input

class M1(SmvModule, SmvOutput):
    def requiresDS(self):
        return [input.table]

    def run(self, i):
        return i[input.table]
