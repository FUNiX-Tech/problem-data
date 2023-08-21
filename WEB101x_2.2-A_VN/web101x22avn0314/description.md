Let's add a `submit` button to your form. Clicking this button will send the data from your form to the URL you specified with your form's `action` attribute.

Here's an example submit button:

```html
<button type="submit">this button submits the form</button>
```

Add a button as the last element of your `form` element with a type of `submit`, and `Submit` as its text.

---

Hãy thêm một nút `submit` vào biểu mẫu của bạn. Khi nhấn nút này, dữ liệu từ biểu mẫu sẽ được gửi đến URL được chỉ định trong thuộc tính `action` của biểu mẫu.

Dưới đây là ví dụ nút submit:

```html
<button type="submit">this button submits the form</button>
```

Hãy thêm một nút làm phần tử cuối cùng trong phần tử `form`. Nút này phải có kiểu `submit`, với nội dung nút là `Submit` (Gửi đi).

---

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
  </form>
</main>
```
