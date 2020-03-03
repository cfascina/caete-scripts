import csv
import random


def add_organic_matter(arr):
    file = open("temp_input.csv", "r")
    readable_csv = csv.reader(file)

    for index, row in enumerate(readable_csv):
        if index == 0:
            row.append("ORGANIC_MATTER")
            arr.append(row)
        else:
            row.append(str(random.uniform(0, 8)))
            arr.append(row)

    return arr


def eighth33r(sand, clay, organic_matter):
    return (-0.251 * sand) + (0.195 * clay) + (0.011 * organic_matter) \
            + (0.006 * (sand * organic_matter)) - (0.027 * (clay * organic_matter)) \
            + (0.452 * (sand * clay)) + 0.299


def eighth(eighth33_result):
    return eighth33_result + (1.283 * pow(eighth33_result, 2) - (0.374 * eighth33_result) - 0.015)


def apply_formulas(arr):
    for index, row in enumerate(arr):
        if index == 0:
            row.append("RESULT")
        else:
            row.append(eighth(eighth33r(float(row[3]), float(row[2]), float(row[5]))))

    return arr


def save_results(arr):
    with open("temp_output.csv", "w", newline = "") as output:
        writer = csv.writer(output)
        writer.writerows(arr)

    return True


if __name__ == '__main__':
    soil_arr = add_organic_matter([])
    result_arr = apply_formulas(soil_arr)

    if save_results(result_arr):
        print('Results saved at "temp_output.csv" file.')
