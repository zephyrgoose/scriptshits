import csv
from collections import Counter
import user_agents
from prettytable import PrettyTable

#Define the number of top browsers to display
TOP_BROWSERS = 2000

#Define the count threshold for user agents to be included in the table
COUNT_THRESHOLD = 250

#Define the filename of the CSV file
FILENAME = 'list.csv'

#Define a list to store the parsed browsers and their counts
browser_counts = Counter()

#Define a variable to store the total count of all browsers
total_count = 0

#Open the CSV file and read its contents
with open(FILENAME, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  #skip the first line
    #Iterate over each row in the CSV file
    for row in reader:
        #Extract the user agent and count from the row
        user_agent, count = row[0], int(row[1])
        #Ignore the user agent if its count is less than the threshold value
        if count < COUNT_THRESHOLD:
            continue
        #Parse the user agent string
        ua = user_agents.parse(user_agent)
        #Extract the browser information
        browser = f"{ua.browser.family} {ua.browser.version_string}"
        #Add the count to the existing count for this browser
        browser_counts[browser] += count
        #Add the count to the total count
        total_count += count

#Create a pretty table
table = PrettyTable(['Browser', 'Count', '% of Total'])
#Add the top x most used browsers to the table
for browser, count in browser_counts.most_common(TOP_BROWSERS):
    percentage = round((count / total_count) * 100, 4)
    table.add_row([browser, count, f"{percentage}%"])

#Set the output format to plain columns
table.set_style(16)

#Print the table
print(f"Top {TOP_BROWSERS} most used browsers with a count of {COUNT_THRESHOLD} or greater:")
print(table)