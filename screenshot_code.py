import win32gui, win32api, win32ui, win32con


def getScreenshot():
    hwnd = win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    
    hDC = win32gui.GetWindowDC(hwnd)
    pDC = win32ui.CreateDCFromHandle(hDC)
    memDC = pDC.CreateCompatibleDC()
    
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(pDC, width, height)
    memDC.SelectObject(screenshot)
    
    memDC.BitBlt((0,0), (width, height), pDC, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(memDC, 'screenshot.bmp')
    
    memDC.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
		
def main():
    getScreenshot()	
	

main()

