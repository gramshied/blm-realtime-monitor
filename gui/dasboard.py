import sys
import matplotlib
matplotlib.use("QtAgg")

import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Beam Loss Monitor")

        layout = QVBoxLayout()

        # STATUS LABEL
        self.status = QLabel("STATUS: NORMAL")
        self.status.setStyleSheet("color: green; font-weight: bold; font-size: 16px;")
        layout.addWidget(self.status)

        # PLOT
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.data = []

        # TIMER FOR REAL-TIME UPDATE
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

    def update_plot(self):

        try:
            with open("build/signal_stream.txt") as f:
                lines = f.readlines()

            self.data = [float(x.strip()) for x in lines[-50:]]

            self.ax.clear()

            # Plot signal
            self.ax.plot(self.data, color="blue")

            # Thresholds
            warning = 2.0
            critical = 2.5

            self.ax.axhline(warning, color="orange", linestyle="--", label="Warning")
            self.ax.axhline(critical, color="red", linestyle="--", label="Critical")

            self.ax.set_title("Beam Signal")
            self.ax.set_ylabel("Amplitude")
            self.ax.set_xlabel("Samples")

            self.ax.legend()

            self.ax.relim()
            self.ax.autoscale_view()

            # STATUS UPDATE
            if len(self.data) > 0:

                latest = self.data[-1]

                if abs(latest) > critical:
                    self.status.setText("STATUS: CRITICAL BEAM LOSS")
                    self.status.setStyleSheet("color:red; font-weight:bold; font-size:16px")

                elif abs(latest) > warning:
                    self.status.setText("STATUS: WARNING")
                    self.status.setStyleSheet("color:orange; font-weight:bold; font-size:16px")

                else:
                    self.status.setText("STATUS: NORMAL")
                    self.status.setStyleSheet("color:green; font-weight:bold; font-size:16px")

            self.canvas.draw()

        except Exception as e:
            print("Waiting for data file...", e)


app = QApplication(sys.argv)

window = Dashboard()
window.resize(800, 500)
window.show()

app.exec()
