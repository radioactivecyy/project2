<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="1"><div class="grid-content ep-bg-purple" /></el-col>
      <el-col
        :span="17"
      ><div class="grid-content ep-bg-purple" />
        <el-form :model="form" class="demo-form-inline">
          <el-form-item>
            <el-input v-model="form.name" placeholder="input address" />
          </el-form-item>
        </el-form>
      </el-col>

      <!-- <el-col :span="6"
        ><div class="grid-content ep-bg-purple" />
        <el-form :model="form" class="demo-form-inline">
          <el-form-item>
            <el-select v-model="form.region" placeholder="github">
              <el-option label="github" value="gihub" />
              <el-option label="gitee" value="gitee" />
            </el-select>
          </el-form-item>
        </el-form>
      </el-col> -->
      <!--  搜索按钮 -->
      <el-col
        :span="3"
      ><div class="grid-content ep-bg-purple" />
        <el-form :model="form" class="demo-form-inline">
          <el-button type="primary" @click="postData">Query</el-button>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { searchRepo } from '@/api/search'
export default {
  data() {
    return {
      // test: ''
      form: {
        name: '',
        region: ''
      }
    }
  },
  methods: {
    onSubmit() {
      this.$message('submit!')
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    },
    postData() {
      searchRepo()
        .then(res => {
          this.test = res.data.status
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
.line {
  text-align: center;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>
