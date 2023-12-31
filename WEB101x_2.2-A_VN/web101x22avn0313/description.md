You can build web forms that actually submit data to a server using nothing more than pure HTML. You can do this by specifying an `action` attribute on your `form` element.

For example:

```html
<form action="url-where-you-want-to-submit-form-data">
  <input />
</form>
```

Nest the existing `input` element inside a `form` element and assign `"https://www.freecatphotoapp.com/submit-cat-photo"` to the `action` attribute of the `form` element.

---

Bạn có thể tạo các biểu mẫu web để có thể gửi dữ liệu cho một server chỉ với HTML. Để làm vậy, bạn có thể chỉ định một thuộc tính `action` trong phần tử `form`.

Ví dụ:

```html
<form action="url-where-you-want-to-submit-form-data">
  <input />
</form>
```

Hãy lồng phần tử `input` vào trong một phần tử `form` và gán `"https://www.freecatphotoapp.com/submit-cat-photo"` cho thuộc tính `action` trong phần tử `form` đó.

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
  <input type="text" placeholder="cat photo URL" />
</main>
```
