from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process_data(self) -> None:
        self.read_data()
        self.process_data_specifics()
        self.write_data()

    def read_data(self) -> None:
        print("Reading data")

    @abstractmethod
    def process_data_specifics(self) -> None:
        pass

    def write_data(self) -> None:
        print("Writing data")


class CSVDataProcessor(DataProcessor):
    def process_data_specifics(self) -> None:
        print("Processing data as CSV")


class JSONDataProcessor(DataProcessor):
    def process_data_specifics(self) -> None:
        print("Processing data as JSON")


if __name__ == "__main__":
    csv_processor = CSVDataProcessor()
    json_processor = JSONDataProcessor()

    print("CSV Data Processor:")
    csv_processor.process_data()

    print("\nJSON Data Processor:")
    json_processor.process_data()
