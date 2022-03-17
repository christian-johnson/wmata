# WMATA Servide Disruption: Data and Analysis

The Washington Metropolitan Area Transit Authority (WMATA), a.k.a. Metro, runs the Washington DC local metrorail and bus service. 
WMATA makes available a daily log of service disruptions on their [website](https://www.wmata.com/service/daily-report/), which is available in plain HTML. 
After WMATA's 7000-series trains were removed from service in late 2021 due to a wheelset issue, I decided to scrape this data and make it available for analysis.
My hope is that by looking at historical service data, we can identify recurring service issues and help improve the safety culture at WMATA.

For transparency, I'm including the code I used to scrape the webpage, although I *do not* recommend you run it yourself; instead, please use the included JSONL file which has been cleaned and formatted for analysis.
