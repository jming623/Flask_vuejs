<template>
  <div id="app">
    <Header />

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
      <div class="container">
        <router-view />
      </div>

    <Footer />
  </div>
</template>

<script>
import Header from './components/common/Header.vue';
import Footer from './components/common/Footer.vue';
import '@/assets/css/flaskapp.css';

export default {
  name: 'App',
  components: {
    Header
    ,Footer
  }
}
</script>