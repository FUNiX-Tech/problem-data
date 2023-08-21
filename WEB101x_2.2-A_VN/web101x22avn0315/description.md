You can require specific form fields so that your user will not be able to submit your form until he or she has filled them out.

For example, if you wanted to make a text input field required, you can just add the attribute `required` within your `input` element, like this: `<input type="text" required>`

---

Make your text `input` a `required` field, so that your user can't submit the form without completing this field.

Then try to submit the form without inputting any text. See how your HTML5 form notifies you that the field is required?

---

Bạn có thể thiết lập các trường biểu mẫu cụ thể thành bắt buộc để người dùng không thể gửi biểu mẫu đi nếu chưa điền vào những trường bắt buộc đó.

Ví dụ, nếu muốn làm cho trường `input` văn bản trở thành bắt buộc, bạn chỉ cần thêm thuộc tính `required` (bắt buộc) bên trong phần tử `input` như sau: `<input type="text" required>`

---

Hãy làm cho `input` văn bản của bạn trở thành một trường `required` (bắt buộc) để người dùng không thể gửi biểu mẫu đi nếu chưa điền vào trường đó.

Sau đó, hãy thử gửi biểu mẫu khi chưa nhập bất kỳ văn bản nào vào trường đó. HTML5 sẽ hiện thông báo yêu cầu bạn phải điền vào trường đó.

```html
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <a href="#"
    ><img
      src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
      alt="A cute orange cat lying on its back."
  /></a>

  <p>Things cats love:</p>
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>
  <p>Top 3 things cats hate:</p>
  <ol>
    <li>flea treatment</li>
    <li>thunder</li>
    <li>other cats</li>
  </ol>
  <form action="https://www.freecatphotoapp.com/submit-cat-photo">
    <input type="text" placeholder="cat photo URL" />
    <button type="submit">Submit</button>
  </form>
</main>
```
