scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.gameOver(false)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    mySprite.vy = -150
})
let mySprite : Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
animation.runImageAnimation(mySprite, [img`
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
        `, img`
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
        `, img`
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
        `], 500, true)
controller.moveSprite(mySprite, 100, 0)
tiles.setCurrentTilemap(tilemap`
    level2
`)
scene.cameraFollowSprite(mySprite)
mySprite.setPosition(21, 18)
mySprite.ay = 220
