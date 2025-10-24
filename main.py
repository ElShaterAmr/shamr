class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    Coin = SpriteKind.create()
    Flower = SpriteKind.create()
    Fireball = SpriteKind.create()
    dimonad = SpriteKind.create()
    projectile1 = SpriteKind.create()
    projectile2 = SpriteKind.create()
    iron = SpriteKind.create()
    gold = SpriteKind.create()
    mob = SpriteKind.create()

def on_overlap_tile(sprite5, location4):
    global current_level
    current_level += 1
    startLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile2
    """),
    on_overlap_tile)

def on_up_pressed():
    if Hops_and_Paw.vy == 0:
        Hops_and_Paw.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(2)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap)

def on_b_pressed():
    global projectilel2
    projectilel2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . f 6 f . . . . . . 
                    . . . . . . . . f 6 f . . . . . 
                    . . . . . . . . f 6 f 6 . . . . 
                    . . . . . . . . . . f 6 f . . . 
                    . . . . . . . . . f f 6 . f . . 
                    . . . . . . . . . . f 6 f . . . 
                    . . . . . . . . . . . f 6 f . . 
                    . . . . . . . . . . . f 6 . f . 
                    . . . . . . . . . . . f f f . . 
                    . . . . . . . . . . . f 6 f . . 
                    . . . . . . . . . . . f 6 f . . 
                    . . . . . . . . . . f 6 f . . . 
                    . . . . . . . . . f 6 . . f . . 
                    . . . . . . . . . f f f f . . . 
                    . . . . . . . . f 6 . f . . . . 
                    . . . . . . . . . f f . . . . .
        """),
        Hops_and_Paw,
        100,
        0)
    music.play(music.create_sound_effect(WaveShape.TRIANGLE,
            1375,
            5000,
            255,
            0,
            105,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
    pause(1000)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite8, otherSprite3):
    info.change_life_by(-2)
sprites.on_overlap(SpriteKind.player, SpriteKind.Fireball, on_on_overlap2)

def on_a_pressed():
    global projectile12
    projectile12 = sprites.create_projectile_from_sprite(img("""
            . . . . . f f . . . . . . . . . 
                    . . . . f . 6 f . . . . . . . . 
                    . . . f f 6 f . . . . . . . . . 
                    . . f . . 6 f . . . . . . . . . 
                    . . . f 6 f . . . . . . . . . . 
                    . . f 6 f . . . . . . . . . . . 
                    . . f 6 f . . . . . . . . . . . 
                    . . f f f . . . . . . . . . . . 
                    . f . 6 f . . . . . . . . . . . 
                    . . f 6 f . . . . . . . . . . . 
                    . . . f 6 f . . . . . . . . . . 
                    . . f . 6 6 f . . . . . . . . . 
                    . . . f f f . . . . . . . . . . 
                    . . . . 6 f 6 f . . . . . . . . 
                    . . . . . f 6 f . . . . . . . . 
                    . . . . . . f 6 f . . . . . . .
        """),
        Hops_and_Paw,
        -100,
        0)
    music.play(music.create_sound_effect(WaveShape.TRIANGLE,
            1330,
            5000,
            255,
            0,
            105,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
    pause(1000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite82, otherSprite32):
    info.change_life_by(-2)
sprites.on_overlap(SpriteKind.player, SpriteKind.mob, on_on_overlap3)

def on_on_overlap4(sprite2, otherSprite2):
    info.change_score_by(4)
    sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.iron, on_on_overlap4)

def on_on_overlap5(sprite10, otherSprite42):
    otherSprite42.destroy()
    if Hops_and_Paw.y < otherSprite42.y:
        info.change_score_by(3)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap5)

def on_on_overlap6(sprite3, otherSprite4):
    info.change_score_by(6)
    sprites.destroy(otherSprite4)
sprites.on_overlap(SpriteKind.player, SpriteKind.dimonad, on_on_overlap6)

def on_overlap_tile2(sprite32, location2):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile7
    """),
    on_overlap_tile2)

def on_on_overlap7(sprite7, otherSprite22):
    global bee
    otherSprite22.destroy()
    bee = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bee,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 1 1 1 f 1 1 1 f . . . . 
                        . . . f 1 1 1 f 1 1 1 f . . . . 
                        . . . . . 1 1 1 1 1 . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . f f 5 5 f 5 5 f f . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . f f 5 5 f 5 5 f f . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . .
            """)],
        100,
        True)
    bee.set_position(Hops_and_Paw.x + 80, Hops_and_Paw.y - 80)
    bee.follow(Hops_and_Paw, 50)
sprites.on_overlap(SpriteKind.player, SpriteKind.Flower, on_on_overlap7)

def on_on_overlap8(sprite4, otherSprite5):
    info.change_score_by(2)
    sprites.destroy(otherSprite5)
sprites.on_overlap(SpriteKind.player, SpriteKind.gold, on_on_overlap8)

def on_overlap_tile3(sprite42, location3):
    game.over(False, effects.melt)
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile3)

