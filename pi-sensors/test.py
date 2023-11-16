import time

if __name__ == '__main__':
	i = 0
	try:
		while True:
			print(f"Test {i}")
			time.sleep(2)
			i+=1
			
	except KeyboardInterrupt:
		print("Program stopped by User")
