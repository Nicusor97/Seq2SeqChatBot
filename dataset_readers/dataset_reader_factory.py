"""
Dataset reader implementation factory
"""
from os import path
from dataset_readers.cornell_dataset_reader import CornellDatasetReader
from dataset_readers.csv_dataset_reader import CSVDatasetReader
from dataset_readers.dailydialog_dataset_reader import DailyDialogDatasetReader


def get_dataset_reader(dataset_dir):
    """Gets the appropriate reader implementation for the specified dataset name.

    Args:
        dataset_dir: The directory of the dataset to get a reader implementation for.
    """
    dataset_name = path.basename(dataset_dir)

    # When adding support for new datasets, add an instance of their reader class to the reader array below.
    #readers = [CornellDatasetReader(), CSVDatasetReader(), DailyDialogDatasetReader()]

    self.set_cornell_dataset_reader(dataset_name)
    self.set_csv_dataset_reader(dataset_name)
    self.set_dialog_dataset_reader(dataset_name)

    raise ValueError("There is no dataset reader implementation for '{0}'. If this is a new dataset, please add one!".format(dataset_name))

def set_cornell_dataset_reader(dataset_name):
    """
    When adding support for new datasets, add an instance of their reader class to the reader array below.
    """
    if dataset_name == CornellDatasetReader():
        return CornellDatasetReader()

def set_csv_dataset_reader(dataset_name):
    """
    When adding support for new datasets, add an instance of their reader class to the reader array below.
    """
    if dataset_name == CSVDatasetReader():
        return CornellDatasetReader()

def set_dialog_dataset_reader(dataset_name):
    """
    When adding support for new datasets, add an instance of their reader class to the reader array below.
    """
    if dataset_name == DailyDialogDatasetReader():
        return DailyDialogDatasetReader()