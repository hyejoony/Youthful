<template>
    <v-container max-width="900">
        <v-row>
            <v-col cols="6">
                <div class="profile-container">
                    <div class="profile-header">
                        <div class="position-relative">
                            <v-avatar color="#658EA7" size="90">
                                <!-- avatarImage가 존재할 경우 이미지를 표시합니다. -->
                                <v-img v-if="avatarImage" :src="avatarImage" alt="User Avatar"></v-img>
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
                <div class="user-info mt-8">
                    <p class="p-1">나이</p><br>
                    <p class="p-1">지역</p><br>
                    <p class="p-1">기준중위소득</p><br>
                    <p class="p-1">직업</p><br>
                </div>
                <hr>
                <v-btn class='signup-bttn' rounded="xl">회원정보 수정</v-btn>
            </v-col>
            <v-col cols="6">
                <UserLikeList />
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>

// 1. 찜 목록

import UserLikeList from '@/components/Account/UserLikeList.vue';

// 2. 프로필 이미지 반영
import { ref } from 'vue';

const fileInput = ref(null);
const avatarImage = ref(null);

// - 파일선택상자 열기
const triggerFileInput = () => {
    // fileInput의 현재 값을 가져와 click() 메서드를 호출하여 파일 선택 대화상자를 엽니다.
    fileInput.value.click();
};

// - 사용자가 선택한 파일 반영
const onFileSelected = (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            avatarImage.value = e.target.result;
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
</style>