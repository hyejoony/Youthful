import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from './account'
import { useRouter } from 'vue-router'

export const UseCommunityStore = defineStore('community', () => {
  const storeAccount = useAccountStore()
  const router = useRouter()
  
  const API_URL = storeAccount.API_URL
  const token = storeAccount.token

  // 게시글 리스트
  const ArticleList = ref([])


  // 키워드를 버튼으로
  const buttons = ref([
    { caption: '적금' },
    { caption: '예금' },
    { caption: '지원금' },
    { caption: '기타' }
  ]);


  // ----- 생성 페이지 -----

  // - 인자로 받기
  const SaveArticle = (payload) => {
    console.log(payload)
    const formData = new FormData()
    formData.append('title', payload.inputTitle);
    formData.append('keyword', payload.selectedButton);
    formData.append('content', payload.inputContent);
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/communities/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: formData
    })
    .then(res => {
      console.log('저장 완료')
      router.push({ name: 'community' })
    })
    .catch(err => {
      console.log(err.response.data)
    })
  }

  // ----- 단일조회 -----
  // 객체 반환
  const getDetail = (id) => {
    const detail = ArticleList.value.find((element) => element.id == id)
    return detail
  }

  // ----- 수정페이지 -----

  // 데이터 저장
  const saveUpdateChanges = (id, editTitle, editContent, editedButton) => {

    // console.log(ArticleList)
    console.log('id', Number(id))
    console.log(ArticleList.value)

    const index = ArticleList.value.findIndex((article) => (article.id) == Number(id))
    console.log('index', index)
    //해당 index의 article 객체의 속성 

    if (index !== -1) {
      // 해당 index의 article 객체의 속성 직접 수정
      ArticleList.value[index].title = editTitle.value;
      ArticleList.value[index].content = editContent.value;
      ArticleList.value[index].keyword = editedButton.value;
      return true
    }

    return false
  }


  // ---- 삭제 페이지 -----
  const deleteArticle = (id) => {
    const index = ArticleList.value.findIndex((article) => (article.id) === id)
    ArticleList.value.splice(index, 1)

  }


  // ---- 댓글 저장 -----
  let idx = 0
  const saveComment = (id, comment) => {
    const article = ArticleList.value.find(element => element.id == id)
    console.log('article', article)
    console.log('id',id)
    console.log('comment', comment.value)
    if (article) {
      article.comments.push({
        commentId: idx++,  // 유니크한 ID 생성
        content: comment.value,
        // userEmail: userEmail,
        createdAt: new Date().toISOString()
      })
      console.log(article.comments)
      return true
    }
  }


  // 댓글 조회 함수
  const getComments = (id) => {
    const article = ArticleList.value.find(article => article.id == id)
    return article ? article.comments : []
  }

   // -----  댓글 수정-----

  // 데이터 저장
  const UpdateComment = (id, commentId) => {
    const index = ArticleList.value.findIndex((article) => (article.id) == Number(id))
    console.log(commentId)
    console.log((ArticleList.value)[index].comments)
    if (index !== -1) {
      // 해당 index의 article 객체의 속성 직접 수정
      const comment_index = (ArticleList.value)[index].comments.findIndex((comment) => (comment.commentId) == Number(commentId)) 
      console.log(comment_index)
      if (comment_index !== -1) {
        return true
      }
    }
  }


    // ----- 데이터 test- reset 함수 -----
    const resetArticle = () => {
      ArticleList.value = []
    }

    

  return {
    buttons, saveUpdateChanges, saveComment, getComments, UpdateComment,
    SaveArticle, ArticleList, deleteArticle, getDetail, resetArticle
  }
}, { persist: true })
