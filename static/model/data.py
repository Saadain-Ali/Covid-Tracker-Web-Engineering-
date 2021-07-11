from typing import List


class data:
    updated: int
    cases: int
    today_cases: int
    deaths: int
    today_deaths: int
    recovered: int
    today_recovered: int
    active: int
    critical: int
    cases_per_one_million: float
    deaths_per_one_million: float
    tests: int
    tests_per_one_million: float
    population: int
    continent: str
    active_per_one_million: float
    recovered_per_one_million: float
    critical_per_one_million: float
    countries: List[str]

    def __init__(self, updated: int, cases: int, today_cases: int, deaths: int, today_deaths: int, recovered: int, today_recovered: int, active: int, critical: int, cases_per_one_million: float, deaths_per_one_million: float, tests: int, tests_per_one_million: float, population: int, continent: str, active_per_one_million: float, recovered_per_one_million: float, critical_per_one_million: float, countries: List[str]) -> None:
        self.updated = updated
        self.cases = cases
        self.today_cases = today_cases
        self.deaths = deaths
        self.today_deaths = today_deaths
        self.recovered = recovered
        self.today_recovered = today_recovered
        self.active = active
        self.critical = critical
        self.cases_per_one_million = cases_per_one_million
        self.deaths_per_one_million = deaths_per_one_million
        self.tests = tests
        self.tests_per_one_million = tests_per_one_million
        self.population = population
        self.continent = continent
        self.active_per_one_million = active_per_one_million
        self.recovered_per_one_million = recovered_per_one_million
        self.critical_per_one_million = critical_per_one_million
        self.countries = countries
