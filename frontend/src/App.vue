<template>
  <div>
  <h1>Краткое содержание текста</h1>
  <br>
  <div class="full-width-div">
    <b-form @submit.prevent="onSubmit">
    <b-form-group
              label="Введите текст, который нужно сократить:"
              label-for="input-1"
          >
    <b-form-input id="input-1" v-model="text" placeholder="Начинайте вводить текст..."></b-form-input>
    </b-form-group>
      <b-button type="submit" variant="primary">Отправить</b-button>
    </b-form>
  </div>

  <br>
  <div>
  <b-row>
        <b-col>
  <TextCardView :text="this.results_first" :title="'Частотный анализ'"/>
  </b-col>
    <b-col>
          <TextCardView :text="this.results_second" :title="'Косинусное расстояние'"/>
  </b-col>
    <b-col>
      <TextCardView :text="this.results_third" :title="'TF IDF'"/>
        </b-col>
  </b-row>
    </div>
  </div>
</template>

<script>
  import {getSummurytext} from "./services/api";
  import TextCardView from "./components/TextCardView.vue";

  export default {
    components: {TextCardView},
    data() {
      return {
        text: '',
        results_first: '',
        results_second: '',
        results_third: ''
      }
    },
    methods: {
      async onSubmit() {
        this.results_first = await getSummurytext(1, this.text)
        this.results_second = await getSummurytext(2, this.text)
        this.results_third = await getSummurytext(3, this.text)
      }
    }
  }
</script>

<style scoped>
/*header {*/
/*  line-height: 1.5;*/
/*  max-height: 100vh;*/
/*}*/

/*.logo {*/
/*  display: block;*/
/*  margin: 0 auto 2rem;*/
/*}*/

/*nav {*/
/*  width: 100%;*/
/*  font-size: 12px;*/
/*  text-align: center;*/
/*  margin-top: 2rem;*/
/*}*/

/*nav a.router-link-exact-active {*/
/*  color: var(--color-text);*/
/*}*/

/*nav a.router-link-exact-active:hover {*/
/*  background-color: transparent;*/
/*}*/

/*nav a {*/
/*  display: inline-block;*/
/*  padding: 0 1rem;*/
/*  border-left: 1px solid var(--color-border);*/
/*}*/

/*nav a:first-of-type {*/
/*  border: 0;*/
/*}*/

/*@media (min-width: 1024px) {*/
/*  header {*/
/*    display: flex;*/
/*    place-items: center;*/
/*    padding-right: calc(var(--section-gap) / 2);*/
/*  }*/

/*  .logo {*/
/*    margin: 0 2rem 0 0;*/
/*  }*/

/*  header .wrapper {*/
/*    display: flex;*/
/*    place-items: flex-start;*/
/*    flex-wrap: wrap;*/
/*  }*/

/*  nav {*/
/*    text-align: left;*/
/*    margin-left: -1rem;*/
/*    font-size: 1rem;*/

/*    padding: 1rem 0;*/
/*    margin-top: 1rem;*/
/*  }*/
  .full-width-div {
  width: 100%;
  margin: 0;
  padding: 0;
  /* Additional styles for the div */
}


</style>