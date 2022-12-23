<template>
  <div class="try_chards">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <h2>{{ name }}</h2>
          <el-button class="button" text @click="handle">Details</el-button>
        </div>
      </template>
      <div class="l">
         <p><svg-icon icon-class="star" /> {{stars }}</p>
          <p><svg-icon icon-class="fork" /> {{forks }}</p>
        
      </div>

      <!-- <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div> -->
    </el-card>
  </div>
</template>
<script>

export default {
  props: {
    name: {
      type: String,
      default: 'github'
    },
    stars: {
      type: Number,
      default: 0
    },
    forks: {
      type: Number,
      default: 0
    },
    ppp:{
      type: String,
      default: '/pytorch'
    }
  },
  data() {
    return {
      site: {
        name: 'github',
        url: 'https://github.com',
        alexa: '10000'
      }
    }
  },
  methods: {
    handle() {
   
      this.$router.push({ path: this.ppp, query: { name: this.name }})
    }
  }
}
</script>
<style>

.button {
  float: right;
  margin-top: 10px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 240px;
}
</style>
<style scoped>
.svg-icon {
  width: 1.2em;
  height: 1.2em;
  vertical-align: -0.15em;
  fill: #409EFF;
  overflow: hidden;
}
</style>
