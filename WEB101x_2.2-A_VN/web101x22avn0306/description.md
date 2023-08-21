You can make elements into links by nesting them within an `a` element.

Nest your image within an `a` element. Here's an example:

```html
<a href="#"
  ><img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="Three kittens running towards the camera."
/></a>
```

Remember to use `#` as your `a` element's `href` property in order to turn it into a dead link.

---

Place the existing image element within an `a` (_anchor_) element.

Once you've done this, hover over your image with your cursor. Your cursor's normal pointer should become the link clicking pointer. The photo is now a link.

---

Bạn có thể thay đổi các phần tử thành các liên kết bằng cách lồng chúng vào một phần tử `a`.

Lồng hình ảnh của bạn trong một phần tử `a`. Đây là một ví dụ:

```html
<a href="#"
  ><img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="Three kittens running towards the camera."
/></a>
```

Hãy nhớ sử dụng `#` làm thuộc tính `href` của phần tử `a` để biến nó thành một dead link.

---

Đặt phần tử hình ảnh hiện có trong phần tử `a`(_anchor_).

Khi bạn đã hoàn thành việc này, hãy di chuột qua hình ảnh. Con trỏ sẽ trở thành con trỏ nhấp vào liên kết. Bức ảnh bây giờ là một liên kết.

```html
<h2>CatPhotoApp</h2>
<main>
  <p>Click here to view more <a href="#">cat photos</a>.</p>

  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  />

  <p>
    Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching
    attack your ankles chase the red dot, hairball run catnip eat the grass
    sniff.
  </p>
  <p>
    Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere
    rip the couch sleep in the sink fluffy fur catnip scratched.
  </p>
</main>
```
