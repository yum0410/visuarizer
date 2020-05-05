import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
from collections import Counter, OrderedDict
import datetime


FONT_PATH = "./ipaexg.ttf"
font_prop = FontProperties(fname=FONT_PATH)


def is_file(save_path, extension_type):
    """
    check save path is file path or dir path.

    Parameters
    ----------
    save_path : str
        target save path str.
    extension_type : str
        file extention type.

    Returns
    -------
    result : bool
        boolean of the save path is file path.
    """

    # remove dot(.) for current dir
    if "./" in save_path:
        save_path.replace("./", "")
    print(save_path)
    if "." + extension_type in save_path:
        return True
    return False

def make_histogram(array, bar_title=None, save_path=None, sort_by_y=True):
    """
    make histogram

    Parameters
    ----------
    array : list
        input data. The histogram is computed over the flattened array.
    save_path : str
        the histogram　image file save path.
    sort_by_y : bool
        sorting flag.

    Returns
    -------
    histogram_data : dict
        the value of the histogram
    """
    if type(array) is not list:
        raise ValueError("the method permit only list values.")
    # TODO support with pd.series

    # elif type(array) is type(pd.Series()):
    #     array.value_counts()

    # counting
    value_counts = Counter(array)

    # sorting
    if sort_by_y:
        # sorting by y(count)
        value_counts = OrderedDict(sorted(value_counts.items()))
    else:
        # sorting by x(value)
        value_counts = OrderedDict(sorted(value_counts.most_common()))

    # make plot
    plt.figure()
    plt.bar(range(1, len(value_counts.keys())+1), value_counts.values(), tick_label=value_counts.keys(), align="center")
    plt.xticks(range(1, len(value_counts.keys())+1), value_counts.keys(), fontproperties=font_prop)
    if bar_title:
        plt.title(bar_title, FontProperties=font_prop)

    # saving
    if save_path:
        if is_file(save_path, "png"):
            # make save path dir
            save_dir = os.path.join(*save_path.split("/")[:-1])
            os.makedirs(save_dir, exist_ok=True)
            plt.savefig(save_path)
        else:
            # make save path dir
            os.makedirs(save_path, exist_ok=True)

            # file name as datetime_hist.png
            now = datetime.datetime.now()
            file_name = "{}_hist.png".format(now.strftime("%Y%m%d%H%M"))
            plt.savefig(os.path.join(save_path, file_name))
    return value_counts

if __name__ == "__main__":
    hoge = ["A", "A", "A", "B", "A", "B", "C", "C", "D"]
    print(make_histogram(hoge, "hoge_ヒストグラム", "./hoge/hoge.png"))
