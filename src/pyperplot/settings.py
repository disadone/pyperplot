import os

directory=os.path.dirname(__file__)

styles_name=['neuron-plot','neuron-mat','neuron-multiplot']
styles_path={}
for s in styles_name:
    styles_path[s]=os.path.join(directory,f'./styles/{s}.mplstyle')