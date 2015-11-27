#!/usr/bin/env python

# A script to watch stabilizer status

from hrpsys_ros_bridge.srv import OpenHRP_StabilizerService_getParameter as getParameter
import rospy
from std_msgs.msg import Empty
from sound_play.msg import SoundRequest
from hrpsys_ros_bridge.msg import ContactStatesStamped, ContactStateStamped, ContactState

# global variable
g_previous_st_controller_mode = None

def controllerModeToString(msg):
    is_lleg_contact = None
    is_rleg_contact = None
    for state in msg.states:
        if state.header.frame_id == "lfsensor":
            if state.state.state == ContactState.ON:
                is_lleg_contact = True
            else:
                is_lleg_contact = False
            if state.header.frame_id == "rfsensor":
                if state.state.state == ContactState.ON:
                    is_rleg_contact = True
                else:
                    is_rleg_contact = False
    if is_lleg_contact or is_rleg_contact:
        return "MODE_ST"
    else:
        return "MODE_AIR"

def isChangedControllerMode(actual_from, actual_to, expected_from, expected_to):
    if (actual_from in expected_from and
        actual_to == expected_to):
        return True
    else:
        return False

def trig():
    g_odom_init_trigger_pub.publish(Empty())
    # Say something
    sound = SoundRequest()
    sound.sound = SoundRequest.SAY
    sound.command = SoundRequest.PLAY_ONCE
    sound.arg = "Robot stands on the ground."
    g_robotsound_pub.publish(sound)
    
def contactStatesCallback(msg):
    global g_previous_st_controller_mode
    global g_odom_init_trigger_pub, g_robotsound_pub
    controller_mode = controllerModeToString(msg)
    if (controller_mode == "MODE_AIR" or 
        controller_mode == "MODE_IDLE" or 
        controller_mode == "MODE_ST"):
        if g_previous_st_controller_mode == None:
            g_previous_st_controller_mode = controller_mode
            if controller_mode == "MODE_ST":
                trig()
        else:
            if isChangedControllerMode(g_previous_st_controller_mode,
                                       controller_mode,
                                       ["MODE_AIR", "MODE_IDLE"],
                                       "MODE_ST"):
                trig()
            g_previous_st_controller_mode = controller_mode

if __name__ == "__main__":
    rospy.init_node("stabilizer_watcher")
    contact_states_sub = rospy.Subscriber("/act_contact_states", ContactStatesStamped, contactStatesCallback)
    g_odom_init_trigger_pub = rospy.Publisher("/odom_init_trigger", Empty)
    g_robotsound_pub = rospy.Publisher("/robotsound", SoundRequest)
    rospy.spin()

