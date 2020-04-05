<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 284bffebcbca82615f3fc8aee3871cb21ed9ec14
>>>>>>> 903fd686acf8c5d2062f707caab8db8ab7fdffd4
>>>>>>> 3e85cd8d717ab4cefa3084a376656a858030b448
"""
The template of the main script of the machine learning process
"""

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)

def ml_loop():
    """
    The main loop of the machine learning process

    This loop is run in a separate process, and communicates with the game process.

    Note that the game process won't wait for the ml process to generate the
    GameInstruction. It is possible that the frame of the GameInstruction
    is behind of the current frame in the game process. Try to decrease the fps
    to avoid this situation.
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.
    ball_served = False

    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()
    a = 0
    b = 0
    c = 0
    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()

        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        if scene_info.status == GameStatus.GAME_OVER or \
            scene_info.status == GameStatus.GAME_PASS:
            # Do some stuff if needed
            ball_served = False

            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue

        # 3.3. Put the code here to handle the scene information

        # 3.4. Send the instruction for this frame to the game process
        if not ball_served:
            comm.send_instruction(scene_info.frame, PlatformAction.SERVE_TO_LEFT)
            ball_served = True
        else:
            ball_x = scene_info.ball[0]
            ball_y = scene_info.ball[1]
            platform_x = scene_info.platform[0]
            platform_y = scene_info.platform[1]
            if ball_y < 150:
                if platform_x <75:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)   
                elif platform_x >75:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                else:
                    comm.send_instruction(scene_info.frame, PlatformAction.NONE)
            else:
                if ball_y - a >0:#down
                    if ball_x - b >0:#right 395-ball_y == height 
                        if (395 - ball_y)>(200-ball_x): #bounce
                            c = 200- ((395 - ball_y)-(200-ball_x))
                        else:
                            c = ball_x + (395 - ball_y)    

                        #comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    else:#left
                        if (395 - ball_y)>ball_x: #bounce
                            c = ((395 - ball_y)-ball_x)
                        else:
                            c = ball_x - (395 - ball_y)   
                    b = ball_x
                    if platform_x <(c-20):
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)   
                    elif platform_x >(c-20):
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    else:
                        comm.send_instruction(scene_info.frame, PlatformAction.NONE)
                    
                       
            

                
                
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
"""
The template of the main script of the machine learning process
"""

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameStatus, PlatformAction
)

def ml_loop():
    """
    The main loop of the machine learning process

    This loop is run in a separate process, and communicates with the game process.

    Note that the game process won't wait for the ml process to generate the
    GameInstruction. It is possible that the frame of the GameInstruction
    is behind of the current frame in the game process. Try to decrease the fps
    to avoid this situation.
    """

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.
    ball_served = False

    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()
    a = 0
    b = 0
    c = 0
    # 3. Start an endless loop.
    while True:
        # 3.1. Receive the scene information sent from the game process.
        scene_info = comm.get_scene_info()

        # 3.2. If the game is over or passed, the game process will reset
        #      the scene and wait for ml process doing resetting job.
        if scene_info.status == GameStatus.GAME_OVER or \
            scene_info.status == GameStatus.GAME_PASS:
            # Do some stuff if needed
            ball_served = False

            # 3.2.1. Inform the game process that ml process is ready
            comm.ml_ready()
            continue

        # 3.3. Put the code here to handle the scene information

        # 3.4. Send the instruction for this frame to the game process
        if not ball_served:
            comm.send_instruction(scene_info.frame, PlatformAction.SERVE_TO_LEFT)
            ball_served = True
        else:
            ball_x = scene_info.ball[0]
            ball_y = scene_info.ball[1]
            platform_x = scene_info.platform[0]
            platform_y = scene_info.platform[1]
            if ball_y < 150:
                if platform_x <75:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)   
                elif platform_x >75:
                    comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                else:
                    comm.send_instruction(scene_info.frame, PlatformAction.NONE)
            else:
                if ball_y - a >0:#down
                    if ball_x - b >0:#right 395-ball_y == height 
                        if (395 - ball_y)>(200-ball_x): #bounce
                            c = 200- ((395 - ball_y)-(200-ball_x))
                        else:
                            c = ball_x + (395 - ball_y)    

                        #comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
                    else:#left
                        if (395 - ball_y)>ball_x: #bounce
                            c = ((395 - ball_y)-ball_x)
                        else:
                            c = ball_x - (395 - ball_y)   
                    b = ball_x
                    if platform_x <(c-20):
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)   
                    elif platform_x >(c-20):
                        comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
                    else:
                        comm.send_instruction(scene_info.frame, PlatformAction.NONE)
                    
                       
            

                
                
>>>>>>> 4525e33285b869b186b3d58eb001ab408fb80400
>>>>>>> 284bffebcbca82615f3fc8aee3871cb21ed9ec14
>>>>>>> 903fd686acf8c5d2062f707caab8db8ab7fdffd4
>>>>>>> 3e85cd8d717ab4cefa3084a376656a858030b448
