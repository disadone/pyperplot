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
    def __init__(self,figure_name=None,figures_folder='figs',figure_markers=None,figure_type='svg',style='neuron-plot',keep_titles=False,**fig_kwargs):
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
        figure_markers : str or list[str] or pyperplot Marker object, optional
            figure markers, such as 'A','B','C','D', by default None
        figure_type : str, optional
            the figure type
        style : str, optional
            path to files in folder {styles}, by default neuron-plot
        keep_titles : bool, optional
            whether to keep title or not, it only works when figure_name!=None, by default False
        fig_kwargs: dict, optional
            for parameters used in `matplotlib.pyplot.subplots`
        """
        self.old_style=mpl.rcParams # store old settings
        plt.style.use(styles_path[style])
        self.fig_folder=figures_folder
        self.fig_name=figure_name
        self.fig_type=figure_type
        self.fig_markers=figure_markers if figure_markers is not None else None
        self.keep_titles=keep_titles
        self.fig_kwargs=fig_kwargs

        self.saving_path=f'{self.fig_folder}/{self.fig_name}.{self.fig_type}'

        self.marked=False
        if not os.path.exists(self.fig_folder):
            os.mkdir(self.fig_folder)
    
    def __enter__(self):

        self.fig,self.axes=plt.subplots(**self.fig_kwargs)
        self._axes_arrayQ=isinstance(self.axes,np.ndarray)
        # if self.figure_markers is not None and self._axes_arrayQ:
        #     assert(self.figure_markers.shape==self.axes.shape)
        return self.fig,self.axes
    
    def __exit__(self,exc_type, exc_value, exc_traceback):
        
        if self.fig_markers is not None:
            if isinstance(self.fig_markers,list) or isinstance(self.fig_markers,np.ndarray):
                for i,ax in enumerate(self.axes.reshape(-1)):
                    ax.text(-0.15,1,self.fig_markers[i], transform=ax.transAxes, weight='bold')
            elif isinstance(self.fig_markers,str):
                self.axes.text(-0.15,1,self.fig_markers, transform=self.axes.transAxes, weight='bold')
            else: # marker object
                markers=self.fig_markers.check(self.saving_path)
                if isinstance(markers,tuple):
                    for i,ax in enumerate(self.axes.reshape(-1)):
                        ax.text(-0.15,1,markers[i], transform=ax.transAxes, weight='bold')
                else:
                    if self._axes_arrayQ:
                        ax=self.axes[0] if len(self.axes.shape)==1  else self.axes[0,0]
                    else:
                        ax=self.axes
                    ax.text(-0.15,1,markers, transform=ax.transAxes, weight='bold')
                self.marked=True
        
        if self.fig_name is not None:
            if not self.keep_titles:
                self.fig.suptitle('') # by default, remove suptitle in figure
                if not self._axes_arrayQ:
                    self.axes.set_title('') # by default, remove title in axes if there is a single axes
            self.fig.savefig(self.saving_path,format=self.fig_type,bbox_inches='tight')
            if self.marked:self.fig_markers.store()
        
        mpl.rcParams.update(self.old_style) # restore default settings

