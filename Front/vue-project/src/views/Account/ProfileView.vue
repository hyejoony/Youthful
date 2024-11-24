<template>
    <v-container max-width="900">
        <v-row>
            <v-col cols="6">
                <div class="profile-container">
                    <div class="profile-header">
                        <div v-if="user" class="position-relative">
                            <v-avatar color="#658EA7" size="90">
                                <v-img 
                                    v-if="user.profile_image" 
                                    :src="`${baseUrl}${user.profile_image}`" 
                                    alt="User Avatar"
                                ></v-img>
                                <v-icon v-else size="85" icon="mdi-account-circle"></v-icon>
                            </v-avatar>
                            <v-btn icon width="38" height="38" color="grey" class="upload-btn"
                                @click="triggerFileInput">
                                <v-icon size="20">mdi-camera</v-icon>
                            </v-btn>
                            <input ref="fileInput" type="file" style="display: none" @change="onFileSelected"
                                accept="image/*">
                        </div>
                        <h1 class="profile-title" style="text-align: center; color: #658EA7;">님의 프로필</h1>
                    </div>
                </div>
                <div class="user-info mt-8" v-if="user"> 
                    <p class="p-1">나이 : {{ age }}대</p><br>
                    <p class="p-1">지역 : {{ user.region }}</p><br>
                    <p class="p-1">기준중위소득 : {{ user.income }}</p><br>
                    <p class="p-1">직업 : {{ user.career }}</p><br>
                </div>
                <hr>
                <div>
                    <v-btn @click="openDialog" class='signup-bttn' rounded="xl">회원정보 수정</v-btn>
                    <!-- 모달창 -->
                    <v-dialog v-model="dialog" max-width="600">
                        <v-card>
                            <v-card-title class="ml-2" style="color: #658EA7;">회원정보 수정</v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row justify="center">
                                        <v-col cols="12" class="text-center">
                                            <!-- position-relative: 상대적 위치 지정 -->
                                            <div class="position-relative">
                                                <v-avatar color="#658EA7" size="70">
                                                    <!-- profile_image가 존재할 경우 이미지를 표시합니다. -->
                                                    <v-img v-if="editProfileImage" :src="editProfileImage" alt="User Avatar"></v-img>
                                                    <v-icon v-else size="65" icon="mdi-account-circle"></v-icon>
                                                </v-avatar>
                                                <v-btn icon width="38" height="38" color="grey" class="upload-btn"
                                                    @click="triggerFileInput">
                                                    <v-icon size="20">mdi-camera</v-icon>
                                                </v-btn>
                                                <input ref="fileInput" type="file" style="display: none" @change="onFileSelected"
                                                    accept="image/*">
                                            </div>
                                        </v-col>
                                    </v-row>
                                </v-container>
                                <v-text-field v-model="editNickname" label="닉네임"></v-text-field>
                                <v-radio-group v-model="editIncome" inline color="#658EA7">
                                    <v-radio label="0~50%" value="0~50%"></v-radio>
                                    <v-radio label="51~75%" value="51~75%"></v-radio>
                                    <v-radio label="76~100%" value="76~100%"></v-radio>
                                    <v-radio label="101~200%" value="101~200%"></v-radio>
                                    <v-radio label="200%~" value="200%~"></v-radio>
                                </v-radio-group>
                                <v-select v-model="editregion" label="지역" :items="regions" variant="solo"></v-select>
                                <v-select v-model="editCareer" label="직업" :items="careers" variant="solo"></v-select><br>
                                <p class="mb-2 p-first"><b>2024년 1인 가구 기준중위 소득표</b></p>
                                    <div class="border-first px-4 py-2 mb-4 d-flex justify-space-between">
                                        <span>1,114,223원</span>
                                        <span>1,671,334원</span>
                                        <span>2,228,445원</span>
                                        <span>4,456,890원</span>
                                        <span>4,456,890원 초과</span>
                                    </div>
                            </v-card-text>
                            <template v-slot:actions>
                                <!-- 이 슬롯은 카드 하단에 버튼과 같은 액션 요소를 추가하는 데 사용 -->
                                <v-btn variant="text" class="ms-auto" text="취소" @click="dialog = false"></v-btn>
                                <v-btn variant="text" style="color: #658EA7;" text='저장' @click="saveChangesFunc()"></v-btn>
                            </template>
                        </v-card>
                    </v-dialog>
                </div>
            </v-col>
            <v-col cols="6">
                <UserLikeList :user="user"/>
            </v-col>
        </v-row>
    </v-container>
</template>


<script setup>


// 1. 찜 목록

import UserLikeList from '@/components/Account/UserLikeList.vue';

// 2. 프로필 이미지 반영
import { ref, onMounted } from 'vue';
import axios from 'axios'
import { useAccountStore } from '@/stores/account'
import { useRoute } from 'vue-router'

const store = useAccountStore()
const route = useRoute()

const user = ref(null)
const age = ref(null)

