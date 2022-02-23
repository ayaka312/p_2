import socket, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--remotefile")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
filepath = args.remotefile
image_name = filepath.split("/")[-1]
get_url = ""
i = 8
if url[0:7] == "http://":
    i = 7
get_url += url[i:(len(url)-1)]
s.connect((get_url, 80))

request = "GET " + filepath + " HTTP/1.1\r\nHost: " + get_url + "\r\n\r\n"
s.send(request.encode())
response =  b''
while True:
	respons = s.recv(2048)
	if not respons:
		break
	response += respons
s.close()
response = response.decode('iso-8859-1')
if "HTTP/1.1 200 OK" in response:
    image_len = len(response.split('\r\n\r\n')[1].encode('iso-8859-1'))
    print("Kich thuoc file anh: " + str(image_len) + " bytes")
    image_type = response.split("\r\n\r\n")[-1]
    image_url =  image_name
    open(image_url, "wb").write(image_type.encode('iso-8859-1'))
else:
    print("Khong ton tai file anh")
    exit(0)
