
import numpy as np

'''
	(f)	    (t)
a	4514	486
b	4473	527
'''

def chi_test(td1):
    td1_suma = sum(td1[0,])
    td1_sumb = sum(td1[1,])
    td1_sum = td1.sum()

    #print(td1_sum, td1_suma, td1_sumb)

    pmat = td1 / td1_sum
    print(pmat)

    pa = td1_suma/td1_sum
    pb = td1_sumb/td1_sum
    pf = sum(td1[:,0])/td1_sum
    pt = sum(td1[:,1])/td1_sum

    epmat = np.array([[pa*pf, pa*pt],
                      [pb*pf, pb*pt]])

    print(epmat)

    #diff = pmat - epmat
    emat = epmat*td1_sum
    diff = td1 - emat
    diff_abs = np.abs(diff)
    # Yate’s chi-squared test is used instead: sum [ (abs(obs - exp) - 0.5) ^ 2 / exp ]
    chi_sq = np.divide(np.square(diff)-diff_abs+0.25, emat)
    print(chi_sq.sum())

td1 = np.array([[4514, 486],
                [4473, 527]])

chi_test(td1)
import scipy.stats as stats
print(stats.chi2_contingency(td1))

td2 = np.array([[17998, 2002],
                [17742, 2258]])

chi_test(td2)
print(stats.chi2_contingency(td2))