def startLevel():
    global flower, fireball, mob2
    if current_level == 0:
        tiles.set_current_tilemap(tilemap("""
            level3
        """))
    elif current_level == 1:
        pass
    elif current_level == 2:
        pass
    elif current_level == 3:
        pass
    else:
        game.over(True)
    tiles.place_on_random_tile(Hops_and_Paw, assets.tile("""
        tile6
    """))
    for value in tiles.get_tiles_by_type(assets.tile("""
        tile6
    """)):
        tiles.set_tile_at(value, assets.tile("""
            tile0
        """))
    scene.camera_follow_sprite(Hops_and_Paw)
    info.set_life(10)
    for value2 in sprites.all_of_kind(SpriteKind.enemy):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.Coin):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Flower):
        value4.destroy()
    for value5 in sprites.all_of_kind(SpriteKind.dimonad):
        sprites.destroy(value5)
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        myTile
    """)):
        flower = sprites.create(img("""
                d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d 9 d d d 
                            d d d 9 d d d d d d 9 9 9 d d d 
                            d d 9 9 9 9 9 d d d 9 d d d d d 
                            d d d d d 9 d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d 9 d d d d d d d 9 d d d 
                            d d d 9 9 9 9 9 d d d 9 9 9 9 d 
                            d d d d d d 9 d d d d d d 9 d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d
            """),
            SpriteKind.dimonad)
        animation.run_image_animation(flower,
            [img("""
                    d d d d d d d d d d d d d d d d 
                                d d d d d d d 9 d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 9 d d d d d d d d d 9 d d 
                                d d 9 9 9 9 d d d d d 9 9 9 9 d 
                                d d d d 9 d d d d d d d 9 d d d 
                                d d d d d d d d 9 d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 9 d d d d d d d d d d 9 d d 
                                d d 9 9 9 9 d d d d 9 9 9 9 d d 
                                d d d 9 d d d d d d d 9 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 9 d d d d d d d d d d d d 
                                d d d d d d d d d d d 9 d 9 d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    d d d d d d d d d d d d d d d d 
                                d d d d d d d 9 d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 9 d d d d d d d d d 9 d d 
                                d d 9 9 9 9 d d d d d 9 9 9 9 d 
                                d d d d 9 d d d d d d d 9 d d d 
                                d d d d d d d d 9 d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 9 d d d d d d d d d d 9 d d 
                                d d 9 9 9 9 d d d d 9 9 9 9 d d 
                                d d d 9 d d d d d d d 9 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 9 d d d d d d d d d d d d 
                                d d d d d d d d d d d 9 d 9 d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    6 6 9 6 6 6 6 6 6 6 6 6 6 6 9 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 6 6 9 6 6 
                                6 6 9 9 9 9 6 6 9 6 6 9 9 9 9 6 
                                6 6 6 6 9 6 6 6 6 6 6 6 9 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 9 6 6 6 6 6 6 6 6 6 6 9 6 6 
                                6 6 9 9 9 9 6 6 6 6 9 9 9 9 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 9 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """),
                img("""
                    6 6 9 6 6 6 6 6 6 6 6 6 6 6 9 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 6 6 9 6 6 
                                6 6 9 9 9 9 6 6 9 6 6 9 9 9 9 6 
                                6 6 6 6 9 6 6 6 6 6 6 6 9 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 9 6 6 6 6 6 6 6 6 6 6 9 6 6 
                                6 6 9 9 9 9 6 6 6 6 9 9 9 9 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 9 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 9 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 9 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """)],
            100,
            True)
        tiles.place_on_tile(flower, value6)
        tiles.set_tile_at(value6, assets.tile("""
            tile0
        """))
    for value62 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        flower = sprites.create(img("""
                d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d 1 d d d d d d 1 d d d d d 
                            d 1 1 1 1 d d d d 1 1 1 1 d d d 
                            d d 1 d d d d d d d d 1 d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d 1 d d d d 
                            d d d 1 d d d d d d 1 1 1 d d d 
                            d 1 1 1 1 d d d d d 1 d d d d d 
                            d d 1 d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d
            """),
            SpriteKind.iron)
        animation.run_image_animation(flower,
            [img("""
                    d d 1 d d d d d d d d d d d 1 d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 1 d d d d d d d d d 1 d d 
                                d d 1 1 1 1 d d 1 d d 1 1 1 1 d 
                                d d d d 1 d d d d d d d 1 d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 1 d d d d d d d d d d 1 d d 
                                d d 1 1 1 1 d d d d 1 1 1 1 d d 
                                d d d 1 d d d d d d d 1 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 1 d d d d d d d d d d d d 
                                d d d d d d d d d d d 1 d d d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    d d 1 d d d d d d d d d d d 1 d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 1 d d d d d d d d d 1 d d 
                                d d 1 1 1 1 d d 1 d d 1 1 1 1 d 
                                d d d d 1 d d d d d d d 1 d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 1 d d d d d d d d d d 1 d d 
                                d d 1 1 1 1 d d d d 1 1 1 1 d d 
                                d d d 1 d d d d d d d 1 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 1 d d d d d d d d d d d d 
                                d d d d d d d d d d d 1 d d d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    6 6 1 6 6 6 6 6 6 6 6 6 6 6 1 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 6 6 1 6 6 
                                6 6 1 1 1 1 6 6 1 6 6 1 1 1 1 6 
                                6 6 6 6 1 6 6 6 6 6 6 6 1 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 1 6 6 6 6 6 6 6 6 6 6 1 6 6 
                                6 6 1 1 1 1 6 6 6 6 1 1 1 1 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 1 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 1 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """),
                img("""
                    6 6 1 6 6 6 6 6 6 6 6 6 6 6 1 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 6 6 1 6 6 
                                6 6 1 1 1 1 6 6 1 6 6 1 1 1 1 6 
                                6 6 6 6 1 6 6 6 6 6 6 6 1 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 1 6 6 6 6 6 6 6 6 6 6 1 6 6 
                                6 6 1 1 1 1 6 6 6 6 1 1 1 1 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 1 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 1 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 1 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """)],
            100,
            True)
        tiles.place_on_tile(flower, value62)
        tiles.set_tile_at(value62, assets.tile("""
            tile0
        """))
    for value63 in tiles.get_tiles_by_type(assets.tile("""
        myTile19
    """)):
        flower = sprites.create(img("""
                d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d 5 d d d d d d d d 5 d d d 
                            d 5 5 5 5 5 d d d d d 5 5 5 5 d 
                            d d 5 d d d d d d d d d d 5 d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d 5 d d d d d d d d 5 d d d d 
                            d 5 5 5 5 d d d d d 5 5 5 5 d d 
                            d d d 5 d d d d d d d 5 d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d 
                            d d d d d d d d d d d d d d d d
            """),
            SpriteKind.gold)
        animation.run_image_animation(flower,
            [img("""
                    d d 5 d d d d d d d d d d d 5 d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 5 d d d d d d d d d 5 d d 
                                d d 5 5 5 5 d d 5 d d 5 5 5 5 d 
                                d d d d 5 d d d d d d d 5 d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 5 d d d d d d d d d d 5 d d 
                                d d 5 5 5 5 d d d d 5 5 5 5 d d 
                                d d d 5 d d d d d d d 5 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 5 5 d d d d d d d d d d d 
                                d d d d d d d d d d d 5 d d d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    d d 5 d d d d d d d d d d d 5 d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 5 d d d d d d d d d 5 d d 
                                d d 5 5 5 5 d d 5 d d 5 5 5 5 d 
                                d d d d 5 d d d d d d d 5 d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d 5 d d d d d d d d d d 5 d d 
                                d d 5 5 5 5 d d d d 5 5 5 5 d d 
                                d d d 5 d d d d d d d 5 d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d d d d d d d d d d d d d d 
                                d d d 5 5 d d d d d d d d d d d 
                                d d d d d d d d d d d 5 d d d d 
                                d d d d d d d d d d d d d d d d
                """),
                img("""
                    6 6 5 6 6 6 6 6 6 6 6 6 6 6 5 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 6 6 5 6 6 
                                6 6 5 5 5 5 6 6 5 6 6 5 5 5 5 6 
                                6 6 6 6 5 6 6 6 6 6 6 6 5 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 5 6 6 6 6 6 6 6 6 6 6 5 6 6 
                                6 6 5 5 5 5 6 6 6 6 5 5 5 5 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 5 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 5 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """),
                img("""
                    6 6 5 6 6 6 6 6 6 6 6 6 6 6 5 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 6 6 5 6 6 
                                6 6 5 5 5 5 6 6 5 6 6 5 5 5 5 6 
                                6 6 6 6 5 6 6 6 6 6 6 6 5 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 5 6 6 6 6 6 6 6 6 6 6 5 6 6 
                                6 6 5 5 5 5 6 6 6 6 5 5 5 5 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 5 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 5 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 5 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                """)],
            100,
            True)
        tiles.place_on_tile(flower, value63)
        tiles.set_tile_at(value63, assets.tile("""
            tile0
        """))
    for value52 in tiles.get_tiles_by_type(assets.tile("""
        tile4
    """)):
        flower = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . e e . . . . . . . . . . 
                            . . . e d f e . . . . . . . . . 
                            . . . e d d d e . . . . . . . . 
                            . . . . e d d d e . . . . . . . 
                            . . . . . e d d d e e . . . . . 
                            . . . . . . e d d e e . . . . . 
                            . . . . . . . e e . . . . . . . 
                            . . . . . . . e e . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Coin)
        animation.run_image_animation(flower,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . e e . . . . . . . . . . 
                                . . . e d f e . . . . . . . . . 
                                . . . e d d d e . . . . . . . . 
                                . . . . e d d d e e . . . . . . 
                                . . . . . e d d e e . . . . . . 
                                . . . . . . e e . . . . . . . . 
                                . . . . . . e e . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . e e . . . . . . 
                                . . . . . . . e f d e . . . . . 
                                . . . . . . e d d d e . . . . . 
                                . . . . e e d d d e . . . . . . 
                                . . . . e e d d e . . . . . . . 
                                . . . . . . e e . . . . . . . . 
                                . . . . . . e e . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . e . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            500,
            True)
        tiles.place_on_tile(flower, value52)
        tiles.set_tile_at(value52, assets.tile("""
            tile0
        """))
        for value622 in tiles.get_tiles_by_type(assets.tile("""
            tile5
        """)):
            flower = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . 3 a . . a 3 . . . . . . 
                                    . . . . a 3 2 2 3 a . . . . . . 
                                    . . 7 7 . a 3 3 a . . . . . . . 
                                    . . 7 7 7 . c c . 7 7 . . . . . 
                                    . . . 8 7 7 7 . 7 7 7 . . . . . 
                                    . . . 8 8 7 7 7 7 8 . . . . . . 
                                    . . . . . 8 7 7 8 . . . . . . . 
                                    . . . . . . 7 8 . . . . . . . .
                """),
                SpriteKind.Flower)
            tiles.place_on_tile(flower, value622)
            tiles.set_tile_at(value622, assets.tile("""
                tile0
            """))
        for value7 in tiles.get_tiles_by_type(assets.tile("""
            myTile13
        """)):
            fireball = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 5 . . . . . . . . 
                                    . . . . 5 5 4 5 5 4 5 5 . . . . 
                                    . . . . . 4 4 4 4 2 4 . . . . . 
                                    . . . 5 4 4 2 2 2 2 4 5 . . . . 
                                    . . . 5 4 . 2 4 2 4 4 2 . . . . 
                                    . . . 5 5 . 2 4 4 2 4 4 . . . . 
                                    . . . 2 5 2 2 4 2 4 4 5 . . . . 
                                    . . . . 5 4 2 2 2 4 5 . . . . . 
                                    . . . . . . 4 . 4 4 4 . . . . . 
                                    . . . 5 . 5 5 5 4 5 5 . . . . . 
                                    . . . . . . . 2 5 5 . . . . . . 
                                    . . . . . . . . . . . . . 5 . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.Fireball)
            tiles.place_on_tile(fireball, value7)
            tiles.set_tile_at(value7, assets.tile("""
                tile0
            """))
            animation.run_movement_animation(fireball, "c 0 -100 0 100 0 0", 2000, True)
            fireball.start_effect(effects.fire)
        for value72 in tiles.get_tiles_by_type(assets.tile("""
            myTile25
        """)):
            mob2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 6 . . . . . . . . 
                                    . . . . 6 6 9 6 6 9 6 6 . . . . 
                                    . . . . . 9 9 9 9 2 9 . . . . . 
                                    . . . 6 9 9 2 2 2 2 9 6 . . . . 
                                    . . . 6 9 . b 9 b 9 9 6 . . . . 
                                    . . . 6 6 . 2 9 9 2 9 9 . . . . 
                                    . . . 6 6 2 2 b 2 9 9 6 . . . . 
                                    . . . . 6 9 2 2 2 9 6 . . . . . 
                                    . . . . . . 9 . 9 9 9 . . . . . 
                                    . . . 6 . 6 6 6 9 6 6 . . . . . 
                                    . . . . . . . 6 6 6 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.mob)
            tiles.place_on_tile(mob2, value72)
            tiles.set_tile_at(value72, assets.tile("""
                tile0
            """))
            animation.run_movement_animation(mob2,
                animation.animation_presets(animation.ease_left),
                2000,
                True)
            fireball.start_effect(effects.fire)

