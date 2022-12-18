<template>
    <button @click="getStar">getStar</button>
</template>
<script>
import { getSystemErrorMap } from 'util'
import * as dataapi from '@/api/getdata'
const getConfig = {
  headers: {
    Accept: 'application/vnd.github.v3.star+json'
  }
}
export default {
  data() {
    return {
      mydata: {}
    }
  },
  methods: {
    async getStar() {
        console.log('sssssssssssssssssssssssssssssssss')
        const res = await dataapi.getStar().then(response => {
            console.log("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
         console.log(response)
        }).catch(error => {
            console.log(error)
        })
       
    }
  },
 
}
</script>
