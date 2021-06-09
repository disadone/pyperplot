# styles

matplotlibrc files for different journals.

you should set the `legend` parameter `bbox_to_anchor=(1,1)` for all graphs

example

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('./neuron.mplstyle')

x=np.arange(100)
y1=np.arange(100)
y2=0.5*y1
y3=0.2*y1**(1.2)
y4=np.sqrt(y1)

plt.plot(x,y1,label='really long sentence, a=123')
plt.plot(x,y2,label='really not short sentence,\nb=2345')
plt.plot(x,y3)
plt.plot(x,y4)

plt.xlabel('something called $e^x$')
plt.ylabel('something called y')
plt.axvspan(8,20,alpha=0.5)
plt.legend()
plt.show()
```
