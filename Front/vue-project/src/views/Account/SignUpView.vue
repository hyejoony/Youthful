<template>
    <!-- v-sheet : container -->
    <h1 color style="text-align: center;">SignUp</h1>
    <v-sheet class="mx-auto" width="550">
        <v-form @submit.prevent="signUp">
            <v-container>
                <v-row justify="center">
                    <v-col cols="12" class="text-center">
                        <!-- position-relative: 상대적 위치 지정 -->
                        <div class="position-relative">
                            <v-avatar color="#658EA7" size="70">
                                <!-- profile_image가 존재할 경우 이미지를 표시합니다. -->
                                <v-img v-if="profile_image" :src="profile_image" alt="User Avatar"></v-img>
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
            <br>

            <p class='errmsg'>{{ store.emailErr }}</p>
            <p class='errmsg'>{{ store.sameErr }}</p>
            <v-text-field v-model="email" clearable label="이메일" placeholder="올바른 이메일 형식 입력"
                variant="solo"></v-text-field>
            <v-text-field v-model="nickname" clearable label="별칭" variant="solo"></v-text-field>
            <p class='errmsg'>{{ store.password1Err }}</p>
            <v-text-field v-model="password1" clearable label="비밀번호" placeholder="영문 대문자, 영문 소문자, 숫자, 특수문자 2가지 포함"
                variant="solo" :type="showPassword1 ? 'text' : 'password'" 
                :append-icon="showPassword1 ? 'mdi-eye' : 'mdi-eye-off'" @click:append="showPassword1 = !showPassword1">
            </v-text-field>
            <p class='errmsg'>{{ store.password2Err }}</p>
            <v-text-field v-model="password2" clearable label="비밀번호 확인" placeholder="한번 더 작성"
                variant="solo" :type="showPassword2 ? 'text' : 'password'" 
                :append-icon="showPassword2 ? 'mdi-eye' : 'mdi-eye-off'" @click:append="showPassword2 = !showPassword2">
            </v-text-field>
            <p class='errmsg'>{{ store.birthyearErr }}</p>
            <v-text-field v-model="birthyear" clearable label="출생연도" placeholder="ex) 1997"
                variant="solo"></v-text-field>

            <div>
                <p class='errmsg'>{{ store.incomeErr }}</p>
                <v-label><b>월 소득구간 금액</b></v-label>
                <v-radio-group v-model="income" inline color="#658EA7">
                    <v-radio label="0~50%" value="0~50%"></v-radio>
                    <v-radio label="51~75%" value="51~75%"></v-radio>
                    <v-radio label="76~100%" value="76~100%"></v-radio>
                    <v-radio label="101~200%" value="101~200%"></v-radio>
                    <v-radio label="200%~" value="200%~"></v-radio>
                </v-radio-group>
                <p class="mb-2 p-first"><b>2024년 1인 가구 기준중위 소득표</b></p>
                <div class="border-first px-4 py-2 mb-4 d-flex justify-space-between">
                    <span>1,114,223원</span>
                    <span>1,671,334원</span>
                    <span>2,228,445원</span>
                    <span>4,456,890원</span>
                    <span>4,456,890원 초과</span>
                </div>
            </div><br>

            <p class='errmsg'>{{ store.regionErr }}</p>
            <v-select v-model="region" label="지역" :items="regions" variant="solo"></v-select>
            <p class='errmsg'>{{ store.careerErr }}</p>
            <v-select v-model="career" label="직업" :items="careers" variant="solo"></v-select><br>

            <div>
                <v-label class="text-subtitle-1 font-weight-bold mb-2">약관 동의</v-label>
                <div class="border-third">
                    <div>
                        <p class="p-second mb-2">서비스 이용약관 동의</p>
                        <p class=" px-4 py-4 mb-4 p-second border-second">
                            본인은 Youthful의 1인 청년 가구 자산관리 서비스 이용약관을 숙지하였으며, 이에 동의합니다.
                            본 약관은 서비스 이용 조건, 회원의 권리와 의무, 서비스 제공 및 변경에 관한 사항을 포함합니다.
                            약관에 동의함으로써 회원은 Youthful이 제공하는 자산관리 서비스를 이용할 수 있으며,
                            관련 법규 및 운영 정책을 준수할 것을 약속합니다. Youthful은 약관 변경 시 사전 고지할 것이며,
                            회원은 변경된 약관에 동의하지 않을 경우 서비스 이용을 중단할 수 있습니다.</p>
                        <v-checkbox class="custom-checkbox" density="compact" v-model="condition1"
                            :rules="[v => !!v || '필수입니다.']" label=" 서비스 이용약관에 동의하십니까?" required></v-checkbox>
                    </div>

                    <div>
                        <p class="p-second mb-2">개인정보 처리 동의</p>
                        <p class=" px-4 py-4 mb-4 p-second border-second">
                            Youthful은 회원의 개인정보를 서비스 제공, 고객 지원, 맞춤형 자산관리 상품 추천을 위해
                            수집 및 활용합니다. 수집되는 정보는 성명, 연락처, 이메일, 금융 정보 등을 포함하며, 이는 안전하게 보관되고 관리됩니다.
                            회원은 언제든지 개인정보 열람, 정정, 삭제를 요청할 수 있으며, Youthful은 관련 법규에 따라 이를 처리할 것입니다.
                            본 동의는 서비스 이용 기간 동안 유효하며, 동의 철회 시 서비스 이용이 제한될 수 있습니다.</p>
                        <v-checkbox class="custom-checkbox" density="compact" v-model="condition2"
                            :rules="[v => !!v || '필수입니다.']" label="개인정보 처리에 동의하십니까?" required></v-checkbox>
                    </div><br>
                </div>
            </div><br>
            <div class="button-container">
                <v-btn type="submit" class='signup-bttn' rounded="xl">가입하기</v-btn>
            </div>
        </v-form>
    </v-sheet>
