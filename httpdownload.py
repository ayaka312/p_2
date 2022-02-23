import socket, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--remotefile")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
filepath = args.remotefile
image_name = filepath.split("/"[-1])
get_url = ""
i = 8
if url[0:7] == "http://":
    i = 7
get_url += url[i:(len(url)-1)]
s.connect((get_url, 80))

request = "GET " + filepath + " HTTP/1.1\r\nHost: " + get_url + "\r\n\r\n"
s.send(request.encode())
response = bytearray()
while True:
	respons = s.recv(2048)
	if not respons:
		break
	response += respons
	
response.decode("utf8")
s.close()
if "HTTP/1.1 200 OK" in response:
    image_len = ""
    image_len_start = response.find("Content-Length: ")
    for j in range(image_len_start + 16, len(response)):
        if chr(response[j].isdigit == True):
            image_len += response[j]
        else:
            break
    print("Kich thuoc file anh: " + image_len.decode() + "bytes")
    image_type = response.split("\r\n\r\n")[-1]
    image_url = "/home/trang/Desktop/challenge04/" + image_name
    open(image_url, "wb").write(image_type)
else:
    print("Khong ton tai file anh")
    exit(0)
