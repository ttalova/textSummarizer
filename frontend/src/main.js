import './assets/main.css'

import { createPinia } from 'pinia'
import Vue, { createApp } from '@vue/compat';
import BootstrapVue from "bootstrap-vue";

import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from "axios";


axios.defaults.baseURL = 'http://127.0.0.1:8000/'

Vue.use(BootstrapVue);
const app = createApp(App)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
