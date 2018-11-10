from lib.line_detector import LineDetector

line_detector = LineDetector('Y11', debug = True)
while True:
    print(line_detector.is_path())
    pyb.delay(300)
