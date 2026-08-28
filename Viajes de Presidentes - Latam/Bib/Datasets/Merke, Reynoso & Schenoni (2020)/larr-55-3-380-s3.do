*PRINCIPAL COMPONENT AGGREGATION

use "FPCh(R&Red).dta", clear

* We first set countries as panel variable and the term as the time variable:

tsset ccode term

* We are interested in estimating a latent variable of foreign policy orientation in what we call a "liberal non-liberal" continuum. 
* For that purpose, we first evaluate the extent to which the dimmensions of foreign policy we are interested in can be aggregated in a single varlable. 
* We start by simply analysins the correlation structure in our data. 

corr economy geopolitics usa

* This measure already reveals these are highly correlated with each other.
* We use  principal component factors first: and a principal component correlation: 

factor economy geopolitics usa, pcf

* Iterated principal factors: 

factor economy geopolitics usa, ipf

* Principl component analysis: 

pca economy geopolitics usa, mineig(1)

* All estimators indicate that the variables load high in one factor with Eigenvalues over 2.5

screeplot, yline(1)

* To check if we are accounting for a fair degree of common variance, we use a Kaiser-Meyer-Olkin measure of sampling adequacy:

estat kmo

* A result of 0.72 shows that we are acconting for a "fair" amount of variance, surpassing the minimum required by Kaiser, Meyer and Olkin.
* The next step is to aggregate dimmensions into one single measure of foreign policy.
* We do it by first creating the predicted values of the aggregated variable "INDEX"

predict INDEX

* We then transform INDEX (which has negative values that complicate the forthcoming aritmethics) into a normalized scale from 0 to 1: 

egen min_INDEX1 =min(INDEX)
egen max_INDEX1 =max(INDEX)
gen foreignpolicy=(INDEX-min_INDEX1)/(max_INDEX1-min_INDEX1)

* In this way we've come to an aggregated variable of "foreignpolicy" which will be the basis for the creation of our dependent variable. 
* All we need to do now is to calculate the change in foreign policy as we did with ideological change before:
