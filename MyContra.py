import cv2
import mediapipe as mp
import numpy as np
import time
import matplotlib.pyplot as plt
import pyautogui

cap = cv2.VideoCapture(0)

pose = mp.solutions.pose
pose_o = pose.Pose()
drawing = mp.solutions.drawing_utils

flag = False

ctrl_down = False
space_down = False
w_down = False
s_down = False
d_down = False
a_down = False

# Checking if full body is in the frame or not
def inFrame(lst):
    global flag
    if not(flag):
        if lst[24].visibility>0.7 and lst[23].visibility>0.7 and lst[16].visibility>0.7 and lst[15].visibility>0.7:
            flag = True
            return True
        else:
            return False
    else:
        if lst[23].visibility>0.7 and lst[15].visibility>0.7:
            return True
        elif lst[24].visibility>0.7 and lst[16].visibility>0.7:
            return True 
        else:
            return False

#Looking Logic
def isLookingup(lst):
    if (lst[15].y*480<=180) or (lst[16].y*480<=180):
        return True
    return False
def isLookingdown(lst):
    if (lst[15].y*480>=280) or (lst[16].y*480>=280):
        return True
    return False
#Running Logic
def isRunningleft(lst):
    if lst[15].x*640>450:
        cv2.line(frm, (450,80), (450,380), (0,255,0), 1)
        return True
    return False
def isRunningright(lst):
    if lst[16].x*640<190:
        cv2.line(frm, (190,80), (190,380), (0,255,0), 1)
        return True
    return False
#Jumping Logic 
def isJump(lst):
    if(lst[0].y*480<80):
        cv2.line(frm, (0,80), (640,80), (0,255,0), 1)
        return True
    return False

#Shooting Logic
def isShoot(lst):
    if abs((lst[15].x*640)-(lst[16].x*640))<80:
        return True
    return False

#Crouching Logic
def isCrouch(lst):
    if (lst[23].y*480 > 380) and (lst[24].y*480>380):
        cv2.line(frm, (0,380), (640,380), (0,255,0), 1)
        return True
    return False

while True:
    _,frm = cap.read()
    
    #processing our image and storing the landmarks in res
    res = pose_o.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))
    drawing.draw_landmarks(frm,res.pose_landmarks,pose.POSE_CONNECTIONS)
    
    # adding each landmark individually to finalres
    if res.pose_landmarks:
        finalres = res.pose_landmarks.landmark

    # inFrame check if all the 4 pts. are visible or not
    if res.pose_landmarks and inFrame(finalres):
        cv2.putText(frm,str(flag),(0,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.line(frm, (0,80), (640,80), (255,0,0), 1)
        cv2.line(frm, (190,80), (190,380), (255,255,255), 1)
        cv2.line(frm, (450,80), (450,380), (255,255,255), 1)
        cv2.line(frm, (0,180), (640,180), (255,255,255), 1)
        cv2.line(frm, (0,280), (640,280), (255,255,255), 1)
        cv2.line(frm, (320,0), (320,480), (255,255,255), 1)
        cv2.line(frm, (0,380), (640,380), (255,255,255), 1)
        #Now the user is present in the frame
        
        #Running check
        if not(isRunningleft(finalres)^isRunningright(finalres)):
            cv2.putText(frm,"Not Running",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if d_down:
                pyautogui.keyUp('d')
                d_down = False
            if a_down:
                pyautogui.keyUp('a')
                a_down = False
        elif isRunningright(finalres):
            cv2.putText(frm,"Running Right",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if not(d_down):
                pyautogui.keyDown('d') 
                d_down = True
            
        else:
            cv2.putText(frm,"Running Left",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if not(a_down):
                pyautogui.keyDown('a') 
                a_down = True
        
        #Jump check
        if isJump(finalres):
            cv2.putText(frm,"Jumping",(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)  
            if not(space_down):
                pyautogui.keyDown("space")
                space_down = True
        else:
            cv2.putText(frm,"Not Jumping",(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if space_down:
                pyautogui.keyUp("space")
                space_down = False
            
        #Shoot check
        if isShoot(finalres):    
            if not(isLookingup(finalres)^isLookingdown(finalres)):
                cv2.putText(frm,"Shooting Straight",(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)  
                if w_down:
                    pyautogui.keyUp("w")
                    w_down = False
                if s_down:
                    pyautogui.keyUp("s")
                    s_down = False
                        
            elif isLookingup(finalres): 
                cv2.putText(frm,"Shooting Up",(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                if not(w_down):
                    pyautogui.keyDown('w')
                    w_down = True  
            else :
                cv2.putText(frm,"Shooting Down",(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)  
                if not(s_down):
                    pyautogui.keyDown('s')
                    s_down = True 
                
            if not(ctrl_down):
                pyautogui.keyDown('ctrlleft')
                ctrl_down = True
                pyautogui.keyUp("ctrlleft")
                ctrl_down = False
        else:
            cv2.putText(frm,"Not Shooting",(50,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if ctrl_down:
                pyautogui.keyUp("ctrlleft")
                ctrl_down = False
            
        #Crouch check
        if isCrouch(finalres):
            cv2.putText(frm,"Crouching",(50,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)     
            if not(s_down):
                pyautogui.keyDown("s")
                s_down = True     
        else:
            cv2.putText(frm,"Not Crouching",(50,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if s_down:
                pyautogui.keyUp("s")
                s_down = False

    else:
        cv2.putText(frm,"Make sure full body in Frame",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    
    
    cv2.imshow("Window",frm)
    if cv2.waitKey(1) == 27:
        # plt.plot(range(len(temp_lst)),temp_lst)
        # plt.show()
        cap.release()
        cv2.destroyAllWindows()
        break