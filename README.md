# ADA 2021 AAF Team Project
    Arsenii Gavrilenko
    Aleksandr Samoilenko
    Anastasiia Filippova
### 12.11.2021  Milestone 2 report
#### Abstract
In the 21 century Internet and Social Networks brought the speed and depth of trend spreading to the new level. Classical media like newspappers now could use Twitter as a resource of information. Based on this trend and data we have we decided to focus on trend spreading over the people. We are going to try to extract from the data some correlations and dependencies in the filed of trend spreading. In fact we have to goals, the first one is to analyze how fast and wide some trends could be. The second goal is to identifing of some biases we could have in the data.
For example some resources or occupations(profesional) could be biased on the some topic. Talking about our data - the frequency of some topic could be much higher or lower that the average.

#### Research Questions:
The trends we are talking about are some topics, for example it could be `climate change, elections, Trump`. In our further analysis we would catch the appereance of this topics in the quoutes. We could use exact substring search or kind of similarity matching as fuzzy matching.
##### Trends spreading
The first direction of our analysis is a simple and straightforward analysis of trens spreading. It then would be used as the base for the second part - biases and correlation analysis. Talking about this part we are going to focus on:
1. The frequency of topic across different years
2. The frequency of topic across different seasons (of the year/ quarters/ months)
3. Which trends are more fast in terms of changing frequency.

##### Identifing biases and correlations
The second part is more deep one. Here we are going to do the core analysis for our final deliverables on the project. Our goal is to find any biases in the data we have. For example:
1. The speed and depth of trends spreading in different country are equal or not?
2. The speed and depth of trends spreading in differend profesional occupations are equal?
3. Gender/Age biases of the different trends spreading
4. Correlation of the topics spreading in the dataset and GoogleTrends data (biases of our dataset/biases of quotes)



#### Proposed additional datasets:
Google Trends API 

 `https://pypi.org/project/pytrends/`
 
>Google trends is a website that analyzes and lists the popular search results on Google search based on various regions and languages. Google Trends is Google’s website (obviously). There is a Python API called pytrends.
We would use this API later to collect the data about our speakers.

WikiData API 

`https://www.wikidata.org/wiki/Wikidata:Main_Page`
> Wikidata is a free and open knowledge base that can be read and edited by both humans and machines.
Wikidata acts as central storage for the structured data of its Wikimedia sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource, and others.
We are going to use this data source to acquire all data about speakers in out initial dataset. For example for the first analysis we are using gender and occupation merged from wiki data. 




#### Methods
We should notice the data we have is very large, that is why we are going to use prepocessing as much as we can. In our case we are going to filter quotes containg some interesting for us words(topics).
##### Raw data processing 

1. Download file from zenodo for specific year and unzip this file: 

    `wget https://zenodo.org/record/4277311/files/quotes-{YEAR}.json.bz2`

    `bzip2 -d quotes-YEAR.json.bz2`

2. Process jsons with quatations to parse quatations with tag climate change:
    
    `python3 scripts/filter.py --year={YEAR}'`
3. Megre this files with wikidata:
    
    `python3 scripts/wikidata_merge.py --year={YEAR}'`
4. Move processed data to data folder (default 'data'):
    
    `mv quotes-{YEAR}-filtered.json data` 
    
    `mv quotes-{YEAR}-wikimerged.json data`
    
5. Merge all json files for all years from 2008 to 2020, received 'data/union.json'.

6. Creat vocabularies for countries and occupations for processed quatations:
    
    `python scripts/utils.py --file=data/union.json`
    
##### Simple Exploratary Analysis
We are going to start with simple graphical and statistical exploration of data.
In this part we are going to use basic data anslysis tools to get in touch with our data and to understand precisely the direction of analysis on the next parts.
1. Checking the distribution of all categorical data we have (gender, occupation)
2. Checking the 
    
##### Correlation analysis



#### Proposed timeline & internal milestones
12 Nov 2021: Milestone P2

19 Nov 2021:
> Adding other topics to the trend research and performing basic analysis. First draft of hypothesis about the data.


26 Nov 2021:
> Correlation analysis MVP - using GoogleTrend API.

3 Dec 2021: 
>Building frontend to better present our data story.
Correlation analysis id done.

10 Dec 2021:
> Frontend is built
All required analyses are done and well-packaged.

17 Dec 2021 Milestone P3
> Preparing slides and frontend for the final presentations.

