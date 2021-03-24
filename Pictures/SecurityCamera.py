"""
Security Camera
@author: laurent.tupin
"""
import os
import datetime as dt


class c_secCam():
    def __init__(self, int_whatToDisplay = 100):
        import cv2
        import winsound
        self.o_sound = winsound
        self.o_cv = cv2
        self.__nameCam = 'Security Cam'
        self.__okFlag = True
        self.__cam = cv2.VideoCapture(0)
        self.__lWhatToDisplay = ['cam', 'diff', 'gray','blur','thresh','cube','contour']
        try:
            self.__whatToDisplay = self.__lWhatToDisplay[int_whatToDisplay]
        except:
            self.__whatToDisplay = 'Security Camera'
        self.__nowSave = dt.datetime(2000, 1, 2)
        self.__nowSend = dt.datetime(2000, 1, 2)
        self.__numPicturesSaved = 0
        
    def closeCam(self):
        self.__cam.release()
        self.o_cv.destroyWindow(self.__nameCam)
        # cv2.destroyAllWindows()
    
    def GetFrame(self):
        bl_ret, frame = self.__cam.read()
        return frame
        
    def GetMove(self):
        bl_ret, frame1 = self.__cam.read()
        bl_ret, frame2 = self.__cam.read()
        diff = self.o_cv.absdiff(frame1, frame2)
        return diff
    
    def GetGray(self):
        gray = self.o_cv.cvtColor(self.GetMove(), self.o_cv.COLOR_RGB2GRAY)
        return gray    
    
    def GetBlurGray(self):
        blur = self.o_cv.GaussianBlur(self.GetGray(), (5, 5), 0)
        return blur    
    
    def GetThresh(self):
        _, thresh = self.o_cv.threshold(self.GetBlurGray(), 20, 255, self.o_cv.THRESH_BINARY)
        return thresh
    
    def GetCube(self):
        Cubic = self.o_cv.dilate(self.GetThresh(), None, iterations = 3)
        return Cubic
    
    def GetContours(self, bl_ignoreSmallMove = True, bl_soundAlert = False, bl_saveImage = False):
        cv = self.o_cv
        sound = self.o_sound
        frame = self.GetFrame()
        contours, _ = cv.findContours(self.GetCube(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if bl_ignoreSmallMove:
                if cv.contourArea(c) > 5000:
                    if bl_saveImage:
                        self.TakePicture()
                    if bl_soundAlert:
                        sound.Beep(500, 200)
                else:   continue
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame
    
    def GetNow(self):
        dte_now = dt.datetime.now()
        str_now = dte_now.strftime("%Y-%m-%d %H-%M-%S")
        return dte_now, str_now
    
    def TakePicture(self):
        dte_now, str_now = self.GetNow()
        if (dte_now - self.__nowSave).total_seconds() > 2 * (self.__numPicturesSaved + 1):
            self.__nowSave = dte_now
            self.__numPicturesSaved += 1
            cv = self.o_cv
            frame = self.GetFrame()
            str_path = os.path.join(os.getcwd(), r'Captures\cam_{}.png'.format(str_now))
            # SAVE IMAGE
            cv.imwrite(str_path, frame)
            if (dte_now - self.__nowSend).days > 1:
                self.__nowSend = dte_now
                # Send Email Alert with Image enclosed
        
    def displayFrame(self, str_whatToDisplay):
        # CHOOSE
        if str_whatToDisplay == 'cam':      o_toDisplay = self.GetFrame()
        elif str_whatToDisplay == 'diff':   o_toDisplay = self.GetMove()
        elif str_whatToDisplay == 'gray':   o_toDisplay = self.GetGray()
        elif str_whatToDisplay == 'blur':   o_toDisplay = self.GetBlurGray()
        elif str_whatToDisplay == 'thresh': o_toDisplay = self.GetThresh()
        elif str_whatToDisplay == 'cube':   o_toDisplay = self.GetCube()
        elif str_whatToDisplay == 'contour':o_toDisplay = self.GetContours()
        else:
            # Security Camera (do not display on screen)
            o_toDisplay = self.GetContours(bl_saveImage = True)
            self.o_cv.imshow(self.__nameCam, 0)
            return 0
        # DISPLAY
        self.o_cv.imshow(self.__nameCam, o_toDisplay)
        
    def LoopOfVerification(self):
        ok_flag = self.__okFlagq
        STOP_KEYBOARD = 'q'
        while self.__cam.isOpened() and ok_flag:
            if self.o_cv.waitKey(10) == ord(STOP_KEYBOARD):
                ok_flag = False
            else:
                self.displayFrame(self.__whatToDisplay)    
        # Close
        self.closeCam()
    
    def __del__(self):
        self.closeCam()
            
        
        
# Launch the class            
i_secCam = c_secCam(4)
i_secCam.LoopOfVerification()
       
   




#=============================================================================
# OLD
#=============================================================================


# ok_flag = True
# cam = cv2.VideoCapture(0)

# while cam.isOpened() and ok_flag:
#     ret, frame1 = cam.read()
#     ret, frame2 = cam.read()
#     diff = cv2.absdiff(frame1, frame2)
#     gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#     dilated = cv2.dilate(thresh, None, iterations = 3)
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)
#     for c in contours:
#         # Do not take small movement into account
#         if cv2.contourArea(c) < 5000:  
#             continue
#         x, y, w, h = cv2.boundingRect(c)
#         cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         #winsound.Beep(500, 200)
#         # Take picture
#         # Send Alert
#     # Show
#     cv2.imshow('Security Cam', frame1)
#     # EXIT 
#     if cv2.waitKey(10) == ord('q'):
#         ok_flag = False
    
# # Closed Window
# cam.release()
# cv2.destroyWindow('Security Cam')
# # cv2.destroyAllWindows()
