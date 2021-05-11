from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def chromeDriver(PATH, chrome_options):
    driver = webdriver.Chrome(driverPATH, options=chrome_options)
    return driver

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('headless')

print("Download Chrome Driver from: https://chromedriver.chromium.org/downloads")
driverPATH = input("Provide path to chrome driver: ")
#driverPATH = "/home/sriram/Documents/chromedriver"

driver = chromeDriver(driverPATH, chrome_options)
websitePATH = "https://chemoinfo.ipmc.cnrs.fr/LEA3D/index.html"
driver.get(websitePATH)

cfProtein_button = driver.find_element_by_name("protein")

#upload file path w/ path
pdbPATH = input("Provide path to pdb file: ")
cfProtein_button.send_keys(pdbPATH)
#cfProtein_button.send_keys("/home/sriram/Documents/6x3x_apo.pdb")

#set coordinates of the center of the binding site (x,y,z)
cordx = driver.find_element_by_name("x")
cordy = driver.find_element_by_name("y")
cordz = driver.find_element_by_name("z")

print("")
x = input("Enter x coordinate: ")
y = input("Enter y coordinate: ")
z = input("Enter z coordinate: ")
print("")

cordx.clear()
cordx.send_keys(x)
#cordx.send_keys("145.6")

cordy.clear()
cordy.send_keys(y)
#cordy.send_keys("122.5")

cordz.clear()
cordz.send_keys(z)
#cordz.send_keys("120.9")

#set Binding site radius
bindingSiteRadius = driver.find_element_by_name("radius")

bindSiteRadius = input("Enter binding site radius: ")

bindingSiteRadius.clear()
bindingSiteRadius.send_keys(bindSiteRadius)
#bindingSiteRadius.send_keys("16.0")

#set Weight in final score
weightInFinalScore = driver.find_element_by_name("dockw")

weight = input("Enter weight in final score: ")

print("\nWaiting for response...\n")

weightInFinalScore.clear()
weightInFinalScore.send_keys(weight)
#weightInFinalScore.send_keys("1")

#make properties array of dictionaries
def dictionaryDefs():
    molecularWeight = {"mwmin" : "350", "mwmax" : "550", "mww" : "1"}

    molLogP = {"logpmin" : "-", "logpmax": "4.8", "logpw" : "0"}

    numOfAtoms = {"nbatommin" : "1", "nbatommax" : "5", "nbatomw" : "1"}

    numOfHDon = {"nbhdmin" : "1", "nbhdmax" : "10", "nbhdw" : "1"}

    numOfHAcc = {"nbhamin" : "-", "nbhamax" : "9", "nbhaw" : "0"}

    polarSolventAccSA = {"psamin" : "-", "psamax" : "140", "psaw" : "0"}

    fsp3 = {"fsp3min" : "0.3", "fsp3max" : "-", "fsp3w" : "0"}

    vol = {"volumemin" : "-", "volumemax" : "-", "volumew" : "0"}

    area = {"areamin" : "-", "areamax" : "-", "areaw" : "0"}

    numOfRotatableBonds = {"rotmin" : "2", "rotmax" : "8", "rotw" : "1"}

    numOfRings = {"nringmin" : "1", "nringmax" : "6", "nringw" : "0"}

    numOfAromaticRings = {"nringamin" : "1", "nringamax" : "4", "nringaw" : "1"}


    allPropertiesArr = [molecularWeight, molLogP, numOfAtoms, numOfHDon, numOfHAcc, polarSolventAccSA, fsp3, vol, area, numOfRotatableBonds, numOfRings, numOfAromaticRings]

    return allPropertiesArr

allPropertiesArr = dictionaryDefs()


#send info of allPropertiesArr to webpage
def populatingProperties(allProperties, driver):
    for dict in allPropertiesArr:
        for key in dict:
            field = driver.find_element_by_name(key)
            field.clear()
            field.send_keys(dict[key])

populatingProperties(allPropertiesArr, driver)

#submit
submitButton = driver.find_element_by_css_selector("body > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(2) > table > tbody > tr:nth-child(6) > td > center > input[type=submit]")

submitButton.click()


#next page after submitButton is clicked

#enter email
emailField = driver.find_element_by_name("email")

email = input("Email: ")

emailField.send_keys(email)
#emailField.send_keys("sriramy2001@gmail.com")

#select de novo drug design
deNovo = driver.find_element_by_name("action")

deNovo.click()

#set number of generations
numOfGen = driver.find_element_by_name("GENMAX")

print("")
gen = input("Number of generations (max = 50): ")

numOfGen.clear()
numOfGen.send_keys(gen)
#numOfGen.send_keys("50")

#set Population size
popSize = driver.find_element_by_name("POP")

size = input("Population size (max = 40): ")

popSize.clear()
popSize.send_keys(size)
#popSize.send_keys("40")

#start with new population
start = driver.find_element_by_name("START")

start.click()

#submit
submitButton2 = driver.find_element_by_css_selector("body > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(8) > td > center > input[type=submit]")

submitButton2.click()
