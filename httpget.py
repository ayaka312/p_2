import socket, html, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = args.url
i = 8
if url[0:7] == "http://":
	i = 7
get_url += url[i:(len(url)-1)]
print(get_url)
s.connect((get_url, 80))
request = "GET / HTTP/1.1\r\nHost: "+get_url+"\r\n\r\n"
s.send(request.encode())

response = s.recv(2048)
s.close()
response = response.decode("utf8")
title_start = response.find("<title>")
title_end = response.find("</title>")

print("Title: ", html.unescape(response[title_start+7:title_end]))
