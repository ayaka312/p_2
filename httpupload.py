import socket, html, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--user")
parser.add_argument("--password")
parser.add_argument("--localfile")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
user = args.user
password = args.password
filepath = args.localfile
request_body = "log=" + user + "&pwd=" + password + "&wp-submit=Log+In"
get_url = ""
i = 8
if url[0:7] == "http://":
	i = 7
get_url += url[i:(len(url)-1)]
s.connect((get_url, 80))
request = "POST /wp-login.php HTTP/1.1\r\nHost: " + get_url + "\r\n"
request += "Content-Length: " + str(len(request_body)) + "\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request += "\r\n" + request_body

s.send(request.encode())

response = s.recv(2048)
s.close()
response = response.decode("utf8")
cookie = ""
if "HTTP/1.1 302 Found" not in response and "login_error" in response:
	print("Upload failed")
	exit(0)
for i in response.split("\r\n"):
	if "Set-Cookie:" in i:
		cookie += " " + i.split(" ")[1] 
request_cookie = "GET /wp-admin/media-new.php HTTP/1.1\r\nHost: " + get_url + "\r\n" + "Cookie:" + cookie + "\r\n\r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((get_url, 80))
s.send(request_cookie.encode())
response_cookie = s.recv(2048)
response_cookie = response_cookie.decode("utf8")
response_cookie_index = response_cookie.find("\"_wpnonce\":\"")
res = response_cookie[response_cookie_index+ 12:response_cookie_index + 22]
filename = filepath.split("/")[-1]
filetype = filename.split(".")[-1]
file_img = open(filepath, 'rb').read()   
request_file = "------WebKitFormBoundary"+"\r\n" + \
	"Content-Disposition: form-data; name=\"name\"" + "\r\n\r\n"+filename+"\r\n"+"------WebKitFormBoundary"+"\r\n" + \
	"Content-Disposition: form-data; name=\"action\"" + "\r\n\r\n" + "upload-attachment"+"\r\n" + "------WebKitFormBoundary" + "\r\n" + \
	"Content-Disposition: form-data; name=\"_wpnonce\""+"\r\n\r\n"+res+"\r\n"+"------WebKitFormBoundary" + "\r\n" + \
	"Content-Disposition: form-data; name=\"async-upload\"; filename=\"" + filename + "\""+"\r\n" + \
	"Content-Type: image/"+filetype+"\r\n\r\n"
request_file = request_file.encode() + file_img + b"\r\n" + b"------WebKitFormBoundary--"
request = "POST /wp-admin/async-upload.php HTTP/1.1\r\n"+"Host: " + get_url + "\r\n" 
request += 'Cookie:' + cookie + '\r\n'
request += "Content-Length: " + str(len(request_file)) + "\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request = request.encode() + request_file   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((get_url, 80))
s.send(request)
response_upfile = s.recv(2048)
response_upfile = response_upfile.decode("utf8")
s.close()
if "HTTP/1.1 200 OK" in response_upfile:
	print("Upload success\r\nFile upload url: ")
	response_upfile_start = response_upfile.find("\"url\":\"") 
	url_upload = ""
	for j in range(response_upfile_start + 7, len(response_upfile)):
		if(response_upfile[j] == "\"":
			break
		url_upload += response_upfile[j]
		url_upload.replace("\\", "")
	print(url_upload)
else:
	print("Upload failed")
	exit(0)
