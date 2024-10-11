const commentForm = document.forms.commentForm;
const commentFormContent = commentForm.content;
const commentFormParentInput = commentForm.parent;
const commentFormSubmit = commentForm.commentSubmit;
const commentPostId = commentForm.getAttribute('data-post-id');

commentForm.addEventListener('submit', createComment);

replyUser()

function replyUser() {
  document.querySelectorAll('.btn-reply').forEach(e => {
    e.addEventListener('click', replyComment);
  });
}

function replyComment() {
  const commentUsername = this.getAttribute('data-comment-username');
  const commentMessageId = this.getAttribute('data-comment-id');
  commentFormContent.value = `${commentUsername}, `;
  commentFormParentInput.value = commentMessageId;
}
async function createComment(event) {
    event.preventDefault();
    commentFormSubmit.disabled = true;
    commentFormSubmit.innerText = "Ожидаем ответа сервера";
    try {
        const response = await fetch(`/post/${commentPostId}/comments/create/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: new FormData(commentForm),
        });
        const comment = await response.json();

        let commentTemplate = `<ul id="comment-thread-${comment.id}">
                                <li class="card border-0">
                                    <div class="row">
                                        <div class="col-md-2">
                                            <img src="${comment.avatar}" style="width: 100px;height: 100px;object-fit: cover;" alt="${comment.author}"/>
                                        </div>
                                        <div class="col-md-10">
                                            <div class="card-body">
                                                <h6 class="card-title">
                                                    <a href="${comment.get_absolute_url}">${comment.author}</a>
                                                </h6>
                                                <p class="card-text">
                                                    ${comment.content}
                                                </p>
                                                <a class="btn btn-sm btn-dark btn-reply" href="#commentForm" data-comment-id="${comment.id}" data-comment-username="${comment.author}">Ответить</a>
                                                <hr/>
                                                <time>${comment.time_create}</time>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                            </ul>`;
        if (comment.is_child) {
            document.querySelector(`#comment-thread-${comment.parent_id}`).insertAdjacentHTML("beforeend", commentTemplate);
        }
        else {
            document.querySelector('.nested-comments').insertAdjacentHTML("beforeend", commentTemplate)
        }
        commentForm.reset()
        commentFormSubmit.disabled = false;
        commentFormSubmit.innerText = "Добавить комментарий";
        commentFormParentInput.value = null;
        replyUser();
    }
    catch (error) {
        console.log(error)
    }
}