import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # get user input for city (chicago, new york city, washington). 

    print()
    print("Hello! Let's explore some US bikeshare data!")

    while True:
        
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington? ')
            if (city.casefold() in cities):
                city = city.casefold()
                break
            else:
                raise ValueError
            
        except ValueError:
            print()
            print("Try again. That was not a valid input. Please select either New York City, Washington, or Chicago. ")
            print()

    # get user input for month (all, january, february, ... , june)

    while True:
        
        try:
            month = input('Which month (January - June) would you like to filter by? (Select "All" for all months) ')
            if (month.casefold() in months):
                month = month.casefold()
                break
            else:
                raise ValueError
            
        except ValueError:
            print()
            print("Try again. That was not a valid input. Please select a month or 'All'. ")
            print()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        
        try:
            day = input('Which day (Monday - Sunday) would you like to filter by? (Select "All" for all days.) ')
            if (day.casefold() in days):
                day = day.casefold()
                break
            else:
                raise ValueError
            
        except ValueError:
            print()
            print("Try again. That was not a valid input. Please select a day of the week. ")
            print()

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
    
    # UNCOMMENT THIS LINE TO SEE ALL COLUMNS OF DATA
    #pd.set_option("display.max_columns", 200)
    
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create 'month', 'day_of_week', and 'hour' columns from 'Start Time'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month if selected
    if month != 'all':

        month = months.index(month)
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        #print('day is: ', day)
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[popular_month].title()))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {}'.format(common_day))

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print('The most common Start Station is: {}'.format(common_startstation))

    # display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print('The most common End Station is: {}'.format(common_endstation))

    # display most frequent combination of start station and end station trip
    frequent_combo = (df['Start Station'] + ',' + df['End Station']).mode()[0]
    print('The most frequent combination of Start and End Stations are: {}'.format(frequent_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total time of all the trips is: {}'.format(total_time))

    # display mean travel time
    rows_count = len(df.index)
    avg_time = total_time/rows_count

    print('The average time of the trips was: {}'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].unique()
    print('Unique user types: ', user_types)

    # Display counts of gender
    try:
         gender_counts = df['Gender'].value_counts()
         print('The number of each gender: ')
         print(gender_counts)
    except KeyError:
        print('\nGender Types: Not Available')

    # Display earliest, most recent, and most common year of birth
    try:

        earliest = df['Birth Year'].min()
        print('The earliest year of birth is: {}'.format(earliest))

        most_recent = df['Birth Year'].max()
        print('The most recent year of birth is: {}'.format(most_recent))

        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(most_common))
    
    except KeyError:
        print('\nBirth Year: Not Available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data on bikeshare users."""
    print(df.head())
    count = 0
    while True:
        rawdata = input('Would you like to see the next 5 rows of raw data? Please enter "yes" or "no". ')
        if rawdata.casefold() != 'yes':
            return
        count += 5
        print(df.iloc[count:count+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.casefold() != 'yes':
            break

if __name__ == "__main__":
	main()