"""
Module settings
"""
import arviz as az
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


class Settings:
    """
    Class Settings: For Jupyter Lab notebooks
    """

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def aesthetics():
        """

        :return:
        """

        matplotlib.rcParams.update({'font.size': 13})
        matplotlib.rcParams['text.usetex'] = False

        sns.set(font_scale=1)

        # noinspection PyUnresolvedReferences
        az.style.use('arviz-darkgrid')

    @staticmethod
    def layout():
        """

        :return:
        """

        plt.rcParams['figure.constrained_layout.use'] = False
