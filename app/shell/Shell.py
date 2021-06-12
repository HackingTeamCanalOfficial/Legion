from abc import ABC, abstractmethod


class Shell(ABC):
    @abstractmethod
    def get_current_working_directory(self) -> str:
        pass

    @abstractmethod
    def remove_file(self, file_path: str) -> None:
        pass

    @abstractmethod
    def remove_directory(self, directory: str) -> None:
        pass

    @abstractmethod
    def create_temporary_directory(self, prefix: str, suffix: str, directory: str):
        pass

    @abstractmethod
    def create_directory_recursively(self, directory: str):
        pass

    @abstractmethod
    def create_named_temporary_file(self, prefix: str, suffix: str, directory: str, delete_on_close: bool):
        pass

    @abstractmethod
    def move(self, source: str, destination: str) -> None:
        pass

    @abstractmethod
    def copy(self, source: str, destination: str) -> None:
        pass

    @abstractmethod
    def isDirectory(self, name: str) -> bool:
        pass

    @abstractmethod
    def isFile(self, name: str) -> bool:
        pass

    @abstractmethod
    def directoryOrFileExists(self, path: str) -> bool:
        pass
