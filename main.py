def ply_thk(density, sfc_weight, fvf):
    return round((sfc_weight / density * (1 + (1 - fvf) / fvf) / 1000), 2)


def laminate_thk(dataframe, column):
    return round(dataframe[column].sum(), 2)


def get_density(material):
    material_density = {
        'Glass Fiber E-type': 2.61,
        'Carbon Fiber': 1.8,
        'Flux': 1.3,
        'Aramid': 1.45,
        'Epoxy': 1.13,
        'Vinylester': 1,
        'Polyurethane': 1.3,
        'Polyester': 1.2}
    return material_density.get(material)


def laminate_density(fib_den, mat_den, fvf):
    return round((fib_den * fvf) + (mat_den * (1 - fvf)), 2)


def aerial_weight(fib_den, mat_den, fvf, lam_thk):
    return round(laminate_density(fib_den, mat_den, fvf) * lam_thk, 2)


def volume_to_weight_fraction(fib_den, lam_den, fvf):
    return round(fvf * (fib_den / lam_den), 2)


def resin_intake(fib_den, mat_den, fvf, lam_thk):
    lam_weight = aerial_weight(fib_den, mat_den, fvf, lam_thk)
    lam_den = laminate_density(fib_den, mat_den, fvf)
    resin_fraction = 1 - volume_to_weight_fraction(fib_den, lam_den, fvf)

    return round(lam_weight * resin_fraction, 2)
