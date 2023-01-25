from src.pre_built.counter import count_ocurrences


def test_counter():
    pythonOcurrencesUpper = count_ocurrences("data/jobs.csv", "Python")
    pythonOcurrencesLower = count_ocurrences("data/jobs.csv", "Python")
    javascriptOcurrencesUpper = count_ocurrences("data/jobs.csv", "Javascript")
    javascriptOcurrencesLower = count_ocurrences("data/jobs.csv", "Javascript")

    assert (pythonOcurrencesUpper == pythonOcurrencesLower)
    assert (javascriptOcurrencesUpper == javascriptOcurrencesLower)

    assert(pythonOcurrencesUpper == 1639)
    assert(javascriptOcurrencesUpper == 122)
