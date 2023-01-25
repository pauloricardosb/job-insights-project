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
    filtered_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            pass
    return filtered_list
