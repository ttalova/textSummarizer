<template>
 <div>
  <b-card
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-title>
    {{this.title}}
    </b-card-title>
    <b-card-text>
    {{this.text}}
    </b-card-text>

  </b-card>
</div>
</template>
<script>
export default {
  props: {
    text: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  },
}
</script>

<style scoped>
</style>
