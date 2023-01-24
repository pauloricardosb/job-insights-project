from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        all_jobs = csv.reader(file, delimiter=",", quotechar='"')

        header, *data = all_jobs

        jobs = []

        for job in data:
            job_dict = {
                header[0]: job[0],
                header[1]: job[1],
                header[2]: job[2],
            }
            jobs.append(job_dict)
        return jobs


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)

    job_types = [job["job_type"] for job in data]
    return list(set(job_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
