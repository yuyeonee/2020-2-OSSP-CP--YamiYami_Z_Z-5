import pygame, sys, time
from pygame.locals import *
from Board import *




#            R    G    B
BLACK = (0, 0, 0)
RED = (225, 13, 27)
GREEN = (98, 190, 68)
BLUE = (64, 111, 249)
ORANGE = (253, 189, 53)
YELLOW = (246, 227, 90)
PINK = (242, 64, 235)
CYON = (70, 230, 210)
GRAY = (26, 26, 26)
WHITE = (255, 255, 255)

# 나중에 사용할 사이즈 조절용 변수임
resize = 1
surver = False

class Tetris:

    #생성자
    def __init__(self):
        self.mode = 'basic'
        self.width = 10  # 가로 칸수
        self.height = 18  # 세로 칸 수
        self.block_size = 25*resize  # 블럭 하나당 크기
        self.display_width = (self.width+4)*self.block_size
        self.display_height = self.height*self.block_size
        self.screen = pygame.display.set_mode((self.display_width,  self.display_height),RESIZABLE)
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen, self.mode)
        self.music_on_off = True
        self.check_reset = True

    #각 키를 누를떄 실행되는 method
    def handle_key(self, event_key, mode):
        if event_key == K_DOWN or event_key == K_s:
            self.board.drop_piece(self.mode)
        elif event_key == K_LEFT or event_key == K_a:
            self.board.move_piece(dx=-1, dy=0)
        elif event_key == K_RIGHT or event_key == K_d:
            self.board.move_piece(dx=1, dy=0)
        elif event_key == K_UP or event_key == K_w:
            self.board.rotate_piece()
        elif event_key == K_SPACE:
            self.board.full_drop_piece(self.mode)
        elif event_key == K_q: #스킬 부분
            self.board.ultimate()
        elif event_key == K_m: # 소리 설정
            self.music_on_off = not self.music_on_off
            if self.music_on_off:
                pygame.mixer.music.play(-1, 0.0)
            else:
                pygame.mixer.music.stop()

#여기에 있던 high스코어 저장하는 것 삭제


    #실행하기
    def run(self):
        pygame.init()
        icon = pygame.image.load('assets/images/icon.PNG')  # png -> PNG로 수정
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tetris')

        self.board.level_speed() #추가 - level1에서 속도

        #start_sound = pygame.mixer.Sound('assets/sounds/Start.wav')
        #start_sound.play()
        #bgm = pygame.mixer.music.load('assets/sounds/bensound-ukulele.mp3')  # (기존 파일은 소리가 안남) 다른 mp3 파일은 소리 난다. 게임진행 bgm변경

        delay = 150
        interval = 100
        pygame.key.set_repeat(delay, interval)


        while True:

            if self.check_reset:
                self.check_reset = False
                #pygame.mixer.music.play(-1, 0.0)  ## 수정 필요 오류 나서 일단 빼둠

            if self.board.game_over():
                pygame.quit()
                break

            for event in pygame.event.get(): #게임진행중 - event는 키보드 누를떄 특정 동작 수할떄 발생
                if event.type == QUIT: #종류 이벤트가 발생한 경우
                    pygame.quit() #모든 호출 종
                    sys.exit() #게임을 종료한다ㅏ.
                elif event.type == KEYUP and event.key == K_p: # 일시 정지 버튼 누르면
                    self.screen.fill(BLACK)         #일시 정지 화면
                    #pygame.mixer.music.stop()       #일시 정지 노래 중둠    오류나서  일단 뺴
                    self.board.pause()
                    #pygame.mixer.music.play(-1, 0.0)
                elif event.type == KEYDOWN: #키보드를 누르면
                    self.handle_key(event.key, self.mode) #handle 메소드 실행
                elif event.type == pygame.USEREVENT:
                    self.board.drop_piece(self.mode)
                #화면 크기 조절해 보기
                elif event.type == VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE )

            # self.screen.fill(BLACK)
            self.board.draw(self, self.mode)
            pygame.display.update() #이게 나오면 구현 시
            self.clock.tick(30) # 초당 프레임 관련


