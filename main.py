
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    browser = QWebView()
    browser.load(QUrl("https://baidu.com"))
    browser.show()

    sys.exit(app.exec_())