</template>

<script setup>

// 프로필 이미지 반영
import { ref, onMounted } from 'vue';
import { useAccountStore } from '@/stores/account';

const store = useAccountStore()

onMounted(() => {
    store.clearErrors()
})

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
    '사업자',
    '아르바이트/비정규직',
    '무직/구직중',
    '군인',
    '스타트업 창업자',
    '기타'
]


const showPassword1 = ref(false)
const showPassword2 = ref(false)
const email = ref(null)
const nickname = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const birthyear = ref(null)
const profile_image = ref(null)
const income = ref(null)
const career = ref(null)
const region = ref(null)
const condition1 = ref(false)
const condition2 = ref(false)
const fileInput = ref(null);
// 파일 객체를 저장할 ref 추가
const profileImageFile = ref(null);

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

const signUp = () => {
    const payload = {
        email: email.value,
        nickname: nickname.value,
        password1: password1.value,
        password2: password2.value,
        birthyear: birthyear.value,
        profile_image: profileImageFile.value,
        income: income.value,
        career: career.value,
        region: region.value,
        condition1: condition1.value,
        condition2: condition2.value
    }
    console.log(payload)
    store.signUp(payload)
}


</script>

<style scoped>
.border-first {
    text-align: center;
    border-radius: 10px;
    background-color: #EFEFEF;
    font-size: 13px;
}

.p-first {
    font-size: 14px;
}

.p-second {
    font-size: 14px;
}

.border-second {
    text-align: center;
    border-radius: 10px;
    background-color: white;
    width: 500px;
    height: 140px;
    font-size: 13px;
    margin-left: 20px;
}

.signup-bttn {
    background-color: #658EA7;
    color: white;
    margin-bottom: 30px;

}

.custom-checkbox :deep(.v-label) {
    font-size: 13px;
    /* 원하는 글자 크기 */
}


/* hr {
    height: 1px;
    background-color: #658EA7;
    border: 0;

} */


.border-third {
    border-radius: 10px;
    background-color: #EFEFEF;
    height: 510px;
    padding: 10px;
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

h1 {
    color: #658EA7;
    margin-bottom: 5px;
}

.errmsg {
    color: red
}


.button-container {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 30px;
}
</style>