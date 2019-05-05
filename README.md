# AGN
Codes to calculate Temperature [K] and Density [particle/cm^3] from the lines ratio of certain ions in the narrow line region of a given AGN. 

The python script takes the values for Einstein Coefficients, collision strength, and statistical weights from [Osterbrock, 2006](http://adsabs.harvard.edu/abs/2006agna.book.....O).
The script is based on the one written by de Robertis, Dufour, & Hunt (fivel.f). The paper explaining the fivel program can be found at [Journal of the Royal Astronomical Society of Canada](http://adsabs.harvard.edu/abs/1987JRASC..81..195D).

---
## Lines_ratio

### Usage and calling sequence

If the program is called as a python module, the calling proccedure is like:
```python
import lines_ratio as lr
  
name = 'data/spec-1070-52591-0072.fits' #Example of .fits data
T, Ne = lr.calculation(name=name)

print("  Temperature  {}\n  Density      {}".format(T,Ne))
```
Here the user will be ased for the ions to make the calculations if they are not specified. Avaliable ions are (O[III] or N[II]) and (S[II] or O[II]) (see Ions example below).  It returns T and Ne, the temperature and particle density in [K] and [particle/cm^3] respectively, of the narrow line region from an AGN.

---
There are two equations used to make the calculations, from ![2p2](https://latex.codecogs.com/gif.latex?2p%5E2)-like ions and ![2p3](https://latex.codecogs.com/gif.latex?2p%5E3)-like ions 


### Ions examples:

1. Equations for ![2p2](https://latex.codecogs.com/gif.latex?2p%5E2)-like ions

   The equation for the ion O[III] is:  

     ![oiii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7BDP%7D%7D%7Bj_%7BSD%7D%7D%3D0.054e%5E%7B32976/T%7D%5Cfrac%7B%5Cleft%5B%20%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D&plus;2.44%5Ctimes%2010%5E5%5Cleft%28%201&plus;0.1107e%5E%7B-32976/T%7D%20%5Cright%29%20%5Cright%5D%7D%20%7B%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D%20&plus;1692%7D)

   While the equation for the ion N[II] is:

     ![nii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7BDP%7D%7D%7Bj_%7BSD%7D%7D%3D0.013e%5E%7B25000/T%7D%5Cfrac%7B%5Cleft%5B%20%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D&plus;1.07%5Ctimes%2010%5E5%5Cleft%28%201&plus;0.106e%5E%7B-25000/T%7D%20%5Cright%29%20%5Cright%5D%7D%20%7B%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D%20&plus;171%7D)


2. Equations for ![2p3](https://latex.codecogs.com/gif.latex?2p%5E3)-like ions

   The equation for the ion S[II] is:

     ![sii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7B6716%7D%7D%7Bj_%7B6731%7D%7D%3D%5Cfrac%7B3A_%7B6716%7D%7D%7B2A_%7B6731%7D%7D%5Cleft%28%20%5Cfrac%7BN_e%20C&plus;0.26A_%7B6731%7D%7D%7BN_e%20C&plus;0.26A_%7B6716%7D%7D%20%5Cright%29)

   And for the O[II] ion is:

     ![oii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7B3726%7D%7D%7Bj_%7B3729%7D%7D%3D%5Cfrac%7B3A_%7B3726%7D%7D%7B2A_%7B3729%7D%7D%5Cleft%28%20%5Cfrac%7BN_e%20C&plus;1.60A_%7B3729%7D%7D%7BN_e%20C&plus;1.60A_%7B3726%7D%7D%20%5Cright%29)


## Graphs

![2p2](plots/2p2.png)  
![2p3](plots/2p3.png)

![gaussian](plots/1gaussian.png)

