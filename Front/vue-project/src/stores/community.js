import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const UseCommunityStore = defineStore('community', () => {

  // 게시글 리스트
  const ArticleList = ref([])

  // article id
  let i = 0

  // 해쉬태그 키워드
  const selectedButton = ref(null);

  // 키워드를 버튼으로
  const buttons = ref([
    { caption: '적금' },
    { caption: '예금' },
    { caption: '지원금' }
  ]);

  // ----- 생성 페이지 -----

  const SaveArticle = (inputTitle, inputContent) => {
    console.log(ArticleList.value)

    ArticleList.value.push({
      // email: email, 
      id: i++,
      title: inputTitle.value,
      content: inputContent.value,
      // keyword: selectedButton.value
    }) //유저 이메일 어떻게 넣더랑~~ 
    console.log(ArticleList.value)
  }

  // Function to select a button
  const selectButton = (index) => {
    // Update the selected button index
    selectedButton.value = index;
  };

  // ----- 단일조회 -----
  // 객체 반환
  const getDetail = (id) => {
    const detail = ArticleList.value.find((element) => element.id == id)
    return detail
  }


  // ----- 수정페이지 -----
  const dialog = ref(false) // 모달창 기본설정


  return {buttons, dialog, editContent, editTitle,
    selectedButton,selectButton, editedButton, saveUpdateChanges,
    inputContent, inputTitle, SaveArticle,ArticleList, deleteArticle, getDetail, resetArticleList,
      }
}, { persist: true })
