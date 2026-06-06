A customized port scanner/banner grabber written in Python.A custom port scanner/banner grabber in Python.

## Project Overview
This is an offensive security reconnaissance tool in the python programming language. It is used to scan a host for services that are running and listening on its ports and retrieve the application "banners" (softwares versions). Finding active ports and versions of installed applications is a vital first step of any penetration test or vulnerability assessment.

The following Cybersecurity skills were shown:
Active Reconnaissance: Insight into the way that network communication processes discovery mapping.
**Socket Programming:** Using Python's built-in socket library to manipulate network stacks uninterpreted.
Information Gathering (Banner Grabbing): To collect signature of software to find out the footprints of services for vulnerability analysis.

## How It Works
The script tries to connect to a list of high priority ports (FTP, SSH, HTTP, HTTPS) for a full connection using basic concepts of TCP handshakes (SOCK_STREAM). It includes custom error management for user canceling and network timeouts.

The tool can be run within Kali Linux as follows:
Make sure you have Python 3 installed. Run the script using the terminal:

```bash
python3 scanner.py
