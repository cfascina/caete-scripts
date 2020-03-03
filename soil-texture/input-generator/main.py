import numpy
import os
import rasterio


def tif2csv(tif_file):
    raster = rasterio.open(tif_file)
    band = raster.read(1)
    raster_arr = [["X", "Y", "VALUE"]]
    no_data = float(-3.3999999521443642e+38)
    path_outputs = os.path.abspath(os.getcwd()) + "/outputs/"

    for x in range(0, raster.width):
        for y in range(0, raster.height):
            if float(band[y, x] == no_data):
                raster_arr.append([float(x), float(y), 0])
            else:
                raster_arr.append([float(x), float(y), float(band[y, x])])

    print(f"Converting {raster.name.split('/')[-1]} to CSV file...")
    np_arr = numpy.asarray(raster_arr)
    numpy.savetxt(f"{path_outputs}{raster.name.split('/')[-1][:-4]}.csv", np_arr, delimiter = ",", fmt = "%s")
    print(f"File saved at {path_outputs}{raster.name.split('/')[-1][:-4]}.csv")
    print("-" * 30)


if __name__ == '__main__':
    path_inputs = os.path.abspath(os.getcwd()) + "/inputs/"

    tif2csv(path_inputs + "clay_half_degree.tif")
    tif2csv(path_inputs + "sand_half_degree.tif")
    tif2csv(path_inputs + "silt_half_degree.tif")
