import numpy as np
import time
from src.State import State
from src.Command import Command
from src.Controller import Controller
# from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
import matplotlib.pyplot as plt 

def main(use_imu=False):
    """Main program
    """

    # Create config
    config = Configuration()
    # hardware_interface = HardwareInterface()

    # # Create imu handle
    # if use_imu:
    #     imu = IMU(port="/dev/ttyACM0")
    #     imu.flush_buffer()

    # Create controller and user input handles
    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )


    print(config.default_stance)
    state = State()
    state.foot_locations = (
                config.default_stance + np.array([0, 0, -0.16])[:, np.newaxis]
            )
    # print("Creating joystick listener...")
    # joystick_interface = JoystickInterface(config)
    # print("Done.")

    last_loop = time.time()

    print("Summary of gait parameters:")
    # print("overlap time: ", config.overlap_time)
    # print("swing time: ", config.swing_time)
    # print("z clearance: ", config.z_clearance)
    # print("x shift: ", config.x_shift)


    command = Command()
    command.horizontal_velocity = np.array([0.2, 0])

    foot_position_data = []
    # Wait until the activate button has been pressed
    # while True:
        # print("Waiting for L1 to activate robot.")
        # while True:
        #     command = joystick_interface.get_command(state)
        #     joystick_interface.set_color(config.ps4_deactivated_color)
        #     if command.activate_event == 1:
        #         break
        #     time.sleep(0.1)
        # print("Robot activated.")
        # joystick_interface.set_color(config.ps4_color)
    count = -1
    
    while count<101:
        
        now = time.time()
        if now - last_loop < config.dt:
            continue
        else:
            count += 1
            last_loop = time.time()

            # # Parse the udp joystick commands and then update the robot controller's parameters
            # command = joystick_interface.get_command(state)
            # if command.activate_event == 1:
            #     print("Deactivating Robot")
            #     break

            # Read imu data. Orientation will be None if no data was available
            # quat_orientation = (
            #     imu.read_orientation() if use_imu else np.array([1, 0, 0, 0])
            # )
            # state.quat_orientation = quat_orientation


            # Step the controller forward by dt
            
            test = controller.run(state, command)
            # print(test)
            if count>50:
                foot_position_data.append(test)





        # # Update the pwm widths going to the servos
        # hardware_interface.set_actuator_postions(state.joint_angles)


    fig, ax = plt.subplots(2,2)

    # Reorganize data
    f1xpos = []
    f1zpos = []

    f2xpos = []
    f2zpos = []

    f3xpos = []
    f3zpos = []

    f4xpos = []
    f4zpos = []

    for d in foot_position_data:
        f1xpos.append(d[0][0])
        f1zpos.append(d[2][0])

        f2xpos.append(d[0][1])
        f2zpos.append(d[2][1])

        f3xpos.append(d[0][2])
        f3zpos.append(d[2][2])
        
        f4xpos.append(d[0][3])
        f4zpos.append(d[2][3])


    COLOR='blue'
    MAP='winter'
    NPOINTS = len(f1xpos)

    cm = plt.get_cmap(MAP)
    colors = plt.cm.winter(np.linspace(0,1,NPOINTS))
    ax[0,0].set_prop_cycle('color',colors)
    for i in range(NPOINTS-1):
        ax[0,0].plot(f1xpos[i:i+2],f1zpos[i:i+2])

    ax[0,1].set_prop_cycle('color',colors)
    for i in range(NPOINTS-1):
        ax[0,1].plot(f2xpos[i:i+2],f2zpos[i:i+2])
    
    ax[1,0].set_prop_cycle('color',colors)
    for i in range(NPOINTS-1):
        ax[1,0].plot(f3xpos[i:i+2],f3zpos[i:i+2])

    ax[1,1].set_prop_cycle('color',colors)
    for i in range(NPOINTS-1):
        ax[1,1].plot(f4xpos[i:i+2],f4zpos[i:i+2])

    



    #ax[0,1].plot(f2xpos,f2zpos)
    #ax[1,0].plot(f3xpos,f3zpos)
    #ax[1,1].plot(f4xpos,f4zpos)
    # 
    #ax[0,0].axis('scaled')
    #ax[0,1].axis('scaled')
    #ax[1,0].axis('scaled')
    #ax[1,1].axis('scaled')

    plt.show()
    

main()
