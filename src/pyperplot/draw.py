

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os

from .settings import styles_path


class SF(object):
    """
    save figure context
    """
    def __init__(self,figure_name=None,figures_folder='figs',figure_type='svg',style='neuron-plot',keep_titles=False,**fig_kwargs):
        """
        context that creates figures with given matplotlib style
        svg is the default format

        Parameters
        ----------
        figure_name : None or str, optional
            figure name, by default None
            if None, figure is not saved
        figures_folder : str, optional
            the folder to save figures, by default 'figs'
        figure_type : str, optional
            the figure type
        style : str, optional
            path to files in folder {styles}, by default neuron-plot
        keep_titles : bool, optional
            whether to keep title or not, by default False
        """
        self.old_style=mpl.rcParams # store old settings
        plt.style.use(styles_path[style])
        self.figure_folder=figures_folder
        self.figure_name=figure_name
        self.figure_type=figure_type
        self.fig_kwargs=fig_kwargs
        if not os.path.exists(self.figure_folder):
            os.mkdir(self.figure_folder)
    
    def __enter__(self):
        self.fig,self.axes=plt.subplots(**self.fig_kwargs)
        return self.fig,self.axes
    
    def __exit__(self,exc_type, exc_value, exc_traceback):
        # plt.tight_layout()
        if not (self.figure_name is None):
            self.fig.suptitle('') # by default, remove suptitle in figure
            if not isinstance(self.axes,np.ndarray):
                self.axes.set_title('') # by default, remove title in axes if there is a single axes
            self.fig.savefig(f'{self.figure_folder}/{self.figure_name}.{self.figure_type}',format=self.figure_type,bbox_inches='tight')
        mpl.rcParams.update(self.old_style) # restore default settings

#%%
if __name__=='__main__':
    print(__file__)
