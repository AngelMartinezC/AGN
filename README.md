# AGN
Codes to calculate Temperature and Density from the lines ratio of certain ions in the narrow line region of a given AGN

The python script takes into account the values from Osterbrock, 2006 


The script is based on the one written by de Robertis, Dufour, & Hunt (fivel.f). The paper explaining the fivel program can be found at Journal of the Royal Astronomical Society of Canada (ISSN 0035-872X), vol. 81, Dec. 1987, p. 195-220

There are two equations uesd to make the calculations, from ![2p2](https://latex.codecogs.com/gif.latex?2p%5E2)-like ions and ![2p3](https://latex.codecogs.com/gif.latex?2p%5E3)-like ions 

### Equations for ![2p2](https://latex.codecogs.com/gif.latex?2p%5E2)-like ions




The equation for the ion O[III] is:  

 ![oiii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7BDP%7D%7D%7Bj_%7BSD%7D%7D%3D0.054e%5E%7B32976/T%7D%5Cfrac%7B%5Cleft%5B%20%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D&plus;2.44%5Ctimes%2010%5E5%5Cleft%28%201&plus;0.1107e%5E%7B-32976/T%7D%20%5Cright%29%20%5Cright%5D%7D%20%7B%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D%20&plus;1692%7D)

While the equation for the ion N[II] is:

 ![nii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7BDP%7D%7D%7Bj_%7BSD%7D%7D%3D0.013e%5E%7B25000/T%7D%5Cfrac%7B%5Cleft%5B%20%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D&plus;1.07%5Ctimes%2010%5E5%5Cleft%28%201&plus;0.106e%5E%7B-25000/T%7D%20%5Cright%29%20%5Cright%5D%7D%20%7B%5Cfrac%7BNe%7D%7BT%5E%7B1/2%7D%7D%20&plus;171%7D)


### Equations for ![2p3](https://latex.codecogs.com/gif.latex?2p%5E3)-like ions


The equation for the ion S[II] is:

 ![sii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7B6716%7D%7D%7Bj_%7B6731%7D%7D%3D%5Cfrac%7B3A_%7B6716%7D%7D%7B2A_%7B6731%7D%7D%5Cleft%28%20%5Cfrac%7BN_e%20C&plus;0.26A_%7B6731%7D%7D%7BN_e%20C&plus;0.26A_%7B6716%7D%7D%20%5Cright%29)

And for the O[II] ion is:

 ![oii](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bj_%7B3726%7D%7D%7Bj_%7B3729%7D%7D%3D%5Cfrac%7B3A_%7B3726%7D%7D%7B2A_%7B3729%7D%7D%5Cleft%28%20%5Cfrac%7BN_e%20C&plus;1.60A_%7B3729%7D%7D%7BN_e%20C&plus;1.60A_%7B3726%7D%7D%20%5Cright%29)


## Graphs
