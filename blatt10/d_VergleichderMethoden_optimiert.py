lst_est_ml = []
lst_est_kq = []

for x in range(0, 501):
    a = createData(0.5, 1000, np.random.randint(0, high=100000, dtype=int))
    n1, bins1 = np.histogram(a, listOfBins(min(a), max(a), 10))
    xcenters1 = (bins1[:-1] + bins1[1:])/2
    b = opt.minimize(negLogLik, args=(expFunc, a),
                     x0=0.5, bounds=[(1e-10, None)])
    if b.success == True:
        lst_est_ml.append(b.x[0])
        c = opt.least_squares(S, x0=0.5, args=(n1, xcenters1))
        if c.success == True:
            lst_est_kq.append(c.x[0])
