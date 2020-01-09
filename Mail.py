from time import sleep
from os import system
from os import name
from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
import datetime

_OS_ = "Linux"
_APPNAME_ = "Gmail Automation Mails"
_VERSION_ = "1.0.0"
_DEVELOPER_ = "Pr0xy"


class GmailAutomation(object):
    def __init__(self, FirstLine, SecondLine, ThirdLine):
        self.FirstLine = FirstLine
        self.SecondLine = SecondLine
        self.ThirdLine = ThirdLine

        print(
            self.FirstLine + "\n" +
            self.SecondLine + "\n" +
            self.ThirdLine
        )

    def MailConfiguration(self, gecodriverpath, gmailadress, inbox, mailarg, passarg, hours, minutes):
        self.geckodriverpath = gecodriverpath
        self.gmailadress = gmailadress
        self.inbox = inbox
        self.gmail = mailarg
        self.password = passarg
        self.hours = hours
        self.minutes = minutes
        self.mails = open("mails.txt", mode="r").readlines()
        self.options = webdriver.FirefoxOptions
        self.webdriver = webdriver.Firefox(executable_path=self.geckodriverpath)
        self.webdriver.maximize_window()
        self.webdriver.get(self.gmailadress)
        self.name = WebDriverWait(self.webdriver, 1).until(EC.presence_of_element_located((By.NAME, "identifier")))
        self.name.send_keys(self.gmail)
        sleep(0.5)
        self.name.send_keys(Keys.ENTER)
        self.passwd = WebDriverWait(self.webdriver, 1).until(EC.presence_of_element_located((By.NAME, "password")))
        sleep(0.5)
        self.passwd.send_keys(self.password)
        sleep(0.5)
        self.passwd.send_keys(Keys.ENTER)
        self.wait = WebDriverWait(self.webdriver, 10)
        sleep(10)
        self.counter = 0
        for self.item in self.mails:
            self.counter += 1
            if self.counter == 200:
                print(
                    Fore.RED + "[!] " + Fore.RESET + "200 Mail gönderildi daha fazlası gönderilemez başka e-mail adresi giriniz.")
                print(Fore.GREEN + "> {}".format(str(self.counter)))
                self.webdriver.quit()
                pass
            else:
                self.getmail = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")))
                self.getmail.click()
                self.to = self.wait.until(EC.presence_of_element_located((By.NAME, "to")))
                sleep(1.5)
                self.to.send_keys(self.item)
                self.subject = self.wait.until(EC.presence_of_element_located((By.NAME, "subjectbox")))
                sleep(1.5)
                self.subject.send_keys("Instagram Verification Badge")
                self.subject.send_keys(Keys.TAB + Keys.CONTROL + "v")
                sleep(1)
                self.subject.send_keys(Keys.CONTROL + Keys.ENTER)
                sleep(1)
                print(
                    Fore.YELLOW + "[" + self.hours + ":" + self.minutes + "] " + Fore.RESET + Fore.GREEN + "[OK][200] > " + Fore.RED + "{}".format(
                        str(self.item)) + Fore.RESET)
                sleep(5)
        self.webdriver.quit()
        sleep(0.3)
        print(Fore.YELLOW + "[*] " + Fore.RESET + "Mail Delivery Completed > " + Fore.GREEN + "{} ".format(
            str(self.counter)) + "Mails")

    def MailsControl(self):
        self.mails = open("mails.txt", mode="r").readlines()
        self.counter = 0
        for self.item in self.mails:
            self.counter += 1
            sleep(0.1)
            print("{}. ".format(str(self.counter)) + Fore.GREEN + "{}".format(self.item) + Fore.RESET)
        print("Total : " + Fore.RED + "{}".format(self.counter))
        pass


if __name__ == "__main__":
    if name == "win32" or name == "win64":
        system("cls")
    else:
        system("clear")
    FirstLine = Fore.YELLOW + "[1] " + Fore.RESET + Fore.GREEN + "Start Mail Automation" + Fore.RESET
    SecondLine = Fore.YELLOW + "[2] " + Fore.RESET + Fore.GREEN + "Mails.txt Control" + Fore.RESET
    ThirdLine = Fore.YELLOW + "[3] " + Fore.RESET + Fore.GREEN + "Exit" + Fore.RESET
    geckodriverpath = "geckodriver"
    gmailadress = "https://accounts.google.com/signin/v2/identifier?hl=tr&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession"
    inbox = "https://mail.google.com/mail/u/0/#inbox?compose=new"
    hours = datetime.datetime.now().strftime("%H")
    minutes = datetime.datetime.now().strftime("%M")
    argsettings = ArgumentParser()
    argsettings.add_argument("-g", "--gmail", required=True, help="E-Mail Adress Enter..")
    argsettings.add_argument("-p", "--password", required=True, help="Password Adress Enter..")
    args = vars(argsettings.parse_args())
    mailarg = args["gmail"]
    passarg = args["password"]
    start = GmailAutomation(FirstLine, SecondLine, ThirdLine)
    choice = input(Fore.YELLOW + "[?] " + Fore.RESET + "Enter Choice : ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            start.MailConfiguration(geckodriverpath, gmailadress, inbox, mailarg, passarg, hours, minutes)
        elif choice == 2:
            start.MailsControl()
        elif choice == 3:
            pass
        else:
            print(Fore.RED + "[!]" + Fore.RESET + "Please Enter Number 1, 2 or 3")
    else:
        print(Fore.RED + "[!]" + Fore.RESET + "Please Enter Number")