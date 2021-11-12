# ada-2021-project-aaaf
1. Download file from zenodo for specific year and unzip this file: 

    `wget https://zenodo.org/record/4277311/files/quotes-YEAR.json.bz2`

    `bzip2 -d quotes-YEAR.json.bz2`

2. Process jsons with quatations to parse quatations with tag climate change:
    
    `python3 scripts/filter.py --file='quotes-{YEAR}.json'`
3. Megre this files with wikidata:
    
    `python3 scripts/merge.py --file='quotes-{YEAR}-processed.json'`
4. Move processed data to data folder (default 'data'):
    
    `mv quotes-{YEAR}-processed.json data` 
    
    `mv quotes-{YEAR}-merged.json data`
    
5. Merge all json files for all years from 2008 to 2020, received 'data/union.json'.

6. Creat vocabularies for countries and occupations for processed quatations:
    
    `python scripts/utils.py --file=data/union.json`

asd
