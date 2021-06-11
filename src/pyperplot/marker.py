

import yaml,re,shutil
import os

class Marker:
    def __init__(self,path,reset=False):
        """read marker setup file

        Parameters
        ----------
        path : str
            path to yml
        reset : bool
            clear all data in target folder, by default False
        """
        with open(path,'r') as f:
            self.y=yaml.load(f,Loader=yaml.Loader)
        
        self.figs=[]
        self.supp_figs=[]

        self.figure_type=self.y['figure_type']

        for k in self.y.keys():
            s=re.search("^fig\d+",k)
            if s is not None:
                self.figs.append(s[0])
        if 'supp' in self.y:
            for k in self.y.keys():
                s=re.search("^fig\d+",k)
                if s is not None:
                    self.supp_figs.append(s[0])
            self.ys=self.y['supp']

        self.origin=self.y['origin']
        self.target=self.y['target']
        self.stored_path=None
    def check(self,fname):
        if fname is not None:
            for f in self.figs:
                if isinstance(self.y[f],dict):
                    for annotation,path in self.y[f].items():
                        filename='-'.join(annotation) if isinstance(annotation,tuple)else annotation
                            
                        name=os.path.join(self.origin,path)

                        if os.path.normpath(fname)==os.path.normpath(f'{name}.{self.figure_type}'):
                            self.stored_path=(fname,os.path.join(self.target,f,f'{filename}.{self.figure_type}'))
                            return annotation
                elif isinstance(self.y[f],str):
                    path=self.y[f]
                    name=os.path.join(self.origin,path)
                    if os.path.normpath(fname)==os.path.normpath(f'{name}.{self.figure_type}'):
                        self.stored_path=(fname,os.path.join(self.target,f,f'{f}.{self.figure_type}'))
                        return None
                else:
                    raise Exception("illegal figure path")
            
            for f in self.supp_figs:
                if isinstance(self.ys[f],dict):
                    for annotation,path in self.ys[f].items():
                        filename='-'.join(annotation) if isinstance(annotation,tuple)else annotation    
                        name=os.path.join(self.origin,path)

                        if os.path.normpath(fname)==os.path.normpath(f'{name}.{self.figure_type}'):
                            self.stored_path=(fname,os.path.join(self.target,'supp',f,f'{annotation}.{self.figure_type}'))
                            return annotation
                elif isinstance(self.ys[f],str):
                    path=self.ys[f]
                    name=os.path.join(self.origin,path)
                    if os.path.normpath(fname)==os.path.normpath(f'{name}.{self.figure_type}'):
                        self.stored_path=(fname,os.path.join(self.target,'supp',f,f'{f}.{self.figure_type}'))
                        return None

                else:
                    raise Exception("illegal figure path")
        raise Exception("not detected situation")
    
    def store(self):
        if self.stored_path is not None:
            dir_name,_=os.path.split(self.stored_path[1])
            os.makedirs(dir_name,exist_ok=True)
            shutil.copy(*self.stored_path)
        


if __name__=='__main__':
    m=Marker('./marker_templates/marker_example.yml')
