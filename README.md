# prog04
#run!

#httpget.py
python3 httpget.py --url http://blogtest.vnprogramming.com/
---

#httppost.py
python3 httppost.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@AD
python3 httppost.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@ADtrag
----

#httpupload.py
python3 httpupload.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@AD --localfile /home/trang/Desktop/challenge04/anh1.png
-----

#httpdownload.py
python3 httpdownload.py --url http://blogtest.vnprogramming.com/ --remotefile /wp-content/uploads/2022/02/anh1-2.jpg

 
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
    		
i = 8
if url[0:7] == "http://":
	i = 7
get_url = url[i:(len(url)-1)]
print(get_url)

#httpget.py python3 httpget.py --url http://blogtest.vnprogramming.com/
#httppost.py 

python3 httppost.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@AD 

python3 httppost.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@ADtrag
#httpupload.py 
python3 httpupload.py --url http://blogtest.vnprogramming.com/ --user test --password test123QWE@AD --localfile /home/tragserver/Desktop/code/challenge4/anh1.png
#httpdownload.py python3 httpdownload.py --url http://blogtest.vnprogramming.com/ --remotefile /wp-content/uploads/2022/02/anh1-2.jpg


request_file = "------WebKitFormBoundary" + "\r\n" + \
	+ 'Content-Disposition: form-data; name="name"' + "\r\n\r\n" + filename + "\r\n"+"------WebKitFormBoundary\r\n" + \
        + 'Content-Disposition: form-data; name="action"' + "\r\n\r\n" + "upload-attachment"+"\r\n"+"------WebKitFormBoundary"+"\r\n" + \
        + 'Content-Disposition: form-data; name="_wpnonce"' + "\r\n\r\n" + res.encode() + "\r\n"+"------WebKitFormBoundary" + "\r\n" + \
        + 'Content-Disposition: form-data; name="async-upload"; filename="' + filename.encode() + '"\r\nContent-Type: image/' + filetype.encode() + \
        + filetype.encode() + "\r\n\r\n" + file_img + "\r\n" + "------WebKitFormBoundary--"
