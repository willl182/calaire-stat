# Evidencias locales M12 (pdftotext -layout)

Extracción y lectura: 25-10-2026. Los fragmentos respaldan numerales. Las ecuaciones del CFR son imágenes: además de pdftotext se leyeron visualmente las páginas PDF 18–20 con Read. Ecuación 1: (meas−audit)/audit ×100; ecuación 2: s_d × raíz[(n−1)/chi-cuadrado inferior 0,10]; ecuaciones 3–5: AB+t_0,95 AS/raíz(n), AB media absoluta y AS desviación muestral de valores absolutos. Coinciden con el libreto y el script. Percentiles de signo confirmados en p.20.

Fuente externa comprobada con WebFetch el 25-10-2026: NIST/SEMATECH, https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm, apartado 1.3.5.8, Chi-Square Test for the Variance; presenta límites de confianza de varianza y sus raíces para desviación estándar. No confundir la cola de una prueba unilateral de varianza con el cuantil que aparece en un límite superior para la desviación.


## M12_fuente_CFR.txt


### 2.3.1.2, línea extraída 252

```text
                    2.3.1.2 Measurement Uncertainty for Automated O3 Methods. The goal for acceptable
                           measurement uncertainty is defined for precision as an upper 90 percent confidence limit
                           for the CV of 7 percent and for bias as an upper 95 percent confidence limit for the
                           absolute bias of 7 percent.

```


### 4.1.1 Percent, línea extraída 1042

```text
4.1.1 Percent Difference. Many of the measurement quality checks start with a comparison of an audit
concentration or value (flow rate) to the concentration/value measured by the monitor and use percent difference
as the comparison statistic as described in equation 1 of this section. For each single point check, calculate the
percent difference, di, as follows:




where meas is the concentration indicated by the PQAO's instrument and audit is the audit concentration of the
standard used in the QC check being measured.

4.1.2 Precision Estimate. The precision estimate is used to assess the one-point QC checks for SO2, NO2, O3, or CO
described in section 3.1.1 of this appendix. The precision estimator is the coefficient of variation upper bound and
is calculated using equation 2 of this section:
```


### 4.1.2 Precision, línea extraída 1053

```text
4.1.2 Precision Estimate. The precision estimate is used to assess the one-point QC checks for SO2, NO2, O3, or CO
described in section 3.1.1 of this appendix. The precision estimator is the coefficient of variation upper bound and
is calculated using equation 2 of this section:




40 CFR Appendix-A-to-Part-58 4.(c)(5) (enhanced display)                                                 page 18 of 26

Appendix A to Part 58, Title 40 (up to date as of 10/20/2026)
                                                                                   40 CFR Appendix-A-to-Part-58 4.(c)(5)
Quality Assurance Requirements for Monitors used in Evaluations of...




where n is the number of single point checks being aggregated; X20.1,n-1 is the 10th percentile of a chi-squared
distribution with n-1 degrees of freedom.

```


### 4.1.3 Bias, línea extraída 1072

```text
4.1.3 Bias Estimate. The bias estimate is calculated using the one-point QC checks for SO2, NO2, O3, or CO described
in section 3.1.1 of this appendix. The bias estimator is an upper bound on the mean absolute value of the percent
differences as described in equation 3 of this section:




where n is the number of single point checks being aggregated; t0.95,n-1 is the 95th quantile of a t-distribution with
n-1 degrees of freedom; the quantity AB is the mean of the absolute values of the di ′ s and is calculated using
equation 4 of this section:




and the quantity AS is the standard deviation of the absolute value of the di ′ s and is calculated using equation 5 of
this section:




40 CFR Appendix-A-to-Part-58 4.(c)(5) (enhanced display)                                                    page 19 of 26

Appendix A to Part 58, Title 40 (up to date as of 10/20/2026)
                                                                                   40 CFR Appendix-A-to-Part-58 4.(c)(5)
Quality Assurance Requirements for Monitors used in Evaluations of...


4.1.3.1 Assigning a sign (positive/negative) to the bias estimate. Since the bias statistic as calculated in equation 3
of this appendix uses absolute values, it does not have a tendency (negative or positive bias) associated with it. A
sign will be designated by rank ordering the percent differences of the QC check samples from a given site for a
particular assessment interval.

4.1.3.2 Calculate the 25th and 75th percentiles of the percent differences for each site. The absolute bias upper
bound should be flagged as positive if both percentiles are positive and negative if both percentiles are negative.
The absolute bias upper bound would not be flagged if the 25th and 75th percentiles are of different signs.
```


