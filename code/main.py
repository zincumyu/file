import  cv2
import  mediapipe as  mp
camera =cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()

while True:
    success,img=camera.read()
    if success:
        img_rgb =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#图像处理
        result =hand_detector.process(img_rgb) #把点坐标赋值
        if result.multi_hand_landmarks:  #如果有
            for handlms in result.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(img,handlms,mp.solutions.hands.HAND_CONNECTIONS)

        cv2.imshow('video',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyWindow()