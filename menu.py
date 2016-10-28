import pygame

class Menu(object):
    def __init__(self):
        self.last_answer = None
        self.last_answer_value = None
        self.MAX_TIMER = 20
        self.cooldown_timer = self.MAX_TIMER

    def draw(self, screen, score, high_score):

        screen.fill([0, 0, 0])
        #If last_answer is False then print the error message
        font = pygame.font.Font(None, 36)
        text = font.render("Witch Game", 1, (255, 255, 0))
        textpos = text.get_rect()
        textpos.left = 200
        screen.blit(text, textpos)

        question = font.render("Press space bar to start the game", 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.top = 65
        screen.blit(question, q_pos)

        question = font.render("Previous Score: {}".format(str(score)), 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.left = 50
        q_pos.top = 125
        screen.blit(question, q_pos)

        question = font.render("High Score: {}".format(str(high_score)), 1, (255, 255, 0))
        q_pos = question.get_rect()
        q_pos.left = 50
        q_pos.top = 165
        screen.blit(question, q_pos)

        pygame.display.update()


    def update(self, keys):

        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return

        #If we answered correctly then return True otherwise false
        if keys[pygame.K_SPACE]:
            return True
        # if keys[pygame.K_b] or keys[pygame.K_a] or keys[pygame.K_c] or keys[pygame.K_d]:
        #     return True

        return False
