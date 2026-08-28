*REPLICATION MATERIAL FOR "Foreign Policy Change in Latin America: Exploring a Middle-Range Concept"

use "FPCh(R&Red).dta", clear

* We first set countries as panel variable and the term as the time variable:

tsset ccode term

* In this article we are interested in change, so we calculate an indicator of change for the main variables in our analysis.
* To calculate change in any variable we substract the value of that variable in the new presidential term minus the value during
* the previous presidential (t0 - t-1). Since this value can sometimes be negative (and we are interested in absolute change instead of 
* its direction), then we square it and take its squareroot, which converts all our values to positive figures. 

*We do this with the variable ideology, since we expect the change in ideology (from president to president) to affect the change in foreign policy: 
* We calculate changes in the idology of the incumbent presidents.

gen presideochange = sqrt((ideology - L.ideology)^2)

* And in the ideology of her party:

gen partyideochange = sqrt((partyideo1 - L.partyideo1)^2)


* We are interested in creating a variable of foreign policy change. For that purpose, we first evaluate the extent to which 
* the dimmensions of foreign policy we are interested in can be aggregated in a single varlable. We use  principal component
* factors, iterated principal factors and a principal component correlation: 

factor economy geopolitics usa, pcf
factor economy geopolitics usa, ipf
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

gen fpchange = sqrt((foreignpolicy - L.foreignpolicy)^2)


* We now treat fpchange as our dependent variable and estimate three models:
* Model 1 (the Domestic Model) estimates the impact of domestic variables that may affect the change in foreign policy 
* the most obvious is the change in the ideology of the president, but also high levels of electoral volatility, strong presidents
* levels of democracy or the effect of a recent presidential crisis may incease the probability of fpchange.
* We specify the model as follows:

xtreg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism, fe robust
est store Model1

* Model 2 (the International Model) estimates the impact of international variables such as the end of the Cold War, 9/11,
* the change in the international economic environment and the level of U.S. and Chinese influence over each Latin American country,
* measured as a per capita specification of total trade with each of these two countries.

xtreg fpchange coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model2


* Finally, we estimate a final model (Model 3) combining the domestic and international factors that we found significant:

xtreg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model3

esttab Model1 Model2 Model3, se

* In Models 1 to 3 we are assuming our dependent variable in continuous, which is not striactly the case. Although fpchange does
* vary in a continuum from 0 to 1, its variation is bounded between 0 and 1, and its distribution is skewed towards 0 or non-change.

hist fpchange

* This problem cannot be easily solved by a logging our DV. This procedure is more likely to complicate the analysis. Although
* it serves as a robustness check to consider that the regressions still render similar results if we log the DV:

gen logfpchange = ln(fpchange)
hist logfpchange
xtreg logfpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust


* But using a logarithmic transformation of our DV is difficult to sustain susbtantively. 
* Also, a logistic approach (like a Logit or Probit model) would not be correct, given our distribution is not derived from 
* a dichotomous variable or, in other terms, is not derived from a Bernoulli probability distribution. Our DV is theoretically bounded 
* between 0 and 1 but we have no "ones" in our dataset.
* Given these reasons, we opt for running Beta regressions, a procedure that is fit for continuous variables bounded betweeen 0 and 1
* Beta regression is also  designed in the GLM framework to capture the kind of distribution of the DV we have shown in the histogram. 
* Beta regression estimators are available in Stata 14 (betareg), and in Stata 8 on throught the package "betafit" downloadable through ssc: 
 
ssc install betafit

* Using this MLE framework we rerun the aforementioned models as 1Beta 2Beta and 3Beta respectively

betafit fpchange, mu(presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism)
est store Model1Beta

betafit fpchange, mu(coldwar s11 gdpgth pctradeusa pctradechi)
est store Model2Beta

betafit fpchange, mu(presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi)
est store Model3Beta

esttab Model1Beta Model2Beta Model3Beta, se


* One can see the results using an OLS and GLM frameworks are consistent.
* Table 1 (the one we report in the article) is the following:

esttab Model1 Model1Beta Model2 Model2Beta Model3 Model3Beta, se


* Our Figures 6 and 7 come out of Model 3 (linear model) and Model3Beta, respectively.
* We start with the predictions of our linear model. 
* This is the code that generates the two linear predictions for our variable "ideologychange"

xtreg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust
quietly margins, at(presideochange = (0(0.1)4)) atmeans vsquish
marginsplot , recastci ( rline ) recast ( line ) ciopts ( lpattern ( dash ))
 
betafit fpchange, mu(presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi)
quietly margins, at(presideochange = (0(0.1)4)) atmeans vsquish
marginsplot , recastci ( rline ) recast ( line ) ciopts ( lpattern ( dash ))


* ROBUSTNESS CHECKS

 
* CHECK 1) As a first robustness check we run the same models with our initial components as dependent variables:
* To do so, we generate a measure of change for each of them: 

gen economychange = sqrt((economy - L.economy)^2)

gen usachange = sqrt((usa - L.usa)^2)

gen geochange = sqrt((geopolitics - L.geopolitics)^2)

* Then we run our same models with the individual components as dependent variables of nine new models.

xtreg economychange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism, fe robust
est store Model1A

xtreg economychange coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model2A

xtreg economychange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model3A

xtreg geochange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism, fe robust
est store Model1B

xtreg geochange coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model2B

xtreg geochange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model3B

xtreg usachange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism, fe robust
est store Model1C

xtreg usachange coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model2C

xtreg usachange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi, fe robust
est store Model3C


esttab Model1 Model1A Model1B Model1C, se

esttab Model2 Model2A Model2B Model2C, se 

esttab Model3 Model3A Model3B Model3C, se


* The results clearly reproduce our findings, which suggests that our aggregate measure is correctly estimated.
* Also, these analyses suggest that our finding are not being skewed by any particular component of our DD fpchange
* As a double check on this last point, see: 

corr fpchange geochange economychange usachange



* CHECK 2) To test for autocorrelation we run our models with a lagged dependent variable. Results do not change substantively.

xtreg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism L.fpchange, fe robust
est store Model1lagged

xtreg fpchange coldwar s11 gdpgth pctradeusa pctradechi L.fpchange, robust
est store Model2lagged

xtreg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi L.fpchange, fe robust
est store Model3lagged

esttab Model1lagged Model1Blagged Model2lagged, se

* CHECK 3) Non-linear relationships. Although our beta parameter already tells us the relations we are estimating are close to linear
* We test that assumption in a more conventional way too, by looking at the residuals of the model: 

reg fpchange presideochange partyideochange volatility shugart fh presinst publicsectorcorr radicalism coldwar s11 gdpgth pctradeusa pctradechi
rvfplot
rvpplot presideochange

* CHECK 4) Again, we take care of non-normality with our beta estimators, but the problem does not seem to be particularly important
* when we do the conventional tests: 

predict residuals, res
qnorm residuals

* CHECK 5) We do not have a multicollinearity problem for any of our variables
estat vif

* CHECK 6) Regarding outliers, a simple scatterplot suggests we do not need to worry: 

scatter fpchange presideochange

* Our analysis of the following statistics corroborates this: 
predict res, rstud
predict cd , cooksd
dfbeta