def on_overlap_tile4(sprite9, location6):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile11
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite6, location5):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile28
    """),
    on_overlap_tile5)

mob2: Sprite = None
fireball: Sprite = None
flower: Sprite = None
bee: Sprite = None
projectile12: Sprite = None
projectilel2: Sprite = None
Hops_and_Paw: Sprite = None
current_level = 0
scene.set_background_color(9)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666699969999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999999999999969999999999999999999999999966999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999999999999999999999996666669
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999969999999999999999999999996669
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999
        9999999999999999999999999999999999999999dd9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999dcb999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999699999
        999999999999999999999999999999999999999ddcb999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999669999
        999999999999999999999999999999999999999dbcbb99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999969999999999996999699996
        999999999999999999999999666999999999999dcccc99999999999699999999999999999999999999999999969999999999999999999999999999999999999999999999999999999999999999996999
        99999999999999999999999996699999999999dbccccb9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999699999
        99999999999999999999999996699699999999dbbccbb9999999699999999999999999999999999999999999999999999999999999999999999999969999999999999999969999999999999969999966
        9999999999999999966999996699999999999ddcbcccbb999996999999999999999996999999999999999999999999999999999999999999999999999999699999999999999999999999699999999969
        9999999999999999969999999999999999999dbcccccbb999999999999999999999999999699969999999999999999999999999999999999999999999999999999999999999999999669699969999966
        699969999999999999999999999999666699cdccbcbcccc699999ddddd9969999dbbb9999999699999999999969999999999999999999999999999999999999999999999999696999999969999999996
        999999999999999999999999999999666696dcbbbcbbbccb99999dbbdb99dd999ddbb9999999999999999999999996999999999999999999999999999969669999999999999999699999969999999999
        696999999999999999969999999699999996dccccccccccb99969dcccb9ddcc9ddccb6696999999699999999969999999996999999999999999999999666669999999999999999966669696999699999
        69999699999999999999999999999999669dccccbbbbccccb6966dbcbb9dccc9dbcbb6699999999999999999999999999999999999999999966669966699669999999699999696969996669666669996
        6999999999999999999969969999999966bdbbbbbbbbbbbbbb966dbccb9dbbb6dbbcc6699999999966999999999999999999996999999669966699669996969999999999996666999996699966666666
        9999999999999999999999999999999999dbbcccccccccbbbb666dcccbbdccbbccccc6669669669966999966669999999699996999999999966996969996969996999996666666669666666666666666
        9999999999999999999699999999999999bcccccccccccccbb6666bcbbcccbbccbcbb6666669999666666996969996669999699999999999999999996999699969966699999999666666666666666666
        999999996699999699999669999999999999cccccccccccc666666bccbcccccccccbb66966666996666669669969966969996999999999999999999999996999669ff6999996996666666666666666ff
        999999999969999669966699999999999999ccbbbbbbcccc666666cccbbbbbbcccccc66966999996996669999999999999966996969999999966669999996696999f969966666666666666666666ffff
        999999999999669996966996699999999999bbcbbccbbbbb6666666bbbcbbbccbbbb66666666996669966666999669999966699666999999966966999699669966ff96666669666666666666666fffff
        999996699696669996999999969999999999bbcbbbbbbbbb66666666bccccccccbb666666666666966966966666669666966696699666999669669666996666666f6666666666666666666666fffffff
        666996666666699966999999999699999999bbbbcccbbbbb66666666dccccccccc6666666666666666666666666666666666666666666666669666666666666666f666666666666666666666ffffffff
        666666666666999666696699999966999999bccccccccccb66666666dccbbbbbcc6666666666666666666666666666666666696666666666666666666666666666f66666666666666666666fffffffff
        6666666666666666666669699969999999999cccccccccc966666666dcbbbccbbc6666666666666666666666666666666666666666666666666666666666666666f666666ff66666666666ffffffffff
        66666666666666666666b9699999969999b696bcccccccb6f6666666ccbbbbcccc666666666666ff6666666666666666666666666666666666666666666666ff66ff66666ff666666666ffffffffffff
        666666666666666666dddbbb9dddd699ddb9bb9ccbbbbbfbbddddb666bbccbbbbcbb66666666666f66666666666666666666666666666666666666666666666ff66f666666f66666666fffffffffffff
        666666666666666666dbbbbfdbbdbbbbbbbb64bccbbbbccdddbbbbbbbcbbbbbbbcc66bbbbbb6666f69666666666666666666666666666666666666666666666fff6ff66666f6f6666fffffffffffffff
        b6666666b6b6b66666dbbbbfbbbbbbb6bbbb64bbbbbbbccbbcbbcbbcccbbbccbbccbb6b44466666f66666666666666666666666666666f6666666666666666666f66ff6666fff66fffffffffffffffff
        b6666666b6b6bb66b6dccccbfcccccbbcccb444bbcbccbcbbbbbcbbbccbbbccbbc4bb66bbb444b6666666666666666666666666666666ff6666666666666666666f66f6666ff66ffffffffffffffffff
        bb6b66bb64bb64bb66dbbbbbbbbbbbbbbcbb444bccbbbccbbcccbbbbccbbbbbbbc44464444bb4b6f66bf6666666666666666666666666ff6666666666666666666ffff6666f66fffffffffffffffffff
        444466bb44464446b6bccbbbbcbcccbbccbc444bbbbbbcccccccccbbbcbbbbcccc444444bb44bbbfbb6f6666666666666666666666666f666f66666666666666666fff666bffffffffffffffffffffff
        44b6b4b4b4b6b4444b4bcccccccccccccccc44bcbbbbbcccc4b4cccbbbbcbbcccc4444446644444fbb6f6bbb666666666666666666666f66ff66666666666666666fff6bbfffffffffffffffffffffff
        444444b4444444444464cbbbbbbcbbbbbbcb444ccbbbbccc44f44ecbbcbbbbbbcc444444b444464f44ffbbbbbb666666666ffff666666f66f6666b666666666666bbff646fffffffffffffffffffffff
        4444446444444444446bccbccbbccbbbccc4ff4ccbccbcc444ff44ccbcbbbbbbcc4444444444446f44ff46bbbb66666666bfbbfff6666f6f6666666666666666b664ff44ffffffffffffffffffffffff
        4444b66b4444446664644ccbbbbbbbbccc4ff46ccbbbbcc444444bdbbccbbcbbccff44464444444f44f44466bb4b66b66b6fb4bff6bbbff66666666666666666b444ff4fffffffffffffffffffffffff
        4444466b44444466644444cccccccccccddddbbccbbbbcc44444dfdbbccbbcbbccffff464464644f44f4b4bbbbbbb666b4ff444fff44ff66bb6666666ff66b6bb4bfffffffffffffffffffffffffffff
        4444446644444444464464cccccccccccddbbbbccbbbbcc44bb4dfdbbccbbbbbcc44f4664444644fff4444b4b6666666bff646b4ff4ff6b44bb666666f666b44b64fffffffffffffffffffffffffffff
        4444444444444f44444466ddbbbbbbbbcbbccccccbbbbbcd44ddffdbbccbbbbbcc44444dd44db44fff444444bb6b66664ff44444fffffddbbb444b6b6fb6bbdbdb3ffffffffffffffffffffffffffffc
        4444464444444f444d4444dbbbccbbbbcbcccccccccbbccd3ddd4ffbbccccccbccddddd4dd3443fff34444bb6bd4d966444444ddffff463d4bd4dd6dff6666dfb4ffffffffffffffffffffffffffffcc
        4444464444444ff44ff4b4dccbccbbcccbcc44ccbbbbbbccdccccccccccbcbbbccddddd4ddd4ddfffbdddd4dd3ddbddddbd446ddffff444d44bdddddff4669dfddffffffffffffffffffffffffffffcc
        4444446444444ffddfd344dbcbbbbbcbbbcc4cccbbccbbcbbcccccccccbbbcbcccdd434ddddffdffdddddfddddd3dddddbddddddffff46d444d4ddddffd9dddfdfffffffffffffffffffffffffffffcc
        44444444444444f3bf44ffdbbbbbcbbbbbbccbbbcbccbbcbbbbcbbbcbbccccccccdddddddddfffffdddddffdddddddddddd444ddffffddddb4ddddddffd66ddfdffffffffffffffffffffffffffffccc
        44444444ddd444ff4f33ffcbbbbbccbbccbccbbbcbbbbbcbbcccbccccbccbbbbccdddd44ddd4fffdd4dddffd4dddddddddddddddffffddd44b4dddddffdddddffffffffffffffffffffffffffffffccc
        44444444dddddddfdf44f4bbccbbbbbbccbbbbbbbbbbbbbbbbccbbbcbbbbbbcbccd4ddddddddfffd4dddddffddddddddddddd6bdfffffdd44444dd4ddfdddddffffffffffffffffffffffffffffffccc
        44444444ddddddd4ff4ff4bbbbbbbcccbbbbbbbbccbbcccbbbbbbbbbcccbbccbccdd4dddddddfffddddddddfddd4ddddddddddddfffffdd44b4ddddddffdddffffffffffffffffffffffffffffffcccc
        6444444ddd3dd44dff6ff4bbbcbbcccccbbcccbbccbbccbbbcccbbbcccccbccbccddfdddddddfffdddd4dddffdffddddddddddddfffffddddddddddddffddfffffffffffffffffffffffffffffffcccc
        4344ddddddddd4ddff4fddcbbcbbccbccbbbcbbbbbbbbbbbbcccbccccbccbbbbccdfffddddddfffddddddddffdfdddddddffddddfffffdddddddddddffffffffffffffffffffffffffffffffffffcccc
        4444ddddb4ddddddfddfd4ccbcbbcccccbbbbbbbbbbbcccbbbbbbcccccccbccbccdffdddddddffffddddddddfffddddd4dffddddfffffddddddddfdfffffffffffffffffffffffffffffffffffffcccc
        4444deedebd4434efffdd4ccbbbbcccccbbbcccccbccccccbbbbbbbcccccbbbcccdffdddddddffffddddddddfffdddddddfdddddfffffddddfdddfdffffffffffffffffffffffffffffffffffffccccc
        4444befeebe4d4beff4444ccbcbbcccccbbccbbbbcccbcbccbbbbbbcccccbbccccddfffdddddffffdddddddddffddddddffdddddfffffdddffdddffffffffffffffffffffffffffffffffffffffccccc
        444eeeefeeeed4e4ff4444ccccbbcccccbbbbbbbccbcbcbcccbccbbcccccbcbbcc44dffdddddffffdddd44dddffddddddffdddddfffffdddffdddfffffffffffffffffffffffffffffffffffffdccccc
        fffeeffffeeeeeffffeffeccbbbbcccccbbbccbcccbcbcbccccccbbcccccbccbccdddffddddfffffddddd4dddfffdddddffdddddfffffdddffdfffffffffffffffffffffffffffffffffffffffdccccf
        effeffedeeffffffffffffccbccbcccccbbbbbbcccbcbcbcbccbcbbbccccbccbccdddffddd4fffffdddddddddfffdddbdffd4dddffffffddffffffffffffffffffffffffffffffffffffffffffdccccc
        beffffedffffffffffffffccbccbbbbbbcccbbccbcbcbcbcbccbbbcbbbbbbbbbbcdddfdddddffffffdddddddbfffdddbcffddddfffffffdfffffffffffffffffffffffffffffffffffffffffffcccccc
        dfffffffffffffffffffffccbbbbbbbbbccbbbccbcbcbcbcbccbbbccccbbbbbbccdddffdddffffffffdddd4dbffffddddffdddffffffffffffffffffffffffffffffffffffffffffffffffffffcccccc
        ffffffffffffffffffffffccbbbbbccbbbbbbbccbcbcbcbcbccbbbbbccbbcbbcccffdffdffffffffffffddccdffffdbddffd4fffffffffffffffffffffffffffffffffffffffffffffffffffffbbfccc
        efffffffffffffffffffffccbcbbcccbbbbbbcccbcbcbcbcbcccbbbbbbbbccbcccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdbbbbbbbc
        ffffffffffffffffffffffccbccbccbbbbbcbcccbcbcbcbcbcccbbbbbcccbccbbccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcbcbbbbbbb
        ffffffffffffffffffffffccccbbbbbbbbccccccbcbcbcbcbcccbccbbbccbbcbbcccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcddbbcccbbbccc
        ffffffffffffffffffffffccccbbbbbcbbcbbcccbcbcbcbcbcccbbbbbbbbbbbbbcccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccbcbbbbccccbbccc
        fffffffffffffffffffffcccccbbbbbcccbbbcccbcbcbcbcbcccbbbbcccbbbbccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbccccbbbbccccbcccc
        ffffffffffffffffffffffccccbbccbbccbbbcccbcbcbcbcbcccbccbcccbbcccbcccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccbbcccbbbbbcccbbccc
        fffffffffffffffffffffbccbbccbbbbbbbbbcccbcbcbcbcbccccccbbbbbbbbbbcccbcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccfccbbbbbccccbbccbbbcc
        fffffffffffffffffffffbcbbbcbbbbbbbbbbcccbcbcbcbcbcccbcbbbbbbbbbbbccccccbccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccbbcccccbbbbbbccbbccbbccc
        ffffffffffffffffffffccbbbbbccbcbbbccbcccbcbcbcbcbccccccbbbcccbbbbcccccbbbcfcbcccffffffffffffffffffffffffffffffffffffffffffffffffffffffcdbbcccccbbbbbbcccccbbbccc
        fffffffffcfffffffffccccccbbccbccbcccbcccbcbcbcbcbcccbcbbbcccbbbbbcccccccbbcccccbcfffcccffffffffffffffffffffffffffffffffffffffffffffffcdcbbbcccbbbbbbbbcccbbbbbcc
        ddcccffffffffffffcccccbcccbbcbbbbbbbbcccbcbcbcbcbcccbbbbbbbbbbbbbcccccccbbcccccccccccbbcfcffffffffffffffffffffffffffffffffffffffffffcdbbbbbcccbbbbbbccbccccbbbbc
        bdddfcbffffffffcccccccbbbcccbbbbbbccbcccbcbcbcbcbcccbbbbbbbbbbbccccccccccbcbbcccccccbbbfcbfcffffffffffffffffffffffffffffffffffffffffcdbbbcccccbbbbbbcbcccccbbbbc
        bbbddbbcffffccccccccccbbcbbcccbbbccbbcccbcbcbcbcbcccbbcbbbbbbbbccccccccccccccccccccccccccbbbbcffffffffffffffffffffffffffffffffffffffcbbbcbccccbbbbbccbccccccbbbc
        bbbbdbbbbcccccccbccbcccccbbbbbbbbcbcccccbcbcbcbcbcccbbcbbbbbbccccccccccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffcbccbccccbbbbccbbcccbbccccc
        bbbbccccccccccbbbccccccccccccccccccccbbbbbbbbbbbbcccbbcbbbcccccccccbcccccccccccccccccccccccbbcbccbccccfffffffffffffffffffffffffffccffbbcbbcccccbbbccbccccbbbccbc
        bbbbbbbbccccccbbcccccbcccccccccccccbbcccccccccccbccccbbcbbccccccccccccccbcbcccccccccccccbbbbbbbccccbbbbbfccccccffffffffffffffffcfccccbbbbbbbcccbbccbbccbbbbbbccc
        bbbccccccbcccccccccbbbbbcccccccccccbbccccccccccccccccccccccccccccccccccccbcccccccccccccbccbbbbbbbccccbcbbbbbbbcccccffffffffcfcccfccccccbcccccccbccbbbbcbbbbbcccb
        bbccccccbbbbbcccccbbccbbbcccccccbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbcccccbccbbbbbbbdbbbcfcccffcbbbbbbccccccbbcccccbbbbbbbccbbbbcccbb
        ccbddddbbbbbbbcccccbcccccccbccbcbcccccccccccccccbcccccccccbbcccccccccbccccccccccccccccccccbbbccccccbbbcccccccbdbbbbcccccccbbbbbbbbbcccbbbbbbbbbbbbbbccbbbbbbbbbb
        ddbbbbccbbbbbbbbbbcccbbcccccccccbcccccccccccccccbcccccccccbccccccccccccccccccccccccccccccccccccccbbbbbbbcccccbbbcccccccbccccbbbbbbcccccbbbbbbbbbbbbbbcccbbbbbbbb
        cbbbbbbbbbbbbbbbbbbcccbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbccccccccccccccbbbbbbcccccccccbbbbbbbbccbbbbbbccccccccccbbbbbbbbbbcccccbbbbb
        cbbbccccccccccccbbbbbcbcccccbbccccccccccccbbbbbccccccccccccccccccccccccccccccbbcccbccccccccccccccccbbbbbcccccbbbbbbbbbbbbbbbccccbbbcccccccccccbbbbbbbcccccccbbbb
        bbbbccccccccbbbbbbbbbbbccbbbbbbbbccccccccbbbcccccbcccccccccccccbbccccccccccccccccccccccccccbcccccccbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbcccccbbbbbccccccccbbcc
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccbbbbbbbccccccccccccbbccccccccccccccccccccccbbbbbbbbbccccbbbccbbbbbbbbbccccccbbbbbbbbbbbbbbbbcbbbbbcccbcc
        bbbbbbcccccccbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccbcccccccccbbcccbcccccccccccbccccccbcccccccccccbbbbbbbbbbccccccccbbbbbbbbbbbbcccbbccccccbc
        bbbccbbbccccccccccbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbcccccbccccbbbbbcccccccbbccccccbbbbbbbbccccccccbccccccbbbbbbbbbbbccbbcccbbbbc
        bbbcdddddbbbbcccccccccccccbbbbbccccbbcbccccccccccccbcccccccccccccccccccccbcbbbbbbbcccccccccccccccccbbbbbbcccccbbbbbbbbbbcccccccccccccccccccbbbbbbbbbbbbbbbbbbbbb
        bbbdcbbbbbbbbbbbbbbbbccccbbccccccccccccccccccccccccccccccbbbbbbcccbcccccccccccccbcccccccccccccccccbbbbbbbbcbbbbbbbbcccccccbcccccccccbbccccccccbbbbbbbbbbbbbbbbbb
        bdbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbccccccccbbbbbbccccccbbbbbbbccccbbbbbbbbbbbbbbbbb
        cddbccccbbbbbbbbbbbbbbcccccccccccccbbbbbccccccccccbcccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbccccccbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        cdcccbcccbbbbbbbbbbbbbbcccccccbbbbbbcccccccccccccccbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbcccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        dcbbbbbbbbbbbbbbbbbbccccccbbbbbcccccccccccccccccccccccccccccccccccccbbccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        dbbbbbbbbbbbccccccccccccccbbbbcccccccbbccccccccccbccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbcccbbcbbbbbbbbccccccbbccccbbccccccccccccccccccccccccccccccccccbbcccccbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbcccccccccccccccccccccccccccc
        bbbbbbbccbbbbbbbbbbbbbbbbbbbbcccbbbccccbbbbbbbccccccccccccbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbccccccccccbbbccccccccccccccc
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbccbbbbbbbbbbbbb
        bbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccbbbbbccccbbbbbbbbbbbbbbbbbbccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccc
        ccccccccccccbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbcbbbbbbbbbcccbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccc
        cccccccccccccccccccccbdddddccccccccccbbbbbbbbbccccccccbbbcccccccccbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbccc
        cccccccccbbbbbcccccccccccccccccccccbbbbbbbcccccccbbcccccccccccbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbccccc
        ccccccccccccbbccccccccccccbbbbbbbbbbbbbccccccbbbbbccccccbbbbbbbbbcbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccc
        bcccccccccccccccccccccccbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbcccccccbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbcccccccccc
        bccccccccccccccccbbbbbbbbbbbbbbbbeccccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccbbbbbbcccccccbbcccccccccccccbbbbb
        cccccccccccbbbbbbbbbbbbbbbbbbbbbbeeccbbd4bddbbdbbb3b444ddd444bbb344bbddbbcb44bbb44bb3444b444444b4be44ecccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbb
        bddddcbbbbbbbb444b4bbb44bb4b4bb4444dd44d44ddb4d3bddddddddd444ddddd44ddddddb33dd4444ddd44344444444e4e44ecbceeeccccbcccccccccccccccccccccbbccccccccccccccccbbbbbbb
        ddbbdd44b44b444444b444b444443444dddddddd4ddddddddddddddd4dddddddbdddddddddddddd44d44dddddd44dddddbd4dd3dd34b3bbdddccccccbbccccccccccccbbbbbbbbbbbbbbcccccbbbbbbb
        bbeee4b44444444dd4d33ddddddddde4dddddddddddddddddddddddddddddddd4d4ddd4dddddddddddd44ddddddddddddddddddddddd3dddbbbdbbdddbbbbbbcbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        b4b43dd44db4ddddd4d44dddddddddbd4ddddddddddddddddddddddddd4ddddddd4dddddddddddddddd44ddddddddddddddddddddd4ddddd44dddddddddbdbddddbdbbddddbbbbbbbbbbbbbbbbbccbbb
        dddd3ddddd4ddddd44dddd4dddddddddddddddddddddddddddddddddddd3dddddd4ddddddddddddddddddddddddddddddddddddddddddddddd4dddddddddddddddddd334db4d3dd4bbd44b3ddbbcbbbb
        d4dddbddddddddddd4dddd4ddddddddddddddd3dddddddddd444ddddddd4dddddddddddddddddddddddddddddddd4ddddddddddddddddddddd4ddddddddddddddddddddd3bd4ddd4dddd4444444ddddd
        ddddddddddddddddd4ddddddddddddddddddd4ddddddddddddd4ddddddddddddddddddddddddddddddddddddd4dddddddddddddddddd4ddddddddddd4ddddddddddddddddddd4d44ddddd4dd44dddddd
        4ddddddd4d444dd4dd4ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd4ddddddddddddddddddddddddddddddd4ddddddddddddddddddddddddddddd4ddddddddd
        dddddddddd444ddddd3ddddddddddddd4ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd44dddddddddddddddddddddddddddddddddd4ddddddddd
"""))
current_level = 0
Hops_and_Paw = sprites.create(img("""
        ...........................
            ...........................
            ...........................
            ...........................
            ...........................
            ...........................
            ...........................
            ...............dd..........
            ...............d1dd........
            ...............d811d.......
            .ddddddddddddddd1151d......
            .d11818111111111111e888....
            .ddddddd111111111d6886.....
            .......d881111188d68696....
            .......d88d...d88d68.696...
            .......d11d...d11d....696..
            .......d88d...d88d.....66..
            .......d11d...d11d.........
            ...........................
            ...........................
            ...........................
            ...........................
    """),
    SpriteKind.player)
