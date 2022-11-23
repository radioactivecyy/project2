<template>
  <div>
    <!-- <table /> -->
    <!-- <按钮 -->
    <svg id="legend_s" height="100" widtn="332"></svg>
    <svg width="332" height="330" id="svgHTML_star" />
  </div>
</template>
<script>
import * as d3 from 'd3'
const format = d3.format(',d')
let current_circle = undefined
let draw_data = undefined
let mychoosei = undefined
export default {
  name: 'App',
  props: {},
  data() {
    return {
      // data是getdata()的返回结果
      data_as_array: [],
      // data_as_json是异步的，所以需要在mounted()中赋值
      data_as_json: {},
      svg: undefined
    }
  },
  mounted() {
    this.CreateBubbleChart()
    this.DrawCircle()
    this.DrawLegend()
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
      this.data_as_json = await d3.csv('/dev-api/api/star_gazer')
      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {
      this.data_as_json = await d3.csv('/dev-api/api/star_gazer')
      draw_data = this.data_as_json
      console.log('draw', draw_data)
      // 给每条数据添加一个属性 asize
      this.svg = d3
        .select('body')
        .select('#svgHTML_star')
        .style('width', '100%')
        .style('height', 'auto')
        .attr('font-size', 10)
        .attr('font-family', 'sans-serif')
        .attr('text-anchor', 'middle')
      const Mysvg = this.svg
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
        .attr('stroke', (d, i) => {
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

          console.log('mmmiii', iii)
          if (current_circle !== undefined) {
            // 全部重新渲染 然后改个目前选中的颜色
            leaf.selectAll('text').remove()
          }
          current_circle = d3.select(this)
          // 如果原来颜色为#aaccff

          current_circle.attr('fill', '#b2e1f9')
          // console.log('current_circle', current_circle
          const showlabel = leaf
            .append('text')
            .attr('dy', '1.3em')
            .text(function (d, i) {
              if (iii === i) {
                return d.data.count
              }
            })
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
          const label = leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        })
        .on('mouseout', function (d) {
          //      // 全部重新渲染为初始状态
          let mychoose = d3.select(this)
          const thisr = mychoose.attr('r')
          let labelx = 0
          let labely = 0
          let iii
          circle.each(function (d, i) {
            const thisr_num = Number(thisr)
            const s = d.r === thisr_num
            if (d.r === thisr_num) {
              labelx = d.x
              labely = d.y
              iii = i
            }
          })
          if (draw_data[iii].flag === '0') {
            mychoose.attr('fill', '#aaccff')
          } else {
            mychoose.attr('fill', '#ff8a8a')
          }
          // console.log('this.data_as_json[iii]', draw_data)
          Mysvg.selectAll('#details-popup').remove()
          leaf.selectAll('text').remove()

          // 删除原有文字重新渲染
          leaf.selectAll('text').remove()
          const label = leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        })
      const label = leaf
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
