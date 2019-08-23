## Biến trong Python

### Biến là gì ? (Variable)
- Biến không có giá trị cụ thể.
- Là một vùng trong bộ nhớ RAM được sử dụng để lưu trữ thông tin.
- Biến giúp lưu trữ dữ liệu và dùng dữ liệu từ chúng để tính toán được thuận tiện và chính xác hơn.
- *Lưu ý* : 	
	- Biến trong Python có phân biệt hoa thường.
	- Tên biến không được bắt đầu bằng số
	- Tên biến không được trùng với 1 số từ khóa của python :
	```
	and	del	from	not	while	as	elif	global	or	
	with	assert	else	if	pass	yield	break	
	except	import	print	class	exec	in	raise	
	continue	finally	is	return	def	for	lambda	try
	```

### Khởi tạo biến
- Cú pháp : `<tên biến> = <giá trị biến>`
	![Imgur](https://i.imgur.com/56WXNOE.png)
- Khởi tạo nhiều biến trên cùng 1 dòng :
		- cú pháp : `<tên biến thứ nhất>, <tên biến thứ hai>,... <tên biến thứ n> = <giá trị biến 1>, <giá trị biến 2>,... <giá trị biến n>`
		- cách nhau bằng dấu phẩy, vị trị giá trị biến và biến tương ứng nhau.
		![Imgur](https://i.imgur.com/1TAEMIS.png)

### Kiểm tra kiểu dữ liệu của biến
- Trong Python, việc khai báo kiểu dữ liệu cho biến không cần thiết mà Python sẽ tự biết kiểu dữ liệu của giá trị gán cho biến.
- Để kiểm tra kiểu dữ liệu của biến ta dùng hàm `type()`
- Cú pháp : `type(<tên biến>)`
	![Imgur](https://i.imgur.com/bac8UKA.png)
![Imgur](https://i.imgur.com/VN9P5Sd.png)
