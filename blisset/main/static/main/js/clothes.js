let slider1 = new Swiper('.slider_1', {
    spaceBetween: 10,
    // freeMode: true,
    slidesPerView: 2,
    watchSlidesProgress: true,
    direction: "vertical",
    speed: 1000,
    loop: true,
    autoplay: {
        delay: 5000,
    },
});

let slider2 = new Swiper('.slider_2', {
    thumbs: {
        swiper: slider1,
    },
    effect: 'fade',
    pagination: {
        el: ".swiper-pagination",
    },
    allowTouchMove: false,
})
const slider2_obj = document.querySelector('.slider_2');

function zoomImg(obj) {
    const img = obj.querySelector('.slider2_img_img');

    slider2_obj.addEventListener("mousemove", onZoom);
    slider2_obj.addEventListener("mouseover", onZoom);
    slider2_obj.addEventListener("mouseleave", offZoom);

    function onZoom(e) {
        const x = e.clientX - obj.getBoundingClientRect().x;
        const y = e.clientY - obj.getBoundingClientRect().y;
        img.style.transformOrigin = `${x}px ${y}px`;
        img.style.transform = "scale(2.5)";
    }

    function offZoom(e) {
        img.style.transformOrigin = `center center`;
        img.style.transform = "scale(1)";
    }
}

objects = document.getElementsByClassName('slider2_photo');

for (let obj of objects) {
    zoomImg(obj);
    // console.log(obj.querySelector('#slider2_img_img'));
}

let mobileSlider = new Swiper('.mobile_slider', {
    effect: 'fade',
    pagination: {
        el: ".swiper-pagination",
    },
    allowTouchMove: true,
})