import socket, html, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--user")
parser.add_argument("--password")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
user = args.user
password = args.password
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
if "HTTP/1.1 302 Found" in response and "login_error" not in response:
	print("User " + user + " dang nhap thanh cong")
else:
	print("User " + user + " dang nhap that bai")
