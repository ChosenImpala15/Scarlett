import glob
import fitz

def search_data(firstArg):
    print("Retrieving...")
    print(firstArg)
    searches = firstArg
    #splits search text into an array of substrings
    searchArray = list((searches.split(' ')))

    #array of file names
    files = glob.glob('*/data/*.pdf')
    bulkText =""
    
    #iterates through files
    for file in files:
        matchAmount = 0
        #checks if each substring is in title
        for search in searchArray:
            if search in file.lower():
                matchAmount+=1
        #if 50% or more matching in title sets bulkText to the pdf text
        if matchAmount>=(len(searchArray)/2):
            doc = fitz.open(file)
            for page in doc:
                bulkText += page.get_text()
            break
    if not bulkText:
        return "No File Matching"
    return bulkText
    

if __name__ == '__main__':
    print(search_data("sir gawain"))
