import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter a city (chicago, new york city, washington): ").strip().lower()

        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter a valid city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month: ").strip().lower()

        if month in ['all','january', 'february', 'march', 'april', 'may',  'june']:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day of the week: ").strip().lower()

        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter a day.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month 
    if month!='all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    #filter by day
    if day!='all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Convert the 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    print('the most common month: ',df['Start Time'].dt.month.mode()[0])

    # TO DO: display the most common day of week
    print('the most common day: ',df['Start Time'].dt.day_name().mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour: ',df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']
    print(' most frequent combination of start station and end station trip: ', df['Station Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        print('counts of user genders',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print('earliest year of barth',df['Birth Year'].min())
        print('most recent year of barth',df['Birth Year'].max())
        print('most common year of barth',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no.\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()