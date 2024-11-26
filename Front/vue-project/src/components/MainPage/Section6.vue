<template>
  <v-card class="mx-auto my-2" max-width="800">
    <v-card-title class="text-h5 bg-blue-grey-darken-3 text-white d-flex align-center">
      <h5 class="ml-2" style="font-size: 15px;">든든한 금융 전문가, 챗봇 '유스'와 함께 해보세요!</h5>
      <v-spacer></v-spacer>
    </v-card-title>

    <!-- API Key 입력 필드 (테스트용) -->
    <v-card-text v-if="!apiKey" class="pt-4">
      <v-text-field v-model="tempApiKey" label="GROQ API Key 입력" type="password" append-inner-icon="mdi-key"
        @click:append-inner="setApiKey" @keyup.enter="setApiKey"></v-text-field>
    </v-card-text>

    <v-card-text class="pt-4">
      <div class="chat-container" ref="chatContainer" style="height: 400px; overflow-y: auto;">
        <template v-for="(message, index) in messages" :key="index">
          <div v-if="message.role === 'user'" class="d-flex justify-end mb-4">
            <v-card-text class="text-right rounded-lg pa-2"
              style="max-width: 40%; background-color: #658EA7; color: white;">
              {{ message.content }}
            </v-card-text>
          </div>
          <div v-else class="d-flex mb-4">
            <v-avatar color="#658EA7" size="30">
        <v-img :src="chatbotImage" alt="User Avatar"></v-img>
      </v-avatar>
            <v-card-text class="bg-grey-lighten-4 rounded-lg pa-2" style="max-width: 70%;">
              {{ message.content }}
            </v-card-text>
          </div>
        </template>
        <v-progress-circular v-if="loading" indeterminate color="primary" class="ma-4"></v-progress-circular>
      </div>
    </v-card-text>

    <v-card-actions class="pa-4 bg-grey-lighten-4">
      <v-text-field v-model="userInput" placeholder="금융 관련 질문을 입력하세요" append-inner-icon="mdi-send"
        @click:append-inner="sendMessage" @keyup.enter="sendMessage" :loading="loading" :disabled="loading || !apiKey"
        hide-details variant="outlined" density="comfortable"></v-text-field>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'

const messages = ref([
  {
    role: 'assistant',
    content: '안녕하세요! 금융 지식 전문가로서 금융과 친해질 수 있도록 알기쉽게 설명해드릴게요! 무엇이 궁금하신가요?'
  }
])
const userInput = ref('')
const loading = ref(false)
const chatContainer = ref(null)
const apiKey = ref('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')
const tempApiKey = ref('')
const chatbotImage = ref('')

onMounted(async () => {
  chatbotImage.value = (await import('@/assets/images/chatbot.png')).default
})
const setApiKey = () => {
  if (tempApiKey.value.trim()) {
    apiKey.value = tempApiKey.value.trim()
    tempApiKey.value = ''
  }
}

const scrollToBottom = async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

watch(messages, () => {
  scrollToBottom()
}, { deep: true })

const sendMessage = async () => {
  if (!userInput.value.trim() || loading.value || !apiKey.value) return

  const userMessage = userInput.value
  messages.value.push({
    role: 'user',
    content: userMessage
  })

  userInput.value = ''
  loading.value = true

  try {
    // Groq API 직접 호출 (테스트용)
    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey.value}`,
        'Content-Type': 'application/json' // 서버가 수신하는 데이터형식
      },
      body: JSON.stringify({
        messages: [
          { "role": "system", "content": "넌 금융 설명 전문가야, 한국어로만 답을 해줘, 고등학생인 내가 물어보는 개념에 대해 예시와 함께 아주 쉽게 설명해줘. 설명해주고나서 잘 이해했는지 꼭 물어봐줘, 내용이 어렵다는 피드백을 바로 받으면 더 쉬운 말들로 재설명해줘. 말 끝에 자료 출처를 간단하게 반드시 적어줘. 그리고 가독성있게 문단으로 띄워서 답변해줘." },
          { "role": "user", "content": userMessage },
          ...messages.value.map(msg => ({
            role: msg.role,
            content: msg.content
          }))
        ],

        model: "llama-3.2-90b-text-preview",
        temperature: 0.3, // 무작위성
        max_tokens: 400, // 모델이 생성할 수 있는 응답길이 // 사용자 입력 토큰, 모델 출력 토큰 포함
        top_p: 0.4 // 언어 모델이 다음 토큰을 선택할 때 고려하는 확률의 누적 임계값을 설정하는 매개변수
        //이 값은 선택된 토큰들의 누적 확률이 지정된 Top P 값에 도달할 때까지 가장 가능성이 높은 토큰들을 포함하는 가장 작은 집합을 결정합니다.
      })
    })

    if (!response.ok) {
      throw new Error('API 호출 실패')
    }

    const data = await response.json()
    messages.value.push({
      role: 'assistant',
      content: data.choices[0].message.content
    })
  } catch (error) {
    messages.value.push({
      role: 'assistant',
      content: '죄송합니다. 오류가 발생했습니다. API 키를 확인하시거나 잠시 후 다시 시도해주세요.'
    })
    console.error('Chat error:', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.chat-container::-webkit-scrollbar {
  width: 6px;
}

.chat-container::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.chat-container::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.chat-container::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>