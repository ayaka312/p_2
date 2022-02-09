import socket
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--remotefile")
args = parser.parse_args()


def recvall(s):
    total_data = []
    response = s.recv(4096)
    while (len(response) > 0):
        total_data.append(response)
        response = s.recv(4096)
    response = b''.join(total_data)
    return response


def getDomain(url):
    domain = ""
    if url[0:8] == "https://":
        for i in range(8, len(url)):
            if url[i] == '/':
                break
            domain += url[i]
    if url[0:7] == "http://":
        for i in range(7, len(url)):
            if url[i] == '/':
                break
            domain += url[i]
    return domain


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
pathFile = args.remotefile
domain = getDomain(url)
client.connect((domain, 80))
request = "GET "+pathFile+" HTTP/1.1\r\n"+"Host: "+domain+"\r\n"+"\r\n"
client.send(request.encode())
response = recvall(client)
len_image = b""
if b"HTTP/1.1 200 OK" in response:
    for i in range(0, len(response)):
        if len_image != b"":
            break
        if response[i:i+16] == b"Content-Length: ":
            for j in range(i+16, len(response)):
                if(not chr(response[j]).isdigit()):
                    len_image = response[i+16:j]
                    break
else:
    print("Khong ton tai file anh.")
    exit(0)
print("Kich thuoc file anh: "+len_image.decode()+" bytes")
content_file = response.split(b"\r\n\r\n")[1]
fileName = pathFile.split('/')[-1]
location = "/home/trang/Desktop/challenge04/"+fileName
open(location, "wb").write(content_file)