### 4.1.3.1 Assigning, línea extraída 1099

```text
4.1.3.1 Assigning a sign (positive/negative) to the bias estimate. Since the bias statistic as calculated in equation 3
of this appendix uses absolute values, it does not have a tendency (negative or positive bias) associated with it. A
sign will be designated by rank ordering the percent differences of the QC check samples from a given site for a
particular assessment interval.

4.1.3.2 Calculate the 25th and 75th percentiles of the percent differences for each site. The absolute bias upper
bound should be flagged as positive if both percentiles are positive and negative if both percentiles are negative.
The absolute bias upper bound would not be flagged if the 25th and 75th percentiles are of different signs.

4.2 Statistics for the Assessment of PM10, PM2.5, and Pb.

4.2.1 Collocated Quality Control Sampler Precision Estimate for PM10, PM2.5, and Pb. Precision is estimated via
```


## M12_fuente_EN.txt


### 3.12, línea extraída 412

```text
3.12
detection limit
smallest concentration of a measurand that can be reliably detected by a specific measurement process

Note 1 to entry:  The detection limit is calculated as 3,3 x (sz/B) where sz is the standard deviation of analyser response at
zero measurand concentration (see 8.4.5) and B is the slope of the calibration function [3].

3.13
expanded uncertainty
```


### 8.4.5         Repeatability, línea extraída 1436

```text
8.4.5         Repeatability standard deviation

After waiting the time equivalent of one independent reading 20, individual measurements both at zero
concentration and at a test concentration (ct) similar to the hourly alert threshold value shall be performed.

From these measurements, the repeatability standard deviation (sr) at zero concentration and at concentration ct
(hourly alert threshold value) shall be calculated according to:


         ∑ (x − x )             2
                         i
     s =  r                                                                                                                        (4)
                       n −1

where

     sr            is the repeatability standard deviation, in nmol/mol;

     xi            is the ith measurement, in nmol/mol;

        x          is the average of the 20 measurements, in nmol/mol;

     n             is the number of measurements, n =,20.




                                                                                                                                   23

BS EN 14625:2012
EN 14625:2012 (E)



The repeatability standard deviation shall be calculated separately for both series of measurements (zero gas and
concentration ct).

sr shall comply with the performance criterion in Table 1, both at zero and at the test concentration ct (hourly alert
threshold value).

The repeatability standard deviation at zero is used in combination with the slope of the calibration function
determined in 8.4.6 to calculate the detection limit of the analyser as [3]:

                       sz
                        ,
                        r
     l       = 3,3 ⋅
         t
                                                                                                                                (5)
         e
         d
                        B
where

     ldet         is the detection limit of the analyser, in nmol/mol;

     sr,z        is the repeatability standard deviation at zero, in nmol/mol;

```


## M12_fuente_GUM.txt


### 4.2.2 The individual, línea extraída 1027

```text
4.2.2 The individual observations qk differ in value because of random variations in the influence quantities,
or random effects (see 3.2.2). The experimental variance of the observations, which estimates the variance
σ 2 of the probability distribution of q, is given by
                             n
                             ∑(       )
                        1               2
        s 2 (qk ) =              qj − q                                                                                          (4)
                      n − 1 j =1

This estimate of variance and its positive square root s(qk), termed the experimental standard deviation
(B.2.17), characterize the variability of the observed values qk , or more specifically, their dispersion about their
mean q .

4.2.3      The best estimate of σ 2 ( q ) = σ 2 n , the variance of the mean, is given by

                    s 2 ( qk )
        s2 (q ) =                                                                                                                (5)
                         n

The experimental variance of the mean s 2 ( q ) and the experimental standard deviation of the mean s ( q )
(B.2.17, Note 2), equal to the positive square root of s 2 ( q ), quantify how well q estimates the expectation µq
of q, and either may be used as a measure of the uncertainty of q .

Thus, for an input quantity Xi determined from n independent repeated observations Xi,k , the standard
uncertainty u(xi) of its estimate x i = X i is u ( x i ) = s ( X i ) , with s 2 ( X i ) calculated according to Equation (5). For
```


