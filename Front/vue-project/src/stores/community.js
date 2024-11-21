import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const UseCommunityStore = defineStore('community', () => {

// 게시글 리스트
const ArticleList = ref([
])

// article id
let i = ref(0)

// 해쉬태그 키워드
const selectedButton = ref(null);

  // 키워드를 버튼으로
  const buttons = ref([
    { caption: '적금' },
    { caption: '예금' },
    { caption: '지원금' }
]);

// ----- 생성 페이지 -----
const inputTitle = ref('')
const inputContent = ref('')


const SaveArticle = () => {
  ArticleList.value.push({
    // email: email, 
    id: i.value++,
    title: inputTitle.value, 
    content: inputContent.value,
    keyword: selectedButton.value
  }) //유저 이메일 어떻게 넣더랑~~ 

  
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

// 임시 수정 데이터
const editTitle = ref('')
const editContent = ref('')

// 임시 수정 변수 
const editedButton = ref(null)
// 데이터 저장
const saveUpdateChanges = (id) => {
  index = ArticleList.value.findIndex((article) => (article.id) === id)
  
  //해당 index의 article 객체의 속성 
    
  if (index !== -1) {
    // 해당 index의 article 객체의 속성 직접 수정
    ArticleList.value[index].title = editTitle.value;
    ArticleList.value[index].content = editContent.value;
    ArticleList.value[index].keyword = selectedButton.value;
  }

  dialog.value = false

}


// ---- 삭제 페이지 -----
const deleteArticle = (id) => {
  const index = ArticleList.value.findIndex((article) => (article.id) === id)
  ArticleList.value.splice(index,1)

}
  return {buttons, dialog, editContent, editTitle,
    selectedButton,selectButton, editedButton, saveUpdateChanges,
    inputContent, inputTitle, SaveArticle,ArticleList, deleteArticle, getDetail, resetArticleList,
     }
}, { persist: true })
