import intervalSeries
import descreteSeries
import histogram
import polygon
import randomGenerator
import mathdefs
from constants import INTERVAL_NUMBER, PATH_TO_DATA

from scipy.stats import norm


def main():
    with open(PATH_TO_DATA) as file:
        data = []
        for line in file:
            line = line.split()
            if line:
                line = [float(element) for element in line]
                data.append(line)

    intSeries = intervalSeries.IntervalSeries(data)
    freqs = intSeries.getFreqs()
    print("freqs: ", freqs)

    descSeries = descreteSeries.DescreteSeries(data)
    descretes = descSeries.getDescretes()
    print("descretes: ", descretes)

    mean = mathdefs.sampleMean(data[0])
    print("mean: ", mean)

    dispersion = mathdefs.sampleDispersion(data[0])
    print("dispersion: ", dispersion)

    deviation = mathdefs.sampleStandardDeviation(data[0])
    print("deviation: ", deviation)

    title = "Variable X (" + str(INTERVAL_NUMBER) + " evenly spaced bins)"
    hist = histogram.Histogram(
        data, "Statistical Data Analysys Histogram", title, "Count")

    poly = polygon.Polygon(
        descretes, freqs, "Statistical Data Analysys Polygon", "Descretes", "Count")

    rangen = randomGenerator.RandomGenerator()
    gen_data = rangen.generate(0, 1, 50)

    a, sigma = norm.fit(gen_data)
    print(f"\ndata: {gen_data}")
    print(f"a: {a}; sigma: {sigma}")


if __name__ == "__main__":
    main()
