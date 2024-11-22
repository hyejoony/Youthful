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
    console.log('idStore', id)
    const detail = ArticleList.value.find((element) => element.id == id)
    console.log(detail)
    return detail
  }

  // ----- 수정페이지 -----

  // 데이터 저장
  const saveUpdateChanges = (payload) => {

    console.log(payload)
    const id = payload.id
    const formData = new FormData()
    formData.append('title', payload.editTitle);
    formData.append('keyword', payload.editedButton);
    formData.append('content', payload.editContent);
    return axios({
      method: 'put',
      url: `${API_URL}/api/v1/communities/${id}/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: formData
    })
    .then(res => {
      console.log('수정 완료')
      return true
    })
    .catch(err => {
      console.log(err.response.data)
      return false
    })
  }


  // ---- 삭제 페이지 -----
  const deleteArticle = (id) => {
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/communities/${id}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {
      console.log('게시글 삭제 완료')
    })
    .catch(err => {
      console.log(err.response.data)
    })

  }


  // ---- 댓글 저장 -----
  const saveComment = (payload) => {
    console.log(payload)
    const id = payload.id
    const formData = new FormData()
    formData.append('content', payload.inputComment);
    return axios({
      method: 'post',
      url: `${API_URL}/api/v1/communities/${id}/comments/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: formData
    })
    .then(res => {
      console.log('댓글 저장 완료')
      return res.data
    })
    .catch(err => {
      console.log(err.response.data)
    })
  }


  // 댓글 조회 함수
  const getComments = (id) => {
    const article = ArticleList.value.find(article => article.id == id)
    return article ? article.comments : []
  }

   // -----  댓글 수정-----

  // 데이터 저장
  const saveUpdateChangesComment = (payload) => {
    console.log(payload)
    const articleId = payload.articleId
    const commentId = payload.commentId
    const formData = new FormData()
    formData.append('content', payload.editContentComment);
    return axios({
      method: 'put',
      url: `${API_URL}/api/v1/communities/${articleId}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: formData
    })
    .then(res => {
      console.log('댓글 수정 완료')
      return true
    })
    .catch(err => {
      console.log(err.response.data)
      return false
    })
  }


  const deleteComment = (articleId, commentId) => {
    return axios({
      method: 'delete',
      url: `${API_URL}/api/v1/communities/${articleId}/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {
      console.log('댓글 삭제 완료')
      return res.data.id
    })
    .catch(err => {
      console.log(err.response.data)
    })
  }


    // ----- 데이터 test- reset 함수 -----
    const resetArticle = () => {
      ArticleList.value = []
    }

    

  return {
    buttons, saveUpdateChanges, saveComment, getComments,SaveArticle, 
    ArticleList, deleteArticle, getDetail, resetArticle, deleteComment, 
    saveUpdateChangesComment
  }
}, { persist: true })
