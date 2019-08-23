## Kiểu dữ liệu số trong Python
- **Số nguyên** : bao gồm các số nguyên dương (1,2,3...), các số nguyên âm (-1,-2,-3,...) và số 0. Kiểu dữ liệu số nguyên trong Python là vô hạn.
	![Imgur](https://i.imgur.com/YYqqPCu.png)

- **Số thực** : bao gồm tập hợp các số nguyên và số thập phân.
	- **Lưu ý:** Thường khi chúng ta viết số thực, phần nguyên và phần thập phân được tách nhau bởi dấu phẩy ( , ). Thế nhưng trong Python, dấu phẩy ( , ) này được thay thế thành dấu chấm ( . )
	- ví dụ : gán cho biến b có giá trị 5.1 và xuất ra kiểu dữ liệu của b :
			![Imgur](https://i.imgur.com/ndpKUvx.png)
	- Số thực trong Python có độ chính xác xấp xỉ 15 chữ số thập phân.
	- ví dụ 10/3 :
		![Imgur](https://i.imgur.com/w2YZKrL.png)

	- Muốn có kết quả có độ chính xác cao hơn thì nên sử dụng `Decimal`
	![Imgur](https://i.imgur.com/Mb69Nvj.png)

- **Phân số** : Để tạo phân số trong python ta dùng hàm Fraction với cú pháp : `Fraction(<tử số>,<mẫu số>)`

	- Ví dụ : 
		![Imgur](https://i.imgur.com/OR1QNlp.png)

- **Các toán tử cơ bản với kiểu dữ liệu số trong python**
	- Một thực thể toán học thường có 2 thành phần :
	
		- **Toán hạng :** có thể là một hằng số, biến số (X, Y)
		- **Toán tử :** xác định cách thức làm việc giữa các toán hạng (+,-,*,/)

	- Dưới đây là một số biểu thức toán học của kiểu dữ liệu số trong python :
		![Imgur](https://i.imgur.com/fVbfPs6.png)
