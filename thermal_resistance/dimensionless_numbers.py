# Renolds Number dimensionless
def Re_1(rho_kg_m3,u_m_s,L_m):
    return rho_kg_m3 * u_m_s * L_m
# Prandl Number
def Pr_1(Cp_J_kgK, lambda_W_mK, mu_Pas):
    return Cp_J_kgK * mu_Pas / lambda_W_mK
