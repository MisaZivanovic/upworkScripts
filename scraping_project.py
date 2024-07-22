import requests
from bs4 import BeautifulSoup

list_of_states = []
list_of_cities = []
list_of_agents = []
agent_dict = {}

def scrapeIt(url,href_class,list_to_append_to):
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("ul", class_="map-list")
    results = results.find_all("li")
    for x in results:
        new = x.find("a",class_=href_class)
        list_to_append_to.append(new.get("href"))

        if list_to_append_to==list_of_agents:
            print("Ima ovoliko agenata",len(list_to_append_to)," u ",url)

url1 = "https://www.newyorklife.com/agents/find-an-agent"
scrapeIt(url1,"ga-link",list_of_states)
print("States finished",len(list_of_states))

for state in list_of_states:
    scrapeIt(state,"ga-link",list_of_cities)
print("cities finished",len(list_of_cities))
for city in list_of_cities:
    scrapeIt(city,"location-name",list_of_agents)

for url in list_of_agents:
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="cmp-agent-profile__details")
    if results!=None:
        h1_text = results.find("h1")
        h1_text = results.get_text(strip=True)
        name = h1_text.replace("Your Financial Professional & Insurance Agent","")
        email_text = results.find("a")
        email_text = email_text.get("href").replace("mailto: ","")
        cell_phone = results.find("div",class_="cmp-agent-profile__phone")
        cell_phone = cell_phone.find_all("span",class_="cmp-agent-profile__phone-value")[1].get_text()

        agent_dict[name]={"email":email_text,"cell phone":cell_phone}
    else:
        print("Empty url =>",url)
        pass
print("All done!")