import pandas as pd 
import matplotlib.pyplot as plt


def remove_outliers(df, range):

    #Creating subset containing columns of interest (see distrbutions above)
    df_outlier_columns = df[[
        'appCat.communication',
        'appCat.entertainment', 'appCat.finance', 'appCat.game',
        'appCat.office', 'appCat.social', 'appCat.travel',
        'appCat.weather', 'screen']]

    stats_subset = df.describe()[df_outlier_columns.columns] #A subset of the described pivot set containing only the columns with outliers

    Q1 = stats_subset.loc['25%']
    Q3 = stats_subset.loc['75%']

    IQR = Q3 - Q1


    upper_bound = Q3 + (range*IQR)
    lower_bound = Q1 - (range*IQR)

    #Removing outliers
    df_outliers_removed = df_outlier_columns.apply(lambda x: [y if y <= upper_bound[x.name] else None for y in x])
    df_outliers_removed = df_outliers_removed.apply(lambda x: [y if y >= lower_bound[x.name] else None for y in x])


    #Replace columns in original data set with the same columns that no-longer contain outliers
    for column in df_outliers_removed.columns:
        df[column] = df_outliers_removed[column]

    

    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 8))  

    # Row 1
    axes[0,0].scatter(df['id'], df['appCat.communication'])
    axes[0,0].set_xlabel('id', fontweight='bold')
    axes[0,0].set_ylabel('appCat.communication', fontweight='bold')

    axes[0,1].scatter(df['id'], df['appCat.entertainment'])
    axes[0,1].set_xlabel('id', fontweight='bold')
    axes[0,1].set_ylabel('appCat.entertainment', fontweight='bold')

    # axes[0,2].scatter(df['id'], df['appCat.social'])
    # axes[0,2].set_xlabel('id', fontweight='bold')
    # axes[0,2].set_ylabel('appCat.social', fontweight='bold')

    axes[0,2].scatter(df['id'], df['appCat.finance'])
    axes[0,2].set_xlabel('id', fontweight='bold')
    axes[0,2].set_ylabel('appCat.finance', fontweight='bold')

    # Row 2

    axes[1,0].scatter(df['id'], df['appCat.game'])
    axes[1,0].set_xlabel('id', fontweight='bold')
    axes[1,0].set_ylabel('appCat.game', fontweight='bold')

    axes[1,1].scatter(df['id'], df['appCat.office'])
    axes[1,1].set_xlabel('id', fontweight='bold')
    axes[1,1].set_ylabel('appCat.office', fontweight='bold')

    axes[1,2].scatter(df['id'], df['appCat.social'])
    axes[1,2].set_xlabel('id', fontweight='bold')
    axes[1,2].set_ylabel('appCat.social', fontweight='bold')

    # Row 3

    axes[2,0].scatter(df['id'], df['appCat.travel'])
    axes[2,0].set_xlabel('id', fontweight='bold')
    axes[2,0].set_ylabel('appCat.travel', fontweight='bold')

    axes[2,1].scatter(df['id'], df['appCat.weather'])
    axes[2,1].set_xlabel('id', fontweight='bold')
    axes[2,1].set_ylabel('appCat.weather', fontweight='bold')

    axes[2,2].scatter(df['id'], df['screen'])
    axes[2,2].set_xlabel('id', fontweight='bold')
    axes[2,2].set_ylabel('screen', fontweight='bold')

    plt.tight_layout()

    plt.show()

