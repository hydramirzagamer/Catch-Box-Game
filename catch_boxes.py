import random
import pygame

pygame.init()


#Screen Height
screen_h = 2130
screen_w = 1030


#Colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
brown = (150, 75, 0)
aqua = (0,255,255)





#Screen and Caption
screen = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("RocketGameByMirza")
pygame.display.update()



#Clock and FPS (Frame Per Second)
clock = pygame.time.Clock()
fps = 40



#Font and Text 
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)
	screen.blit(screen_text, [x,y])
	


#Main Program
def main():
	exit_game = False
	game_over = False
	
	#Import Highscore File
	with open("hiscore.txt", "r") as f:
		hi_score = f.read()
	
	
	#Computer Boxes
	comp_x = random.randint(0, 1030)
	comp_x1 = random.randint(0, 1030)
	comp_x2 = random.randint(0, 1030)
	comp_x3 = random.randint(0, 1030)
	comp_y = random.randint(0, 300)
	comp_y1 = random.randint(0, 300)
	comp_y2 = random.randint(0, 300)
	comp_y3 = random.randint(0, 300)
	
	#Importing Image
	
	bg_img = pygame.image.load('click_to_start.png')
	bg_img = pygame.transform.scale(bg_img, (500, 150))
	
	
	#Computer Boxes Speed
	rm = random.randint(2, 10)
	rl = random.randint(2, 10)
	rn = random.randint(2, 10)
	r = random.randint(2, 10)
	print(r, rm, rl, rn)
	
	
	#Box Size
	comp_size = 70
	
	
	#Score and Game Over
	score = 0
	over = 0
	over_o = 3
	
	#Player Size and Position
	player_x = 500
	player_y = 1900
	player_size = 50
	p_size = 150
	
	
	#Main Loop Start
	while not exit_game:
		#GameOver
		if game_over:
			screen.fill(aqua)
			screen.blit(bg_img,(300, 1000))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#Score Save
					with open("hiscore.txt", "w") as f:
						f.write(str(hi_score))
					exit_game = True
				
				#Buttons
				if event.type == pygame.MOUSEBUTTONDOWN:
					#Button Pos For Mobile Devices
					(pos_x,pos_y)= (pygame.mouse.get_pos())
					if pos_x>300 and pos_x<800:
						if pos_y>1000 and pos_y<1200:
							main()
		
					
						
		else:
			#Get Event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				#Touch Event	
				if event.type == pygame.MOUSEBUTTONDOWN:
					(pos_x,pos_y)= (pygame.mouse.get_pos())
					
					#Right
					if pos_x>500:
						player_x += 50
					#Left
					if pos_x<500:
						player_x -= 50
						
			#Game Over +1		
			if comp_y > screen_h:
				over += 1
				over_o -= 1
				comp_x = random.randint(0, 1030)
				comp_y = random.randint(0, 400)
				rm = random.randint(2, 10)
				
				
			if  comp_y1 > screen_h:
				over += 1
				over_o -= 1
				comp_y1 = random.randint(0, 400)
				comp_x1 = random.randint(0, 1030)
				rn = random.randint(2, 10)
				
			if  comp_y2 > screen_h:
				over += 1
				over_o -= 1
				comp_y2 = random.randint(0, 400)
				comp_x2 = random.randint(0, 1030)
				rl = random.randint(2, 10)
				
			if  comp_y3 > screen_h:
				over += 1
				over_o -= 1
				comp_y3 = random.randint(0, 400)
				comp_x3 = random.randint(0, 1030)
				r = random.randint(2, 10)
				
			#Increase Score
			if abs (player_x-comp_x) <100 and abs (player_y-comp_y) <80:
				score += 6
				comp_x = random.randint(0, 1030)
				comp_y = random.randint(0, 400)
				rm = random.randint(2, 10)
				
				
			if abs (player_x-comp_x1) <100 and abs (player_y-comp_y1) <40:
				score += 6
				
				comp_y1 = random.randint(0, 400)
				comp_x1 = random.randint(0, 1030)
				
				rn = random.randint(2, 10)
				
			
			if abs (player_x-comp_x2) <100 and abs (player_y-comp_y2) <40:
				score += 6
				
				comp_y2 = random.randint(0, 400)
				comp_x2 = random.randint(0, 1030)
				rl = random.randint(2, 10)
				
			if abs (player_x-comp_x3) <100 and abs (player_y-comp_y3) <40:
				score += 6
				
				comp_y3 = random.randint(0, 400)
				comp_x3 = random.randint(0, 1030)
				r = random.randint(2, 10)
				
			#Game Over	
			if over == 3:
				game_over = True
			
			#Hi Score Write
			if score > int(hi_score):
				hi_score = score
			
			#Screen Fill With Color	
			screen.fill(aqua)
			
			#Boxes Speed
			comp_y += rm
			comp_y1 += rn
			comp_y2 += rl
			comp_y3 += r
			
			#High Score Text and Chances Left
			text_screen("Score: " + str(score) + "  High Score: " + str(hi_score), red, 5, 5)
			text_screen("Chance Left: " + str(over_o), red, 800, 5)
			#Draw Comp Boxes
			pygame.draw.rect(screen, brown, [comp_x, comp_y, comp_size, comp_size])
			pygame.draw.rect(screen, brown, [comp_x1, 	comp_y1, comp_size, comp_size])
			pygame.draw.rect(screen, brown, [comp_x2, 	comp_y2, comp_size, comp_size])
			pygame.draw.rect(screen, brown, [comp_x3, 	comp_y3, comp_size, comp_size])
			
			#Draw Player
			pygame.draw.rect(screen, black, [player_x, player_y, p_size, player_size])
			
		#Screen Update
		pygame.display.update()
		clock.tick(fps)
		
	pygame.quit()
	quit()
	
#Call Main Function	
main()