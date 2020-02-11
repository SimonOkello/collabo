// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';


import Index from './components/Index.vue';

Vue.config.productionTip = false;

Vue.component('index-component', Index);


const app = new Vue({
  el: '#app',

});
