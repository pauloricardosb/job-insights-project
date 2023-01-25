from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    result = [
        int(salary)
        for salary in {salary["max_salary"] for salary in data}
        if salary.isnumeric()
    ]
    return max(result)


def get_min_salary(path: str) -> int:
    data = read(path)
    result = [
        int(salary)
        for salary in {salary["min_salary"] for salary in data}
        if salary.isnumeric()
    ]
    return min(result)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        sal = int(salary)
    except (TypeError, KeyError):
        raise ValueError

    if (min > max):
        raise ValueError
    return min <= sal <= max


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
