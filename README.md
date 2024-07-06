# File WatchDog

## Introduction

File WatchDog is a script designed to monitor changes in a specified directory and replicate those changes to another directory. It uses Python and requires Git for version control.

## Prerequisites

Before running this project, ensure you have the following installed on your computer:

- **Git**: Version control system.
- **Python**: Programming language (version 3.x recommended).

## Installation

1. **Clone the Project Repository**

   Open your terminal and clone the repository using the following command:

   ```sh
   git clone https://github.com/luisFelipeFreitas/fileWatchDog.git
   cd fileWatchDog
   ```

### Execution

    To execute the code, use the following command in your terminal:

    ```sh
   py watchdog.py interval_in_seconds original_folder_path replica_folder_path
   ```

### Parameters
    interval_in_seconds: The time interval in seconds at which the original folder is checked for changes.
    original_folder_path: The path to the original folder that you want to monitor.
    replica_folder_path: The path to the replica folder where changes will be mirrored.