{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "235270d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#open cv is a open source computer vision library given by python this is used for image processing (makes our task very easy)\n",
    "import cv2#import open cv library\n",
    "from random import randrange as r"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "af3ebda9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#haar cascade algorithm works on gray scale images only  https://github.com/opencv/opencv/tree/master/data/haarcascades\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ff3d21e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "traineddata=cv2.CascadeClassifier(\"front_face.xml\")#train dataset to detect image done by classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6a1414a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#choose image\n",
    "#img=cv2.imread(\"rachit.jpg.jpg\")\n",
    "#img=cv2.imread(\"two.jpg\")\n",
    "webcam=cv2.VideoCapture(0)#0 sinnce webcam is accessed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "87bcf4ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "end of program\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    success,img=webcam.read()\n",
    "    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "    facecordinate=traineddata.detectMultiScale(grayimg)\n",
    "    for x,y,w,h in facecordinate:\n",
    "        cv2.rectangle(img,(x,y),(x+w,y+h),(r(0,256),r(0,256),r(0,256)),2)\n",
    "\n",
    "\n",
    "    cv2.imshow('window',img)\n",
    "    key=cv2.waitKey(1)#1milisecond \n",
    "    if(key==81 or key==113):\n",
    "        break\n",
    "webcam.release()    \n",
    "#cv2.imshow(\"single person\",img)#name at window and which image to show\n",
    "#cv2.waitKey()\n",
    "print(\"end of program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0f2499c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#cv2.waitKey()#pause execution until any key is pressed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aae144d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#conversion to grey scale \n",
    "#grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "#cv2.imshow(\"rachit\",grayimg)\n",
    "#cv2.waitKey()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "96c8cbdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[211 129 213 213]]\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "13610d2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "facecordinate=traineddata.detectMultiScale(grayimg)#detect faces from min to max possiblity and brings the coordinate\n",
    "print(facecordinate)\n",
    "#[[209  85 231 231]]  x,y,w,h\n",
    "for x,y,w,h in facecordinate:\n",
    "    cv2.rectangle(img,(x,y),(x+w,y+h),(r(0,256),r(0,256),r(0,256)),2)\n",
    "\n",
    "\n",
    "cv2.imshow('window',img)\n",
    "cv2.waitKey()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0603458a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "248f8159",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86a5e784",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9de26b7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50efba4b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f69dfd81",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d0d9ccb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df85c2cd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
