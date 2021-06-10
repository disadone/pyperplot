        
import unittest
import matplotlib as mpl
from pyperplot import SF

class TestSFWith(unittest.TestCase):
    
    def test_StyleRestore(self):
        old_style=mpl.rcParams
        with SF() as (fig,axes):
            axes.plot([1,2,3])
        new_style=mpl.rcParams
        self.assertEqual(old_style,new_style)
    
        