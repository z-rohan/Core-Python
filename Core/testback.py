'''
from Bank import *

bal_check()
deposit(500)
bal_check()
withdrawal(1000)
bal_check()
'''

from Bank import *

bal_check(bal)
bal=deposit(500,bal)
bal_check(bal)
bal=withdrawal(1000,bal)
bal_check(bal)