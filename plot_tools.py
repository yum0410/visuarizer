import matplotlib.pyplot as plt
import os


def create_multi_label_count_hist(df, ml_col, save_figure_path=None):
    """create histogram of multi label count

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contained multi label
    ml_col : str
        multi label column name
    save_figure_path : str
        figure save dir path

    Returns
    -------
    plt : matplotlib.pyplot
        histogram plt object
    """
    df[ml_col+"_cnt"] = df.apply(lambda x: len(x[ml_col]), axis=1)
    plt.hist(df[ml_col+"_cnt"])
    plt.title(ml_col+" label_count")
    if save_figure_path:
        if ".csv" in save_figure_path:
            plt.savefig(save_figure_path)
        else:
            plt.savefig(os.path.join(save_figure_path, ml_col+"_cnt.png"))
    return plt

