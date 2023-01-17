import pandas as pd

column = ["Kwesi", "Kan", "Sekou", "Kam"]
titled_column = {"name": column}
data = pd.DataFrame(titled_column)
print(data)