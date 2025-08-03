import pandas as pd


def read_data(filename = 'Davide_BlindAnalysis151203.xlsx'):
    column_names = {
        'V1-A': 'num_tests_A',
        'V2-A': 'quality_A',
        'V3-A': 'productivity_A',
        'V1-B': 'num_tests_B',
        'V2-B': 'quality_B',
        'V3-B': 'productivity_B'
    }
    df = pd.read_excel(filename)
    df.drop(df.columns.difference(column_names.keys()), 1, inplace=True)
    df.rename(columns=column_names, inplace=True)
    return df


if __name__ == '__main__':
    print(read_data())
