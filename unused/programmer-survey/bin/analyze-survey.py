#!/usr/bin/env python

import sys
import argparse
import numpy as np
import pandas as pd
import plotly.express as px
import statsmodels.formula.api as sm


MODEL_COLUMNS = ['EdLevel', 'DevType', 'OpenSourcer', 'YearsCodePro', 'Gender', 'Dependents']
ALL_COLUMNS = ['Respondent', 'ConvertedComp'] + MODEL_COLUMNS


def main():
    '''
    Filter and analyze survey data.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='input file')
    parser.add_argument('--save', type=str, help='figure directory (default is no save)')
    parser.add_argument('--show', action='store_true', help='show figures')
    parser.add_argument('--verbose', action='store_true', help='report intermediate results for checking')
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    data = simplify(data, args)
    show_by_gender(data, args)

    by_devtype = split_by_devtype(data, args)
    show_by_devtype(by_devtype, args)

    model = create_model(by_devtype, args)
    print(model.summary())


def simplify(data, args):
    '''
    Simplify data.
    '''
    if args.verbose: print(f'initial length {len(data)}')

    # Americans in full-time positions earning between $30K and $2M.
    data = data[
        (data.Country == 'United States') &
        (data.Employment == 'Employed full-time') &
        (30e3 < data.ConvertedComp) &
        (data.ConvertedComp < 2e6)
    ]
    if args.verbose: print(f'after initial filter {len(data)}')

    # Groups to remove.
    managers_ctos = data.DevType.str.contains('Engineering manager|Product manager|Senior executive/VP')
    if args.verbose: print(f'number of managers and CTOs {managers_ctos.sum()}')
    academics = data.DevType.str.contains('Academic researcher|Scientist|Educator')
    if args.verbose: print(f'number of academics {academics.sum()}')
    if args.verbose: print(f'number in both {(managers_ctos & academics).sum()}')
    data = data[~ (managers_ctos | academics)]
    if args.verbose: print(f'number after removal {len(data)}')

    # Simplify education levels (be careful about smart single quotes).
    if args.verbose: print(f'number of EdLevel NA before {data.EdLevel.isna().sum()}')
    data.EdLevel = data.EdLevel.replace({
        "I never completed any formal education": "Less than bachelor's",
        "Primary/elementary school": "Less than bachelor's",
        "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": "Less than bachelor's",
        "Some college/university study without earning a degree": "Less than bachelor's",
        "Associate degree": "Less than bachelor's",
        "Bachelor’s degree (BA, BS, B.Eng., etc.)": "Bachelor's degree",
        "Other doctoral degree (Ph.D, Ed.D., etc.)": "Graduate degree",
        "Master’s degree (MA, MS, M.Eng., MBA, etc.)": "Graduate degree",
        "Professional degree (JD, MD, etc.)": "Graduate degree"
    })
    if args.verbose: print(f'EdLevel is {data.EdLevel.unique()}')
    if args.verbose: print(f'number of EdLevel NA after {data.EdLevel.isna().sum()}')

    # Simplify open source contributions.
    data.OpenSourcer = data.OpenSourcer.replace({
        "Never": "Never",
        "Less than once per year": "Sometimes",
        "Less than once a month but more than once per year": "Often",
        "Once a month or more often": "Often"
    })
    if args.verbose: print(f'OpenSource is {data.OpenSourcer.unique()}')

    # Simplify gender.
    if args.verbose: print(f'Gender entries are {data.Gender.unique()}')
    data.Gender = data.Gender.replace(to_replace = r'.*Non-binary.*', value='Non-binary', regex=True)
    data = data[data.Gender.isin(["Man", "Woman", "Non-binary"])]
    if args.verbose: print(f'Gender is {data.Gender.unique()}')

    # Simplify years of professional coding in the same way as R's readr::parse_number.
    data.YearsCodePro = data.YearsCodePro.replace({
        'Less than 1 year': '1',
        'More than 50 years': '50'
    })
    data.YearsCodePro = pd.to_numeric(data.YearsCodePro)

    # Drop unneeded columns.
    data = data[ALL_COLUMNS]
    return data


def show_by_gender(data, args):
    '''
    Plot and show distribution of incomes by gender.
    '''
    fig = px.histogram(data, x='ConvertedComp', color='Gender',
                       histnorm='density', opacity=0.2, barmode='overlay', log_x=True)
    if args.show: fig.show()
    if args.save: fig.write_image(f'{args.save}/salary_by_gender.svg')
    stats = data\
        .groupby('Gender')\
        .agg({'Respondent': 'count', 'ConvertedComp': 'median'})
    print(stats)


def split_by_devtype(data, args):
    '''
    Split salaries by development type.
    '''
    data.DevType = data.DevType.str.lower()
    data.DevType = data.DevType.str.split(';')
    data = data.explode('DevType')
    data.DevType = data.DevType.str.replace('developer, ', '')
    data.DevType = data.DevType.replace({
        "data or business analyst": "data analyst",
        "data scientist or machine learning specialist": "data scientist",
        "desktop or enterprise applications": "desktop",
        "devops specialist": "devops",
        "embedded applications or devices": "embedded",
        "engineer, data": "data engineer",
        "engineer, site reliability": "devops"
    })
    data = data[~ (data.DevType.isna() |
                   data.DevType.isin(['other', 'student', 'marketing or sales professional']))]
    if args.verbose: print('dev types are ', sorted(data.DevType.unique()))
    return data


def show_by_devtype(data, args):
    '''
    Show results by developer type.
    '''
    fig = px.box(data, x='Gender', y='ConvertedComp', color='Gender',
                 facet_col='DevType', facet_col_wrap=4)
    if args.show: fig.show()
    if args.save: fig.write_image(f'{args.save}/salary_by_devtype.svg')


def create_model(data, args):
    '''
    Create a simple linear model based on compensation and developer type.
    '''
    data = data[(data.ConvertedComp < 300e3) &
                (data.YearsCodePro < 30) &
                data.Gender.isin(["Man", "Woman"])]
    formula = f'np.log(ConvertedComp) ~ {" + ".join(MODEL_COLUMNS)} - 1'
    print(formula)
    model = sm.ols(formula=formula, data=data).fit()
    return model


if __name__ == '__main__':
    main()
