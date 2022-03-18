def test_reproduction():
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt
    plt.plot([0, 1], [0, 1])
