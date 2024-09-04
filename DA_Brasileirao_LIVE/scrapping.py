import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver and open the website
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://ge.globo.com/futebol/brasileirao-serie-a/"
driver.get(url)

# Scape the Team Names and Scores
# team_names = driver.find_elements(By.CSS_SELECTOR, ".classificacao__equipes .classificacao__equipes--nome")
rows = driver.find_elements(By.CSS_SELECTOR, 'tr.classificacao__tabela--linha')
for row in rows:
    points = row.find_elements(By.CSS_SELECTOR, 'td.classificacao__pontos')
    # last_games = row.find_elements(By.CSS_SELECTOR, 'td.classificacao__pontos--ultimos_jogos span')
    
    print (row.text)
    print (points)
    print (points.text)

    # # Print the points
    # for point in points:
    #     print (point.text, end=' ')
    
    # # Print the last game results
    # for game in last_games:
    #     if 'classificacao__ultimos_jogos--v' in game.get_attribute('class'):
    #         print('V', end=' ')
    #     elif 'classificacao__ultimos_jogos--d' in game.get_attribute('class'):
    #         print('D', end=' ')
    #     elif 'classificacao__ultimos_jogos--e' in game.get_attribute('class'):
    #         print('E', end=' ')
    
    print()  


print()
driver.quit()

class Team:
    # Attributes : name, points, matches, wins, draws, losses, goals_for, goals_against, last_games
    def __init__(self, name:str, row:list):
        self.name = name
        self.row  = row
        self.points = ""
        self.matches = ""
        self.wins = ""
        self.draws = ""
        self.losses = ""
        self.goals_for = ""
        self.goals_against = ""
        self.last_games = ""

