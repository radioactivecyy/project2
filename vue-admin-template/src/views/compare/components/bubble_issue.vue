<template>
  <div>
    <!-- <table /> -->
    <!-- <按钮 -->
    <svg width="332" height="330" id="svgHTML_i" />
  </div>
</template>
<script>
import * as d3 from 'd3'
const format = d3.format(',d')
let current_circle = undefined
let draw_data = undefined
export default {
  name: 'App',
  props: {},
  data() {
    return {
      // data是getdata()的返回结果
      data_as_array: [],
      // data_as_json是异步的，所以需要在mounted()中赋值
      data_as_json: {},
      svg: undefined,
    }
  },
  mounted() {
    this.CreateBubbleChart()
    this.DrawCircle()
  },
  methods: {
    // async 函数getdata()，用于获取数据
    
    flatNodeHeirarchy() {
      const root = { children: this.data_as_json } // remove the first value from the dataset - which is an aggregate we don't need
      return d3.hierarchy(root).sum(d => d.count)
    },
    packedData() {
      const width = 570
      const height = 570

      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async CreateBubbleChart() {
      // 初始化a的类型为Array
      this.data_as_json = await d3.csv('/dev-api/api/issur')
      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {
      this.data_as_json = await d3.csv('/dev-api/api/issue')
      draw_data = this.data_as_json
      // 给每条数据添加一个属性 asize
      this.svg = d3
        .select('body')
        .select('#svgHTML_i')
        .style('width', '100%')
        .style('height', 'auto')
        .attr('font-size', 10)
        .attr('font-family', 'sans-serif')
        .attr('text-anchor', 'middle')
      const leaf = this.svg
        .selectAll('g')
        .data(this.packedData().leaves())
        .enter()
        .append('g')
        .attr('transform', d => `translate(${d.x + 1},${d.y + 1})`)

      const circle = leaf
        .append('circle')
        .attr('r', d => d.r)
        // 根据下标判断是否是pytorch的数据，是的话就用红色，否则用蓝色
        .attr('fill', (d, i) => {
          //  console.log('d',d)
          if (d.data.flag === '0') {
            return '#aaccff'
          } else {
            return '#ff8a8a'
          }
        })
        .attr('stroke', (d,i)=>{
          if (d.data.duplicate === '0') {
            return '#aaccff'
          } else {
            return '#ff8a8a'
          }
        })
        .on('mouseover', function (d, i) {
          let iii
          const thisI = i
          // 遍历leaf 找到目前选中的是哪个
          leaf.each(function (d, i) {
            if (d.x === thisI.x && d.y === thisI.y) {
              iii = i
            }
          })
          leaf.selectAll('text').remove()
          current_circle = d3.select(this)
          // 设置为选中的颜色
          current_circle.attr('fill', '#b2e1f9')
          leaf
            .append('text')
            .attr('dy', '1.6em')
            .text(function (d, i) {
              if (iii === i) {
                return d.data.count
              }
            })
            // 设置字体大小为定值
            .attr('font-size', 13)
            // .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
          leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        })
        .on('mouseout', function (d, i) {
          //      // 全部重新渲染为初始状态
          let iii
          const thisI = i

          // 遍历leaf 找到目前选中的是哪个
          leaf.each(function (d, i) {
            if (d.x === thisI.x && d.y === thisI.y) {
              iii = i
            }
          })
          const mychoose = d3.select(this)
          // 设置为原始颜色
          if (draw_data[iii].flag === '0') {
            mychoose.attr('fill', '#aaccff')
          } else {
            mychoose.attr('fill', '#ff8a8a')
          }

          // 删除原有文字重新渲染
          leaf.selectAll('text').remove()
          leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        })
      leaf
        .append('text')
        .attr('dy', '0.3em')
        .text(d => d.data.company)
        .attr('font-size', d => d.r / 4)
        .attr('color', 'black')
   
    }
  }
  //   buildnameheader
}
</script>
