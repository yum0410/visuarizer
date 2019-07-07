def select_over_cell_from_row(row, th_value):
    """select over th_value cell from row

    Parameters
    ----------
    row : pandas.Series
        Series. target is DataFrame.apply(..., axis=1)
    th_value : float
        th value

    Returns
    -------
    dict : dict
        over cell {"column_name": cell_value}
    """
    return {str(key): val for key, val in row.items() if row.name != key and val>=th_value}
