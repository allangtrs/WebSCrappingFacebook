# Facebook Marketplace Scrapper
This is a Python script that uses the Selenium and Pandas libraries to scrape data from Facebook Marketplace search results and save it in a CSV file.

## Final Product
This code example is designed to scrape Facebook Marketplace for bass guitar listings and store the relevant data in a CSV file. The data includes the name of the bass, its price, and a URL to the listing.

## Tools Used
The code is written in Python and uses the following libraries:

- pandas: for storing the scraped data in a DataFrame and exporting it to a CSV file.
- selenium: for automating the web browsing process and scraping data from Facebook Marketplace.
- webdriver: for driving the Chrome browser and navigating Facebook Marketplace.

## Execution Process
The process of scraping Facebook Marketplace for bass guitar listings involves the following steps:

1. Open Chrome browser using the webdriver and navigate to the Facebook login page.
2. Enter the user's login credentials and login to Facebook.
3. Navigate to the Facebook Marketplace and search for "Bass".
4. Scroll down to load more items, then scrape the relevant data from the listings.
5. Store the data in a Python dictionary and convert it to a pandas DataFrame.
6. Export the DataFrame to a CSV file.

## Conclusion
This code can be used as a starting point for anyone who wants to scrape data from Facebook Marketplace. With a few modifications, it can be adapted to scrape data for other types of listings as well. However, it is important to note that web scraping can be against the terms of service of some websites, so users should proceed with caution and ensure they are not violating any rules or regulations.
