import rospy
import pyaudio
import time
import speech_recognition as sr
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

r = sr.Recognizer()
bankbot_state = 0




KeyWord = {"ห้อง 1":"Room_1","ห้อง 2":"Room_2","ห้อง 3":"Room_3","ห้องใหญ่":"Room_main"}



Goal = {"Room_1":[-5.625,1.401,0.703,0.7103],"Room_2":[1.339,1.357,0.705,0.7087],"Room_3":[5.688,1.017,0.703,0.7107],"Room_main":[-4.466,-4.523,0.999,0.0042],"Charger_Station":[3.552,-3.475,0.703,0.7102]}




def movebase_client(map_odom_desire):

   
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   
    client.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = map_odom_desire[0]
    goal.target_pose.pose.position.y = map_odom_desire[1]
    goal.target_pose.pose.orientation.z = map_odom_desire[2]
    goal.target_pose.pose.orientation.w = map_odom_desire[3]

  
    client.send_goal(goal)

    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
 
        return client.get_result()   


if __name__ == '__main__':
    try:
       
        rospy.init_node('movebase_client_py')



        while 1:

            
            if (bankbot_state == 0):
                rospy.loginfo("Going to Charger_Station For Sethome")
                if movebase_client(Goal["Charger_Station"]):
                    rospy.loginfo("Reached At The Charger_Station")
                    bankbot_state = 1


            elif (bankbot_state == 1):  
                try:
                    with sr.Microphone() as source:      
                        print("Say The Room That You Want")          
                        audio = r.listen(source, phrase_time_limit = 10)
                        print("Please Stop Your Command And Wait A Few Minute")
                        word = r.recognize_google(audio,language='th')
                        print(word)
                        try:
                            rospy.loginfo("Going to" + KeyWord[word])
                            if movebase_client(Goal[KeyWord[word]]):
                                rospy.loginfo("Reached At The Room That You Want")
                                bankbot_state = 2
                        except:
                            pass

                except:
                    pass

            elif (bankbot_state == 2):  
                rospy.loginfo("Customer Can Keep The Coffee")
                rospy.loginfo("The Robot Will Back To The Charger_Station In 10 Seconds")
                time.sleep(10)
                bankbot_state = 0
            




    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
