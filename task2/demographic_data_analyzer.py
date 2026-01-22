import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'].value_counts(normalize=True)['Bachelors']) * 100, 1
    )

    # 4. What percentage of people with advanced education make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced_education]
    percentage_higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~advanced_education]
    percentage_lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours
    # per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. What country has the highest percentage of people that earn >50K?
    country_salary = (
        df[df['salary'] == '>50K']['native-country'].value_counts()
        / df['native-country'].value_counts()
        * 100
    )

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", percentage_higher_education_rich)
        print("Percentage without higher education that earn >50K:", percentage_lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_education_rich': percentage_higher_education_rich,
        'percentage_lower_education_rich': percentage_lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
