import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("مرورگر وب سایت")
        self.setGeometry(100, 100, 1024, 768)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://example.com"))
        
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserApp()
    window.show()
    sys.exit(app.exec_())