#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pybrain.datasets import ClassificationDataSet

import os

class ImagesDatasetGenerator:
    def __init__(self, input_size, nb_classes, classes_labels):
        self.dataset = ClassificationDataSet(input_size, nb_classes, classes_labels)

        self.folders = {}
        self.filters= {}
        self.classes_labels = classes_labels

    def getClassesLabels(self):
        return self.classes_labels

    def getDataset(self):
        return self.dataset

    def getFolders(self):
        return self.folders

    def getFilters(self, class_label=False):
        if class_label:
            self.validateClassLabel(class_label)
            return self.filters[class_label]
        else:
            return self.filters

    def setFilters(self, class_label, filter_list):
        self.validateClassLabel(class_label)
        self.filters[class_label] = filter_list

    def validateClassLabel(self, class_label):
        if not class_label in self.classes_labels:
            raise LookupError("class label %s not found [%s]" % (class_label, ",".join(self.classes_labels)))

    def addFolder(self, path, class_label):
        self.validateClassLabel(class_label)

        if not class_label in self.folders:
            self.folders[class_label] = []
            self.filters[class_label] = []

        if not os.access(path, os.F_OK):
            raise IOError("unreadable path: %s" % (path) )

        if not path in self.folders[class_label]:
            self.folders[class_label].append(path)



