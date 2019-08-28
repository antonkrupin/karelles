/*кнопки для открытия формы*/
var button = document.querySelectorAll('.button');
/* пункты вопросов и ответов */
var question = document.querySelectorAll('.question');
var answer = document.querySelectorAll('.question_answer');
/* получение блока формы */
var form = document.querySelector('.form');
/* получение кнопки для закрытия формы */
var from_close_button = document.querySelector('.form span');
/*кнопка отправки дынных формы */
var send_button = document.querySelector('#send_data');

/* получение картинок примеров материалов дз */
var examples_img = document.querySelectorAll('.fourth_block__img .img img');
var examples_img_popup = document.querySelector('.examples_big')
var ex_img = document.querySelector('.examples_big__img');


for(i=0;i<examples_img.length;i++){
    examples_img[i].onclick = function(){
        var img_coord = Math.round(getCoords(this));
        var top_coord = $(this).offset().top;
        $('body, html').animate({scrollTop: top_coord - 100}, 1000);
        examples_img_popup.style.top = img_coord - 100 + 'px';
        var src_path = this.getAttribute("src");
        var img = ex_img.querySelector("img");
        img.setAttribute("src",src_path);
        examples_img_popup.style.display = "block";
    };
}
/* закрытие окна с большим изображением диплома */
if (examples_img_popup != null){
    examples_img_popup.onclick = function(){
        examples_img_popup.style.display = "none";
    };
}


/* функция получения координат */
function getCoords(elem){
    var box = elem.getBoundingClientRect();
    var res = 0;
    return res = box.top + pageYOffset - 100;
}

send_button.onclick = function(){
    console.log("test");
}

/*блок вопросов и ответов */
for(i=0;i<question.length;i++){
    question[i].onclick = function(){
        this.childNodes[3].classList.toggle("active");
        this.childNodes[1].classList.toggle("active_title");
    }
}

/* закрытие формы */
from_close_button.onclick = function(){
    $(form).fadeOut(400);
};

/* открытие формы при нажатии на кнопку */
for(var i = 0; i < button.length; i++){
    button[i].onclick = function(){
        var form_coord = Math.round(getCoords(this));
        var top_coord = $(this).offset().top;
        $('body, html').animate({scrollTop: top_coord - 400}, 1000);
        form.style.top = form_coord + 'px';
        form.style.display = "block";
    };
}
