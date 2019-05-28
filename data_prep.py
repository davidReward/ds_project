import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings # Ignores any warning    

def fat_to_numeric(x):
    if (x == 'Low Fat') or (x == 'low fat') or (x == 'LF'):
        return 0
    if (x == 'Regular') or (x == 'reg'):
        return 1
    
def type_to_numeric(x):
    if (x == 'Dairy'):
        return 0
    if (x == 'Soft Drinks'):
        return 1
    if (x == 'Meat'):
        return 2
    if (x == 'Fruits and Vegetables'):
        return 3
    if (x == 'Household'):
        return 4
    if (x == 'Baking Goods'):
        return 5
    if (x == 'Snack Foods'):
        return 6
    if (x == 'Frozen Foods'):
        return 7
    if (x == 'Breakfast'):
        return 8
    if (x == 'Health and Hygiene'):
        return 9
    if (x == 'Hard Drinks'):
        return 10
    if (x == 'Canned'):
        return 11
    if (x == 'Breads'):
        return 12
    if (x == 'Starchy Foods'):
        return 13
    if (x == 'Others'):
        return 14
    if (x == 'Seafood'):
        return 15
    
def size_to_numeric(x):
    if (x == 'Small'):
        return 0
    if (x == 'Medium'):
        return 1
    if (x == 'High'):
        return 2
    return 3
    
def loc_type_to_numeric(x):
    if (x=='Tier 1'):
        return 0
    if (x=='Tier 2'):
        return 1
    if (x=='Tier 3'):
        return 2

def outlet_type_to_numeric(x):
    if (x=='Supermarket Type1'):
        return 0
    if (x=='Supermarket Type2'):
        return 1
    if (x=='Supermarket Type3'):
        return 2
    if (x=='Grocery Store'):
        return 3

def proc_data(path):
    df = pd.read_csv(path)
    df['Item_Type_n'] = df['Item_Type'].apply(type_to_numeric)
    df['Item_Fat_Content_n'] = df['Item_Fat_Content'].apply(fat_to_numeric)
    
    df['Item_Weight'].fillna(df['Item_Weight'].mean() ,inplace=True)
    
    df['Outlet_Size_n'] = df['Outlet_Size'].apply(size_to_numeric)
    
    df['Outlet_Location_Type_n'] = df['Outlet_Location_Type'].apply(loc_type_to_numeric)
    

    
    for index, row in df.iterrows():
        if (row['Outlet_Size_n']== 3):
            if (row['Outlet_Type'] == 'Grocery Store') or (row['Outlet_Type'] == 'Supermarket Type1'):
                df.at[index, 'Outlet_Size'] = 'Small'
            if (row['Outlet_Type'] == 'Supermarket Type2') or (row['Outlet_Type'] == 'Supermarket Type3'):
                df.at[index, 'Outlet_Size'] = 'Medium'
    
    df['Outlet_Type_n'] = df['Outlet_Type'].apply(outlet_type_to_numeric)
    
    del df['Item_Type'], df['Item_Fat_Content'], df['Outlet_Size'], df['Outlet_Location_Type'], df['Outlet_Type']
    
    return df

    
    
