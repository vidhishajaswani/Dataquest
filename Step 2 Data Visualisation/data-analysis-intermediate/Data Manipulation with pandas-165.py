## 1. Overview ##

import pandas
food_info=pandas.read_csv("food_info.csv")
col_names=food_info.columns.tolist()
print(col_names)
print(food_info.head(3))

## 2. Transforming a Column ##

div_1000 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2

sodium_grams = food_info["Sodium_(mg)"] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

## 3. Performing Math with Multiple Columns ##

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

grams_of_protein_per_gram_of_water=food_info["Protein_(g)"]/food_info["Water_(g)"]
milligrams_of_calcium_and_iron=food_info["Calcium_(mg)"]+food_info["Iron_(mg)"]

## 4. Create a Nutritional Index ##

weighted_protein=2*food_info["Protein_(g)"]
weighted_fat=-0.75*food_info["Lipid_Tot_(g)"]
initial_rating=weighted_protein+weighted_fat



## 5. Normalizing Columns in a Data Set ##

print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"]/max_protein

max_lipid = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"]/max_lipid

## 6. Creating a New Column ##

normalized_protein = (food_info["Protein_(g)"] - food_info["Protein_(g)"].min()) / (food_info["Protein_(g)"].max() - food_info["Protein_(g)"].min())
normalized_fat = (food_info["Lipid_Tot_(g)"] - food_info["Lipid_Tot_(g)"].min()) / (food_info["Lipid_Tot_(g)"].max() - food_info["Lipid_Tot_(g)"].min())
food_info["Normalized_Protein"]=normalized_protein
food_info["Normalized_Fat"]=normalized_fat

## 7. Create a Normalized Nutritional Index ##

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat
food_info["Norm_Nutr_Index"] = (2*food_info["Normalized_Protein"]) - (0.75*food_info["Normalized_Fat"])

## 8. Sorting a DataFrame by a Column ##

food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])

food_info.sort_values("Norm_Nutr_Index",inplace=True, ascending=False)