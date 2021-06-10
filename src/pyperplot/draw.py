import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
aa=np.asarray
import os
import string

from .settings import styles_path


class SF(object):
    """
    save figure context
    """
    def __init__(self,figure_name=None,figures_folder='figs',figure_type='svg',figure_markers=None,style='neuron-plot',keep_titles=False,**fig_kwargs):
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
        figure_markers : str or list[str], optional
            figure markers, such as 'A','B','C','D', by default None
        style : str, optional
            path to files in folder {styles}, by default neuron-plot
        keep_titles : bool, optional
            whether to keep title or not, it only works when figure_name!=None, by default False
        fig_kwargs: dict, optional
            for parameters used in `matplotlib.pyplot.subplots`
        """
        self.old_style=mpl.rcParams # store old settings
        plt.style.use(styles_path[style])
        self.figure_folder=figures_folder
        self.figure_name=figure_name
        self.figure_type=figure_type
        self.figure_markers=aa(figure_markers)
        self.keep_titles=keep_titles
        self.fig_kwargs=fig_kwargs

        if not os.path.exists(self.figure_folder):
            os.mkdir(self.figure_folder)
    
    def __enter__(self):

        self.fig,self.axes=plt.subplots(**self.fig_kwargs)
        self._axes_arrayQ=isinstance(self.axes,np.ndarray)
        if self._axes_arrayQ:
            assert(self.figure_markers.shape==self.axes.shape)
        return self.fig,self.axes
    
    def __exit__(self,exc_type, exc_value, exc_traceback):
        if self._axes_arrayQ:
            for i,ax in enumerate(self.axes.reshape(-1)):
                ax.text(-0.15,1,self.figure_markers[i], transform=ax.transAxes, weight='bold')
        else:
            self.axes.text(-0.15,1,self.figure_markers, transform=self.axes.transAxes, weight='bold')
        
        if not (self.figure_name is None):
            if self.keep_titles:
                self.fig.suptitle('') # by default, remove suptitle in figure
                if not self._axes_arrayQ:
                    self.axes.set_title('') # by default, remove title in axes if there is a single axes
            self.fig.savefig(f'{self.figure_folder}/{self.figure_name}.{self.figure_type}',format=self.figure_type,bbox_inches='tight')
        mpl.rcParams.update(self.old_style) # restore default settings

