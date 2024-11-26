<template>
    <div class="chatbot-container">
        <!-- 챗봇 토글 버튼: 투명 배경, 아이콘 클릭으로 채팅창 열기/닫기 -->
        <div class="chatbot-wrapper">
            <v-btn @click="toggleChat" icon class="transparent-btn">
                <v-img :src="chatbotImage" alt="User Avatar" class="small-img "></v-img>
              <!-- 말풍선 -->
            </v-btn>
            <div  v-if="!isChatOpen" class="speech-bubble">
        안녕하세요 !
      </div>

        </div>
        <!-- Chatbot Window -->
        <div v-if="isChatOpen" class="chat-window" >
            <v-card class="mx-auto my-2">
                <v-card-title class="text-h5 text-white d-flex align-center" style="background-color: #658EA7;">
                    <h5 class="ml-2" style="font-size: 15px;">든든한 금융 전문가, 챗봇 '유스'와 함께 해보세요!</h5>
                    <v-spacer></v-spacer>
                </v-card-title>

                <!-- API Key 입력 필드 (테스트용) -->
                <v-card-text v-if="!apiKey" class="pt-4">
                    <v-text-field v-model="tempApiKey" label="GROQ API Key 입력" type="password"
                        append-inner-icon="mdi-key" @click:append-inner="setApiKey"
                        @keyup.enter="setApiKey"></v-text-field>
                </v-card-text>

                <!-- Chat Messages -->
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
                        <v-progress-circular v-if="loading" indeterminate color="primary"
                            class="ma-4"></v-progress-circular>
                    </div>
                </v-card-text>

                <!-- User Input -->
                <v-card-actions class="pa-4 bg-grey-lighten-4">
                    <v-text-field v-model="userInput" placeholder="금융 관련 질문을 입력하세요" append-inner-icon="mdi-send"
                        @click:append-inner="sendMessage" @keyup.enter="sendMessage" :loading="loading"
                        :disabled="loading || !apiKey" hide-details variant="outlined"
                        density="comfortable"></v-text-field>
                </v-card-actions>
            </v-card>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'

// State variables
const isChatOpen = ref(false)
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

// Methods
const toggleChat = () => {
    isChatOpen.value = !isChatOpen.value
}

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
                'Content-Type': 'application/json'
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
                temperature: 0.3,
                max_tokens: 400,
                top_p: 0.4
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
.chatbot-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}


.speech-bubble {
    position: relative;
    background: #f0f0f0;
    border-radius: 10px;
    padding: 10px;
    max-width: 200px;
    font-size: 12px;

    /* 말풍선 화살표 효과 */
    &::before {
        content: '';
        position: absolute;
        left: -10px;
        top: 10px;
        border-width: 5px 10px 5px 0;
        border-style: solid;
        border-color: transparent #f0f0f0 transparent transparent;
    }
}



/* 버튼 투명 처리: 배경, 테두리, 그림자 제거 */
.transparent-btn {
    background-color: transparent !important;
    border: none;
    box-shadow: none;
}

.small-img {
    width: 40px;
    height: 40px;
    margin-right: 10px;

}

.chatbot-container {
    position: fixed;
    bottom: 600px;
    right: 20%;
    z-index: 1000;
}

.chat-window {
    width: 530px;
    height: auto;
    
}

.chat-container::-webkit-scrollbar {
    width: 6px;
}

.chat-container::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.chat-container::-webkit-scrollbar-thumb {
    background: #888;
}

.chat-container::-webkit-scrollbar-thumb:hover {
    background: #555;
}
</style>