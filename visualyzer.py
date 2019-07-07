import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import plot_tools

def select_corr(df, th_value):
    corr_df = df.corr()
    def _select_corr(row):
        return {str(key): val for key, val in row.items() if row.name != key and (val>th_value or val<-th_value)}
    corr_df["selected"] = corr_df.apply(lambda x: _select_corr(x), axis=1)
    return corr_df["selected"]

if __name__ == "__main__":
    dummy = pd.DataFrame({"A": [["しいたけ", "しめじ", "えのき"],
                                ["えりんぎ", "えのき"],
                                ["まいたけ", "しめじ", "えのき", "しいたけ"],
                                ["えのき"],
                                ["えりんぎ"],
                                ["まいたけ"],
                                ["しいたけ"]
                            ],
                        "B": [600, 300, 1000, 100, 200, 400, 300]
                        })

    plot_tools.to_hist_ml_class(dummy, "A")
    plot_tools.to_hist_ml_label(dummy["A"])

    # use to_corr_heatmap
    mlb = MultiLabelBinarizer()
    dummy_vec = mlb.fit_transform(dummy["A"])
    dummy_vec = pd.DataFrame(dummy_vec, columns=mlb.classes_)
    corr_df = plot_tools.to_corr_heatmap(dummy_vec, 0.1)
    
