import pyautogui
import time

def find_click_point(x, y):
	im = pyautogui.screenshot()
	set_color = im.getpixel((x, y))
	for i in range(0, 20):
		if(im.getpixel((x, y + i*5)) != (255, 255, 255)):
			return (x, y + i*5)
	
	return (0, 0)

def confirm_load_area(x, y):
	im = pyautogui.screenshot()
	flag = True
	set_color = im.getpixel((x, y))
	for i in range(0, 10):
		for j in range(0, 10):
			if(im.getpixel((x + i*3, y + j*3)) != set_color):
				flag = False
				break
		
		if(flag == False):
			break
	
	return flag

wh = pyautogui.size()

cnt = 0
time_cnt = 0
while(1):
	time.sleep(3)
	
	time_cnt += 1
	time_cnt = time_cnt%2
	
	if(time_cnt == 0):
		pyautogui.moveTo(pyautogui.position()[0] + 3, pyautogui.position()[1], duration=0.25)
	else:
		pyautogui.moveTo(pyautogui.position()[0] - 3, pyautogui.position()[1], duration=0.25)
	print(pyautogui.position())
	
	#pyautogui.moveTo(wh.width*0.377, wh.height*0.19, duration=0.25)
	
	im = pyautogui.screenshot()
	# for i in range(10):
	#print(im.getpixel((wh.width - 10, wh.height/2)))
	print(wh)
	# input("break")
	print(cnt)
	scan_result = confirm_load_area(20, wh.height - 30)
	if(scan_result == True):
		cnt += 1
	else:
		cnt = 0
	
	print(pyautogui.position())
	
	print(im.getpixel((wh.width - 5, wh.height/2)))
	
	if(cnt > 2):
		if(im.getpixel((wh.width - 5, wh.height/2)) == (255, 255, 255)):
			print("BP1")
			if(find_click_point(wh.width*0.377, wh.height*0.19) != (0, 0)):
				pyautogui.click(find_click_point(wh.width*0.377, wh.height*0.19), duration=0.25)
			else:#959, 297
				pyautogui.click(find_click_point(wh.width*0.499, wh.height*0.275), duration=0.25)
		else:
			print("BP2")
			for i in range(10):	
				pyautogui.scroll(-200)
				time.sleep(0.3)
			pyautogui.click(wh.width - 10, wh.height/2, duration=0.25)
		cnt = 0	
		pyautogui.moveTo(wh.width*0.9, wh.height*0.9, duration=0.25)
		

