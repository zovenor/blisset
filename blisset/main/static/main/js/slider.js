let slider = new Swiper('.slider__container', {
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 5000,
    },
    speed: 1000,
    loop: true,
    parallax: true,
});

let page2_descs = ['готовь подарки для любимых', 'беспроигрышный подарок']
let page2_buttons = ['']

let slider1__page2 = new Swiper('.slider1__page2', {
    speed: 1000,
    loop: true,
    autoplay: {
        delay: 5000,
    },
    parallax: true,
    grabCursor: true,
    effect: "creative",
    allowTouchMove: false,
    creativeEffect: {
        prev: {
            shadow: true,
            translate: ["-20%", 0, -1],
        },
        next: {
            translate: ["100%", 0, 0],
        },
    },
});

let slider2__page2 = new Swiper('.slider2__page2', {
    speed: 1000,
    loop: true,
    parallax: true,
    grabCursor: true,
    allowTouchMove: false,
    effect: "creative",
    creativeEffect: {
        prev: {
            shadow: true,
            translate: ["-20%", 0, -1],
        },
        next: {
            translate: ["80%", 0, 0],
        },
    },

});

let page2_button_slider = new Swiper('.page2_button_slider', {
    loop: true,
    parallax: true,
    effect: 'fade',
    allowTouchMove: false,
    fadeEffect: {
        crossFade: true
    },
})
let page2_title = new Swiper('.page2-title', {
    loop: true,
    parallax: true,
    effect: 'fade',
    allowTouchMove: false,
    fadeEffect: {
        crossFade: true
    },
});
let page2_desc = new Swiper('.page2_desc', {
    loop: true,
    parallax: true,
    allowTouchMove: false,
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
})
let page2_text2 = new Swiper('.page2-text2', {
    loop: true,
    parallax: true,
    allowTouchMove: false,
    effect: 'fade',
    fadeEffect: {
        crossFade: true
    },
})

slider1__page2.controller.control = slider2__page2;
slider2__page2.controller.control = page2_button_slider;
page2_button_slider.controller.control = page2_title;
page2_title.controller.control = page2_desc;
page2_desc.controller.control = page2_text2;
