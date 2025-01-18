import cv2

from backend.display.frame_display import ColoredDisplay, BlackAndWhiteDisplay, CombinedDisplay


class FrameLiveStream:
    def __init__(self, cap, display, collection):
        self.cap = cap
        self.display = display
        self.collection = collection

class ColoredLiveStream(FrameLiveStream):
    def __init__(self, cap, display, collection):
        super().__init__(cap, display, collection)
        self.color = ColoredDisplay(cap, display, collection)

    def regularFramesContinuous(self):
        while self.cap.isOpened():
            self.color.regularFrame()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

class BlackAndWhiteLiveStream(FrameLiveStream):
    def __init__(self, cap, num, display, collection):
        super().__init__(cap, display, collection)
        self.num = num
        self.bw = BlackAndWhiteDisplay(cap, num, display, collection)

    def infiniteBlackFramesDiscrete(self):
        while self.cap.isOpened():
            self.bw.blackFrame()
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.bw.blackFrame()
                    break
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    return
            self.num+=1

    def infiniteBlackFramesContinuous(self):
        while self.cap.isOpened():
            while True:
                self.bw.blackFrame()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    return
            self.num+=1
            cv2.waitKey(0)

    def oneBlackFrame(self):
        while self.cap.isOpened():
            self.bw.blackFrame()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.waitKey(0)

class CombinedLiveStream(FrameLiveStream):
    def __init__(self, cap, num, display, collection):
        super().__init__(cap, display, collection)
        self.num = num
        self.combined = CombinedDisplay(cap, num, display, collection)

    def combinedFrames(self, frame1, frame2):
        image = cv2.addWeighted(frame1, 0.5, frame2, 0.5, 0)
        #to be continued
