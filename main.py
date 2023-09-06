def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . 5 f 1 5 . . . . . . .
                    . . . 4 4 5 5 5 5 . . . . . . .
                    . . . 4 4 4 5 5 5 . . . 5 . . .
                    . . . . . . 5 5 5 5 5 5 5 . . .
                    . . . . . . 5 5 5 5 5 . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        my_sprite,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

bogey: Sprite = None
projectile: Sprite = None
my_sprite: Sprite = None
my_sprite = sprites.create(img("""
    . . . . . . . . . . b 5 b . . .
    . . . . . . . . . b 5 b . . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . . . . b b 5 d 1 f 5 d 4 c . .
    . . . . b 5 5 1 f f d d 4 4 4 b
    . . . . b 5 5 d f b 4 4 4 4 b .
    . . . b d 5 5 5 5 4 4 4 4 b . .
    . . b d d 5 5 5 5 5 5 5 5 b . .
    . b d d d d 5 5 5 5 5 5 5 5 b .
    b d d d b b b 5 5 5 5 5 5 5 b .
    c d d b 5 5 d c 5 5 5 5 5 5 b .
    c b b d 5 d c d 5 5 5 5 5 5 b .
    . b 5 5 b c d d 5 5 5 5 5 d b .
    b b c c c d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""),
    SpriteKind.player)
my_sprite.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(my_sprite, 200, 200)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
        . . 2 2 b b b b b . . . . . . .
        . 2 b 4 4 4 4 4 4 b . . . . . .
        2 2 4 4 4 4 3 3 4 4 b . . . . .
        2 b 4 4 4 4 4 4 3 4 b . . . . .
        2 b 4 4 4 4 4 4 4 3 4 b . . . .
        2 b 4 4 4 4 4 4 4 4 4 b . . . .
        2 b 4 4 4 4 4 4 4 4 4 e . . . .
        2 2 b 4 4 4 4 4 4 4 b e . . . .
        . 2 b b b 4 4 4 b b b e . . . .
        . . e b b b b b b b e e . . . .
        . . . e e b 4 4 b e e e b . . .
        . . . . . e e e e e e b d b b .
        . . . . . . . . . . . b 1 1 1 b
        . . . . . . . . . . . c 1 d d b
        . . . . . . . . . . . c 1 b c .
        . . . . . . . . . . . . c c . .
    """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.left = scene.screen_width()
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)

def on_on_overlap(sprite,otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
    sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_projectile_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_projectile_overlap)