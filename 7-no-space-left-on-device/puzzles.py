from collections import namedtuple
from dataclasses import dataclass, field
from typing import Type

with open("input.txt") as f:
    commands = f.read().split("\n")


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Type['Directory'] = None
    directories: dict[str: Type['Directory']] = field(default_factory=dict)
    files: list[File] = field(default_factory=list)


class FileSystem:
    def __init__(self, command_output: list, total_disk_space: int) -> None:
        self.total_disk_space = total_disk_space
        self.root = Directory("/")
        self.current_working_directory = Directory
        for index, command in enumerate(command_output):
            if command.startswith("$ cd"):
                self.change_directory(command.split()[2])
            elif command.startswith("$ ls"):
                try:
                    idx = next(idx for idx, command in enumerate(command_output[index+1:]) if "$" in command)
                    self.directory_contents(command_output[index + 1:][:idx])
                except StopIteration:
                    self.directory_contents(command_output[index + 1:])
            else:
                pass

    def change_directory(self, argument: str) -> None:
        if argument == "/":
            self.current_working_directory = self.root
        elif argument == "..":
            self.current_working_directory = self.current_working_directory.parent
        else:
            try:
                self.current_working_directory.directories[argument]
            except KeyError:
                self.current_working_directory.directories[argument] = Directory(argument, self.current_working_directory)
            self.current_working_directory = self.current_working_directory.directories[argument]

    def directory_contents(self, contents: list) -> None:
        for content in contents:
            indicator, name = content.split()
            if "dir" in indicator:
                self.current_working_directory.directories[name] = Directory(name, self.current_working_directory)
            else:
                self.current_working_directory.files.append(File(name, int(indicator)))

    def directory_size(self, directory: Directory = None, directories: list[Directory] = None, contains: list = None) -> int:
        if directories is None:
            directories = [directory]
            contains = []
        if directory is None:
            directories = [self.root]
        for entry in directories:
            directories.extend(entry.directories.values())
            contains.append(directories.pop(0))
            self.directory_size(entry, directories=directories, contains=contains)
        files = []
        [files.extend(directory.files) for directory in contains]
        return sum(file.size for file in files)

    def directories(self, directories: list[Directory] = None, all_directories: list[Directory] = None) -> list[Directory]:
        if directories is None:
            directories = [self.root]
            all_directories = []
        for directory in directories:
            directories.extend(directory.directories.values())
            all_directories.append(directories.pop(0))
            self.directories(directories, all_directories)
        return all_directories


if __name__ == "__main__":
    file_system = FileSystem(commands, 70000000)
    DirectorySize = namedtuple("DirectorySize", "name size")
    directory_sizes = []

    for directory in file_system.directories():
        size = file_system.directory_size(directory)
        directory_sizes.append(DirectorySize(directory.name, size))

    print("puzzle 1:", sum([directory.size for directory in directory_sizes if directory.size <= 100000]))

    unused_space = file_system.total_disk_space - directory_sizes[0].size
    space_needed = 30000000 - unused_space

    directory_to_delete = DirectorySize(None, 70000000)
    for directory in directory_sizes:
        if space_needed < directory.size < directory_to_delete.size:
            directory_to_delete = DirectorySize(directory.name, directory.size)

    print("puzzle 2:", directory_to_delete.size)
