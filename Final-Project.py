"""
Final-Project.py
Author: Payton
Credit: <add your sources here>
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class AlienShooterGame(App):
    def space(self, event):

    def __init__(self, width, height):
        
        super().__init__(width, height)
        bg_asset = ImageAsset("images/sky-lights-space-dark.jpg")
        txt_asset = TextAsset("Control Dwon 3: Tokyo Drift Mode", width = 300, align ='center', style='40px Times', fill=Color(0xff2222,1)) 
        bg = Sprite(bg_asset, (0,0))
        bg = Sprite(bg_asset, (0,512))
        bg = Sprite(bg_asset, (512,0))
        bg = Sprite(bg_asset, (512,512))
        txt=Sprite(txt_asset, (0,0))
        sun_asset = ImageAsset("images/sun.png")
        sun = Sun ((400,300))
        left_location = 1
        SpaceShip((300,350))
        SpaceShip2((600,350))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(SpaceShip2):
            ship.step()
        explosions = self.getSpritesbyClass(ExplosionSmall)
        for explosion in explosions:
            explosion.step()

myapp = ControlDwon(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()