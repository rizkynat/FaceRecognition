import face_recognition
import cv2
import numpy as np


class VideoCap:
    def __init__(self, index_input_video, rx, ry):
        all_face_locations = []
        all_face_encodings = []
        self.count_faces = [0,]
        self.count_humans = [0,]
        self.video_capture = cv2.VideoCapture(index_input_video)
        self.ret, self.current_frame = self.video_capture.read()
        self.current_frame_resized = cv2.resize(self.current_frame, (0, 0), fx=rx, fy=ry)
        self.current_frame_resized = self.current_frame_resized[:, :, ::-1]

    def input_source(self, input, fx, fy):
        self.video_capture = cv2.VideoCapture(input)
        self.ret, self.current_frame = self.video_capture.read()
        self.current_frame_resized = cv2.resize(self.current_frame, (0, 0), fx=fx, fy=fy)
        self.current_frame_resized = self.current_frame_resized[:, :, ::-1]

    def get_count_human(self):
        max_human = max(self.count_humans)
        return max_human

    def get_count_face(self):
        max_human = max(self.count_faces)
        return max_human

    def get_video_capture(self):
        return self.video_capture

    def _update_current_frame(self):
        self.ret, self.current_frame = self.get_video_capture().read()

    def _resize_current_frame(self, rx, ry):
        self.current_frame_resized = cv2.resize(
            self.current_frame, (0, 0), fx=rx, fy=ry)

    def face_recog(self, upsample, model):
        self.all_face_locations = face_recognition.face_locations(
            self.get_current_frame_resized(), upsample, model)

    def get_frame_enhancement(self, b, c):
        brightness = b
        constrast = c
        self.current_frame_enhancement = cv2.addWeighted(self.current_frame_resized, constrast,       np.zeros(
            self.current_frame_resized.shape, self.current_frame_resized.dtype), 0, brightness)

    def get_current_frame(self):
        return self.current_frame

    def get_current_frame_read(self):
        return self.ret, self.current_frame

    def get_current_frame_resized(self):
        return self.current_frame_resized

    def get_all_face_locations(self):
        return self.all_face_locations

    def get_all_face_encodings(self):
        self.all_face_encodings = face_recognition.face_encodings(self.get_current_frame_resized(), self.all_face_locations)
        return self.all_face_encodings
