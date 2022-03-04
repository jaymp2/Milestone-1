# -*- coding: utf-8 -*-
def mendels_law(hom, het, rec):
    import math
    parents = hom + het + rec
    dom_gen = 2*hom + het
    res_gen = 2 * rec + het
    genes = 2* parents
    possible_off = parents*(parents-1)*4
    paths_off = (hom * ((hom-1) + het+rec) + het*(het-1+hom+rec) + rec * (hom+rec-1+het))*4
    paths_domoff = (4*hom * ((hom-1) + het+rec)+ het*(3*(het-1)+4*hom+2*rec)+ rec * (4*hom+0*(rec-1)+2*het))

    prob = (paths_domoff/paths_off)
    return prob
