from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
# run in background (no browser opens)
chrome_options.add_argument('headless')
# path to browser 
driver = webdriver.Chrome('/Users/hhemba109/Desktop/Projekte/Python/drivers/chromedriver', options=chrome_options)

# fill string with links and transform to list(array)
f= open('links.txt', 'r')
link_list = f.read().split('\n')


# list of search terms
search_terms = [["Fußball", "Handball", "Tennis"]]


def do_stuff():
    print("started process")
    for i in range(0, len(link_list)):
        driver.get(link_list[i])
        print(link_list[i])

        # get source code of visited page 
        html_source = driver.page_source

        # count appearances of search termns 
        count1 = html_source.count(search_terms[0][0])
        count2 = html_source.count(search_terms[0][1])
        count3 = html_source.count(search_terms[0][2])

        # append searchtermlist with occurences  
        search_terms.append([count1, count2, count3])

        # open csv file to fill with results
        output_file = open('output.csv', 'w')


        # write results to output file 
        with output_file:
            writer = csv.writer(output_file)
            writer.writerows(search_terms)

    quit()

do_stuff()




