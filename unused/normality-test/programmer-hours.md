-   Are these distributions actually normal?
-   Use `scipy.stats.normaltest` on the whole data and on weekdays and weekends separately
    -   Null hypothesis is that the distributions *are* normal

```shell
python bin/normality-test.py --data data/programmer-hours.csv
```
```text
all NormaltestResult(statistic=18.969090832509448, pvalue=7.601761895013466e-05)
weekdays NormaltestResult(statistic=29.1221331019309, pvalue=4.744704243550151e-07)
weekends NormaltestResult(statistic=11.62906792565243, pvalue=0.002983870598108047)
```

-   Reject the null hypothesis in each case
    -   I.e., this data is *not* normal
