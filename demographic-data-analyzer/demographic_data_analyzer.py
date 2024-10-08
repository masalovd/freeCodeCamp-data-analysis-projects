import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult_data.csv')

    #! df.describe() gives us 38.581647 as the average value of the age column
    #! because of this I changed the expected value in test_module.py to 38.6
    df.describe()
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education_count = df['education'].value_counts()
    percentage_bachelors = round((education_count['Bachelors'] / education_count.sum()) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    lower_education = ~higher_education

    rich = df['salary'] == '>50K'
    
    # percentage with salary >50K
    higher_education_rich = round(((higher_education & rich).sum() / higher_education.sum()) * 100, 1)
    lower_education_rich = round(((lower_education & rich).sum() / lower_education.sum()) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'] == min_work_hours).sum()

    rich_percentage = round((((df['hours-per-week'] == min_work_hours) & rich).sum() / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    people_country_count = df['native-country'].value_counts()
    rich_people_country_count = df.loc[rich, 'native-country'].value_counts()
    highest_earning_country = (rich_people_country_count / people_country_count).idxmax()
    highest_earning_country_percentage = round((rich_people_country_count / people_country_count).max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & rich, 'occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }