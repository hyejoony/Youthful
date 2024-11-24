<template>
    <v-card class="mx-auto my-4" max-width="800">
      <v-card-title class="text-h5 bg-blue-grey-darken-3 text-white d-flex align-center">
        <v-icon icon="mdi-robot" class="mr-2" />
        금융 전문가 AI
        <v-spacer></v-spacer>
        <v-chip color="success" size="small">온라인</v-chip>
      </v-card-title>
  
      <!-- API Key 입력 필드 (테스트용) -->
      <v-card-text v-if="!apiKey" class="pt-4">
        <v-text-field
          v-model="tempApiKey"
          label="GROQ API Key 입력"
          type="password"
          append-inner-icon="mdi-key"
          @click:append-inner="setApiKey"
          @keyup.enter="setApiKey"
        ></v-text-field>
      </v-card-text>
  
      <v-card-text class="pt-4">
        <div class="chat-container" ref="chatContainer" style="height: 400px; overflow-y: auto;">
          <template v-for="(message, index) in messages" :key="index">
            <div v-if="message.role === 'user'" class="d-flex justify-end mb-4">
              <v-card-text class="text-right bg-blue-lighten-5 rounded-lg pa-2" style="max-width: 70%;">
                {{ message.content }}
              </v-card-text>
            </div>
            <div v-else class="d-flex mb-4">
              <v-avatar size="40" color="blue-grey-darken-3" class="mr-2">
                <v-icon icon="mdi-robot" color="white" />
              </v-avatar>
              <v-card-text class="bg-grey-lighten-4 rounded-lg pa-2" style="max-width: 70%;">
                {{ message.content }}
              </v-card-text>
            </div>
          </template>
          <v-progress-circular
            v-if="loading"
            indeterminate
            color="primary"
            class="ma-4"
          ></v-progress-circular>
        </div>
      </v-card-text>
  
      <v-card-actions class="pa-4 bg-grey-lighten-4">
        <v-text-field
          v-model="userInput"
          placeholder="금융 관련 질문을 입력하세요"
          append-inner-icon="mdi-send"
          @click:append-inner="sendMessage"
          @keyup.enter="sendMessage"
          :loading="loading"
          :disabled="loading || !apiKey"
          hide-details
          variant="outlined"
          density="comfortable"
        ></v-text-field>
      </v-card-actions>
    </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted, nextTick, watch } from 'vue'
  
  const messages = ref([
    {
      role: 'assistant',
      content: '안녕하세요! 금융과 관련된 궁금한 점을 물어보세요. 전문적인 답변을 제공해드리겠습니다.'
    }
  ])
  const userInput = ref('')
  const loading = ref(false)
  const chatContainer = ref(null)
  const apiKey = ref('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')
  const tempApiKey = ref('')
  
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
            {"role": "system", "content": "you are a helpful finance assistant."},
            {"role": "user", "content": userMessage}
          ],
          model: "mixtral-8x7b-32768",
          temperature: 0.5,
          max_tokens: 1024,
          top_p: 1
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