from operator import index
import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    for index in data:
        date, county, state, fips, cases, deaths = index #identifying elements in the data

        if county == 'Rockingham' and state == 'Virginia' and cases >= 1: #loop to find first Rockingham case
            Rockingham_first_case_date = date
            break
    
    for index in data:
        date, county, state, fips, cases, deaths = index #identifying elements in the data

        if county == 'Harrisonburg city' and state == 'Virginia' and cases >= 1: #loop to find first Harrisonburg case
            Harrisonburg_first_case_date = date
            break
    
    print('The first positive COVID case in Harrisonburg was on the date', Harrisonburg_first_case_date, '.')    #Printing first case answers
    print('The first positive COVID case in Rockingham County was on the date', Rockingham_first_case_date, '.')
    

    return Rockingham_first_case_date, Harrisonburg_first_case_date

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    previous_cases_Rockingham = 0           #initializing variables
    previous_cases_Harrisonburg = 0
    max_cases_Rockingham = 0
    max_cases_Harrisonburg = 0
    date_Rockingham = ''        #stating variables to later store information
    date_Harrisonburg = ''

    for index in data:
        date, county, state, fips, cases, deaths = index #identifying elements in the data

        if county == 'Rockingham' and state == 'Virginia': #Checking if location of index is contrained to Rockingham and Virginia
            new_cases_Rockingham = cases - previous_cases_Rockingham #loops through all data to find the max cases until looped through all data
            previous_cases_Rockingham = cases
            if new_cases_Rockingham > max_cases_Rockingham:
                max_cases_Rockingham = new_cases_Rockingham
                date_Rockingham = date
        
        if county == 'Harrisonburg city' and state == 'Virginia': #Checking if location of index is contrained to Harrisonburg and Virginia
            new_cases_Harrisonburg = cases - previous_cases_Harrisonburg #loops through all data to find the max cases until looped through all data
            previous_cases_Harrisonburg = cases
            if new_cases_Harrisonburg > max_cases_Harrisonburg:
                max_cases_Harrisonburg = new_cases_Harrisonburg
                date_Harrisonburg = date

   
    print('The greatest number of new cases reported in Harrisonburg was', max_cases_Harrisonburg, 'on the date', date_Harrisonburg, '.')   #Printing maximum cases answers
    print('The greatest number of new cases reported in Rockingham County was', max_cases_Rockingham, 'on the date', date_Rockingham, '.')
    return max_cases_Rockingham, max_cases_Harrisonburg

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    seven_day_Rockingham = 0    #initializing variables
    worst_start_date_Rockingham = ""   #stating variables to later store information
    worst_end_date_Rockingham = ""
    rockingham_rows = []  # variable to store list of specific data from large COVID data set
    seven_day_Harrisonburg = 0
    worst_start_date_Harrisonburg = ""
    worst_end_date_Harrisonburg = ""
    harrisonburg_rows = []

    for row in data:
        if row[1] == 'Rockingham' and row[2] == 'Virginia':  #sorting only data contrianed by Rockingham and Virginia into a list
            rockingham_rows.append(row)
        if row[1] == 'Harrisonburg city' and row[2] == 'Virginia': #sorting only data contrianed by Harrisonburg and Virginia into a list
            harrisonburg_rows.append(row)

    for i in range(7, len(rockingham_rows)):    #loop to find data in the datatset over seven-day span
        current_data = rockingham_rows[i]
        previous_data = rockingham_rows[i-7]

        date, county, state, fips, cases, deaths = current_data     #identifying elements in the current data
        prev_date, prev_country, prev_state, prev_fips, prev_cases, prev_deaths = previous_data #identifying elements in the previous data 7 days prior

        current_cases = int(cases) - int(prev_cases)    #calculating current cases for the i in list

        if current_cases > seven_day_Rockingham:        #looping through all data and the greatest cases in seven day span is stored
                    seven_day_Rockingham = current_cases
                    worst_start_date_Rockingham = prev_date #start and end dates for that 7 day time span are stored
                    worst_end_date_Rockingham = date

    for i in range(7, len(harrisonburg_rows)):  #loop to find data in the datatset over seven-day span
        current_data = harrisonburg_rows[i]
        previous_data = harrisonburg_rows[i-7]

        date, county, state, fips, cases, deaths = current_data  #identifying elements in the current data
        prev_date, prev_country, prev_state, prev_fips, prev_cases, prev_deaths = previous_data  #identifying elements in the previous data 7 days prior

        current_cases = int(cases) - int(prev_cases)    #calculating current cases for the i in list

        if current_cases > seven_day_Harrisonburg: #looping through all data and the greatest cases in seven day span is stored
                    seven_day_Harrisonburg = current_cases
                    worst_start_date_Harrisonburg = prev_date   #start and end dates for that 7 day time span are stored
                    worst_end_date_Harrisonburg = date


    
    print('The worst 7-day period in Harrisonburg started on the date', worst_start_date_Harrisonburg, #Printing worst seven days answers
          'and ended on the date', worst_end_date_Harrisonburg, 'with', seven_day_Harrisonburg, 'cases.')
    print('The worst 7-day period in Rockingham County started on the date', worst_start_date_Rockingham, 
          'and ended on the date', worst_end_date_Rockingham, 'with', seven_day_Rockingham, 'cases.')
    return seven_day_Rockingham, seven_day_Harrisonburg

if __name__ == "__main__":
    data = parse_nyt_data('C:\\Users\\austi\\OneDrive\\Documents\\GitHub\\ENGR315-sp2026-student\\Exams\Assignment 1 - COVID Data\\us-counties.csv')

    # for (date,county, state, fips, cases, deaths) in data:
    #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data)


