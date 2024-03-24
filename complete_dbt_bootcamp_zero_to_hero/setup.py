from setuptools import find_packages, setup

setup(
    name="complete_dbt_bootcamp_zero_to_hero",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "complete_dbt_bootcamp_zero_to_hero": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-snowflake",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