class Mini:
    #생성자
    def __init__(self):
        self.mode = 'mini'
        self.width = 5  # 가로 칸수
        self.heik_ght = 15  # 세로 칸 수
        self.blocsize = 35*resize  # 블럭 하나당 크기
        self.display_width = (self.width+4)*self.block_size
        self.display_height = self.height*self.block_size

        self.screen = pygame.display.set_mode((self.display_width,  self.display_height),RESIZABLE)
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen, 'mini')
        self.music_on_off = True
        self.check_reset = True

    #각 키를 누를떄 실행되는 method
    def handle_key(self, event_key, mode):
        if event_key == K_DOWN or event_key == K_s:
            self.board.drop_piece(self.mode)
        elif event_key == K_LEFT or event_key == K_a:
            self.board.move_piece(dx=-1, dy=0)
        elif event_key == K_RIGHT or event_key == K_d:
            self.board.move_piece(dx=1, dy=0)
        elif event_key == K_UP or event_key == K_w:
            self.board.rotate_piece()
        elif event_key == K_SPACE:
            self.board.full_drop_piece(self.mode)
        elif event_key == K_q: #스킬 부분
            self.board.ultimate()
        elif event_key == K_m: # 소리 설정
            self.music_on_off = not self.music_on_off
            if self.music_on_off:
                pygame.mixer.music.play(-1, 0.0)
            else:
                pygame.mixer.music.stop()

    #가장 높은 점수 불러 오는 부분
    def HighScore(self):
        try:
            f = open('assets/save.txt', 'r')
            l = f.read()
            f.close()
            if int(l) < self.board.score:
                h_s = self.board.score
                f = open('assets/save.txt', 'w')
                f.write(str(self.board.score))
                f.close()
            else:
                h_s = l
            self.board.HS(str(h_s))
        except:
            f = open('assets/save.txt', 'w')
            f.write(str(self.board.score))
            f.close()
            self.board.HS(str(self.board.score))

    #실행하기
    def run(self):
        pygame.init()
        icon = pygame.image.load('assets/images/icon.PNG')  # png -> PNG로 수정
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tetris')

        self.board.level_speed() #추가 - level1에서 속도

        #start_sound = pygame.mixer.Sound('assets/sounds/Start.wav')
        #start_sound.play()
        #bgm = pygame.mixer.music.load('assets/sounds/bensound-ukulele.mp3')  # (기존 파일은 소리가 안남) 다른 mp3 파일은 소리 난다. 게임진행 bgm변경

        delay = 150
        interval = 100
        pygame.key.set_repeat(delay, interval)


        while True:

            if self.check_reset:
                self.check_reset = False
                #pygame.mixer.music.play(-1, 0.0)  ## 수정 필요 오류 나서 일단 빼둠

            if self.board.game_over():
                pygame.quit()
                break

            for event in pygame.event.get(): #게임진행중 - event는 키보드 누를떄 특정 동작 수할떄 발생
                if event.type == QUIT: #종류 이벤트가 발생한 경우
                    pygame.quit() #모든 호출 종
                    sys.exit() #게임을 종료한다ㅏ.
                elif event.type == KEYUP and event.key == K_p: # 일시 정지 버튼 누르면
                    self.screen.fill(BLACK)         #일시 정지 화면
                    #pygame.mixer.music.stop()       #일시 정지 노래 중둠    오류나서 일단 뺴
                    self.board.pause()
                    #pygame.mixer.music.play(-1, 0.0)
                elif event.type == KEYDOWN: #키보드를 누르면
                    self.handle_key(event.key, self.mode) #handle 메소드 실행
                elif event.type == pygame.USEREVENT:
                    self.board.drop_piece(self.mode)

                #화면 크기 조절해 보기
                elif event.type == VIDEORESIZE:
                    videoresize = event.w/self.display_width
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


            # self.screen.fill(BLACK)
            self.board.draw(self, self.mode)
            pygame.display.update() #이게 나오면 구현 시
            self.clock.tick(30) # 초당 프레임 관련
