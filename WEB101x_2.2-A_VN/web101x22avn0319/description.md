You can set a checkbox or radio button to be checked by default using the `checked` attribute.

To do this, just add the word `checked` to the inside of an `input` element. For example:

```html
<input type="radio" name="test-name" checked />
```

---

Set the first of your radio buttons and the first of your checkboxes to both be checked by default.

---

Bạn có thể thiết lập để checkbox hoặc nút radio nào đó được chọn theo mặc định bằng cách sử dụng thuộc tính `checked`.

Để làm vậy, bạn chỉ cần thêm `checked` vào bên trong phần tử `input`. Ví dụ:

```html
<input type="radio" name="test-name" checked />
```

---

Hãy thiết lập sao cho nút radio đầu tiên và checkbox đầu tiên là lựa chọn mặc định.

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
    <label for="indoor"
      ><input id="indoor" type="radio" name="indoor-outdoor" value="indoor" />
      Indoor</label
    >
    <label for="outdoor"
      ><input id="outdoor" type="radio" name="indoor-outdoor" value="outdoor" />
      Outdoor</label
    ><br />
    <label for="loving"
      ><input id="loving" type="checkbox" name="personality" value="loving" />
      Loving</label
    >
    <label for="lazy"
      ><input id="lazy" type="checkbox" name="personality" value="lazy" />
      Lazy</label
    >
    <label for="energetic"
      ><input
        id="energetic"
        type="checkbox"
        name="personality"
        value="energetic"
      />
      Energetic</label
    ><br />
    <input type="text" placeholder="cat photo URL" required />
    <button type="submit">Submit</button>
  </form>
</main>
```
