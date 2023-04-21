import pandas as pd

df = pd.read_csv("extraData\\50000_patents.csv")

patentNrs = df["patent"].tolist()

# Create a dictionary to store the keywords for each patent
patent_keywords = {}
for patent_nr in patentNrs:
    patent_keywords[patent_nr] = []

with open("extraData\\keywords.txt", "r") as f:
    for line in f:
        if patentNrs == []:
            break
        txt = line[:-1]
        
        patent, keywords = txt.split(",")
        patent = int(patent)
        
        if patent in patentNrs:
            # Add the keywords to the list of keywords for the patent
            patent_keywords[patent].append(keywords)
            # Remove the patent from the list of patents to find keywords for
            patentNrs.remove(patent)
            
#Match keywords to patent
df["keywords"] = df["patent"].apply(lambda x: " ".join(patent_keywords[int(x)]))

#Save the dataframe to a csv file
df.to_csv('extraData\\50000_patents_with_keywords.csv', index=False)
