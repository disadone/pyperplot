# pyperplot



matplotlibrc files for different journals.

you should set the `legend` parameter `bbox_to_anchor=(1,1)` for all graphs

intallation

```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyperplot --upgrade
```
or
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyperplot --upgrade
```

example

```python
import pyperplot as ppp

with ppp.SF('hello',nrows=2) as (fig,axes):
    axes[0].plot([1,2,3])
    axes[1].plot([3,2,1])
```
or 

```python
import pyperplot as ppp

with ppp.SF('hello',figure_folder='figs',figure_type='svg',style='neuron-plot',nrows=2) as (fig,axes):
    axes[0].plot([1,2,3])
    axes[1].plot([3,2,1])
```
A file named 'hello.svg' should be generated in a folder named 'figs' automatically created.

see (unfinished) [documentation](https://pyperplot.readthedocs.io/en/latest/)