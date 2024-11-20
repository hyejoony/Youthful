
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import vuetify from './plugins/vuetify'
import { createHead } from '@vueuse/head' // 플러그인 생성


import App from './App.vue'
import router from './router'

const app = createApp(App)
const head = createHead() //플러그인 인스턴스 생성


app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(head)

app.mount('#app')
