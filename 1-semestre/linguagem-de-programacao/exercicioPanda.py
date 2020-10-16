import pandas
client = {
    "Nome": ['Daniel', 'Renata', 'Paloma', 'Toninho'],
    "Idade": [25, 28, 24, 24]
}

dataFrame = pandas.DataFrame(client)

print (dataFrame)
print( dataFrame.Idade.mean())