### 5.2.1 Equation, línea extraída 1687

```text
5.2.1 Equation (10) and those derived from it such as Equations (11a) and (12) are valid only if the input
quantities Xi are independent or uncorrelated (the random variables, not the physical quantities that are
assumed to be invariants — see 4.1.1, Note 1). If some of the Xi are significantly correlated, the correlations
must be taken into account.

5.2.2 When the input quantities are correlated, the appropriate expression for the combined variance u c2 ( y)
associated with the result of a measurement is

                      N N                                        N         2              N −1 N
                              ∂f ∂f                     ⎛ ∂f ⎞ 2                        ∂f ∂f
      u c2    ( y) = ∑∑       ∂x ∂x j
                                              (
                                      u xi , x j =      ⎜  ) ∑
                                                          ∂x
                                                             ⎟ u ( xi ) + 2                ∑∑
                                                                                        ∂x ∂x j
                                                                                                       (
                                                                                                u xi , x j     )                 (13)
                     i =1 j =1 i                   i =1 ⎝ i ⎠               i =1 j =i +1 i

where xi and xj are the estimates of Xi and Xj and u(xi, xj) = u(xj, xi) is the estimated covariance associated
with xi and xj. The degree of correlation between xi and xj is characterized by the estimated correlation
coefficient (C.3.6)

```


### G.3.2 If z, línea extraída 4871

```text
G.3.2 If z is a normally distributed random variable with expectation µ z and standard deviation σ, and z is
the arithmetic mean of n independent observations zk of z with s ( z ) the experimental standard deviation of z
[see Equations (3) and (5) in 4.2], then the distribution of the variable t = ( z − µ z ) s ( z ) is the t-distribution or
Student's distribution (C.3.8) with v = n − 1 degrees of freedom.

Consequently, if the measurand Y is simply a single normally distributed quantity X, Y = X; and if X is estimated
by the arithmetic mean X of n independent repeated observations Xk of X, with experimental standard
deviation of the mean s ( X ), then the best estimate of Y is y = X and the experimental standard deviation of
that estimate is u c ( y) = s ( X ). Then t = ( z − µ z ) s ( z ) = ( X − X ) s ( X ) = ( y − Y ) u c ( y ) is distributed according to
the t-distribution with

     Pr ⎡⎣ − t p ( v ) u t u t p ( v ) ⎤⎦ = p                                                                                  (G.1a)

or

     Pr ⎡⎣ − t p ( v ) u ( y − Y ) u c ( y ) u t p ( v ) ⎤⎦ = p                                                                (G.1b)

which can be rewritten as

     Pr ⎡⎣ y − t p ( v ) u c ( y ) u Y u y + t p ( v ) u c ( y ) ⎤⎦ = p                                                        (G,1c)

In these expressions, Pr[ ] means “probability of” and the t-factor tp(v) is the value of t for a given value of
the parameter v — the degrees of freedom (see G.3.3) — such that the fraction p of the t distribution is
encompassed by the interval −tp(v) to +tp(v). Thus the expanded uncertainty

     Up = k p u c ( y ) = tp ( v ) u c ( y )                                                                                   (G.1d)

defines an interval y − Up to y + Up, conveniently written as Y = y ± Up, that may be expected to encompass a
fraction p of the distribution of values that could reasonably be attributed to Y, and p is the coverage probability
or level of confidence of the interval.

G.3.3 The degrees of freedom v is equal to n − 1 for a single quantity estimated by the arithmetic mean of
```
