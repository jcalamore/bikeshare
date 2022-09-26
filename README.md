
## Explore Bikeshare Data

### Description
This program uses Python to explore data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington D.C.

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it to point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

The bicycle-sharing systems make it easy for a user to access a dock within the system to unlock or return bicycles. The technology also provides a wealth of data that can be used to explore how these bike-sharing systems are used.

### The Datasets
Data was provided by [Motivate](https://www.motivateco.com), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

Randomly selected data for the first six months of 2017 was provided for all three cities. All three of the data files contained the same core six columns:

    Start Time (e.g., 2017-01-01 00:07:57)
    End Time (e.g., 2017-01-01 00:20:53)
    Trip Duration (in seconds - e.g., 776)
    Start Station (e.g., Broadway & Barry Ave)
    End Station (e.g., Sedgwick St & North Ave)
    User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

    Gender
    Birth Year

The original files are fairly large and messy, but they can be accessed here: [Chicago](https://www.divvybikes.com/system-data), [NYC](https://citibikenyc.com/system-data), and [Washington](https://www.capitalbikeshare.com/system-data).

These files had more columns and they differed in format in many cases, so some data wrangling had to be performed to condense these files to the above core six columns.

### Statistics Computed
This program computes a variety of descriptive statistics, as shown below:

1. Popular times of travel (i.e., occurs most often in the "Start Time" field)

    * Most common month
    * Most common day of week
    * Most common hour of day

2. Popular stations and trip

    * Most common start station
    * Most common end station
    * Most common trip from start to end (i.e., most frequent combination of start/end station)

3. Trip Duration

    * Total travel time
    * Average travel time

4. User info

    * Counts of each user type
    * Counts of each gender (only available for NYC and Chicago)
    * Earliest, most recent, most common year of birth (only available for NYC and Chicago)

