import cv2
import mediapipe as mp
import numpy as np

#角度检测
def get_angle(v1, v2):
    angle = np.dot(v1, v2) / (np.sqrt(np.sum(v1 * v1)) * np.sqrt(np.sum(v2 * v2)))
    angle = np.arccos(angle) / 3.14 * 180

    return angle

def get_str_close(list_lms):
        #自己的右视频的左
        z_16 =list_lms[16] - list_lms[14]
        z_14 =list_lms[14] - list_lms[12]
        angle_z =get_angle(z_16,z_14)
        print(angle_z)




if __name__ == "__main__":

    # 打开视频流
    cap = cv2.VideoCapture(0)  # 或者替换为需要监控的视频文件路径

    # 加载姿势识别模型
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_drawing = mp.solutions.drawing_utils
    while True:
        # 读取一帧图像
        success, img = cap.read()
        if not success:
            continue
        image_height, image_width, _ = np.shape(img)

        # 转换为RGB  对视频帧进行处理
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)

        # 检测画面中的人和姿势# 在画面中绘制姿势连接线
        if results.pose_landmarks:
            # 采集所有关键点的坐标
            pose_xy = results.pose_landmarks
            list_lms = []
            for i in range(31):
                pos_x = pose_xy.landmark[i].x * image_width
                pos_y = pose_xy.landmark[i].y * image_height
                list_lms.append([int(pos_x), int(pos_y)])

            mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

            #转矢量
            list_lms = np.array(list_lms, dtype=np.int32)
            #打印
            get_str_close(list_lms)

            #test
            # print(list_lms)


        cv2.imshow("Yoga Pose Detection",img)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()











