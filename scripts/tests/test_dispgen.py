import scripts.display_genetic as dg


def test():
    p_set = {'CROSS': 'pmx', 'MUTATION': 'swap', 'MUT_PROB': 0, 'WINDOWING': -1, 'ELITISM': 0, 'SCALE': 'inverse'}
    main = dg.Main('genetic')
    main.display('Essonne_pmx', p_set)
