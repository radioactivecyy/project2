<template>
  <div class="try_chards">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>{{ name }}</span>
          <el-button class="button" text @click="handle">Show details</el-button>
        </div>
      </template>
      <div class="l">
        <p>stars:{{ stars }}</p>
        <p>forks:{{ forks }}</p>
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
  width: 480px;
}
</style>
