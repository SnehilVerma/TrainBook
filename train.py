from selenium import webdriver
from datetime import datetime
from threading import Timer



driver = webdriver.Firefox()
driver.maximize_window()
#driver.get('https://www.google.co.in/')
'''driver.get('http://www.d2kindia.com/')'''
driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
print(driver.title)



'''
def press_submit():
	subclick=driver.find_element_by_id('MainContent_btnSubmit')
	subclick.click()
	print(driver.current_url)
	


def book_ticket():
	elem1=driver.find_element_by_link_text('Register')
	elem1.click()
	print(driver.current_url)
	inputElement = driver.find_element_by_id("MainContent_txtName")
	inputElement.send_keys('Snehil Verma')
	x=datetime.today()
	y=x.replace(day=x.day+1,hour=13,minute=24,second=30,microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t1=Timer(secs,press_submit)
	t1.start()




#CLICK A LINK AT HH:MM:SS:MSMS ON A DESIRED WEBSITE.

x=datetime.today()
y=x.replace(day=x.day+1,hour=13,minute=23,second=30,microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t=Timer(secs,book_ticket)
t.start()

'''

def book_now():
	print(driver.current_url)
	elem1=driver.find_element_by_id('12533-SL-TQ-0')
	elem1.click()

	'''
	inputElement4=driver.find_element_by_id('addPassengerForm:psdetail:0:p507118422')
	inputElement4.send_keys('Gaurav Rai')
	inputElement5=driver.find_element_by_id('addPassengerForm:psdetail:0:psgnAge')
	inputElement5.send_keys('20')
	inputElement6=driver.find_element_by_id('addPassengerForm:psdetail:0:psgnGender')
	inputElement6.send_keys('Male')
	inputElement7=driver.find_element_by_id('addPassengerForm:psdetail:0:psgnGender')
	inputElement7.send_keys('LOWER')'''

	'''ON YOUR OWN ACCORD FROM HERE. FILL THE REMAINING DETAILS .YOU WOULD BE PRETTY AHEAD IN THE GAME RIGHT FROM HERE'''








def press_submit():
	print(driver.current_url)
	subclick=driver.find_element_by_id('jpform:jpsubmit')
	subclick.click()

	'''radioButton = driver.find_element_by_name("quota")
	radioButton.get(4).click()'''
	driver.find_element_by_css_selector("input[type='radio'][value='TQ']").click()
	sleeper_book=driver.find_element_by_id('cllink-12533-SL-3')
	sleeper_book.click()

	x=datetime.today()
	y=x.replace(day=x.day+1,hour=16,minute=42,second=10,microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t1=Timer(secs,book_now)
	t1.start()


	'''rsize=radioButtons.size()'''


	

def press_login():
	subclick=driver.find_element_by_id('loginbutton')
	subclick.click()
	print(driver.current_url)


	inputElement = driver.find_element_by_id("jpform:fromStation")
	inputElement.send_keys('KANPUR CENTRAL - CNB')
	inputElement2 = driver.find_element_by_name("jpform:toStation")
	inputElement2.send_keys('MUMBAI CST - CSTM')
	inputElement3=driver.find_element_by_id('jpform:journeyDateInputDate')
	inputElement3.send_keys('08-06-2017')
	x=datetime.today()
	y=x.replace(day=x.day+1,hour=16,minute=42,second=00,microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t1=Timer(secs,press_submit)
	t1.start()



	
	


def book_ticket():
	'''elem1=driver.find_element_by_link_text('Register')
	elem1.click()'''
	print(driver.current_url)
	inputElement = driver.find_element_by_id("usernameId")
	inputElement.send_keys('grai3040')
	inputElement = driver.find_element_by_name("j_password")
	inputElement.send_keys('guc314')
		
	x=datetime.today()
	y=x.replace(day=x.day+1,hour=16,minute=41,second=40,microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t1=Timer(secs,press_login)
	t1.start()




#CLICK A LINK AT HH:MM:SS:MSMS ON A DESIRED WEBSITE.

x=datetime.today()
y=x.replace(day=x.day+1,hour=16,minute=41,second=30,microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t=Timer(secs,book_ticket)
t.start()





'''
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get('http://christopher.su')
'''
