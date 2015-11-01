# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:52:27 2015

@author: lijinke
"""



import vrep
import sys
import numpy as np
import time
import math
from scipy import interpolate



clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)

arr=np.ndarray(shape=(30,30,10),dtype=float)

errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Sensor_1',vrep.simx_opmode_oneshot_wait)
errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor (clientID,sensor1,vrep.simx_opmode_streaming)            

errorCode,sensor2=vrep.simxGetObjectHandle(clientID,'Sensor_2',vrep.simx_opmode_oneshot_wait)
errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor (clientID,sensor2,vrep.simx_opmode_streaming)            

time.sleep(3)
                               

index=0
index2=0
index3=0
for index in range(30):
    for index2 in range(30):
        for index3 in range(10):
        #for index3 in range(1):
             #Block an neue Position
            x=0.4+0.4*index
            y=0.2+0.4*index2
            z=0.3+0.4*index3
            vrep.simxSetObjectPosition (clientID,sensor1,-1,(x,y,z),vrep.simx_opmode_oneshot)
            vrep.simxSetObjectPosition (clientID,sensor2,-1,(x-0.4,y,z),vrep.simx_opmode_oneshot)
            time.sleep(0.2)            
            #Kollision prüfen 
            #vrep.simxGetCollisionHandle (regular API equivalent: simGetCollisionHandle)
            errorCode,detectionState1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor (clientID,sensor1,vrep.simx_opmode_buffer)            
            errorCode,detectionState2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor (clientID,sensor2,vrep.simx_opmode_buffer)            
                        
            if (detectionState1 or detectionState2):            
                arr[index,index2,index3]=1   #Ergebnis speichern
            else:
                arr[index,index2,index3]=0 
            #time.sleep(0.2)