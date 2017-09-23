import requests, os, notify
from bs4 import BeautifulSoup

def scrapeData() : 
    print("Fetching source ...")
    try :
        ls = requests.get("http://www.livescores.com/")
    except Exception as e :
        print(e)
        return False
    # query and extract source for livescores.com
    
    print("feeding source to beautiful soup .. \n")
    soup = BeautifulSoup(ls.text, 'html.parser')
    # serve the html to beautiful for parsing using html-parser
    
    scoresDict = { }
    # this is going to be a dictionary that will store the scores for each team
    
    for el in soup.find_all("div", "row-gray") :
    
	    homeTeam = el.find("div", "tright").get_text().strip()
	    homeTeamScore = el.find("div", "sco").get_text().split("-")[0].strip()
	    # this extracts the name and score of the home team
	    
	    scoresDict[homeTeam] = homeTeamScore
	    
    
	    awayTeam = el.find(attrs={"class": "ply name"}).get_text().strip()
	    awayTeamScore = el.find("div", "sco").get_text().split("-")[1].strip()
	    
	    scoresDict[awayTeam] = awayTeamScore

	    # this will extract the name and score of the away team
	    # print("{} {}-{} {}".format(homeTeam, homeTeamScore, awayTeamScore, awayTeam))
	    # we print it out
    return scoresDict

# def run() :
#     scrapeData()
#     if change in score :
#         notify.showNotif("Golazo!!", "{} goal!!}")
#         time.sleep(1)
#     time.sleep(1)
#     run()

