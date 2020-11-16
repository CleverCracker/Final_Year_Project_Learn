import cv2
import numpy as np

# Load YoLo
yolo_path = './ObjectDetection/Yolo_Darknet/'
net = cv2.dnn.readNet(yolo_path+'yolov3.weights',
                      yolo_path+'yolo.cfg')

classes = []
with open(yolo_path + 'coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]


# Load Image
images_path = 'ObjectDetection/images/'
img = cv2.resize(cv2.imread(images_path + 'room.jpg'), None, fx=.5, fy=.5)
height, width, channels = img.shape

# Detection Object
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True)

# for b in blob:
#     for n, img_blob in enumerate(b):
#         cv2.imshow(str(n), img_blob)

net.setInput(blob)
outs = net.forward(output_layers)

# * Showing Informations on the Screen
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object Detection
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            # cv2.circle(img, (center_x, center_y), 10, (0, 255, 0), 2)

            # Rectangle Draw
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = classes[class_ids[i]]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, label, (x, y+20), font, 1, (0, 0, 0), 1)
        print()

# Test Showing Image
cv2.imshow('Camera Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
