Author

M. Sankaranarayanan

Project Description

JioTV Log Harvester is a Python based log collection system that gathers log messages from multiple JioTV services through TCP socket communication. The application stores logs in separate binary files and allows users to read them later. This project demonstrates networking, multithreading, binary file handling, and data storage using Python.

Features

Collect logs from multiple JioTV servers

Receive logs through TCP socket communication

Handle multiple client connections

Store logs in binary files

Read and display stored logs

Simple and easy Python implementation

Technologies Used

Python

Socket Programming

Multithreading

Pickle

Binary File Handling

Project Files

server.py

har.py

readbinary.py

LoginServer.bin

StreamingServer.bin

RecommendationServer.bin

DatabaseServer.bin

CDNServer.bin

Working

The client sends JioTV service logs through a TCP connection.

The Log Harvester receives each log message.

Logs are separated based on the server name.

Each server stores its logs in a separate binary file.

The readbinary program displays all stored logs.

Learning Outcomes

Learn TCP socket programming

Understand multithreading

Work with binary files

Use the Pickle module

Manage logs from multiple services

Future Improvements

Add database storage

Create a graphical user interface

Generate log reports

Support real time log monitoring

Add log filtering options

Conclusion

This project demonstrates a simple centralized JioTV log collection system using Python. It helps in understanding socket programming, multithreading, and binary file handling while collecting and managing logs from multiple simulated JioTV services.