controller.move_sprite(Hops_and_Paw, 80, 0)
startLevel()

def on_on_update():
    if Hops_and_Paw.vy < 0:
        Hops_and_Paw.set_image(img("""
            .....................
                        ..........dd.........
                        ..........d1dd.......
                        ..........d111d......
                        ..........d8851d.....
                        ..d1d....d1111e888...
                        ..d8d....d111d886....
                        ..d1d...d811d.86f6...
                        ..d1d...d11111816f6..
                        ..d8d..d8111dddd.66..
                        ..d1ddd111111181.....
                        ..d1111111...........
                        .....d111d...........
                        ....d11d8d...........
                        ....d8dd1d...........
                        ....d1d..............
        """))
    elif Hops_and_Paw.vy > 0:
        Hops_and_Paw.set_image(img("""
            .........................
                        .....ddd.................
                        ....dd8d.................
                        ....d1dd.................
                        ....d8d..................
                        ....d1d..................
                        ....d11d.................
                        ...d1111.................
                        ...d8111d................
                        ...d81111d.dd............
                        ...d1d1111dd1dd..........
                        ...d1.d11118111d.........
                        ...d1.1d81811151d........
                        ...d8.8d8181111e888......
                        ...d1.1d1.1d..6886.......
                        .......d1.1d..686f6......
                        .......d8.1d..68.6f6.....
                        .......d1.81d.....66.....
                        .........................
                        .........................
                        .........................
        """))
    elif Hops_and_Paw.x % 2 == 0:
        Hops_and_Paw.set_image(img("""
            ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...............dd..........
                        ...............d1dd........
                        ...............d811d.......
                        .ddddddddddddddd1151d......
                        .d11818111111111111e888....
                        .ddddddd111111111d6886.....
                        .......d881111188d686f6....
                        .......d88d...d88d68.6f6...
                        .......d11d...d11d....66...
                        .......d88d...d88d.........
                        .......d11d...d11d.........
                        ...........................
                        ...........................
                        ...........................
                        ...........................
        """))
    else:
        Hops_and_Paw.set_image(img("""
            ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...........................
                        ...............dd..........
                        ...............d1dd........
                        ...............d811d.......
                        .ddddddddddddddd1151d......
                        .d11818111111111111e888....
                        .ddddddd111111111d6886.....
                        .......d881111188d686f6....
                        .......d88d...d88d68.6f6...
                        .......d11d...d11d....66...
                        .......d88d...d88d.........
                        .......d11d...d11d.........
                        ...........................
                        ...........................
                        ...........................
                        ...........................
        """))
    if (Hops_and_Paw.is_hitting_tile(CollisionDirection.LEFT) or Hops_and_Paw.is_hitting_tile(CollisionDirection.RIGHT)) and Hops_and_Paw.vy >= 0:
        Hops_and_Paw.vy = 0
        Hops_and_Paw.ay = 0
        Hops_and_Paw.set_image(img("""
            ......................
                        ......................
                        ......................
                        ..............66......
                        ...........8.6f6......
                        ...........86f6.......
                        ..........d886........
                        .........d1e888.......
                        ........d151666.......
                        ........d111dddddd....
                        .......d1811188181....
                        .......dddd1188181....
                        ..........d111dddd....
                        ..........d111........
                        ..........d111........
                        ..........d111........
                        ..........d111........
                        ..........d1188181....
                        ..........d1188181....
                        ..........d1dddddd....
                        ..........d8d.........
                        ..........d1d.........
                        ..........d8d.........
                        ..........d1d.........
                        ..........d1d.........
                        ..........ddd.........
                        ......................
        """))
    else:
        Hops_and_Paw.ay = 350
    if Hops_and_Paw.vx < 0 or Hops_and_Paw.is_hitting_tile(CollisionDirection.LEFT):
        Hops_and_Paw.image.flip_x()
        Hops_and_Paw.set_image(Hops_and_Paw.image)
    else:
        pass
game.on_update(on_on_update)
