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
      // 路径path对应在router目录下  定义的path属性值
      // , parmas: { 'name': this.name }
      this.$router.push({ path: '/repo-detail', query: { name: this.name }})
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
  width: 260px;
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
