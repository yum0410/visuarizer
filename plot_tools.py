import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd
import seaborn as sns


FONT_PATH = "./ipaexg.ttf"
font_prop = FontProperties(fname=FONT_PATH)

def to_hist_ml_class(df, ml_col, save_figure_path=None):
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
        plt.savefig(os.path.join(save_figure_path, ml_col+"_cnt.png"))
    return plt

def to_hist_ml_label(ml_series, save_figure_path=None):
    """create figure of multi label value counts

    Parameters
    ----------
    ml_series : pandas.Series
        Series contained multi label
    save_figure_path : str
        figure save dir path

    Returns
    -------
    plt : matplotlib.pyplot
        histogram plt object
    """
    mlb = MultiLabelBinarizer()
    vec = mlb.fit_transform(ml_series)
    vec = pd.DataFrame(vec, columns=mlb.classes_)
    plt.bar(range(1, vec.shape[1]+1), vec.sum().values,
            tick_label=vec.columns, align="center")
    plt.title(ml_series.name+" class counts", fontproperties=font_prop)
    plt.xticks(range(1, vec.shape[1]+1), vec.columns, fontproperties=font_prop)
    if save_figure_path:
        plt.savefig(os.path.join(save_figure_path, ml_series.name+"_class_counts.png"))
    plt.show()

def to_corr_heatmap(df, threshold_value, save_figure_path=None):
    """create heatmap column corr 

    Parameters
    ----------
    df : pandas.DataFrame
        preprocessed DataFrame
    threshold_value : float
        corr threshold value
    save_figure_path : str
        figure save dir path

    Returns
    -------
    plt : matplotlib.pyplot
        histogram plt object
    """
    corr_df = df.corr()
    def _select_corr(row):
        return {str(key): val for key, val in row.items() if row.name != key and (val>threshold_value or val<-threshold_value)}
    _, ax = plt.subplots(figsize=(8,8))
    sns.heatmap(corr_df, annot=True, fmt=".2f")
    ax.set_title("correlation")
    ax.set_xticklabels(ax.get_xmajorticklabels(), rotation=0, fontproperties=font_prop)
    ax.set_yticklabels(ax.get_ymajorticklabels(), rotation=0, fontproperties=font_prop)
    plt.show()
    if save_figure_path:
        plt.savefig(os.path.join(save_figure_path, "correlation.png"))
    corr_df["selected"] = corr_df.apply(lambda x: _select_corr(x), axis=1)
    return corr_df["selected"]
