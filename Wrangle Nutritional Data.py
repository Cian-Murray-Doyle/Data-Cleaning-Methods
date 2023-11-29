# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:26:43 2023

@author: cian3
"""

from urllib.request import urlretrieve
import pandas as pd

madden_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/112/Madden_s_Dairy.csv"
nell_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/113/Nell_s_Soups_and_Stocks.csv"
clerkin_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/114/Clerkin_Nuts_and_Grains.csv"
mahon_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/115/Mahon_Produce.csv"
nutley_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/116/Nutley_Fish_and_Seafood.csv"
foley_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/117/Foley_s_Butchers.csv"
tolsco_url = "https://ac-101708228-virtuoso-prod.s3.amazonaws.com/uploads/download/118/Tolsco_Foods.csv"

urlretrieve(madden_url, "Madden_s_Dairy.csv")
urlretrieve(nell_url, "Nell_s_Soups_and_Stocks.csv")
urlretrieve(clerkin_url, "Clerkin_Nuts_and_Grains.csv")
urlretrieve(mahon_url, "Mahon_Produce.csv")
urlretrieve(nutley_url, "Nutley_Fish_and_Seafood.csv")
urlretrieve(foley_url, "Foley_s_Butchers.csv")
urlretrieve(tolsco_url, "Tolsco_Foods.csv")

madden = pd.read_csv("Madden_s_Dairy.csv",)
nell = pd.read_csv("Nell_s_Soups_and_Stocks.csv")
clerkin = pd.read_csv("Clerkin_Nuts_and_Grains.csv")
mahon = pd.read_csv("Mahon_Produce.csv")
nutley = pd.read_csv("Nutley_Fish_and_Seafood.csv")
foley = pd.read_csv("Foley_s_Butchers.csv")
tolsco = pd.read_csv("Tolsco_Foods.csv")

food=pd.concat([madden,nell,clerkin,mahon,nutley,foley,tolsco])
food.reset_index(inplace=True,drop=True)
food

food["Grams"]=food["Grams"].str.strip("g:").astype("float64")
food["Calories"]=food["Calories"].str.strip("kcal:").astype("float64")
food.head()

food[food["Grams"]>1000]
food[food["Grams"]<0]
food.loc[239,"Grams"]=110
food[food["Calories"]>1500]
food[food["Calories"]<0]
food[food["Grams"]>1500]
food[food["Grams"]<0]

food[food["Protein"]>250]
food[food["Protein"]<0]
food.loc[7,"Protein"]=food.loc[7,"Protein"]*-1
food.loc[113,"Protein"]=food.loc[113,"Protein"]*-1

food[food["Fat"]>250]
food[food["Fat"]<0]
food.loc[14,"Fat"]=6
food.loc[212,"Fat"]=36
food.loc[44,"Fat"]=food.loc[44,"Fat"]*-1

food[food["Fiber"]>250]
food[food["Fiber"]<0]
food[food["Carbs"]>250]
food[food["Carbs"]<0]
food.loc[36,"Carbs"]=food.loc[36,"Carbs"]*-1
food.loc[81,"Carbs"]=food.loc[81,"Carbs"]*-1

food.isna().sum()
food[food["Protein"].isna()]
food.loc[6,"Protein"]=food.loc[6,"Grams"]-food.loc[6,"Fat"]-food.loc[6,"Fiber"]-food.loc[6,"Carbs"]
food.loc[111,"Protein"]=food.loc[111,"Grams"]-food.loc[111,"Fat"]-food.loc[111,"Fiber"]-food.loc[111,"Carbs"]
food[food["Fat"].isna()]
food.loc[84,"Fat"]=food.loc[84,"Grams"]-food.loc[84,"Protein"]-food.loc[84,"Fiber"]-food.loc[84,"Carbs"]
food.loc[193,"Fat"]=food.loc[193,"Grams"]-food.loc[193,"Protein"]-food.loc[193,"Fiber"]-food.loc[193,"Carbs"]
food.loc[215,"Fat"]=food.loc[215,"Grams"]-food.loc[215,"Protein"]-food.loc[215,"Fiber"]-food.loc[215,"Carbs"]
food[food["Fiber"].isna()]
food.loc[66,"Fiber"]=food.loc[66,"Grams"]-food.loc[66,"Protein"]-food.loc[66,"Fat"]-food.loc[66,"Carbs"]
food[food["Carbs"].isna()]
food.loc[92,"Carbs"]=food.loc[92,"Grams"]-food.loc[92,"Protein"]-food.loc[92,"Fat"]-food.loc[92,"Fiber"]

food[food.duplicated()]
food.drop_duplicates(inplace=True)
food.reset_index(inplace=True,drop=True)
food[food.duplicated()]

food["Food Type"].value_counts()
print(food.to_string())
replacements={
    "Drairy":"Dairy",
    "Fruit":"Fruits",
    "Mreat & Poultry":"Meat & Poultry",
    "Oil & Fats":"Oils & Fats",
    "insert_category_here":"Seafood"
}
food=food.replace(replacements)
food["Food Type"].value_counts()

incorrect_calories =(
    (
    round(food["Calories"]-((food["Protein"]+food["Fiber"]+food["Carbs"])*4)-(food["Fat"]*9),1)
    )
    !=0
)
food[incorrect_calories]
food["Calories"]=((food["Protein"]+food["Fiber"]+food["Carbs"])*4)+(food["Fat"]*9)
incorrect_calories =(
    (
    round(food["Calories"]-((food["Protein"]+food["Fiber"]+food["Carbs"])*4)-(food["Fat"]*9),1)
    )
    !=0
)
food[incorrect_calories]

food.to_csv('ingredients_cleaned.csv',index=False)

