import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

testurl="file:///C:/Users/vamsi/Desktop/BidAlert.htm"#url to Scrape

uClient=uReq(testurl)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

#Columns to be Parsed
BidAlertNos=[]
AgencyBidNos=[]
Titles=[]
ReceivedDates=[]
CloseDates=[]
PurchaseTypes=[]
DeliveryPoints=[]
DeliveryDates=[]
IssuingAgencies=[]
UsingAgencies=[]
States=[]
AgencyTypes=[]
Contacts=[]

#Logic to parse html
tables = page_soup.find_all(class_='bidmatches')
for i in tables:
    innertables = i.find_all('table')
    for i in innertables:
        subinnertables=i.find_all('table')
        for sit in subinnertables:
            table_rows=sit.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text.strip().replace('\n',' ') for i in td]

                #print(row)
                if len(row)==2:
                    if row[0].startswith('Bid Alert No.:'):
                        BidAlertNos.append(row[1])
                    elif row[0].startswith('Agency Bid No.:'):
                        AgencyBidNos.append(row[1])
                    elif row[0].startswith('Title:'):
                        Titles.append(row[1])
                    elif row[0].startswith('Received Date:'):
                        ReceivedDates.append(row[1])
                    elif row[0].startswith('Close Date:'):
                        CloseDates.append(row[1])
                    elif row[0].startswith('Delivery Point:'):
                        DeliveryPoints.append(row[1])
                    elif row[0].startswith('Issuing Agency:'):
                        IssuingAgencies.append(row[1])
                    elif row[0].startswith('Using Agency:'):
                        UsingAgencies.append(row[1])
                    elif row[0].startswith('State:'):
                        States.append(row[1])
                    elif row[0].startswith('Agency Type:'):
                        AgencyTypes.append(row[1])
                   

#Creating Dataframe
BidInfoDF = pd.DataFrame(
    {
    "BidAlertNo":BidAlertNos,
     "AgencyBidNos":AgencyBidNos,
     "Titles":Titles,
     "ReceivedDates":ReceivedDates,
     "CloseDates":CloseDates,
     "DeliveryPoints":DeliveryPoints,
     "IssuingAgencies":IssuingAgencies,
     "UsingAgencies":UsingAgencies,
     "States":States,
     "AgencyTypes":AgencyTypes,
    }
)

#Writing file to csv
BidInfoDF.to_csv("C:\\Users\\vamsi\\Desktop\ETL\\BidInfo.csv",index=False)







