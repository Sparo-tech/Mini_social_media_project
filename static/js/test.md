const username= document.getElementById('username');




$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url:'',
            success:function(response){
                
            },
            error:function(response){
                console.log(response)
            }
        });
    },60000);
})





















//const likeBtn= $(`.like-btn${post_id}`);
const likeForm = document.getElementById('like-form');

$(document).ready(function() {

    $('.like-form').submit(function(e){
        e.preventDefault()
    

        url =  $(this).attr('action')
        post_id =  $(this).attr('id')

        $.ajax({
            type:'POST',
            url:url,
            data:{
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
                'post_id':post_id
            },
            success:function(response){
               
                //console.log(response.like_count)
                //likeBtn.innerText('ddd')
                const likeBtn= $(`.like-btn${post_id}`);
                //like-btn{{post.id}}
                console(likeBtn)
                like_icon = document.createElement('i')
                cls= ['far','fa-thumbs-up','text-primary']
                like_icon.classList.add(...cls)
               likeBtn.innerText = `${response.like_count}`
               likeBtn.appendChild(like_icon)
            }
        })

    })
})