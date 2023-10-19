import dlib
import cv2
from imutils import face_utils
from scipy.spatial import distance
import math
import FeatureMeasurement as fm
import pandas as pd
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# This is taken from https://github.com/sandyying/APM-Drowsiness-Detection/blob/master/Live%20Demo.ipynb
# and https://github.com/hackenjoe/Advanced_Drowsiness_Detection/blob/main/drowsiness_detection.ipynb
def average(y_pred):
  for i in range(1,len(y_pred)-1):
    if i % 240 == 0 or (i+1) % 240 == 0:
      pass
    else: 
      average = float(y_pred[i-1] +  y_pred[i] + y_pred[i+1])/3
      if average >= 0.5:
        y_pred[i] = 1
      else:
        y_pred[i] = 0
  return y_pred

df = pd.read_csv('dataset/totalwithmaininfo.csv',sep=',')
#df = df.drop(df.columns[0])

participants = set(df.Participant)
df = df.drop(["Participant"], axis=1)
#df = df[df.Y != 5.0]  
df.loc[df.Y == 0.0, "Y"] = int(0)
df.loc[df.Y == 10.0, "Y"] = int(2)
df.loc[df.Y == 5.0, "Y"] = int(1)

train_percentage = 18/len(participants)
train_samples = int(len(df) * train_percentage)
test_samples = len(df) - train_samples

df_train = df[:train_samples]
df_test = df[-test_samples:]

X_test = df_test.drop(["Y"], axis=1)
y_test = df_test["Y"]

X_train = df_train.drop('Y', axis=1)
y_train = df_train['Y']

acc3_list = []
f1_score3_list = []
roc_3_list = []


#9 was the highest
neigh = KNeighborsClassifier(9)
#print(f"Neighbors: {neigh.get_params()['n_neighbors']}")
neigh.fit(X_train, y_train) 

'''pred_KN = neigh.predict(X_test)
pred_KN = average(pred_KN)
acc3 = accuracy_score(y_test, pred_KN)
print(str(acc3*100)+"%")'''

def modelKNNLocal(landmarks,mean,std):
    """Returns features and classification result"""
    Result_String,fontColour = None,None
    features = pd.DataFrame(columns=["MOE","EAR","MAR","Circularity"])
    eye = landmarks[36:68] # Extracting relevant parts (eyes + mouth)
    ear = fm.EAR(eye)
    mar = fm.MAR(eye)
    moe = fm.mouth_over_eye(eye)
    cir = fm.mouth_over_eye(eye)
    df = features.append({"MOE":moe,"EAR": ear,"MAR": mar,"Circularity": cir},ignore_index=True)

    # Normalisation
    df["EAR_N"] = (df["EAR"] - mean["EAR"]) / std["EAR"]
    df["MAR_N"] = (df["MAR"] - mean["MAR"]) / std["MAR"]
    df["Circularity_N"] = (df["Circularity"] - mean["Circularity"]) / std["Circularity"]
    df["MOE_N"] = (df["MOE"] - mean["MOE"]) / std["MOE"]

    Result = neigh.predict(df)  
    prob = neigh.predict_proba(df)
    if Result == 2:
        Result_String = "Drowsy"
        fontColour = (0,0,255)
    elif Result >= 1:
        Result_String = "Possibly Drowsy"
        fontColour = (100,100,255)
    else:
        Result_String = "Not Drowsy"
        fontColour = (255,255,255)
    return Result_String, fontColour,prob

def modelKNNWebServer(json,mean,std):
    """Returns features and classification result"""
    features = pd.DataFrame(columns=["EAR","MAR","Circularity","MOE"])
    ear = json.get("EAR")
    mar = json.get("MAR")
    moe = json.get("MOE")
    cir = json.get("CIR")
    mean = json.get("MEAN")
    std = json.get("STD")
    df = features.append({"EAR":ear,"MAR": mar,"Circularity": cir,"MOE": moe},ignore_index=True)

    # Normalisation
    df["EAR_N"] = (df["EAR"] - mean["EAR"]) / std["EAR"]
    df["MAR_N"] = (df["MAR"] - mean["MAR"]) / std["MAR"]
    df["Circularity_N"] = (df["Circularity"] - mean["Circularity"]) / std["Circularity"]
    df["MOE_N"] = (df["MOE"] - mean["MOE"]) / std["MOE"]

    '''df["EAR_N"] = (df["EAR"] - mean.get("EAR")) / std.get("EAR")
    df["MAR_N"] = (df["MAR"] - mean.get("MAR")) / std.get("MAR")
    df["Circularity_N"] = (df["Circularity"] - mean.get("CIR")) / std.get("CIR")
    df["MOE_N"] = (df["MOE"] - mean.get("MOE")) / std.get("MOE")'''
    
    Result = neigh.predict(df)  
    if Result == 1:
        Result_String = "Drowsy"
    else:
        Result_String = "Alert"
    
    return Result_String