onMounted(() => {
  console.log('ID', route.params.id)
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/profile/${route.params.id}/`,
    headers: {
        Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
        console.log(res.data);
        user.value = res.data;
        console.log(res.data.profile_image)

        // 현재 연도 가져오기
        const currentYear = new Date().getFullYear();
        // 나이 계산
        const ageTrue = currentYear - res.data.birthyear;
        // 10대, 20대, 30대 등으로 구분하여 age 변수에 저장
        if (ageTrue >= 10 && ageTrue < 20) {
            age.value = 10;
        } else if (ageTrue >= 20 && ageTrue < 30) {
            age.value = 20;
        } else if (ageTrue >= 30 && ageTrue < 40) {
            age.value = 30;
        } else if (ageTrue >= 40 && ageTrue < 50) {
            age.value = 40;
        } else if (ageTrue >= 50 && ageTrue < 60) {
            age.value = 50;
        } else if (ageTrue >= 60 && ageTrue < 70) {
            age.value = 60;
        }  else if (ageTrue >= 70 && ageTrue < 80) {
            age.value = 70;
        } else if (ageTrue >= 80 && ageTrue < 90) {
            age.value = 80;
        } else if (ageTrue >= 90 && ageTrue < 100) {
            age.value = 100;
        } 
    })
    .catch((err) => {
      console.log(err)
    })
})


const fileInput = ref(null);
// const avatarImage = ref(null);


const dialog = ref(false) // 모달창 기본설정

// 임시 수정 데이터
const editProfileImage = ref(null)
const profileImageFile = ref(null);
const editNickname = ref('')
const editIncome = ref('')
const editCareer = ref('')
const editregion = ref('')

// 모달 열 때 기존 내용을 수정용 변수에 복사 
const openDialog = () => {
    editProfileImage.value = `${baseUrl}${user.value.profile_image}`
    editNickname.value = user.value.nickname
    editIncome.value = user.value.income
    editCareer.value = user.value.career
    editregion.value = user.value.region
    dialog.value = true
}

// 회원정보 수정
const saveChangesFunc = async () => {
    const payload = {
        id: store.userId,
        editProfileImage: profileImageFile.value,
        editNickname: editNickname.value,
        editIncome: editIncome.value,
        editCareer: editCareer.value,
        editregion: editregion.value
    }
    const result = await store.saveUpdateChanges(payload)
    user.value.profile_image = profileImageFile
    user.value.nickname = editNickname
    user.value.income = editIncome
    user.value.career = editCareer
    user.value.region = editregion
    dialog.value = false
}



const regions = [
    '서울특별시',
    '부산광역시',
    '대구광역시',
    '인천광역시',
    '광주광역시',
    '대전광역시',
    '울산광역시',
    '세종특별자치시',
    '경기도',
    '강원특별자치도',
    '충청북도',
    '충청남도',
    '전라북도',
    '전라남도',
    '경상북도',
    '경상남도',
    '제주특별자치도'
]

const careers = [
    '학생',
    '회사원',
    '공무원',
    '전문직',
    '자영업자',
    '프리랜서',
    '사업자',
    '아르바이트/비정규직',
    '전업주부',
    '무직/구직중',
    '은퇴자',
    '농업/어업/임업',
    '군인',
    '교사/교육자',
    '의료종사자',
    '금융업 종사자',
    'IT업계 종사자',
    '서비스업 종사자',
    '제조업 종사자',
    '스타트업 창업자',
    '사회복지사',
    '연구원',
    '기타'
]

const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// - 파일선택상자 열기
const triggerFileInput = () => {
    // fileInput의 현재 값을 가져와 click() 메서드를 호출하여 파일 선택 대화상자를 엽니다.
    fileInput.value.click();
};

// - 사용자가 선택한 파일 반영
const onFileSelected = (event) => {
    const file = event.target.files[0];
    if (file) {
        profileImageFile.value = file; // 파일 객체 저장
        const reader = new FileReader();
        reader.onload = (e) => {
            profile_image.value = e.target.result;
        };
        reader.readAsDataURL(file);
    }
};

</script>

<style scoped>
.profile-container {
    padding: 20px;
}

.profile-header {
    display: flex;
    /* 가로정렬 */
    align-items: center;
    gap: 20px;
    /* 아바타와 제목 사이의 간격 */
}

.position-relative {
    position: relative;
    display: inline-block;
}

.upload-btn {
    position: absolute;
    bottom: 0;
    right: 0;
    transform: translate(20%, 20%);
}

.user-info {
    padding: 20px;
}

.p-1 {
    color: #767676;
}

hr {
    height: 1px;
    background-color: #658EA7;
    border: 0;
}

.signup-bttn {
    background-color: #658EA7;
    color: white;
    margin-bottom: 30px;
    margin-top: 30px;

}

.border-first {
    text-align: center;
    border-radius: 10px;
    background-color: #EFEFEF;
    font-size: 13px;
}

.p-first {
    font-size: 14px;
}
</style>