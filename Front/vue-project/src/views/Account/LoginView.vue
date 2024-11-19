<template>
    <div class="login-container">
        <h1 style="text-align: center;">Login</h1>
        <v-sheet class="mt-1">
            <v-card class="mx-auto px-6 py-8" max-width="500">
                <v-form v-model="form" @submit.prevent="onSubmit">
                    <v-text-field v-model="email" :readonly="loading" variant="solo" :rules="[required]" class="mb-2"
                        label="Email" clearable></v-text-field>

                    <v-text-field v-model="password" :readonly="loading" variant="solo" :rules="[required]"
                        label="Password" clearable></v-text-field>
                    <br>
                    <v-btn :disabled="!form" :loading="loading" color="#658EA7" rounded="xl" type="submit" block>
                        가입하기
                    </v-btn>
                </v-form>
                <p class="p-1">아직 회원이 아니시라면? <RouterLink :to="{ name: 'signup'}"><b> 회원가입</b></RouterLink></p>
            </v-card>
        </v-sheet>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

/// 폼 데이터 로직
// 폼 데이터
const form = ref(false)
const email = ref('')
const password = ref('')
const loading = ref(false)

// 유효성 검사 규칙
const required = (v) => !!v || '입력은 필수입니다.'

// 폼 제출 처리
const onSubmit = async () => {
    if (!form.value) return

    loading.value = true
    // 여기에 로그인 로직을 구현합니다.
    // 예: API 호출, 인증 처리 등
    try {
        // 로그인 API 호출 예시
        // const response = await loginApi(email.value, password.value)

        // 로그인 성공 시 처리
        console.log('Login successful')
        // 로그인 후 리다이렉트
        router.push({ name: 'home' })
    } catch (error) {
        // 에러 처리
        console.error('Login failed:', error)
    } finally {
        loading.value = false
    }
}

</script>

<style scoped>
h1 {
    color: #658EA7;
}

.p-1 {
    color: #658EA7;
    margin-top: 5px;
    font-size: 13px;
    text-align: center;
}

.login-container {
  margin-top: 20vh; /* 뷰포트 높이의 10%만큼 위쪽 마진 추가 */
}
</style>