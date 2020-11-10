import netCDF4 as nc

ncFile = 'aux/hadgem2es-soil-ancil.nc'
dataset = nc.Dataset(ncFile)
# print(dataset)

# Dimensões do Dataset:
# print(dataset.dimensions)

# Variáveis do Dataset:
# print(dataset.variables)

# Valores de variáveis (verificar quais existem na célula acima):
print(dataset['longitude'][:])
# print(dataset['field336'][:])
