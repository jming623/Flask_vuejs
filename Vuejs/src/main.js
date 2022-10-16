import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import axios from 'axios'
import router from './routes';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = true;

Vue.prototype.$axios = axios;

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
    render: h => h(App)
    ,router
}).$mount('#app');

