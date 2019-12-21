#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import PolygonStamped,Point32
from teb_local_planner.msg import FeedbackMsg,TrajectoryMsg,TrajectoryPointMsg
import numpy as np
import matplotlib.pyplot as plt

def feedback_callback(msg):
    global trajectory

    if not msg.trajectories:
        trajectory=[]
        return
    trajectory=msg.trajectories[msg.selected_trajectory_idx].trajectory

def plot_velocity(fig,ax_v1,ax_v2,t,y1,y2):
    ax_v1.cla()  #clear active axis
    ax_v1.grid()
    ax_v1.set_ylabel('Trans. velocity [m/s]')
    ax_v1.plot(t,y1,'-b.')
    ax_v2.cla()
    ax_v2.grid()
    ax_v2.set_ylabel('Rot. velocity [rad/s]')
    ax_v2.set_xlabel('Time [s]')
    ax_v2.plot(t,y2,'-r.')
    fig.suptitle('visualize_velocity')
    fig.canvas.draw()

def velocity_plotter():
    global trajectory
    rospy.init_node("visualize_velocity",anonymous=True)

    topic_name = "/test_optim_node/teb_feedback"
    rospy.Subscriber(topic_name,FeedbackMsg,feedback_callback,queue_size=1)
    rospy.loginfo("Visualize velocity published on %s topic",topic_name)

    fig,(ax_v1,ax_v2) = plt.subplots(2,sharex=True)  #two subplots sharing the same x axis

    plt.ion()  # turn on interactive mode
    plt.show()  # display

    r=rospy.Rate(2)

    while not rospy.is_shutdown():
        t=[]
        y1=[]
        y2=[]
        for point in trajectory:
            t.append(point.time_from_start.to_sec())
            y1.append(point.velocity.linear.x)
            y2.append(point.velocity.angular.z)

        plot_velocity(fig,ax_v1,ax_v2,np.asarray(t),np.asarray(y1),np.asarray(y2))
        r.sleep()

if __name__=="__main__":
    try:
        trajectory=[]
        velocity_plotter()
    except rospy.ROSInterruptException:
        pass
