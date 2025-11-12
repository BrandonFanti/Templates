from __future__ import annotations

import pyqtgraph as pg

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
    QBoxLayout
)

class QChartXY(QtWidgets.QWidget):
    def __init__(
        self,
        x,y,
        *,
        title="SINE",
        title_styles={"color":"black","size":"20pt"},
        legend_x_title="X",
        legend_y_title="Y",
        legend_y_styles={"":"","":""},
        legend_title_styles={"color": "red", "font-size": "18px"},
        pen = pg.mkPen(color=(0, 0, 255)),
        background="w",
        point_symbol="o", #circle
        point_symbol_size=15,
        point_symbol_color="red"
    ):
        super().__init__()

        plot_graph = pg.PlotWidget()
        plot_graph.setBackground(background)
        plot_graph.setTitle(title, **title_styles)
        plot_graph.setLabel("bottom", legend_x_title, **legend_title_styles)
        plot_graph.setLabel("left", legend_y_title, **legend_title_styles)
        plot_graph.addLegend()
        plot_graph.showGrid(x=True, y=True)
        plot_graph.setXRange(min(x), max(x))
        plot_graph.setYRange(min(y), max(y))
        plot_graph.plot(
            x,
            y,
            name="Plot",
            pen=pen,
            symbol=point_symbol,
            symbolSize=point_symbol_size,
            symbolBrush=point_symbol_color,
        )
        plot_graph.setMinimumHeight(300)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

        layout.addWidget(plot_graph)

        self.setLayout(layout)
