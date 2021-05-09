import scripts.display_genetic as dg


def test():
    p_set = {'CROSS': 'mpx', 'MUTATION': 'swap', 'MUT_PROB': 0.005, 'WINDOWING': 10, 'ELITISM': 0.001, 'SCALE': 'inverse'}
    main = dg.Main('genetic')
    main.display('Essonne', p_set)
