symbols = "H,He,Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe,Cs,Ba,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu,Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn,Fr,Ra,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr,Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og".split(
    ","
)

symbol_set = set(symbol.lower() for symbol in symbols)


def decompose_into_symbols(s: str):
    filtered_string = "".join(filter(str.isalpha, s)).lower()
    memo = {}

    def can_decompose(start):
        if start in memo:
            return memo[start]
        if start == len(filtered_string):
            return []

        if filtered_string[start : start + 1] in symbol_set:
            result = can_decompose(start + 1)
            if result is not None:
                memo[start] = [filtered_string[start : start + 1]] + result
                return memo[start]

        if (
            start + 1 < len(filtered_string)
            and filtered_string[start : start + 2] in symbol_set
        ):
            result = can_decompose(start + 2)
            if result is not None:
                memo[start] = [filtered_string[start : start + 2]] + result
                return memo[start]

        memo[start] = None
        return None

    decomposition = can_decompose(0)
    return (
        [s.capitalize() for s in decomposition] if decomposition is not None else False
    )
