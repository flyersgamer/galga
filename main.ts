controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(img`
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
        `, my_sprite, 200, 0)
})
let bogey : Sprite = null
let projectile : Sprite = null
let my_sprite : Sprite = null
my_sprite = sprites.create(img`
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
`, SpriteKind.Player)
my_sprite.setStayInScreen(true)
info.setLife(3)
controller.moveSprite(my_sprite, 200, 200)
game.onUpdateInterval(500, function on_update_interval() {
    
    bogey = sprites.create(img`
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
    `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.left = scene.screenWidth()
    bogey.y = randint(0, scene.screenHeight())
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_projectile_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
