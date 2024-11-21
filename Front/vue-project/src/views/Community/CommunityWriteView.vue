<template>
    <v-form @submit.prevent="SaveArticleFunc">
        <v-card width="900" height="400" elevation="4">
            <card-title>
                <v-text-field  v-model="inputTitle" placeholder="제목을 작성해주세요."
                    variant="solo"></v-text-field>
            </card-title>
            <hr style="color: #767676;">
            <card-content>
                <v-text-field  v-model="inputContent" class="v-text-field2"
                    placeholder="본문을 작성해주세요."></v-text-field>
            </card-content>
            <div>
                <p>키워드를 선택해주세요.</p>
                <v-btn v-for="(btn, index) in storeCommunity.buttons" :key="index"
                    :class="{ 'active-button': selectedButton === btn.caption }" @click="selectButton(btn.caption)"
                    density="compact">
                    {{ btn.caption }}
                </v-btn>
            </div>
        </v-card>
        <v-btn type="submit" class="mt-2" :class="{ 'active-button': isFormValid }"
            :disabled="!isFormValid || !selectedButton" density="compact">
            글 올리기
        </v-btn>
    </v-form>
</template>

<script setup>
import { UseCommunityStore } from '@/stores/community';
import { useRouter } from 'vue-router';
import { ref, computed } from 'vue'
const router = useRouter()
const storeCommunity = UseCommunityStore()

// 이 컴포넌트에서 입력한 데이터 
const inputTitle = ref('')
const inputContent = ref('')
// 해쉬태그 키워드
const selectedButton = ref(null);

const selectButton = (caption) => {
    selectedButton.value = caption
}

// 유효성 검사 규칙
// const required = (v) => !!v || '입력은 필수입니다.'

const isFormValid = computed(() => {
  return !!inputTitle.value && !!inputContent.value && !!selectedButton.value
})

console.log('selectedButton', selectedButton)

// 인자로 전달
const SaveArticleFunc = () => {
    if (isFormValid.value) {
        const payload = {
            inputTitle: inputTitle.value,
            inputContent: inputContent.value,
            selectedButton: selectedButton.value
        }
        storeCommunity.SaveArticle(payload)
        router.push({ name: 'community'})
    }
}


</script>


<style scoped>
.v-text-field2 {
    height: 200px;
}

.active-button {
    background-color: #658EA7;
    color: white;
}
</style>