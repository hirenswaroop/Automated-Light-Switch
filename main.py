import pygame as pg
import time
import pigpio

pg.init()
screen = pg.display.set_mode([600, 600])

pi = pigpio.pi()

pi.set_mode(13, pigpio.OUTPUT)
pi.set_PWM_range(13, 100)
pi.set_PWM_frequency(13, 50)
is_on = False

while True:
	for event in pg.event.get():
		if event.type == pg.MOUSEBUTTONDOWN:
			if not is_on and event.button == 1:
				print('ON')
				is_on = True
				pi.set_servo_pulsewidth(13, 2000)
				pi.set_PWM_dutycycle(13, 50)
				time.sleep(1)
				pi.set_PWM_dutycycle(13, 0)
				pi.set_servo_pulsewidth(13, 1500)
			elif is_on and event.button == 3:
				print('OFF')
				is_on = False
				pi.set_servo_pulsewidth(13, 1000)
				pi.set_PWM_dutycycle(13, 50)
				time.sleep(1)
				pi.set_PWM_dutycycle(13, 0)
				pi.set_servo_pulsewidth(13, 1500)