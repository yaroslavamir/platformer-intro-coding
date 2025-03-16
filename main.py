def on_overlap_tile(sprite, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_a_pressed():
    mySprite.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
animation.run_image_animation(mySprite,
    [img("""
            . f f f . f f f f . f f f . 
                f f f f f c c c c f f f f f 
                f f f f b c c c c b f f f f 
                f f f c 3 c c c c 3 c f f f 
                . f 3 3 c c c c c c 3 3 f . 
                . f c c c c 4 4 c c c c f . 
                . f f c c 4 4 4 4 c c f f . 
                . f f f b f 4 4 f b f f f . 
                . f f 4 1 f d d f 1 4 f f . 
                . . f f d d d d d d f f . . 
                . . e f e 4 4 4 4 e f e . . 
                . e 4 f b 3 3 3 3 b f 4 e . 
                . 4 d f 3 3 3 3 3 3 c d 4 . 
                . 4 4 f 6 6 6 6 6 6 f 4 4 . 
                . . . . f f f f f f . . . . 
                . . . . f f . . f f . . . .
        """),
        img("""
            . . . . . . . . . . . . . . 
                . f f f . f f f f . f f f . 
                f f f f f c c c c f f f f f 
                f f f f b c c c c b f f f f 
                f f f c 3 c c c c 3 c f f f 
                . f 3 3 c c c c c c 3 3 f . 
                . f c c c c 4 4 c c c c f . 
                . f f c c 4 4 4 4 c c f f . 
                . f f f b f 4 4 f b f f f . 
                . f f 4 1 f d d f 1 4 f f . 
                . . f f d d d d d 4 e f e . 
                . f e f f b b b e d d 4 e . 
                . e 4 f b 3 3 3 e d d e . . 
                . . . f 6 6 6 6 f e e . . . 
                . . . f f f f f f f . . . . 
                . . . f f f . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . 
                . f f f . f f f f . f f f . 
                f f f f f c c c c f f f f f 
                f f f f b c c c c b f f f f 
                f f f c 3 c c c c 3 c f f f 
                . f 3 3 c c c c c c 3 3 f . 
                . f c c c c 4 4 c c c c f . 
                . f f c c 4 4 4 4 c c f f . 
                . f f f b f 4 4 f b f f f . 
                . f f 4 1 f d d f 1 4 f f . 
                . e f e 4 d d d d d f f . . 
                . e 4 d d e b b b f f e f . 
                . . e d d e 3 3 b e f 4 e . 
                . . . e e f 6 6 6 6 f . . . 
                . . . . f f f f f f f . . . 
                . . . . . . . . f f f . . .
        """)],
    500,
    True)
controller.move_sprite(mySprite, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
scene.camera_follow_sprite(mySprite)
mySprite.set_position(21, 18)
mySprite.ay = 220