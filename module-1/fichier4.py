def rect():
    print('entres la valeur de la longeur du paralèlépipède réctangle ')
    a = input()
    longueur = float(a)

    print('entres la valeurs de la profondeur du paralèlépipède réctangle')
    c = input()
    profondeur = float(c)

    print('entres la valeurs de la largeur du paralèlépipède rectangle')
    e = input()
    largeur = float(e)

    v_rect = longueur*profondeur*largeur

    print('entre la valeur du rayon de cercle')
    g = input()
    rayon = float(g)

    v_sphere = 4/3*3.14*rayon*rayon*rayon


    if (v_sphere < v_rect):
        print(f'le volume du paralèlépipèdes réctangle est plus grand que celui du cercle {v_sphere:.2f} < {v_rect}')
    else:
        print('le volume du cercle est plus grand que celui du paralèlépipède réctangle {v_sphere:.2f} > {v_rect}')

    '''
    :.3f permet de limiter le nombre de chiffre apres la virgule de 3
    '''

rect()