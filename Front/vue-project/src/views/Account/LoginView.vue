<template>
    <div class="login-container">
        <h1 style="text-align: center;">Login</h1>
        <v-sheet class="mt-1">
            <v-card class="mx-auto px-6 py-8" max-width="500">
                <v-form v-model="form" @submit.prevent="logIn">
                    <v-text-field v-model="email" :readonly="loading" variant="solo" :rules="[required]" class="mb-2"
                        label="Email" clearable></v-text-field>

                    <v-text-field v-model="password" :readonly="loading" variant="solo" :rules="[required]"
                        label="Password" clearable :type="showPassword ? 'text' : 'password'"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="showPassword = !showPassword">
                    </v-text-field>
                    <br>
                    <v-btn :disabled="!form" :loading="loading" color="#658EA7" rounded="xl" type="submit" block>
                        로그인 하기
                    </v-btn>
                </v-form>
                <p class="p-1">아직 회원이 아니시라면? <RouterLink :to="{ name: 'signup'}"><b> 회원가입</b></RouterLink></p>
            </v-card>
        </v-sheet>
        <p class='errmsg'>{{ store.loginErr }}</p>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/account';

const store = useAccountStore()

const router = useRouter()

const showPassword = ref(false);

/// 폼 데이터 로직
// 폼 데이터
const form = ref(false)
const email = ref('')
const password = ref('')
const loading = ref(false)

// 유효성 검사 규칙
const required = (v) => !!v || '입력은 필수입니다.'

const logIn = () => {
    const payload = {
        email: email.value,
        password: password.value
    }
    store.logIn(payload)
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

.errmsg {
    color: red;
    text-align: center;
    margin-top: 2rem;
}
</style>