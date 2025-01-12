from retinaface import RetinaFace
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import time
start_time = time.time()
obj = DeepFace.verify(img1_path = 'student/stu1/stu1_1.jpg', img2_path = 'final_images/stu2_0.jpg', model_name = 'Facenet512', detector_backend = 'retinaface', enforce_detection=False)
end_time = time.time()

elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
print(obj['verified'])