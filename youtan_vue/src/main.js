import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:3000'
axios.defaults.headers.post['Content-Type'] = 'multipart/form-data'

createApp(App).use(store).use(router).mount('#app')
