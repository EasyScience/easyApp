# SPDX-FileCopyrightText: 2023 EasyDiffraction contributors
# SPDX-License-Identifier: BSD-3-Clause
# © 2023 Contributors to the EasyDiffraction project <https://github.com/easyscience/EasyDiffraction>

from PySide6.QtCore import QObject, Property

from EasyApp.Logic.Logging import LoggerLevelHandler

from Logic.Py.Project import Project
from Logic.Py.Status import Status
from Logic.Py.Report import Report


class BackendProxy(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._logger = LoggerLevelHandler(self)
        self._project = Project(self)
        self._status = Status(self)
        self._report = Report(self)

    @Property('QVariant', constant=True)
    def logger(self):
        return self._logger

    @Property('QVariant', constant=True)
    def project(self):
        return self._project

    @Property('QVariant', constant=True)
    def status(self):
        return self._status

    @Property('QVariant', constant=True)
    def report(self):
        return self._report