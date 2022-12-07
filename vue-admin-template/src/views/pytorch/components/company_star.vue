<template>
  <div>
    <!-- <table /> -->
    <!-- <按钮 -->
    <!-- <h1>{{testData
    }}</h1> -->
    <svg width="332" height="330" id="svgHTML_star" />
  </div>
</template>
<script>
import * as d3 from 'd3'


const format = d3.format(',d')
let current_circle = undefined
export default {
  name: 'App',
  props: {
    dataAsJson: {
      type: Array,
      default: null
    },
    testData:{

      type: Number,
      default: 0
    }
  },
  data() {
    return {
      data_as_array: [],
      svg: undefined
    }
  },
  watch: {
    dataAsJson: function (val) {
      if(val === null) {
        return
      }
      this.DrawCircle()
    },
    testData: function (val) {
      if(val === null) {
        return
      }
      this.DrawCircle()
    }
  },
  mounted() {
    // this.data_as_array = this.BuildNameHeader()
    this.CreateBubbleChart()
    this.DrawCircle()
  },
  methods: {
    // async 函数getdata()，用于获取数据

    flatNodeHeirarchy() {
      const root = { children: this.dataAsJson } // remove the first value from the dataset - which is an aggregate we don't need
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
    

      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {

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
        .attr('fill', d => '#aaccff')
        .on('mouseover', function (d) {
          if (current_circle !== undefined) {
            current_circle.attr('fill', d => '#aaccff')
            leaf.selectAll('text').remove()
          }
          current_circle = d3.select(this)
          current_circle.attr('fill', '#b2e1f9')
          const thisr = current_circle.attr('r')
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
          if (current_circle !== undefined) {
            current_circle.attr('fill', d => '#aaccff')
            leaf.selectAll('text').remove()
          }
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
